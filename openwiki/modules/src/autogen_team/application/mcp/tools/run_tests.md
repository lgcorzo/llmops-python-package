---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: run_tests"
source_path: "src/autogen_team/application/mcp/tools/run_tests.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-08-06T06:46:32.976356+00:00"
---

# Module Specification: run_tests

* **Source Reference:** `src/autogen_team/application/mcp/tools/run_tests.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to run tests.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Manage and execute operations for run_tests.

**Main Workflow:**
- Initialize components and process requests for run_tests.

## 2. Dependencies
**Imports:**
- `__future__.annotations`
- `abc`
- `os`
- `shutil`
- `subprocess`
- `sys`
- `tempfile`
- `typing`
- `loguru.logger`
- `autogen_team.core.security.safe_join`

**Exported Classes:**
- `SandboxBackend`
- `SubprocessSandbox`
- `FirecrackerSandbox`

**Exported Functions:**
- `run_tests`

## 3. Architecture & Execution
### Internal Architecture
Follows standard modular design, encapsulating state and behavior within defined classes and functions.

### Execution Flow
Sequential execution of defined functions and class methods.

### Sequence Explanation
Clients instantiate classes or call functions, which execute business logic and return results.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    class SandboxBackend {
        +run_tests() : Any
    }
    class SubprocessSandbox {
        +run_tests() : Any
    }
    class FirecrackerSandbox {
        +__init__() : Any
        +run_tests() : Any
    }
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [__future__.annotations] : imports
    [Module] --> [abc] : imports
    [Module] --> [os] : imports
    [Module] --> [shutil] : imports
    [Module] --> [subprocess] : imports
    [Module] --> [sys] : imports
    [Module] --> [tempfile] : imports
    [Module] --> [typing] : imports
    [Module] --> [loguru.logger] : imports
    [Module] --> [autogen_team.core.security.safe_join] : imports
@enduml
```

## 5. Class & Method Specifications
### `SandboxBackend` ([`src/autogen_team/application/mcp/tools/run_tests.py`](/src/autogen_team/application/mcp/tools/run_tests.py))
#### Overview
Abstract sandbox backend for running tests.

Provides an interface for future Firecracker MicroVM integration.

#### Attributes
- None found.

#### Methods
##### `run_tests(self, workspace_dir: str, timeout: int) -> Any` (Public)
**Description:** Run tests in the sandbox.

Args:
    workspace_dir: Path to the workspace with changes applied.
    timeout: Maximum execution time in seconds.

Returns:
    Dict with passed, summary, and details fields.

**Inputs:**
- `workspace_dir`: str
- `timeout`: int

**Output:**
- Return Type: `Any`
- Semantic Meaning: The resulting value after processing the run_tests action.

**Side Effects:**
- Modifies internal instance state if applicable; performs operations constrained to its domain boundaries.

**Complexity:**
- Time Complexity: O(1) or O(N) depending on implementation details.
- Space Complexity: O(1) auxiliary space expected.

**Example:**
```python
result = SandboxBackend.run_tests(..., ...)
```

### `SubprocessSandbox` ([`src/autogen_team/application/mcp/tools/run_tests.py`](/src/autogen_team/application/mcp/tools/run_tests.py))
#### Overview
Subprocess-based sandbox for running pytest.

#### Attributes
- None found.

#### Methods
##### `run_tests(self, workspace_dir: str, timeout: int) -> Any` (Public)
**Description:** Run pytest via subprocess in the given workspace.

Args:
    workspace_dir: Path to the workspace with changes applied.
    timeout: Maximum execution time in seconds.

Returns:
    Dict with passed, summary, and details fields.

**Inputs:**
- `workspace_dir`: str
- `timeout`: int

**Output:**
- Return Type: `Any`
- Semantic Meaning: The resulting value after processing the run_tests action.

**Side Effects:**
- Modifies internal instance state if applicable; performs operations constrained to its domain boundaries.

**Complexity:**
- Time Complexity: O(1) or O(N) depending on implementation details.
- Space Complexity: O(1) auxiliary space expected.

**Example:**
```python
result = SubprocessSandbox.run_tests(..., ...)
```

### `FirecrackerSandbox` ([`src/autogen_team/application/mcp/tools/run_tests.py`](/src/autogen_team/application/mcp/tools/run_tests.py))
#### Overview
Firecracker-based sandbox using SandboxService.

#### Constructor
**Initialization:** Initializes `FirecrackerSandbox` with required dependencies and sets up initial internal state.

#### Attributes
- `service`

#### Methods
##### `__init__(self, sandbox_service: Any) -> Any` (Public)
**Description:** Executes the __init__ operation, mutating state or calculating derived values as necessary.

**Inputs:**
- `sandbox_service`: Any

**Output:**
- Return Type: `Any`
- Semantic Meaning: The resulting value after processing the __init__ action.

**Side Effects:**
- Modifies internal instance state if applicable; performs operations constrained to its domain boundaries.

**Complexity:**
- Time Complexity: O(1) or O(N) depending on implementation details.
- Space Complexity: O(1) auxiliary space expected.

**Example:**
```python
instance = FirecrackerSandbox()
result = instance.__init__(...)
```

##### `run_tests(self, workspace_dir: str, timeout: int) -> Any` (Public)
**Description:** Note: This is a synchronous wrapper for the async service.
In a real scenario, the tool should be async.

**Inputs:**
- `workspace_dir`: str
- `timeout`: int

**Output:**
- Return Type: `Any`
- Semantic Meaning: The resulting value after processing the run_tests action.

**Side Effects:**
- Modifies internal instance state if applicable; performs operations constrained to its domain boundaries.

**Complexity:**
- Time Complexity: O(1) or O(N) depending on implementation details.
- Space Complexity: O(1) auxiliary space expected.

**Example:**
```python
instance = FirecrackerSandbox()
result = instance.run_tests(..., ...)
```

## 6. Module Functions
### `run_tests(changes: Any, workspace_path: str, timeout: int, sandbox: Any)`
Run pytest against code changes in an isolated sandbox.

Args:
    changes: Dict with files_changed list (path, action, content).
    workspace_path: Original workspace path to copy from.
    timeout: Max execution time in seconds.
    sandbox: Optional sandbox backend (defaults to SubprocessSandbox).

Returns:
    Dict with passed bool, summary string, and details.

**Inputs:**
- `changes`: Any
- `workspace_path`: str
- `timeout`: int
- `sandbox`: Any

**Output:**
- Return Type: `Any`
