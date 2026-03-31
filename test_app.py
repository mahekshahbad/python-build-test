from app import add

def test_add():
    assert add(2, 3) == 5

AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY



name: Trigger TruffleHog Scan

on:
  push:
  pull_request:

jobs:
  call-trufflehog:
    uses: medica-dev-platform/test-access/.github/workflows/trufflehog.yml@main

    with:
      working-directory: .
      exclude-patterns: |
        *.md
        docs/
      fail-on-secrets: true
