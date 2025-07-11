# MLOps Python Package
the original repository is fmind https://github.com/fmind/llmops-python-package

[![check.yml](https://github.com/lgcorzo/llmops-python-package/actions/workflows/check.yml/badge.svg)](https://github.com/lgcorzo/llmops-python-package/actions/workflows/check.yml)
[![publish.yml](https://github.com/lgcorzo/llmops-python-package/actions/workflows/publish.yml/badge.svg)](https://github.com/lgcorzo/llmops-python-package/actions/workflows/publish.yml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://lgcorzo.github.io/llmops-python-package/)
[![License](https://img.shields.io/github/license/lgcorzo/llmops-python-package)](https://github.com/lgcorzo/llmops-python-package/blob/main/LICENCE.txt)
[![Release](https://img.shields.io/github/v/release/lgcorzo/llmops-python-package)](https://github.com/lgcorzo/llmops-python-package/releases)

**This repository contains a Python code base with best practices designed to support your MLOps initiatives.**

The package leverages several [tools](#tools) and [tips](#tips) to make your MLOps experience as flexible, robust, productive as possible.

You can use this package as part of your MLOps toolkit or platform (e.g., Model Registry, Experiment Tracking, Realtime Inference, ...).

**Related Resources**:
- **[MLOps Coding Course (Learning)](https://github.com/MLOps-Courses/mlops-coding-course)**: Learn how to create, develop, and maintain a state-of-the-art MLOps code base.
- **[Cookiecutter MLOps Package (Template)](https://github.com/lgcorzo/cookiecutter-mlops-package)**: Start building and deploying Python packages and Docker images for MLOps tasks.

# Table of Contents

- [MLOps Python Package](#mlops-python-package)
- [Table of Contents](#table-of-contents)
- [Install](#install)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Next Steps](#next-steps)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Execution](#execution)
  - [Automation](#automation)
  - [Workflows](#workflows)
- [Tools](#tools)
  - [Automation](#automation-1)
    - [Commits: Commitizen](#commits-commitizen)
    - [Git Hooks: Pre-Commit](#git-hooks-pre-commit)
    - [Tasks: PyInvoke](#tasks-pyinvoke)
  - [CI/CD](#cicd)
    - [Runner: GitHub Actions](#runner-github-actions)
  - [CLI](#cli)
    - [Parser: Argparse](#parser-argparse)
    - [Logging: Loguru](#logging-loguru)
  - [Code](#code)
    - [Coverage: Coverage](#coverage-coverage)
    - [Editor: VS Code](#editor-vs-code)
    - [Formatting: Ruff](#formatting-ruff)
    - [Quality: Ruff](#quality-ruff)
    - [Security: Bandit](#security-bandit)
    - [Testing: Pytest](#testing-pytest)
    - [Typing: Mypy](#typing-mypy)
    - [Code Versioning: Git](#code-versioning-git)
    - [Data Versioning: DVC](#data-versioning-dvc)
      - [**Motivations**](#motivations)
      - [**Features**](#features)
      - [**Limitations**](#limitations)
      - [**Alternatives**](#alternatives)
      - [**Additional Resources**](#additional-resources)
  - [Configs](#configs)
    - [Format: YAML](#format-yaml)
    - [Parser: OmegaConf](#parser-omegaconf)
    - [Reader: Cloudpathlib](#reader-cloudpathlib)
    - [Validator: Pydantic](#validator-pydantic)
  - [Data](#data)
    - [Container: Pandas](#container-pandas)
    - [Format: Parquet](#format-parquet)
    - [Schema: Pandera](#schema-pandera)
  - [Docs](#docs)
    - [API: pdoc](#api-pdoc)
    - [Format: Google](#format-google)
    - [Hosting: GitHub Pages](#hosting-github-pages)
  - [Model](#model)
    - [Evaluation: Scikit-Learn Metrics](#evaluation-scikit-learn-metrics)
    - [Format: Mlflow Model](#format-mlflow-model)
    - [Registry: Mlflow Registry](#registry-mlflow-registry)
    - [Tracking: Mlflow Tracking](#tracking-mlflow-tracking)
  - [Package](#package)
    - [Evolution: Changelog](#evolution-changelog)
    - [Format: Wheel](#format-wheel)
    - [Manager: Poetry](#manager-poetry)
    - [Runtime: Docker](#runtime-docker)
  - [Programming](#programming)
    - [Language: Python](#language-python)
    - [Version: Pyenv](#version-pyenv)
  - [Observability](#observability)
    - [Reproducibility: Mlflow Project](#reproducibility-mlflow-project)
    - [Monitoring : Mlflow Evaluate](#monitoring--mlflow-evaluate)
    - [Alerting: Plyer](#alerting-plyer)
    - [Lineage: Mlflow Dataset](#lineage-mlflow-dataset)
    - [Explainability: SHAP](#explainability-shap)
    - [Infrastructure: Mlflow System Metrics](#infrastructure-mlflow-system-metrics)
- [Tips](#tips)
  - [AI/ML Practices](#aiml-practices)
    - [Data Catalog](#data-catalog)
    - [Hyperparameter Optimization](#hyperparameter-optimization)
    - [Data Splits](#data-splits)
  - [Design Patterns](#design-patterns)
    - [Directed-Acyclic Graph](#directed-acyclic-graph)
    - [Program Service](#program-service)
    - [Soft Coding](#soft-coding)
    - [SOLID Principles](#solid-principles)
    - [IO Separation](#io-separation)
  - [Python Powers](#python-powers)
    - [Context Manager](#context-manager)
    - [Python Package](#python-package)
  - [Software Engineering](#software-engineering)
    - [Code Typing](#code-typing)
    - [Config Typing](#config-typing)
    - [Dataframe Typing](#dataframe-typing)
    - [Object Oriented](#object-oriented)
    - [Semantic Versioning](#semantic-versioning)
  - [Testing Tricks](#testing-tricks)
    - [Parallel Testing](#parallel-testing)
    - [Test Fixtures](#test-fixtures)
  - [VS Code](#vs-code)
    - [Code Workspace](#code-workspace)
    - [GitHub Copilot](#github-copilot)
    - [VSCode VIM](#vscode-vim)
- [Resources](#resources)
  - [Python](#python)
  - [AI/ML/MLOps](#aimlmlops)
  - [UML course:](#uml-course)
    - [1. **Asociación**](#1-asociación)
      - [Código Python:](#código-python)
      - [Representación UML:](#representación-uml)
    - [2. **Agregación**](#2-agregación)
      - [Código Python:](#código-python-1)
      - [Representación UML:](#representación-uml-1)
    - [3. **Composición**](#3-composición)
      - [Código Python:](#código-python-2)
      - [Representación UML:](#representación-uml-2)
    - [4. **Dependencia**](#4-dependencia)
      - [Código Python:](#código-python-3)
      - [Representación UML:](#representación-uml-3)
    - [Resumen de Relaciones:](#resumen-de-relaciones)
    - [1. Asociación](#1-asociación-1)
    - [2. Agregación](#2-agregación-1)
    - [3. Composición](#3-composición-1)
    - [4. Dependencia](#4-dependencia-1)
    - [Cómo interpretar:](#cómo-interpretar)
    - [Ejemplo en Python](#ejemplo-en-python)
    - [Representación en Mermaid para UML](#representación-en-mermaid-para-uml)
    - [Explicación:](#explicación)
  - [Monitoring](#monitoring)
  - [docker compose example:](#docker-compose-example)
  - [autogen Studio.](#autogen-studio)
  - [openai with mlflow example:](#openai-with-mlflow-example)

# Install

This section details the requirements, actions, and next steps to kicºkstart your MLOps project.

## Prerequisites

- [Python>=3.12](https://www.python.org/downloads/): to benefit from [the latest features and performance improvements](https://docs.python.org/3/whatsnew/3.12.html)
- [Poetry>=1.8.2](https://python-poetry.org/): to initialize the project [virtual environment](https://docs.python.org/3/library/venv.html) and its dependencies

## Installation

1. [Clone this GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) on your computer
```bash
# with ssh (recommended)
$ git clone git@github.com:lgcorzo/llmops-python-package
# with https
$ git clone https://github.com/lgcorzo/llmops-python-package
```
2. [Run the project installation with poetry](https://python-poetry.org/docs/)
```bash
$ cd llmops-python-package/
$ poetry install
```
3. Adapt the code base to your desire

## Next Steps

Going from there, there are dozens of ways to integrate this package to your MLOps platform.

For instance, you can use Databricks or AWS as your compute platform and model registry.

It's up to you to adapt the package code to the solution you target. Good luck champ!

# Usage

This section explains how configure the project code and execute it on your system.

to run the ui for autogen the command is;

``` bash
autogenstudio ui --port 8090
```

![1740767154031](image/README/1740767154031.png)

## Configuration

You can add or edit config files in the `confs/` folder to change the program behavior.

```yaml
# confs/training.yaml
job:
  KIND: TrainingJob
  inputs:
    KIND: ParquetReader
    path: data/inputs_train.parquet
  targets:
    KIND: ParquetReader
    path: data/targets_train.parquet
```

This config file instructs the program to start a `TrainingJob` with 2 parameters:
- `inputs`: dataset that contains the model inputs
- `targets`: dataset that contains the model target

You can find all the parameters of your program in the `src/[package]/jobs/*.py` files.

You can also print the full schema supported by this package using `poetry run autogen_team --schema`.

## Execution

The project code can be executed with poetry during your development:

```bash
$ poetry run autogen_team confs/tuning.yaml
$ poetry run autogen_team confs/training.yaml
$ poetry run autogen_team confs/promotion.yaml
$ poetry run autogen_team confs/inference.yaml
$ poetry run autogen_team confs/evaluations.yaml
$ poetry run autogen_team confs/explanations.yaml
```
debug in vscode  is possible th the following configuration:
```json
{
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Poetry evaluations Debug",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/src/autogen_team/__main__.py", // Adjust the entry point path
            "args": [
                "confs/evaluations.yaml"
            ], // Arguments passed to your script
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}", // Set the working directory to the project root
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src"
            } // Ensure module discovery
        }
    ]
}
```

In production, you can build, ship, and run the project as a Python package:

```bash
poetry build
poetry publish # optional
python -m pip install [package]
[package] confs/inference.yaml
## added mocogpt for integration test
poetry add --group checks "mocogpt[cli]@git+https://github.com/lgcorzo/mocogpt.git"
```

You can also install and use this package as a library for another AI/ML project:

```python
from [package] import jobs

job = jobs.TrainingJob(...)
with job as runner:
    runner.run()
```

**Additional tips**:
- You can pass extra configs from the command line using the `--extras` flag
  - Use it to pass runtime values (e.g., a result from previous job executions)
- You can pass several config files in the command-line to merge them from left to right
  - You can define common configurations shared between jobs (e.g., model params)
- The right job task will be selected automatically thanks to [Pydantic Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions)
  - This is a great way to run any job supported by the application (training, tuning, ....

## Automation

This project includes several automation tasks to easily repeat common actions.

You can invoke the actions from the [command-line](https://www.pyinvoke.org/) or [VS Code extension](https://marketplace.visualstudio.com/items?itemName=dchanco.vsc-invoke).

```bash
# execute the project DAG
$ inv projects
# create a code archive
$ inv packages
# list other actions
$ inv --list
```

**Available tasks**:
- **checks.all (checks)** - Run all check tasks.
- **checks.code** - Check the codes with ruff.
- **checks.coverage** - Check the coverage with coverage.
- **checks.format** - Check the formats with ruff.
- **checks.poetry** - Check poetry config files.
- **checks.security** - Check the security with bandit.
- **checks.test** - Check the tests with pytest.
- **checks.type** - Check the types with mypy.
- **cleans.all (cleans)** - Run all tools and folders tasks.
- **cleans.cache** - Clean the cache folder.
- **cleans.coverage** - Clean the coverage tool.
- **cleans.dist** - Clean the dist folder.
- **cleans.docs** - Clean the docs folder.
- **cleans.environment** - Clean the project environment file.
- **cleans.folders** - Run all folders tasks.
- **cleans.mlruns** - Clean the mlruns folder.
- **cleans.mypy** - Clean the mypy tool.
- **cleans.outputs** - Clean the outputs folder.
- **cleans.poetry** - Clean poetry lock file.
- **cleans.pytest** - Clean the pytest tool.
- **cleans.projects** - Run all projects tasks.
- **cleans.python** - Clean python caches and bytecodes.
- **cleans.requirements** - Clean the project requirements file.
- **cleans.reset** - Run all tools, folders, and sources tasks.
- **cleans.ruff** - Clean the ruff tool.
- **cleans.sources** - Run all sources tasks.
- **cleans.tools** - Run all tools tasks.
- **cleans.venv** - Clean the venv folder.
- **commits.all (commits)** - Run all commit tasks.
- **commits.bump** - Bump the version of the package.
- **commits.commit** - Commit all changes with a message.
- **commits.info** - Print a guide for messages.
- **containers.all (containers)** - Run all container tasks.
- **containers.build** - Build the container image with the given tag.
- **containers.compose** - Start up docker compose.
- **containers.run** - Run the container image with the given tag.
- **docs.all (docs)** - Run all docs tasks.
- **docs.api** - Document the API with pdoc using the given format and output directory.
- **docs.serve** - Serve the API docs with pdoc using the given format and computer port.
- **formats.all** - (formats) Run all format tasks.
- **formats.imports** - Format python imports with ruff.
- **formats.sources** - Format python sources with ruff.
- **installs.all (installs)** - Run all install tasks.
- **installs.poetry** - Install poetry packages.
- **installs.pre-commit** - Install pre-commit hooks on git.
- **mlflow.all (mlflow)** - Run all mlflow tasks.
- **mlflow.doctor** - Run mlflow doctor to diagnose issues.
- **mlflow.serve** - Start mlflow server with the given host, port, and backend uri.
- **packages.all (packages)** - Run all package tasks.
- **packages.build** - Build a python package with the given format.
- **projects.all (projects)** - Run all project tasks.
- **projects.environment** - Export the project environment file.
- **projects.requirements** - Export the project requirements file.
- **projects.run** - Run an mlflow project from MLproject file.

## Workflows

This package supports two GitHub Workflows in `.github/workflows`:
- `check.yml`: validate the quality of the package on each Pull Request
- `publish.yml`: build and publish the docs and packages on code release.

You can use and extend these workflows to automate repetitive package management tasks.

# Tools

This sections motivates the use of developer tools to improve your coding experience.

## Automation

Pre-defined actions to automate your project development.

### Commits: [Commitizen](https://commitizen-tools.github.io/commitizen/)

- **Motivations**:
  - Format your code commits
  - Generate a standard changelog
  - Integrate well with [SemVer](https://semver.org/) and [PEP 440](https://peps.python.org/pep-0440/)
- **Limitations**:
  - Learning curve for new users
- **Alternatives**:
  - Do It Yourself (DIY)

### Git Hooks: [Pre-Commit](https://pre-commit.com/)

- **Motivations**:
  - Check your code locally before a commit
  - Avoid wasting resources on your CI/CD
  - Can perform extra actions (e.g., file cleanup)
- **Limitations**:
  - Add overhead before your commit
- **Alternatives**:
  - [Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks): less convenient to use

### Tasks: [PyInvoke](https://www.pyinvoke.org/)

- **Motivations**:
  - Automate project workflows
  - Sane syntax compared to alternatives
  - Good trade-off between power/simplicity
- **Limitations**:
  - Not familiar to most developers
- **Alternatives**:
  - [Make](https://www.gnu.org/software/make/manual/make.html): most popular, but awful syntax

## CI/CD

Execution of automated workflows on code push and releases.

### Runner: [GitHub Actions](https://github.com/features/actions)

- **Motivations**:
  - Native on GitHub
  - Simple workflow syntax
  - Lots of configs if needed
- **Limitations**:
  - SaaS Service
- **Alternatives**:
  - [GitLab](https://about.gitlab.com/): can be installed on-premise

## CLI

Integrations with the Command-Line Interface (CLI) of your system.

### Parser: [Argparse](https://docs.python.org/3/library/argparse.html)

- **Motivations**:
  - Provide CLI arguments
  - Included in Python runtime
  - Sufficient for providing configs
- **Limitations**:
  - More verbose for advanced parsing
- **Alternatives**:
  - [Typer](https://typer.tiangolo.com/): code typing for the win
  - [Fire](https://github.com/google/python-fire): simple but no typing
  - [Click](https://click.palletsprojects.com/en/latest/): more verbose

### Logging: [Loguru](https://loguru.readthedocs.io/en/stable/)

- **Motivations**:
  - Show progress to the user
  - Work fine out of the box
  - Saner logging syntax
- **Limitations**:
  - Doesn't let you deviate from the base usage
- **Alternatives**:
  - [Logging](https://docs.python.org/3/library/logging.html): available by default, but feel dated

## Code

Edition, validation, and versioning of your project source code.

### Coverage: [Coverage](https://coverage.readthedocs.io/en/latest/)

https://krijnvanderburg.medium.com/automatically-generate-and-visualize-python-code-coverage-308e65627925

- **Motivations**:
  - Report code covered by tests
  - Identify code path to test
  - Show maturity to users
- **Limitations**:
  - None
- **Alternatives**:
  - None?

### Editor: [VS Code](https://code.visualstudio.com/)

- **Motivations**:
  - Open source
  - Free, simple, open source
  - Great plugins for Python development
- **Limitations**:
  - Require some configuration for Python
- **Alternatives**:
  - [PyCharm](https://www.jetbrains.com/pycharm/): provide a lot, cost a lot
  - [Vim](https://www.vim.org/): I love it, but there is a VS Code plugin
  - [Spacemacs](https://www.spacemacs.org/): I love it even more, but not everybody loves LISP

### Formatting: [Ruff](https://docs.astral.sh/ruff/)

- **Motivations**:
  - Super fast compared to others
  - Don't waste time arranging your code
  - Make your code more readable/maintainable
- **Limitations**:
  - Still in version 0.x, but more and more adopted
- **Alternatives**:
  - [YAPF](https://github.com/google/yapf): more config options that you don't need
  - [Isort](https://pycqa.github.io/isort/) + [Black](https://black.readthedocs.io/en/stable/): slower and need two tools

### Quality: [Ruff](https://docs.astral.sh/ruff/)

- **Motivations**:
  - Improve your code quality
  - Super fast compared to others
  - [Great integration with VS Code](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- **Limitations**:
  - None
- **Alternatives**:
  - [PyLint](https://www.pylint.org/): too slow and too complex system
  - [Flake8](https://flake8.pycqa.org/en/latest/): too much plugins, I prefer Pylint in practice

### Security: [Bandit](https://bandit.readthedocs.io/en/latest/)

- **Motivations**:
  - Detect security issues
  - Complement linting solutions
  - Not to heavy to use and enable
- **Limitations**:
  - None
- **Alternatives**:
  - None

### Testing: [Pytest](https://docs.pytest.org/en/latest/)

- **Motivations**:
  - Write tests or pay the price
  - Super easy to write new test cases
  - Tons of good plugins (xdist, sugar, cov, ...)
- **Limitations**:
  - Doesn't support parallel execution out of the box
- **Alternatives**:
  - [Unittest](https://docs.python.org/fr/3/library/unittest.html): more verbose, less fun

### Typing: [Mypy](https://mypy-lang.org/)

- **Motivations**:
  - Static typing is cool!
  - Communicate types to use
  - Official type checker for Python
- **Limitations**:
  - Can have overhead for complex typing
- **Alternatives**:
  - [PyRight](https://github.com/microsoft/pyright): check big code base by MicroSoft
  - [PyType](https://google.github.io/pytype/): check big code base by Google
  - [Pyre](https://pyre-check.org/): check big code base by Facebook

### Code Versioning: [Git](https://git-scm.com/)

- **Motivations**:
  - If you don't version your code, you are a fool
  - Most popular source code manager (what else?)
  - Provide hooks to perform automation on some events
- **Limitations**:
  - Git can be hard: https://xkcd.com/1597/
- **Alternatives**:
  - [Mercurial](https://www.mercurial-scm.org/): loved it back then, but git is the only real option

### Data Versioning: [DVC](https://dvc.org/)


#### **Motivations**
- **Version Control for Data:** Just as versioning code is essential, versioning data ensures reproducibility, collaboration, and traceability in machine learning workflows.
- **Integration with Git:** DVC works seamlessly with Git, enabling you to track datasets and models alongside code.
- **Automation and Pipelines:** DVC provides tools for creating pipelines, automating data processing, and ensuring consistent workflows across teams.
- **Scalability:** Handles large datasets without burdening Git by storing data in external storage solutions.

#### **Features**
- **Data and Model Tracking:** Tracks datasets, models, and experiments without including large files in Git repositories.
- **External Storage Support:** Supports various storage backends, including AWS S3, Google Cloud Storage, Azure, SSH, and local file systems.
- **Reproducible Pipelines:** Allows users to define and execute machine learning workflows with dependencies and outputs tracked automatically.
- **Experiment Management:** Simplifies running and tracking multiple experiments, making comparisons straightforward.

#### **Limitations**
- **Learning Curve:** Requires understanding of Git and DVC-specific concepts to fully leverage its capabilities.
- **Complexity for Small Projects:** Overhead may not be justified for simple projects or teams unfamiliar with Git.
- **Storage Configuration:** Initial setup for remote storage can be tedious for non-technical users.
- **Dependency on Git:** Full functionality depends on having a properly configured Git repository.

#### **Alternatives**
- **[Git LFS](https://git-lfs.com/):** Focuses on large file versioning but lacks pipeline and experiment management capabilities.
- **[Pachyderm](https://www.pachyderm.com/):** Offers data versioning and pipeline management but is more suited for large-scale, enterprise environments.
- **[LakeFS](https://lakefs.io/):** A Git-like version control system specifically for data lakes.
- **[Quilt](https://quiltdata.com/):** Simplifies dataset sharing and versioning with a user-friendly UI.

#### **Additional Resources**
- **[Getting Started with DVC](https://dvc.org/doc/start):** Official tutorial for beginners.
- **[DVC Pipelines Guide](https://dvc.org/doc/user-guide/pipelines):** Learn to create reproducible pipelines.
- **[Remote Storage Setup](https://dvc.org/doc/user-guide/setup-remote):** Detailed instructions on configuring remote storage.
- **[DVC vs Git LFS](https://dvc.org/doc/user-guide/dvc-vs-git-lfs):** A comparison of DVC and Git LFS.

## Configs

Manage the configs files of your project to change executions.

### Format: [YAML](https://yaml.org/)

- **Motivations**:
  - Change execution without changing code
  - Readable syntax, support comments
  - Allow to use OmegaConf <3
- **Limitations**:
  - Not supported out of the box by Python
- **Alternatives**:
  - [JSON](https://www.json.org/json-en.html): no comments, more verbose
  - [TOML](https://toml.io/en/): less suited to config merge/sharing

### Parser: [OmegaConf](https://omegaconf.readthedocs.io/en/2.3_branch/)

- **Motivations**:
  - Parse and merge YAML files
  - Powerful, doesn't get in your way
  - Achieve a lot with few lines of code
- **Limitations**:
  - Do not support remote files (e.g., s3, gcs, ...)
    - You can combine it with [cloudpathlib](https://cloudpathlib.drivendata.org/stable/)
- **Alternatives**:
  - [Hydra](https://hydra.cc/docs/intro/): powerful, but gets in your way
  - [DynaConf](https://www.dynaconf.com/): more suited for app development

### Reader: [Cloudpathlib](https://cloudpathlib.drivendata.org/stable/)

- **Motivations**:
  - Read files from cloud storage
  - Better integration with cloud platforms
  - Support several platforms: AWS, GCP, and Azure
- **Limitations**:
  - Support of Python typing is not great at the moment
- **Alternatives**:
  - Cloud SDK (GCP, AWS, Azure, ...): vendor specific, overkill for this task

### Validator: [Pydantic](https://docs.pydantic.dev/latest/)

- **Motivations**:
  - Validate your config before execution
  - Pydantic should be builtin (period)
  - Super charge your Python class
- **Limitations**:
  - None
- **Alternatives**:
  - [Dataclass](https://docs.python.org/3/library/dataclasses.html): simpler, but much less powerful
  - [Attrs](https://www.attrs.org/en/stable/): no validation, less intuitive to use

## Data

Define the datasets to provide data inputs and outputs.

### Container: [Pandas](https://pandas.pydata.org/)

- **Motivations**:
  - Load data files in memory
  - Lingua franca for Python
  - Most popular options
- **Limitations**:
  - Lot of [gotchas](https://www.tutorialspoint.com/python_pandas/python_pandas_caveats_and_gotchas.htm)
- **Alternatives**:
  - [Polars](https://www.pola.rs/): faster, saner, but less integrations
  - [Pyspark](https://spark.apache.org/docs/latest/api/python/): powerful, popular, distributed, so much overhead
  - Dask, Ray, Modin, Vaex, ...: less integration (even if it looks like pandas)

### Format: [Parquet](https://parquet.apache.org/)

- **Motivations**:
  - Store your data on disk
  - Column-oriented (good for analysis)
  - Much more efficient and saner than text based
- **Limitations**:
  - None
- **Alternatives**:
  - [CSV](https://en.wikipedia.org/wiki/Comma-separated_values): human readable, but that's the sole benefit
  - [Avro](https://avro.apache.org/): good alternative for row-oriented workflow

### Schema: [Pandera](https://pandera.readthedocs.io/en/stable/)

- **Motivations**:
  - Typing for dataframe
  - Communicate data fields
  - Support pandas and [others](https://pandera.readthedocs.io/en/stable/supported_libraries.html)
- **Limitations**:
  - None
- **Alternatives**:
  - [Great Expectations](https://greatexpectations.io/): powerful, but much more difficult to integrate

## Docs

Generate and share the project documentations.

### API: [pdoc](https://pdoc.dev/)

- **Motivations**:
  - Share docs with others
  - Simple tool, only does API docs
  - Get the job done, get out of your way
- **Limitations**:
  - Only support API docs (i.e., no custom docs)
- **Alternatives**:
  - [Sphinx](https://www.sphinx-doc.org/en/master/): Most complete, overkill for simple projects
  - [Mkdocs](https://www.mkdocs.org/): no support for API doc, which is the core feature

### Format: [Google](https://google.github.io/styleguide/pyguide.html)

- **Motivations**:
  - Common style for docstrings
  - Most writeable out of alternatives
  - I often write a single line for simplicity
- **Limitations**:
  - None
- **Alternatives**:
  - [Numpy](https://numpydoc.readthedocs.io/en/latest/format.html): less writeable
  - [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html): baroque style

### Hosting: [GitHub Pages](https://pages.github.com/)

- **Motivations**:
  - Easy to setup
  - Free and simple
  - Integrated with GitHub
- **Limitations**:
  - Only support static content
- **Alternatives**:
  - [ReadTheDocs](https://about.readthedocs.com/?ref=readthedocs.com): provide more features

## Model

Toolkit to handle machine learning models.

### Evaluation: [Scikit-Learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)

- **Motivations**:
  - Bring common metrics
  - Avoid reinventing the wheel
  - Avoid implementation mistakes
- **Limitations**:
  - Limited set of metric to be chosen
- **Alternatives**:
  - Implement your own: for custom metrics

### Format: [Mlflow Model](https://mlflow.org/docs/latest/models.html)

- **Motivations**:
  - Standard ML format
  - Store model dependencies
  - Strong community ecosystem
- **Limitations**:
  - None
- **Alternatives**:
  - [Pickle](https://docs.python.org/3/library/pickle.html): work out of the box, but less suited for big array
  - [ONNX](https://onnx.ai/): great for deep learning, [no guaranteed compatibility for the rest](https://onnxruntime.ai/docs/reference/compatibility.html)

### Registry: [Mlflow Registry](https://mlflow.org/docs/latest/model-registry.html)

- **Motivations**:
  - Save and load models
  - Separate production from consumption
  - Popular, open source, work on local system
- **Limitations**:
  - None
- **Alternatives**:
  - [Neptune.ai](https://neptune.ai/): SaaS solution
  - [Weights and Biases](https://wandb.ai/site): SaaS solution

### Tracking: [Mlflow Tracking](https://mlflow.org/docs/latest/tracking.html)

- **Motivations**:
  - Keep track of metrics and params
  - Allow to compare model performances
  - Popular, open source, work on local system
- **Limitations**:
  - None
- **Alternatives**:
  - [Neptune.ai](https://neptune.ai/): SaaS solution
  - [Weights and Biases](https://wandb.ai/site): SaaS solution

## Package

Define and build modern Python package.

### Evolution: [Changelog](https://en.wikipedia.org/wiki/Changelog)

- **Motivation**:
  - Communicate changes to user
  - Can be updated with [Commitizen](https://commitizen-tools.github.io/commitizen/changelog/)
  - Standardized with [Keep a Changelog](https://keepachangelog.com/)
- **Limitations**:
  - None
- **Alternatives**:
  - None

### Format: [Wheel](https://peps.python.org/pep-0427/)

- **Motivations**:
  - [Has several advantages](https://realpython.com/python-wheels/#advantages-of-python-wheels)
  - Create source code archive
  - Most modern Python format
- **Limitations**:
  - Doesn't ship with C/C++ dependencies (e.g., CUDA)
    - i.e., use Docker containers for this case
- **Alternatives**:
  - [Source](https://docs.python.org/3/distutils/sourcedist.html): older format, less powerful
  - [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html): slow and hard to manage

### Manager: [Poetry](https://python-poetry.org/)

- **Motivations**:
  - Define and build Python package
  - Most popular solution by GitHub stars
  - Pack every metadata in a single static file
- **Limitations**:
  - Cannot add dependencies beyond Python (e.g., CUDA)
    - i.e., use Docker container for this use case
- **Alternatives**:
  - [Setuptools](https://docs.python.org/3/distutils/setupscript.html): dynamic file is slower and more risky
  - Pdm, Hatch, PipEnv: https://xkcd.com/1987/

### Runtime: [Docker](https://www.docker.com/resources/what-container/)

- **Motivations**:
  - Create isolated runtime
  - Container is the de facto standard
  - Package C/C++ dependencies with your project
- **Limitations**:
  - Some company might block Docker Desktop, you should use alternatives
- **Alternatives**:
  - [Conda](https://docs.conda.io/en/latest/): slow and heavy resolver

## Programming

Select your programming environment.

### Language: [Python](https://www.python.org/)

- **Motivations**:
  - Great language for AI/ML projects
  - Robust with additional tools
  - Hundreds of great libs
- **Limitations**:
  - Slow without C bindings
- **Alternatives**:
  - [R](https://www.r-project.org/): specific purpose language
  - [Julia](https://julialang.org/): specific purpose language

### Version: [Pyenv](https://github.com/pyenv/pyenv)

- **Motivations**:
  - Switch between Python version
  - Allow to select the best version
  - Support global and local dispatch
- **Limitations**:
  - Require some shell configurations
- **Alternatives**:
  - Manual installation: time consuming

## Observability

### Reproducibility: [Mlflow Project](https://mlflow.org/docs/latest/projects.html)

- **Motivations**:
  - Share common project formats.
  - Ensure the project can be reused.
  - Avoid randomness in project execution.
- **Limitations**:
  - Mlflow Project is best suited for small projects.
- **Alternatives**:
  - [DVC](https://dvc.org/): both data and models.
  - [Metaflow](https://metaflow.org/): focus on machine learning.
  - **[Apache Airflow](https://airflow.apache.org/)**: for large scale projects.

### Monitoring : [Mlflow Evaluate](https://mlflow.org/docs/latest/model-evaluation/index.html)

- **Motivations**:
  - Compute the model metrics.
  - Validate model with thresholds.
  - Perform post-training evaluations.
- **Limitations**:
  - Mlflow Evaluate is less feature-rich as alternatives.
- **Alternatives**:
  - **[Giskard](https://www.giskard.ai/)**: open-core and super complete.
  - **[Evidently](https://www.evidentlyai.com/)**: open-source with more metrics.
  - [Arize AI](https://arize.com/): more feature-rich but less flexible.
  - [Graphana](https://grafana.com/): you must do everything yourself.

### Alerting: [Plyer](https://github.com/kivy/plyer)

- **Motivations**:
  - Simple solution.
  - Send notifications on system.
  - Cross-system: Mac, Linux, Windows.
- **Limitations**:
  - Should not be used for large scale projects.
- **Alternatives**:
  - [Slack](https://slack.com/): for chat-oriented solutions.
  - [Datadog](https://www.datadoghq.com/): for infrastructure oriented solutions.

### Lineage: [Mlflow Dataset](https://mlflow.org/docs/latest/tracking/data-api.html)

- **Motivations**:
  - Store information in Mlflow.
  - Track metadata about run datasets.
  - Keep URI of the dataset source (e.g., website).
- **Limitations**:
  - Not as feature-rich as alternative solutions.
- **Alternatives**:
  - [Databricks Lineage](https://docs.databricks.com/en/admin/system-tables/lineage.html): limited to Databricks.
  - [OpenLineage and Marquez](https://marquezproject.github.io/): open-source and flexible.

### Explainability: [SHAP](https://shap.readthedocs.io/en/latest/)

- **Motivations**:
  - Most popular toolkit.
  - Support various models (linear, model, ...).
  - Integration with Mlflow through the [SHAP module](https://mlflow.org/docs/latest/python_api/mlflow.shap.html).
- **Limitations**:
  - Super slow on large dataset.
  - Mlflow SHAP module is not mature enough.
- **Alternatives**:
  - [LIME](https://github.com/marcotcr/lime): not maintained anymore.

### Infrastructure: [Mlflow System Metrics](https://mlflow.org/docs/latest/system-metrics/index.html)

- **Motivations**:
  - Track infrastructure information (RAM, CPU, ...).
  - Integrated with Mlflow tracking.
  - Provide hardware insights.
- **Limitations**:
  - Not as mature as alternative solutions.
- **Alternatives**:
  - [Datadog](https://www.datadoghq.com/): popular and mature solution.

# Tips

This sections gives some tips and tricks to enrich the develop experience.

```bash
pyreverse  -A -o plantuml -p autogen_team src/autogen_team
```
## [AI/ML Practices](https://machinelearningmastery.com/)

### [Data Catalog](https://docs.kedro.org/en/stable/data/data_catalog.html)

**You should decouple the pointer to your data from how to access it.**

In your code, you can refer to your dataset with a tag (e.g., `inputs`, `targets`).

This tag can then be associated to a reader/writer implementation in a configuration file:

```yaml
  inputs:
    KIND: ParquetReader
    path: data/inputs_train.parquet
  targets:
    KIND: ParquetReader
    path: data/targets_train.parquet
```

In this package, the implementation are described in `src/[package]/io/datasets.py` and selected by `KIND`.

### [Hyperparameter Optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization)

**You should select the best hyperparameters for your model using optimization search.**

The simplest projects can use a `sklearn.model_selection.GridSearchCV` to scan the whole search space.

This package provides a simple interface to this hyperparameter search facility in `src/[package]/utils/searchers.py`.

For more complex project, we recommend to use more complex strategy (e.g., [Bayesian](https://en.wikipedia.org/wiki/Bayesian_optimization)) and software package (e.g., [Optuna](https://optuna.org/)).

### [Data Splits](https://machinelearningmastery.com/difference-test-validation-datasets/)

**You should properly split your dataset into a training, validation, and testing sets.**

- *Training*: used for fitting the model parameters
- *Validation*: used to find the best hyperparameters
- *Testing*: used to evaluate the final model performance

The sets should be exclusive, and the testing set should never be used as training inputs!

This package provides a simple deterministic strategy implemented in `src/[package]/utils/splitters.py`.

## [Design Patterns](https://en.wikipedia.org/wiki/Software_design_pattern)

### [Directed-Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

**You should use Directed-Acyclic Graph (DAG) to connect the steps of your ML pipeline.**

A DAG can express the dependencies between steps while keeping the individual step independent.

This package provides a simple DAG example in `tasks/dags.py`. This approach is based on [PyInvoke](https://www.pyinvoke.org/).

In production, we recommend to use a scalable system such as [Airflow](https://airflow.apache.org/), [Dagster](https://dagster.io/), [Prefect](https://www.prefect.io/), [Metaflow](https://metaflow.org/), or [ZenML](https://zenml.io/).

### [Program Service](https://en.wikipedia.org/wiki/Systemd)

**You should provide a global context for the execution of your program.**

There are several approaches such as [Singleton](https://en.wikipedia.org/wiki/Singleton_pattern), [Global Variable](https://en.wikipedia.org/wiki/Global_variable), or [Component](https://github.com/stuartsierra/component).

This package takes inspiration from [Clojure mount](https://github.com/tolitius/mount). It provides an implementation in `src/[package]/io/services.py`.

### [Soft Coding](https://en.wikipedia.org/wiki/Softcoding)

**You should separate the program implementation from the program configuration.**

Exposing configurations to users allow them to influence the execution behavior without code changes.

This package seeks to expose as much parameter as possible to the users in configurations stored in the `confs/` folder.

### [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

**You should implement the SOLID principles to make your code as flexible as possible.**

- *Single responsibility principle*:  Class has one job to do. Each change in requirements can be done by changing just one class.
- *Open/closed principle*: Class is happy (open) to be used by others. Class is not happy (closed) to be changed by others.
- *Liskov substitution principle*: Class can be replaced by any of its children. Children classes inherit parent's behaviours.
- *Interface segregation principle*: When classes promise each other something, they should separate these promises (interfaces) into many small promises, so it's easier to understand.
- *Dependency inversion principle*: When classes talk to each other in a very specific way, they both depend on each other to never change. Instead classes should use promises (interfaces, parents), so classes can change as long as they keep the promise.

In practice, this mean you can implement software contracts with interface and swap the implementation.

For instance, you can implement several jobs in `src/[package]/jobs/*.py` and swap them in your configuration.

To learn more about the mechanism select for this package, you can check the documentation for [Pydantic Tagged Unions](https://docs.pydantic.dev/dev-v2/usage/types/unions/#discriminated-unions-aka-tagged-unions).

### [IO Separation](https://en.wikibooks.org/wiki/Haskell/Understanding_monads/IO)

**You should separate the code interacting with the external world from the rest.**

The external is messy and full of risks: missing files, permission issue, out of disk ...

To isolate these risks, you can put all the related code in an `io` package and use interfaces

## [Python Powers](https://realpython.com/)

### [Context Manager](https://docs.python.org/3/library/contextlib.html)

**You should use Python context manager to control and enhance an execution.**

Python provides contexts that can be used to extend a code block. For instance:

```python
# in src/[package]/scripts.py
with job as runner:  # context
    runner.run()  # run in context
```

This pattern has the same benefit as [Monad](https://en.wikipedia.org/wiki/Monad_(functional_programming)), a powerful programming pattern.

The package uses `src/[package]/jobs/*.py` to handle exception and services.

### [Python Package](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

**You should create Python package to create both library and application for others.**

Using Python package for your AI/ML project has the following benefits:
- Build code archive (i.e., wheel) that be uploaded to Pypi.org
- Install Python package as a library (e.g., like pandas)
- Expose script entry points to run a CLI or a GUI

To build a Python package with Poetry, you simply have to type in a terminal:
```bash
# for all poetry project
poetry build
# for this project only
inv packages
```

## [Software Engineering](https://en.wikipedia.org/wiki/Software_engineering)

### [Code Typing](https://docs.python.org/3/library/typing.html)

**You should type your Python code to make it more robust and explicit for your user.**

Python provides the [typing module](https://docs.python.org/3/library/typing.html) for adding type hints and [mypy](https://mypy-lang.org/) to checking them.

```python
# in src/[package]/core/models.py
@abc.abstractmethod
def fit(self, inputs: schemas.Inputs, targets: schemas.Targets) -> "Model":
    """Fit the model on the given inputs and target."""

@abc.abstractmethod
def predict(self, inputs: schemas.Inputs) -> schemas.Outputs:
    """Generate an output with the model for the given inputs."""
```

This code snippet clearly state the inputs and outputs of the method, both for the developer and the type checker.

The package aims to type every functions and classes to facilitate the developer experience and fix mistakes before execution.

### [Config Typing](https://docs.pydantic.dev/latest/)

**You should type your configuration to avoid exceptions during the program execution.**

Pydantic allows to define classes that can validate your configs during the program startup.

```python
# in src/[package]/utils/splitters.py
class TrainTestSplitter(Splitter):
    shuffle: bool = False  # required (time sensitive)
    test_size: int | float = 24 * 30 * 2  # 2 months
    random_state: int = 42
```

This code snippet allows to communicate the values expected and avoid error that could be avoided.

The package combines both OmegaConf and Pydantic to parse YAML files and validate them as soon as possible.

### [Dataframe Typing](https://pandera.readthedocs.io/en/stable/)

**You should type your dataframe to communicate and validate their fields.**

Pandera supports dataframe typing for Pandas and other library like PySpark:

```python
# in src/package/schemas.py
class InputsSchema(Schema):
    instant: papd.Index[papd.UInt32] = pa.Field(ge=0, check_name=True)
    dteday: papd.Series[papd.DateTime] = pa.Field()
    season: papd.Series[papd.UInt8] = pa.Field(isin=[1, 2, 3, 4])
    yr: papd.Series[papd.UInt8] = pa.Field(ge=0, le=1)
    mnth: papd.Series[papd.UInt8] = pa.Field(ge=1, le=12)
    hr: papd.Series[papd.UInt8] = pa.Field(ge=0, le=23)
    holiday: papd.Series[papd.Bool] = pa.Field()
    weekday: papd.Series[papd.UInt8] = pa.Field(ge=0, le=6)
    workingday: papd.Series[papd.Bool] = pa.Field()
    weathersit: papd.Series[papd.UInt8] = pa.Field(ge=1, le=4)
    temp: papd.Series[papd.Float16] = pa.Field(ge=0, le=1)
    atemp: papd.Series[papd.Float16] = pa.Field(ge=0, le=1)
    hum: papd.Series[papd.Float16] = pa.Field(ge=0, le=1)
    windspeed: papd.Series[papd.Float16] = pa.Field(ge=0, le=1)
    casual: papd.Series[papd.UInt32] = pa.Field(ge=0)
    registered: papd.Series[papd.UInt32] = pa.Field(ge=0)
```

This code snippet defines the fields of the dataframe and some of its constraint.

The package encourages to type every dataframe used in `src/[package]/core/schemas.py`.

### [Object Oriented](https://en.wikipedia.org/wiki/Object-oriented_programming)

**You should use the Objected Oriented programming to benefit from [polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)).**

Polymorphism combined with SOLID Principles allows to easily swap your code components.

```python
class Reader(abc.ABC, pdt.BaseModel):

    @abc.abstractmethod
    def read(self) -> pd.DataFrame:
        """Read a dataframe from a dataset."""
```

This code snippet uses the [abc module](https://docs.python.org/3/library/abc.html) to define code interfaces for a dataset with a read/write method.

The package defines class interface whenever possible to provide intuitive and replaceable parts for your AI/ML project.

### [Semantic Versioning](https://semver.org/)

**You should use semantic versioning to communicate the level of compatibility of your releases.**

Semantic Versioning (SemVer) provides a simple schema to communicate code changes. For package X.Y.Z:
- *Major* (X): major release with breaking changed (i.e., imply actions from the benefit)
- *Minor* (Y): minor release with new features (i.e., provide new capabilities)
- *Patch* (Z): patch release to fix bugs (i.e., correct wrong behavior)

Poetry and this package leverage Semantic Versioning to let developers control the speed of adoption for new releases.

## [Testing Tricks](https://en.wikipedia.org/wiki/Software_testing)

### [Parallel Testing](https://pytest-xdist.readthedocs.io/en/stable/)

**You can run your tests in parallel to speed up the validation of your code base.**

Pytest can be extended with the [pytest-xdist plugin](https://pytest-xdist.readthedocs.io/en/stable/) for this purpose.

This package enables Pytest in its automation tasks by default.

### [Test Fixtures](https://docs.pytest.org/en/latest/explanation/fixtures.html)

**You should define reusable objects and actions for your tests with [fixtures](https://docs.pytest.org/en/latest/explanation/fixtures.html).**

Fixture can prepare objects for your test cases, such as dataframes, models, files.

This package defines fixtures in `tests/conftest.py` to improve your testing experience.

## [VS Code](https://code.visualstudio.com/)

### [Code Workspace](https://code.visualstudio.com/docs/editor/workspaces)

**You can use VS Code workspace to define configurations for your project.**

[Code Workspace](https://code.visualstudio.com/docs/editor/workspaces) can enable features (e.g. formatting) and set the default interpreter.

```json
{
	"settings": {
		"editor.formatOnSave": true,
		"python.defaultInterpreterPath": ".venv/bin/python",
    ...
	},
}
```

This package defines a workspace file that you can load from `[package].code-workspace`.

### [GitHub Copilot](https://github.com/features/copilot)

**You can use GitHub Copilot to increase your coding productivity by 30%.**

[GitHub Copilot](https://github.com/features/copilot) has been a huge productivity thanks to its smart completion.

You should become familiar with the solution in less than a single coding session.

### [VSCode VIM](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

**You can use VIM keybindings to more efficiently navigate and modify your code.**

Learning VIM is one of the best investment for a career in IT. It can make you 30% more productive.

Compared to GitHub Copilot, VIM can take much more time to master. You can expect a ROI in less than a month.

# Resources

This section provides resources for building packages for Python and AI/ML/MLOps.

## Python

- https://github.com/krzjoa/awesome-python-data-science#readme
- https://github.com/ml-tooling/best-of-ml-python
- https://github.com/ml-tooling/best-of-python
- https://github.com/ml-tooling/best-of-python-dev
- https://github.com/vinta/awesome-python

## AI/ML/MLOps

- https://github.com/josephmisiti/awesome-machine-learning
- https://github.com/visenger/awesome-mlops

## UML course:

En UML, las relaciones entre clases suelen dividirse en cuatro tipos principales de dependencias o relaciones: **asociación**, **agregación**, **composición**, y **dependencia**. A continuación, se explican cada una con ejemplos en Python y cómo se representan en un diagrama UML.

---

### 1. **Asociación**
- Representa una relación entre dos clases que colaboran entre sí.
- Es una relación débil y bidireccional (en general).
- Ejemplo: Un `Alumno` se asocia con un `Profesor`.

#### Código Python:
```python
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor  # Relación de asociación

# Ejemplo de uso
profesor = Profesor("Dr. García")
alumno = Alumno("Juan", profesor)

print(f"{alumno.nombre} tiene como profesor a {alumno.profesor.nombre}")
```

#### Representación UML:
- Línea sólida simple entre `Alumno` y `Profesor`.

---

### 2. **Agregación**
- Es un tipo especial de asociación.
- Representa una relación "todo-parte", pero donde las partes pueden existir independientemente del todo.
- Ejemplo: Un `Departamento` tiene varios `Empleado`s, pero si el departamento deja de existir, los empleados pueden seguir existiendo.

#### Código Python:
```python
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []  # Relación de agregación

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

# Ejemplo de uso
empleado1 = Empleado("Alice")
empleado2 = Empleado("Bob")
departamento = Departamento("Recursos Humanos")
departamento.agregar_empleado(empleado1)
departamento.agregar_empleado(empleado2)

print(f"El departamento {departamento.nombre} tiene a:")
for empleado in departamento.empleados:
    print(f"- {empleado.nombre}")
```

#### Representación UML:
- Línea con un rombo vacío en el lado del "todo" (`Departamento`).

---

### 3. **Composición**
- Es una relación "todo-parte" más fuerte.
- Las partes no pueden existir sin el todo.
- Ejemplo: Un `Coche` tiene un `Motor`, y si el coche deja de existir, el motor también.

#### Código Python:
```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)  # Relación de composición

# Ejemplo de uso
coche = Coche("Toyota", "V8")
print(f"El coche {coche.marca} tiene un motor {coche.motor.tipo}")
```

#### Representación UML:
- Línea con un rombo sólido en el lado del "todo" (`Coche`).

---

### 4. **Dependencia**
- Representa que una clase utiliza otra temporalmente.
- Es la relación más débil y generalmente unidireccional.
- Ejemplo: Una `Impresora` depende de un `Documento` para imprimirlo.

#### Código Python:
```python
class Documento:
    def __init__(self, texto):
        self.texto = texto

class Impresora:
    def imprimir(self, documento):
        print(f"Imprimiendo documento: {documento.texto}")

# Ejemplo de uso
doc = Documento("Informe Anual")
impresora = Impresora()
impresora.imprimir(doc)
```

#### Representación UML:
- Línea punteada con una flecha hacia la clase que se utiliza (`Documento`).

---

### Resumen de Relaciones:
| Relación      | Código Python               | UML                       |
|---------------|-----------------------------|---------------------------|
| Asociación    | `profesor` dentro de `Alumno` | Línea sólida simple       |
| Agregación    | `empleados` dentro de `Departamento` | Línea con rombo vacío     |
| Composición   | `motor` dentro de `Coche`    | Línea con rombo sólido    |
| Dependencia   | `Impresora` usa `Documento` | Línea punteada            |

Aquí tienes los ejemplos representados en **Mermaid**, un lenguaje para generar diagramas en Markdown. Puedes copiar y pegar estos diagramas en un entorno compatible con Mermaid (como un editor Markdown con soporte, GitHub, o un visor en línea).

---

### 1. Asociación
```mermaid
classDiagram
    class Alumno {
        -nombre: string
        -profesor: Profesor
    }
    class Profesor {
        -nombre: string
    }
    Alumno --> Profesor : tiene
```

---

### 2. Agregación
```mermaid
classDiagram
    class Departamento {
        -nombre: string
        -empleados: List<Empleado>
        +agregar_empleado(empleado: Empleado): void
    }
    class Empleado {
        -nombre: string
    }
    Departamento o-- Empleado : contiene
```

---

### 3. Composición
```mermaid
classDiagram
    class Coche {
        -marca: string
        -motor: Motor
    }
    class Motor {
        -tipo: string
    }
    Coche *-- Motor : contiene
```

---

### 4. Dependencia
```mermaid
classDiagram
    class Impresora {
        +imprimir(documento: Documento): void
    }
    class Documento {
        -texto: string
    }
    Impresora ..> Documento : usa
```

---

### Cómo interpretar:
- **Línea sólida simple (`-->`)**: Representa una asociación.
- **Rombo vacío (`o--`)**: Representa una agregación.
- **Rombo sólido (`*--`)**: Representa una composición.
- **Línea punteada (`..>`)**: Representa una dependencia.
Cuando una clase es **derivada** de otra, la relación entre ellas es de **herencia**. En UML, la herencia se representa con una **línea sólida con una flecha hueca** que apunta de la clase derivada a la clase base.

### Ejemplo en Python
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Ladra"

class Gato(Animal):
    def hacer_sonido(self):
        return "Maulla"

# Ejemplo de uso
perro = Perro("Firulais")
gato = Gato("Misu")

print(f"{perro.nombre} {perro.hacer_sonido()}")
print(f"{gato.nombre} {gato.hacer_sonido()}")
```

### Representación en Mermaid para UML
```mermaid
classDiagram
    class Animal {
        -nombre: string
        +hacer_sonido(): string
    }
    class Perro {
        +hacer_sonido(): string
    }
    class Gato {
        +hacer_sonido(): string
    }
    Animal <|-- Perro
    Animal <|-- Gato
```

---

### Explicación:
- **Animal** es la clase base o superclase.
- **Perro** y **Gato** son clases derivadas o subclases.
- La relación de herencia indica que las subclases heredan los atributos y métodos de la clase base, pero pueden sobrescribirlos (como `hacer_sonido` en este caso).

## Monitoring
best option [Evidentlyai](https://www.evidentlyai.com/) 

## docker compose example:

```txt

  kafka_inference:
      image: autogen_team:latest
      restart: unless-stopped
      container_name: kafka_inference
      networks:
        - servnet
        - minio_mlflow_mlflownet
      environment:
      - DEFAULT_KAFKA_SERVER=kafka_server:9092
      - DEFAULT_GROUP_ID=llmops-regression
      - DEFAULT_AUTO_OFFSET_RESET=earliest
      - DEFAULT_INPUT_TOPIC=llm_input_topic
      - DEFAULT_OUTPUT_TOPIC=llm_output_topic
      - DEFAULT_FASTAPI_HOST=127.0.0.1
      - DEFAULT_FASTAPI_PORT=8100
      - MLFLOW_TRACKING_URI=http://mlflow_server:5000
      - MLFLOW_REGISTRY_URI=http://mlflow_server:5000
      - MLFLOW_EXPERIMENT_NAME=autogen_team_experiment
      - MLFLOW_REGISTERED_MODEL_NAME=autogen_team
      - MLFLOW_EXPERIMENT_NAME=autogen_team_experiment
      - MLFLOW_REGISTERED_MODEL_NAME=autogen_team_model

      ports:
          - 8200:8100
      extra_hosts:
        - "host.docker.internal:host-gateway"
```
## autogen Studio.

autogenstudio ui --port 8081

## openai with mlflow example: 
https://mlflow.org/docs/latest/llms/openai/notebooks/openai-code-helper.html
https://mlflow.org/docs/latest/llms/openai/index.html#introduction
