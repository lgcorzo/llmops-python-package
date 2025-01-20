"""Define trainable machine learning models."""

# %% IMPORTS

import abc
import typing as T

import pydantic as pdt
import shap

from autogen_team.core import schemas

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

    # params
    max_tokens: int = 128000
    temperature: float = 0.5
    prompt: str = "imput text"
    

    @T.override
    def predict(self, inputs: schemas.Inputs) -> schemas.Outputs:
        model = self.get_internal_model()
        prediction = model.predict(inputs)
        outputs = schemas.Outputs({schemas.OutputsSchema.prediction: prediction}, index=inputs.index)
        return outputs

    @T.override
    def explain_model(self) -> schemas.FeatureImportances:
        model = self.get_internal_model()
        regressor = model.named_steps["regressor"]
        transformer = model.named_steps["transformer"]
        column_names = transformer.get_feature_names_out()
        feature_importances = schemas.FeatureImportances(
            data={
                "feature": column_names,
                "importance": regressor.feature_importances_,
            }
        )
        return feature_importances

    @T.override
    def explain_samples(self, inputs: schemas.Inputs) -> schemas.SHAPValues:
        model = self.get_internal_model()
        regressor = model.named_steps["regressor"]
        transformer = model.named_steps["transformer"]
        transformed = transformer.transform(X=inputs)
        explainer = shap.TreeExplainer(model=regressor)
        shap_values = schemas.SHAPValues(
            data=explainer.shap_values(X=transformed),
            columns=transformer.get_feature_names_out(),
        )
        return shap_values

    @T.override
    def get_internal_model(self) -> pipeline.Pipeline:
        model = self._pipeline
        if model is None:
            raise ValueError("Model is not fitted yet!")
        return model


ModelKind = BaselineSklearnModel
