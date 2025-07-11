# %% IMPORTS

import _pytest.capture as pc
import pytest
from autogen_team import jobs
from autogen_team.core import models
from autogen_team.io import datasets, registries, services

# %% JOBS


@pytest.mark.parametrize("alias_or_version", [1, "Promotion"])
def test_explanations_job(
    alias_or_version: str | int,
    mlflow_service: services.MlflowService,
    alerts_service: services.AlertsService,
    logger_service: services.LoggerService,
    inputs_samples_reader: datasets.ParquetReader,
    tmp_models_explanations_writer: datasets.ParquetWriter,
    tmp_samples_explanations_writer: datasets.ParquetWriter,
    model_alias: registries.Version,
    loader: registries.CustomLoader,
    capsys: pc.CaptureFixture[str],
) -> None:
    # given
    if isinstance(alias_or_version, int):
        assert str(alias_or_version) == str(
            model_alias.version
        ), "Model version should be the same!"
    else:
        assert alias_or_version == model_alias.aliases[0], "Model alias should be the same!"
    # when
    job = jobs.ExplanationsJob(
        logger_service=logger_service,
        alerts_service=alerts_service,
        mlflow_service=mlflow_service,
        inputs_samples=inputs_samples_reader,
        models_explanations=tmp_models_explanations_writer,
        samples_explanations=tmp_samples_explanations_writer,
        alias_or_version=alias_or_version,
        loader=loader,
    )
    with job as runner:
        out = runner.run()
    # then
    # - vars
    assert set(out) == {
        "self",
        "logger",
        "inputs_samples",
        "model_uri",
        "model",
        "models_explanations",
        "samples_explanations",
    }
    # - inputs
    assert out["inputs_samples"].ndim == 2, "Inputs samples should be a dataframe!"
    # - model uri
    assert str(alias_or_version) in out["model_uri"], "Model URI should contain the model alias!"
    assert (
        mlflow_service.registry_name in out["model_uri"]
    ), "Model URI should contain the registry name!"
    # - model
    assert isinstance(out["model"], models.Model), "Model should be an instance of a project Model!"
    # - model explanations
    assert len(out["models_explanations"].index) >= len(
        out["inputs_samples"].columns
    ), "Model explanations should have at least as many columns as inputs samples!"
    # - samples explanations
    assert len(out["samples_explanations"].index) == len(
        out["inputs_samples"].index
    ), "Samples explanations should have the same number of rows as inputs samples!"
    assert len(out["samples_explanations"].columns) >= len(
        out["inputs_samples"].columns
    ), "Samples explanations should have at least as many columns as inputs samples!"
    # - alerting service
    assert (
        "Explanations Job Finished" in capsys.readouterr().out
    ), "Alerting service should be called!"
