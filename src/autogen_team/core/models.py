"""Define trainable machine learning models."""

# %% IMPORTS

import abc
import typing as T

import pydantic as pdt
from typing import Any, Dict

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat

from autogen_ext.models.openai import OpenAIChatCompletionClient


from autogen_team.core import schemas
from autogen_team.tools.weather import get_weather

# %% TYPES

# Model params
ParamKey = str
ParamValue = T.Any
Params = dict[ParamKey, ParamValue]



# %% MODELS


class Model(abc.ABC, pdt.BaseModel, strict=True, frozen=False, extra="forbid"):
    """Base class for a project model.

    Use a model to adapt AI/ML frameworks.
    e.g., to swap easily one model with another.
    """

    KIND: str

    def get_params(self, deep: bool = True) -> Params:
        """Get the model params.

        Args:
            deep (bool, optional): ignored.

        Returns:
            Params: internal model parameters.
        """
        params: Params = {}
        for key, value in self.model_dump().items():
            if not key.startswith("_") and not key.isupper():
                params[key] = value
        return params

    def set_params(self, **params: ParamValue) -> T.Self:
        """Set the model params in place.

        Returns:
            T.Self: instance of the model.
        """
        for key, value in params.items():
            setattr(self, key, value)
        return self

    @abc.abstractmethod
    def load_context(self, model_config: Dict[str, Any]):
        """
        Load the model from the specified artifacts directory.
        """

    @abc.abstractmethod
    def fit(self, inputs: schemas.Inputs, targets: schemas.Targets) -> T.Self:
        """Fit the model on the given inputs and targets.

        Args:
            inputs (schemas.Inputs): model training inputs.
            targets (schemas.Targets): model training targets.

        Returns:
            T.Self: instance of the model.
        """

    @abc.abstractmethod
    def predict(self, inputs: schemas.Inputs) -> schemas.Outputs:
        """Generate outputs with the model for the given inputs.

        Args:
            inputs (schemas.Inputs): model prediction inputs.

        Returns:
            schemas.Outputs: model prediction outputs.
        """

    def explain_model(self) -> schemas.FeatureImportances:
        """Explain the internal model structure.

        Raises:
            NotImplementedError: method not implemented.

        Returns:
            schemas.FeatureImportances: feature importances.
        """
        raise NotImplementedError()

    def explain_samples(self, inputs: schemas.Inputs) -> schemas.SHAPValues:
        """Explain model outputs on input samples.

        Raises:
            NotImplementedError: method not implemented.

        Returns:
            schemas.SHAPValues: SHAP values.
        """
        raise NotImplementedError()

    def get_internal_model(self) -> T.Any:
        """Return the internal model in the object.

        Raises:
            NotImplementedError: method not implemented.

        Returns:
            T.Any: any internal model (either empty or fitted).
        """
        raise NotImplementedError()


class BaselineAutogenModel(Model):
    """Simple baseline model based on autogen.

    Parameters:
        max_tokens (int): maximum token of the prompt
        max_tokens (float): temperature for the sampling
        promtp (str): prompt for the model
    """

    KIND: T.Literal["BaselineAutogenModel"] = "BaselineAutogenModel"

    assistant_agent: AssistantAgent
    team: RoundRobinGroupChat

    @T.override
    def load_context(self, model_config: Dict[str, Any]):
        """
        Load the model from the specified artifacts directory.
        """
        self.assistant_agent = AssistantAgent(
            name="assistant_agent",
            tools=[get_weather],
            model_client=OpenAIChatCompletionClient(model="gpt-4o-2024-08-06"),
        )

        termination = TextMentionTermination("TERMINATE") | MaxMessageTermination(10)
        self.team = RoundRobinGroupChat(participants=[self.assistant_agent], termination_condition=termination)

    @T.override
    def predict(self, inputs: schemas.Inputs) -> schemas.Outputs:
        """
        Predicts the output using the assistant team based on the given inputs.
        """
        # Initialize a list to collect messages or results
        results = []

        # Stream responses from the team
        response_stream = self.team.run(task=inputs)
        for  msg in response_stream:
            if hasattr(msg, "content"):
                # Collect content messages
                results.append(msg.content)

            if isinstance(msg, TaskResult):
                # Handle the final task result if needed
                results.append(f"Task Result: {msg.result}")
                # Break or terminate loop if needed after TaskResult
                break

        # Join results or format as needed
        prediction = "\n".join(results)

        # Return the outputs schema
        outputs = schemas.Outputs({schemas.OutputsSchema.prediction: prediction}, index=inputs.index)

        return outputs


ModelKind = BaselineAutogenModel
