---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: okf_validate"
source_path: "skills/validate/scripts/okf_validate.py"
description: "AST-generated documentation for the module."
tags: ["generated", "ast"]
timestamp: "2026-09-02T05:14:17.114881+00:00"
---

# Module Specification: okf_validate

* **Source Reference:** `skills/validate/scripts/okf_validate.py`

## 1. Architectural Role & Responsibilities
**Purpose:**
Provides functionality related to okf validate.

**Architecture Layer:**
- Infrastructure/Other

**Responsibilities:**
- Not explicitly defined.

**Main Workflow:**
- Not explicitly defined.

## 2. Dependencies
**Imports:**
- `argparse`
- `glob`
- `os`
- `re`
- `sys`
- `typing.Any`

**Exported Classes:**
- None

**Exported Functions:**
- `extract_frontmatter`
- `check_frontmatter_fields`
- `check_absolute_paths`
- `check_mermaid_syntax`
- `validate_wiki`
- `main`

**Exported Interfaces:**
- Not explicitly defined.

**Public API:**
- Not explicitly defined.

## 3. Architecture & Execution
### Internal Architecture
Not explicitly defined.

### Execution Flow
Not explicitly defined.

### Sequence Explanation
Not explicitly defined.

### Examples
Not explicitly defined.

## 4. UML 2.0 Diagrams
### Class Diagram
```plantuml
@startuml
    ' No classes found in module
@enduml
```

### Package Diagram
```plantuml
@startuml
    package "skills" {
        package "validate" {
            package "scripts" {
                [okf_validate.py]
            }
        }
    }
@enduml
```

### Sequence Diagram
```plantuml
@startuml
    extract_frontmatter -> split : call
    extract_frontmatter -> len : call
    extract_frontmatter -> _parse_yaml : call
    extract_frontmatter -> startswith : call
    check_frontmatter_fields -> join : call
    check_frontmatter_fields -> sorted : call
    check_frontmatter_fields -> append : call
    check_frontmatter_fields -> get : call
    check_absolute_paths -> splitlines : call
    check_absolute_paths -> append : call
    check_absolute_paths -> search : call
    check_absolute_paths -> enumerate : call
    check_mermaid_syntax -> count : call
    check_mermaid_syntax -> append : call
    check_mermaid_syntax -> enumerate : call
    check_mermaid_syntax -> strip : call
    check_mermaid_syntax -> startswith : call
    check_mermaid_syntax -> splitlines : call
    validate_wiki -> relpath : call
    validate_wiki -> read : call
    validate_wiki -> glob : call
    validate_wiki -> print : call
    validate_wiki -> extend : call
    validate_wiki -> extract_frontmatter : call
    validate_wiki -> append : call
    validate_wiki -> getcwd : call
    validate_wiki -> check_mermaid_syntax : call
    validate_wiki -> strip : call
    validate_wiki -> sorted : call
    validate_wiki -> len : call
    validate_wiki -> open : call
    validate_wiki -> join : call
    validate_wiki -> check_absolute_paths : call
    validate_wiki -> check_frontmatter_fields : call
    main -> ArgumentParser : call
    main -> parse_args : call
    main -> exit : call
    main -> isdir : call
    main -> validate_wiki : call
    main -> print : call
    main -> add_argument : call
@enduml
```

### Component Diagram
```plantuml
@startuml
    package "Infrastructure/Other" {
        [okf_validate.py]
    }
    [okf_validate.py] --> [argparse]
    [okf_validate.py] --> [glob]
    [okf_validate.py] --> [os]
    [okf_validate.py] --> [re]
    [okf_validate.py] --> [sys]
    [okf_validate.py] --> [typing.Any]
@enduml
```

### Dependency Graph
```plantuml
@startuml
    [Module] --> [argparse] : imports
    [Module] --> [glob] : imports
    [Module] --> [os] : imports
    [Module] --> [re] : imports
    [Module] --> [sys] : imports
    [Module] --> [typing.Any] : imports
@enduml
```

## 5. Class & Method Specifications
## 6. Module Functions
### `extract_frontmatter(content: str) -> tuple[dict[str, Any], str]` (Public)
**Description:** Split YAML frontmatter from Markdown body.

**Inputs:**
- `content`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `tuple[dict[str, Any], str]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = extract_frontmatter(...)
```

### `check_frontmatter_fields(fm: dict[str, Any], filepath: str, strict: bool) -> list[str]` (Public)
**Description:** Validate required and optional frontmatter fields.

**Inputs:**
- `fm`
  - type: dict[str, Any]
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `filepath`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `strict`
  - type: bool
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `list[str]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = check_frontmatter_fields(..., ..., ...)
```

### `check_absolute_paths(body: str, filepath: str) -> list[str]` (Public)
**Description:** Detect absolute file paths in the document body.

**Inputs:**
- `body`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `filepath`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `list[str]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = check_absolute_paths(..., ...)
```

### `check_mermaid_syntax(body: str, filepath: str) -> list[str]` (Public)
**Description:** Basic structural validation of Mermaid code blocks.

**Inputs:**
- `body`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `filepath`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None

**Output:**
- return type: `list[str]`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = check_mermaid_syntax(..., ...)
```

### `validate_wiki(wiki_path: str, strict: bool) -> int` (Public)
**Description:** Validate all .md files under wiki_path. Returns error count.

**Inputs:**
- `wiki_path`
  - type: str
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: False
  - default value: None
- `strict`
  - type: bool
  - meaning: Not explicitly defined.
  - valid values: Not explicitly defined.
  - optional?: True
  - default value: False

**Output:**
- return type: `int`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = validate_wiki(..., ...)
```

### `main() -> None` (Public)
**Description:** Executes the main operation.

**Inputs:**
- None

**Output:**
- return type: `None`
- semantic meaning: Not explicitly defined.
- possible null values: Not explicitly defined.
- exceptions: Not explicitly defined.

**Side Effects:**
- Database updates: Not explicitly defined.
- File operations: Not explicitly defined.
- Network calls: Not explicitly defined.
- Cache: Not explicitly defined.
- State changes: Not explicitly defined.

**Complexity:**
- Time Complexity: Not explicitly defined.
- Space Complexity: Not explicitly defined.

**Example:**
```python
result = main()
```

## 7. Call Graph
```plantuml
@startuml
[okf_validate] --> [ArgumentParser] : calls
[okf_validate] --> [relpath] : calls
[okf_validate] --> [safe_load] : calls
[okf_validate] --> [read] : calls
[okf_validate] --> [glob] : calls
[okf_validate] --> [isdir] : calls
[okf_validate] --> [getcwd] : calls
[okf_validate] --> [append] : calls
[okf_validate] --> [open] : calls
[okf_validate] --> [get] : calls
[okf_validate] --> [join] : calls
[okf_validate] --> [splitlines] : calls
[okf_validate] --> [check_absolute_paths] : calls
[okf_validate] --> [isinstance] : calls
[okf_validate] --> [count] : calls
[okf_validate] --> [extend] : calls
[okf_validate] --> [add_argument] : calls
[okf_validate] --> [split] : calls
[okf_validate] --> [search] : calls
[okf_validate] --> [parse_args] : calls
[okf_validate] --> [validate_wiki] : calls
[okf_validate] --> [print] : calls
[okf_validate] --> [extract_frontmatter] : calls
[okf_validate] --> [main] : calls
[okf_validate] --> [strip] : calls
[okf_validate] --> [sorted] : calls
[okf_validate] --> [len] : calls
[okf_validate] --> [startswith] : calls
[okf_validate] --> [exit] : calls
[okf_validate] --> [check_mermaid_syntax] : calls
[okf_validate] --> [_parse_yaml] : calls
[okf_validate] --> [compile] : calls
[okf_validate] --> [enumerate] : calls
[okf_validate] --> [endswith] : calls
[okf_validate] --> [partition] : calls
[okf_validate] --> [check_frontmatter_fields] : calls
@enduml
```

## 8. Cross References
- **Dependencies:** [Dependencies](../../../../dependencies/index.md)
- **Used by:** None
- **Calls:** ArgumentParser, relpath, safe_load, read, glob, isdir, getcwd, append, open, get, join, splitlines, check_absolute_paths, isinstance, count, extend, add_argument, split, search, parse_args, validate_wiki, print, extract_frontmatter, main, strip, sorted, len, startswith, exit, check_mermaid_syntax, _parse_yaml, compile, enumerate, endswith, partition, check_frontmatter_fields
- **Called from:** ../../../src/autogen_team/__main__.md, convert_links.md, ../../../Scripts/send_kafka_test.md, ../../../src/autogen_team/infrastructure/messaging/kafka_app.md, ../../../tests/test_scripts.md, ../../../tests/repro_kafka_log.md, ../../../Scripts/test_mcp_client_simple.md, ../../../Scripts/trigger_mission.md, ../../../Scripts/run_hatchet_worker.md, ../../../Scripts/verify_agent_mcp.md, ../../../tests/registry/adapters/test_security_mlflow_adapter.md, ../../../tests/evaluation/metrics/test_metrics.md, ../../../tests/infrastructure/messaging/test_kafka_app.md
- **Related classes:** [Classes](../../../../classes/index.md)
- **Related diagrams:** [Diagrams](../../../../diagrams/index.md)
