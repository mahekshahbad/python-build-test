# Python Build – Composite Action

## Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Action Location](#action-location)
- [What This Action Does](#what-this-action-does)
- [How It Works](#how-it-works)
- [Inputs](#inputs)
- [Usage Example](#usage-example)
- [Execution Environment](#execution-environment)
- [Workflow Flow](#workflow-flow)
- [Design Decisions](#design-decisions)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Summary](#summary)

---

## Overview

This document describes the **Python Build composite action** created in the `github-common-actions` repository.

This action is responsible for preparing the Python environment by installing dependencies required for the project.

---

## Purpose

The main objectives of this composite action are:

- Standardize dependency installation across repositories  
- Ensure consistent Python environments  
- Reduce duplication of setup steps  
- Provide a reusable build component  

---

## Action Location

```
github-common-actions/
└── python-build/
    └── action.yml
```


---

## What This Action Does

The composite action performs the following:

- Displays Python version  
- Upgrades `pip`  
- Installs dependencies from `requirements.txt`  

---

## How It Works

The action executes the following steps:

### 1. Show Python Version
- Prints the Python version being used

### 2. Install Dependencies
- Upgrades `pip`
- Installs dependencies from `requirements.txt`

---

## Inputs

| Input           | Required | Default | Description                      |
|----------------|----------|--------|----------------------------------|
| python-version | No       | 3.9    | Python version used for execution|

---

## Usage Example

```yaml
- name: Python Build
  uses: medica-dev-platform/github-common-actions/python-build@<branch-name>
  with:
    python-version: "3.9"
```

## Execution Environment

| Component       | Details           |
|----------------|------------------|
| Runner         | self-hosted      |
| Execution Mode | Docker container |
| Base Image     | python:<version> |

### Why Container-Based Execution?

- Ensures consistent Python versions  
- Avoids dependency conflicts  
- Eliminates host machine inconsistencies  

---

## Workflow Flow

1. Workflow is triggered  
2. Python version is displayed  
3. pip is upgraded  
4. Dependencies are installed  

---

## Design Decisions

### Composite Action Approach
- Runs within the same job  
- Easily reusable across repositories  

### Generic Implementation
- No hardcoded project-specific configurations  
- Works across multiple Python projects  

---

## Limitations

- Assumes presence of `requirements.txt`   
- Does not include dependency caching  

---

## Future Improvements

- Add dependency caching  
- Support optional requirements files (e.g., dev/test)  
- Improve error handling  

---

## Summary

The Python Build composite action standardizes dependency installation and environment setup, enabling consistent and reusable CI workflows across repositories.
