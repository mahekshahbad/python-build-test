name: TruffleHog Secret Scan (Repo + Issues + PRs)

on:
  # push:
  #   branches:
  #     - main
  # pull_request:
  workflow_dispatch:
    inputs:
      repo_url:
        description: "GitHub repo URL to scan (e.g. https://github.com/trufflesecurity/test_keys)"
        required: false
        default: "https://github.com/medica-dev-platform/test1"
      results_filter:
        description: "Filter results: verified, unknown, unverified, or comma-separated combo"
        required: false
        default: "verified,unknown,unverified"

jobs:
  trufflehog-scan:
    name: TruffleHog - Scan Repo + Issues + PRs
    runs-on: self-hosted

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      # ---------------------------------------------------------------
      # 1. Standard git-history scan using the official TruffleHog action
      # ---------------------------------------------------------------
      - name: TruffleHog - Git History Scan
        uses: trufflesecurity/trufflehog@main
        with:
          extra_args: --results=verified,unknown

      # ---------------------------------------------------------------
      # 2. Full GitHub scan including Issues & PR comments
      #    Uses the `github` scanner which needs a token with repo access.
      #    Docs: trufflehog github --repo=<url> --issue-comments --pr-comments
      # ---------------------------------------------------------------
      - name: Determine repo to scan
        id: repo
        run: |
          if [ -n "${{ github.event.inputs.repo_url }}" ]; then
            echo "url=${{ github.event.inputs.repo_url }}" >> "$GITHUB_OUTPUT"
          else
            echo "url=https://github.com/${{ github.repository }}" >> "$GITHUB_OUTPUT"
          fi

          if [ -n "${{ github.event.inputs.results_filter }}" ]; then
            echo "filter=${{ github.event.inputs.results_filter }}" >> "$GITHUB_OUTPUT"
          else
            echo "filter=verified,unknown" >> "$GITHUB_OUTPUT"
          fi

      - name: TruffleHog - Scan Issues & PR Comments
        run: |
          docker run --rm \
            trufflesecurity/trufflehog:latest \
            github \
              --repo=${{ steps.repo.outputs.url }} \
              --issue-comments \
              --pr-comments \
              --token=${{ secrets.TRUFFLEHOG_TOKEN }} \
              --results=${{ steps.repo.outputs.filter }} \
              --json
        env:
          TRUFFLEHOG_TOKEN: ${{ secrets.TRUFFLEHOG_TOKEN }}

===============



Testing secret detection

AWS_SECRET_ACCESS_KEY=abcd1234secretkey
password=supersecret123


permissions:
  contents: read
  issues: read
  pull-requests: read



jq -r '
  select(.DetectorName != null) |
  "Detector: \(.DetectorName) |
   Source: \(
     .SourceMetadata.Data.Filesystem.file
     // (.SourceMetadata.Data.GitHub.repository + " (Issue/PR)")
     // "unknown"
   ) |
   Line: \(
     .SourceMetadata.Data.Filesystem.line
     // "N/A"
   )"
' trufflehog-results.json



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
