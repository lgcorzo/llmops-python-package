"""Define and validate dataframe schemas."""

import typing as T
import pandera as pa
import pandera.typing as papd
import pandera.typing.common as padt

# %% SCHEMAS


class Schema(pa.DataFrameModel):
    """Base class for defining schemas with validation capabilities."""

    class Config:
        """Default configurations for all schemas."""

        coerce: bool = True
        strict: bool = True

    @classmethod
    def validate(cls, data: dict) -> bool:
        """Validate a given data dictionary against the schema.

        Args:
            data (dict): The data to validate.

        Returns:
            bool: True if validation is successful, False otherwise.
        """
        try:
            cls.validate(data)
            return True
        except Exception as e:
            print(f"Validation failed: {e}")
            return False


class MetadataSchema(Schema):
    """Schema for metadata in outputs."""

    timestamp: papd.Series[padt.String] = pa.Field()
    model_version: papd.Series[padt.String] = pa.Field()


class InputsSchema(Schema):
    """Schema for validating large string inputs."""

    input: papd.Series[padt.String] = pa.Field()


class OutputsSchema(Schema):
    """Schema for structured JSON outputs."""

    response: papd.Series[padt.String] = pa.Field()
    metadata: T.Optional[MetadataSchema] = pa.Field()


class TargetsSchema(Schema):
    """Schema for the project target."""

    input: papd.Series[padt.String] = pa.Field()
    prediction: papd.Series[padt.String] = pa.Field()


class SHAPValuesSchema(Schema):
    """Schema for SHAP values."""

    class Config:
        dtype: str = "float32"
        strict: bool = False


class FeatureImportancesSchema(Schema):
    """Schema for feature importances."""

    feature: papd.Series[padt.String] = pa.Field()
    importance: papd.Series[padt.Float32] = pa.Field()


Inputs = papd.DataFrame[InputsSchema]
Targets = papd.DataFrame[TargetsSchema]
Outputs = papd.DataFrame[OutputsSchema]
SHAPValues = papd.DataFrame[SHAPValuesSchema]
FeatureImportances = papd.DataFrame[FeatureImportancesSchema]

# Test examples to illustrate usage
if __name__ == "__main__":
    # Example for InputSchema validation
    input_data = {"input": "Some large input string"}
    print("Input validation result:", InputsSchema.validate(input_data))

    # Example for OutputSchema validation
    output_data = {
        "response": "Generated output string",
        "metadata": {"timestamp": "2025-01-15T12:00:00Z", "model_version": "v1.0.0"},
    }
    print("Output validation result:", OutputsSchema.validate(output_data))
