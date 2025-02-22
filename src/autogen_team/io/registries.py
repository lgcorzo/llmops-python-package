"""Savers, loaders, and registers for model registries."""

# %% IMPORTS

import abc
import json
import os
import typing as T

import mlflow
import pandas as pd
import pydantic as pdt
from typing import Any, Dict

from autogen_team.core import models, schemas
from autogen_team.utils import signers

# %% TYPES

# Results of model registry operations
Info: T.TypeAlias = mlflow.models.model.ModelInfo
Alias: T.TypeAlias = mlflow.entities.model_registry.ModelVersion
Version: T.TypeAlias = mlflow.entities.model_registry.ModelVersion

# %% HELPERS


def uri_for_model_alias(name: str, alias: str) -> str:
    """Create a model URI from a model name and an alias.

    Args:
        name (str): name of the mlflow registered model.
        alias (str): alias of the registered model.

    Returns:
        str: model URI as "models:/name@alias".
    """
    return f"models:/{name}@{alias}"


def uri_for_model_version(name: str, version: int) -> str:
    """Create a model URI from a model name and a version.

    Args:
        name (str): name of the mlflow registered model.
        version (int): version of the registered model.

    Returns:
        str: model URI as "models:/name/version."
    """
    return f"models:/{name}/{version}"


def uri_for_model_alias_or_version(name: str, alias_or_version: str | int) -> str:
    """Create a model URi from a model name and an alias or version.

    Args:
        name (str): name of the mlflow registered model.
        alias_or_version (str | int): alias or version of the registered model.

    Returns:
        str: model URI as "models:/name@alias" or "models:/name/version" based on input.
    """
    if isinstance(alias_or_version, int):
        return uri_for_model_version(name=name, version=alias_or_version)
    else:
        return uri_for_model_alias(name=name, alias=alias_or_version)


# %% SAVERS


class Saver(abc.ABC, pdt.BaseModel, strict=True, frozen=True, extra="forbid"):
    """Base class for saving models in registry.

    Separate model definition from serialization.
    e.g., to switch between serialization flavors.

    Parameters:
        path (str): model path inside the Mlflow store.
    """

    KIND: str

    path: str = "model"
    config_file: str = "model_config.json"

    @abc.abstractmethod
    def save(self, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) -> Info:
        """Save a model in the model registry.

        Args:
            model (models.Model): project model to save.
            signature (signers.Signature): model signature.
            input_example (schemas.Inputs): sample of inputs.

        Returns:
            Info: model saving information.
        """


class CustomSaver(Saver):
    """Saver for project models using the Mlflow PyFunc module.

    https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html
    https://mlflow.org/blog/autogen-image-agent
    https://mlflow.org/blog/custom-pyfunc
    """

    KIND: T.Literal["CustomSaver"] = "CustomSaver"

    class Adapter(mlflow.pyfunc.PythonModel):  # type: ignore[misc]
        """Adapt a custom model to the Mlflow PyFunc flavor for saving operations.

        https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html?#mlflow.pyfunc.PythonModel
        """

        # TBD load context:
        def __init__(self, model: models.Model):
            """Initialize the custom saver adapter.

            Args:
                model (models.Model): project model.
            """
            self.model = model
            self.model_config = {
                "provider": "openai_chat_completion_client",  # Use LiteLLM-compatible client
                "config": {
                    "model": "azure-gpt",  # LiteLLM model
                    "api_base": "http://litellm:4000/v1",  # LiteLLM Gateway URL
                    "api_key": "sk-12345",
                    "temperature": 0.7,  # Optional
                    "max_tokens": 512,  # Optional
                },
            }

        def load_context(self, context: mlflow.pyfunc.PythonModelContext):
            """
            Load the model from the specified artifacts directory.
            """
            model_file_path = context.artifacts["config_file"]
            # Define the configuration
            model_config = json.load(open(model_file_path, "r", encoding="utf-8"))
            # Load the model
            self.model.load_context(model_config)

        def predict(self, context: mlflow.pyfunc.PythonModelContext, inputs: schemas.Inputs) -> schemas.Outputs:
            """Generate predictions with a custom model for the given inputs.

            Args:
                context (mlflow.pyfunc.PythonModelContext): mlflow context.
                model_input (schemas.Inputs): inputs for the mlflow model.
                params (dict[str, T.Any] | None): additional parameters.

            Returns:
                schemas.Outputs: validated outputs of the project model.
            """
            output = self.model.predict(inputs=inputs)
            return output

    @T.override
    def save(self, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) -> Info:
        adapter = CustomSaver.Adapter(model=model)
        return mlflow.pyfunc.log_model(
            python_model=adapter,
            signature=signature,
            artifact_path=self.path,
            artifacts={"config_file": os.path.join(self.path, self.config_file)},
            input_example=input_example,
        )


SaverKind = CustomSaver 

# %% LOADERS


class Loader(abc.ABC, pdt.BaseModel, strict=True, frozen=True, extra="forbid"):
    """Base class for loading models from registry.

    Separate model definition from deserialization.
    e.g., to switch between deserialization flavors.
    """

    KIND: str

    class Adapter(abc.ABC):
        """Adapt any model for the project inference."""

        @abc.abstractmethod
        def load_context(self, model_config: Dict[str, Any]):
            """
            Load the model from the specified artifacts directory.
            """

        @abc.abstractmethod
        def predict(self, inputs: schemas.Inputs) -> schemas.Outputs:
            """Generate predictions with the internal model for the given inputs.

            Args:
                inputs (schemas.Inputs): validated inputs for the project model.

            Returns:
                schemas.Outputs: validated outputs of the project model.
            """

    @abc.abstractmethod
    def load(self, uri: str) -> "Loader.Adapter":
        """Load a model from the model registry.

        Args:
            uri (str): URI of a model to load.

        Returns:
            Loader.Adapter: model loaded.
        """


class CustomLoader(Loader):
    """Loader for custom models using the Mlflow PyFunc module.

    https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html
    """

    KIND: T.Literal["CustomLoader"] = "CustomLoader"

    class Adapter(Loader.Adapter):
        """Adapt a custom model for the project inference."""

        def __init__(self, model: mlflow.pyfunc.PyFuncModel) -> None:
            """Initialize the adapter from an mlflow pyfunc model.

            Args:
                model (mlflow.pyfunc.PyFuncModel): mlflow pyfunc model.
            """
            self.model = model

        @T.override
        def load_context(self, model_config: Dict[str, Any]):
            """
            Load the model from the specified artifacts directory.
            """
            self.model.load_context(model_config)

        @T.override
        def predict(self, inputs: schemas.Inputs) -> schemas.Outputs:
            # model validation is already done in predict
            prediction = self.model.predict(data=inputs)
            
            # Return the outputs schema
            outputs = schemas.Outputs(
                pd.DataFrame(
                    {
                        "response": [prediction],
                        "metadata": [{"timestamp": "2025-01-15T12:00:00Z", "model_version": "v1.0.0"}],
                    }
                )
            )
            return outputs

    @T.override
    def load(self, uri: str) -> "CustomLoader.Adapter":
        model = mlflow.pyfunc.load_model(model_uri=uri)
        adapter = CustomLoader.Adapter(model=model)
        return adapter


LoaderKind = CustomLoader 

# %% REGISTERS


class Register(abc.ABC, pdt.BaseModel, strict=True, frozen=True, extra="forbid"):
    """Base class for registring models to a location.

    Separate model definition from its registration.
    e.g., to change the model registry backend.

    Parameters:
        tags (dict[str, T.Any]): tags for the model.
    """

    KIND: str

    tags: dict[str, T.Any] = {}

    @abc.abstractmethod
    def register(self, name: str, model_uri: str) -> Version:
        """Register a model given its name and URI.

        Args:
            name (str): name of the model to register.
            model_uri (str): URI of a model to register.

        Returns:
            Version: information about the registered model.
        """


class MlflowRegister(Register):
    """Register for models in the Mlflow Model Registry.

    https://mlflow.org/docs/latest/model-registry.html
    """

    KIND: T.Literal["MlflowRegister"] = "MlflowRegister"

    @T.override
    def register(self, name: str, model_uri: str) -> Version:
        return mlflow.register_model(name=name, model_uri=model_uri, tags=self.tags)


RegisterKind = MlflowRegister
