# Python Build & Test – Composite Action

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
- [Issues Encountered & Fixes](#issues-encountered--fixes)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Summary](#summary)

---

## Overview

This document describes the **Python Build & Test composite action** created in the `github-common-actions` repository.

The action standardizes the CI process for Python projects by encapsulating dependency installation and test execution into a reusable component.

---

## Purpose

The main objectives of this composite action are:

- Standardize Python CI workflows across repositories  
- Reduce duplication of build and test logic  
- Ensure consistent execution environments  
- Simplify integration for new and existing repositories  

---

## Action Location

```
github-common-actions/
└── python-build-test/
    └── action.yml
```

---

## What This Action Does

The composite action performs the following:

- Installs Python dependencies  
- Ensures `pytest` is available  
- Runs test cases  
- Generates test reports in JUnit XML format  

---

## How It Works

The action executes the following steps:

### 1. Install Dependencies
- Upgrades `pip`
- Installs dependencies from `requirements.txt` (if present)
- Installs `pytest`

### 2. Run Tests
- Executes tests using `pytest`
- Generates a JUnit XML report:
test-results/results.xml


---

## Inputs

| Input           | Required | Default | Description                      |
|----------------|----------|--------|----------------------------------|
| python-version | No       | 3.9    | Python version used for execution|

---

## Usage Example

```yaml
name: CI - Python Build & Test

on:
  push:
    branches:
      - master

jobs:
  build-and-test:
    runs-on: self-hosted

    container:
      image: python:3.9

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run Python Build & Test
        uses: medica-dev-platform/github-common-actions/python-build-test@<branch-name>
        with:
          python-version: "3.9"
```

## Execution Environment

| Component       | Details           |
|----------------|------------------|
| Runner         | self-hosted      |
| Execution Mode | Docker container |
| Base Image     | python |

### Why Container-Based Execution?

- Ensures consistent Python versions  
- Avoids dependency conflicts  
- Eliminates host machine inconsistencies  

---

## Workflow Flow

The overall execution flow of the composite action is:

1. Workflow is triggered on push  
2. Code is checked out  
3. Container environment is initialized  
4. Dependencies are installed  
5. Pytest is installed and executed  
6. Test results are generated in XML format  

---

## Design Decisions

### Composite Action Approach
- Runs within the same job  
- Easier integration into existing workflows  
- No need for cross-job dependency handling  

### Generic Implementation
- No hardcoded project-specific configurations  
- Works across multiple Python repositories  

### Pytest with JUnit XML
- Standard format for CI reporting  
- Compatible with external tools  

---

## Issues Encountered & Fixes

### Python Version Issues
- Failures due to incompatible Python versions  
- Fixed by using Docker container with specified version   

---

## Limitations

- Assumes presence of `requirements.txt` if dependencies are needed  
- Does not manage environment-specific configurations   
- Does not support matrix builds  

---

## Future Improvements
 
- Implement dependency caching  
- Improve logging and debugging support  
- Allow configurable test directory  

---

## Summary

The Python Build & Test composite action provides a reusable and consistent approach to CI across repositories. It simplifies setup, reduces duplication, and ensures reliable execution in controlled environments.
