# GitHub issue migration cookbook

This is a separate migration workflow. Do not load it during normal `/plan → /spec → /ship` execution.

1. Reuse a tracking item already promoted to Epic; do not duplicate it as a child Task.
2. Create one Jira Task per executable GitHub issue under the Epic.
3. Maintain an explicit `gh# -> Jira key` ledger and skip mapped rows; creation is not inherently idempotent.
4. Create first, then assign separately when create-time assignment is unreliable.
5. Map closed GitHub issues to Jira Closed only when the migration semantics genuinely mean terminal/delivered; do not misuse decomposed closure.
6. Convert Markdown to ADF. Prefix imported comments with GitHub author/date because Jira records the API token owner as author.
7. Use `jira_rest.py set-parent` for re-parenting/cross-level parent updates.
8. Preserve provenance: prepend `Migrated from GitHub #<n>`, add Jira backlink on GitHub, and close rather than delete source issues.

Stage payloads, preserve the mapping ledger, and make reruns idempotent.
