# Python Test – Composite Action

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
- [Reports Generated](#reports-generated)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Summary](#summary)

---

## Overview

This document describes the **Python Test composite action** created in the `github-common-actions` repository.

This action is responsible for executing test cases and generating test and coverage reports.

---

## Purpose

The main objectives of this composite action are:

- Standardize test execution across repositories  
- Generate JUnit XML reports for CI tools  
- Generate coverage reports for quality analysis  

---

## Action Location

```
github-common-actions/
└── python-test/
    └── action.yml
```


---

## What This Action Does

The composite action performs the following:

- Installs `pytest` and `pytest-cov`  
- Runs test cases  
- Generates JUnit XML test reports  
- Generates code coverage reports  
- Uploads reports as artifacts  

---

## How It Works

The action executes the following steps:

### 1. Install Test Dependencies
- Installs `pytest` and `pytest-cov`

### 2. Run Tests
- Executes tests using `pytest`
- Ignores specific test files if required

### 3. Generate Reports
- **JUnit XML report:** `test-results/results.xml`  
- **Coverage XML report:** `coverage.xml`


### 4. Upload Reports
- Uploads test and coverage reports as artifacts  

---

## Inputs

| Input           | Required | Default | Description                      |
|----------------|----------|--------|----------------------------------|
| python-version | No       | 3.9    | Python version used for execution|

---

## Usage Example

```yaml
- name: Python Test
uses: medica-dev-platform/github-common-actions/python-test@<branch-name>
with:
  python-version: "3.9"
```

## Execution Environment

| Component       | Details           |
|----------------|------------------|
| Runner         | self-hosted      |
| Execution Mode | Docker container |
| Base Image     | python:<version> |

---

## Workflow Flow

1. Workflow is triggered  
2. Test dependencies are installed  
3. Tests are executed using pytest  
4. JUnit XML report is generated  
5. Coverage report is generated  
6. Reports are uploaded as artifacts  

---

## Design Decisions

### Pytest Framework
- Widely used and flexible testing framework  

### JUnit XML Format
- Standard format for CI/CD tools  
- Compatible with SonarQube and reporting tools  

### Coverage Integration
- Provides visibility into code quality  
- Helps enforce testing standards  

---

## Reports Generated

| Report Type     | Path                         | Purpose                      |
|----------------|------------------------------|------------------------------|
| Test Report    | `test-results/results.xml`   | Test execution results       |
| Coverage Report| `coverage.xml`               | Code coverage for analysis   |

---

## Limitations

- Assumes test files are located in `test/` directory  
- Hardcoded test paths and ignore rules  
- No configurable test selection  
- Installs test dependencies on every run  

---

## Future Improvements

- Add test path as configurable input  
- Add coverage threshold enforcement  
- Add dependency caching  
- Improve logging and debugging  

---

## Summary

The Python Test composite action provides a standardized and reusable way to execute tests and generate reports. It ensures consistency across repositories and enables integration with quality tools like SonarQube.
