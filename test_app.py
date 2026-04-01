scan-issues-prs:
  description: "Scan GitHub issues and PR comments"
  required: false
  type: boolean
  default: true



# --------------------------
# 3B. Scan Issues & PR Comments
# --------------------------
- name: Scan GitHub Issues & PRs
  if: ${{ inputs.scan-issues-prs }}
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    echo "Scanning GitHub issues and PR comments..."

    trufflehog github \
      --repo="${{ github.repository }}" \
      --json \
      --no-update \
      > trufflehog-github-results.json 2>&1 || true

    echo "GitHub scan completed"




# --------------------------
# Merge Results
# --------------------------
- name: Merge Scan Results
  run: |
    echo "Merging scan results..."

    if [ -f trufflehog-github-results.json ]; then
      cat trufflehog-results.json trufflehog-github-results.json > combined-results.json
      mv combined-results.json trufflehog-results.json
    fi










======================


- name: Prepare TruffleHog Ignore File
  id: ignore
  run: |
    echo "Creating ignore file"

    TRUFFLEHOG_IGNORE="${RUNNER_TEMP}/.trufflehogignore"

    # Default patterns (safe baseline)
    printf "%s\n" \
      ".git/" \
      "node_modules/" \
      ".terraform/" \
      ".terraform.lock.hcl" \
      "test-results/" \
      "security-reports/" \
      ".*\\.sarif$" \
      ".*\\.json$" \
      > "$TRUFFLEHOG_IGNORE"

    # Append user-provided patterns
    if [ -n "${{ inputs.trufflehog-ignore-patterns }}" ]; then
      echo "Adding user provided ignore patterns"
      echo "${{ inputs.trufflehog-ignore-patterns }}" >> "$TRUFFLEHOG_IGNORE"
    fi

    echo "TRUFFLEHOG_IGNORE=$TRUFFLEHOG_IGNORE" >> $GITHUB_ENV





inputs:
  trufflehog-ignore-patterns:
    description: "Custom ignore patterns (newline separated)"
    required: false
    type: string
    default: ""


trufflehog-ignore-patterns: |
        *.md
        docs/
        *.txt




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



if [ "$SECRET_COUNT" -gt 0 ]; then
  echo "❌ Secrets found!"
  echo "---- Detected Secrets ----"

  jq -r '
    select(.DetectorName != null) |
    "Detector: \(.DetectorName) | File: \(.SourceMetadata.Data.Filesystem.file // "unknown") | Line: \(.SourceMetadata.Data.Filesystem.line // "N/A")"
  ' trufflehog-results.json || true

  echo "--------------------------"

  if [ "${{ inputs.fail-on-secrets }}" = "true" ]; then
    exit 1
  fi
fi
