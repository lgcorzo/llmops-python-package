---
type: api
title: "to_object"
source_path: "src/autogen_team/infrastructure/io/configs.py"
description: "Convert a config object to a python object.  Args:     config (Config): representation of the config.     resolve (bool): resolve variables. Defaults to True.  Returns:     object: conversion of the config to a python object."
tags: [api]
last_verified_commit: "dc137c3"
---

# to_object

Source File: `src/autogen_team/infrastructure/io/configs.py`

Convert a config object to a python object.  Args:     config (Config): representation of the config.     resolve (bool): resolve variables. Defaults to True.  Returns:     object: conversion of the config to a python object.

## Architecture Visualization

```mermaid
flowchart TD
    Start --> Init
    Init --> call_0[to_container]
    call_0 --> End
```
