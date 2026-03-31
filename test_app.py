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


AWS_KEY=AKIAIOSFODNN7EXAMPLE
AWS_SECRET=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
GITHUB_TOKEN=ghp_REDACTED_TEST_TOKEN_1234567890ab
SLACK_WEBHOOK=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
