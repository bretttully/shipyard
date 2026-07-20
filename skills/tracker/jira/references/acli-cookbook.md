# Extended ACLI cookbook

Load only for Jira mechanics not covered by the core skill.

```bash
# Epic  (staging files are namespaced by target key, or a slug before a key exists)
acli jira workitem create --project "${ACLI_PROJECT:?}" --type Epic \
  --summary "<title>" --description-file .scratch/<slug>-epic.adf.json

# Task under Epic
acli jira workitem create --project "${ACLI_PROJECT:?}" --type Task \
  --parent PROJ-100 --summary "<title>" --description-file .scratch/PROJ-100-task.adf.json

# Comments
acli jira workitem comment create --key PROJ-123 --body-file .scratch/PROJ-123-comment.adf.json
acli jira workitem comment list --key PROJ-123

# Dependency: PROJ-123 blocks PROJ-124 (PROJ-123 is the blocker).
# Do NOT create blocker links with `acli link create --out/--in`: its flags are inverted
# relative to Jira's model (empirically `--in` is the blocker), so it silently creates the
# reverse link. Use the helper, which sets direction via the REST model and verifies it:
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py link --blocker PROJ-123 --blocked PROJ-124
```

Deleting a link is unambiguous and stays on `acli`: `acli jira workitem link delete --id <id> --yes`.

`--yes` is not universal; use it only where the installed command supports it.

## Labels

Do not depend on ambiguous ACLI append-vs-replace semantics. Use the REST helper, which reads the current label set and writes back the preserved set plus the requested label:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py add-label PROJ-123 decomposed
```

## Parent update / re-parenting

Use the REST helper rather than putting credentials in curl argv:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py set-parent PROJ-123 PROJ-100
```

Ask before crossing into another project or portfolio hierarchy.

## Raw REST reads (when `acli` truncates or rejects)

`view --fields '*all'` truncates relational fields (parent, issue links, labels). The helper reads them raw — see the ADAPTER's read ladder:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py get PROJ-123 --fields parent,issuelinks,labels
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py comment-get PROJ-123 <COMMENT_ID>
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/jira_rest.py transitions PROJ-123   # valid targets after a rejected transition
```
