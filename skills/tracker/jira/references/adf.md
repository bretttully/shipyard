# Markdown to ADF

Author bodies/comments as Markdown in `.scratch/`, convert, then upload ADF JSON:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/md_to_adf.py .scratch/body.md > .scratch/body.adf.json
acli jira workitem edit --key PROJ-123 --description-file .scratch/body.adf.json
acli jira workitem comment create --key PROJ-123 --body-file .scratch/body.adf.json
```

`md_to_adf.py` always re-execs into a dedicated isolated virtual environment and installs exact, hash-checked converter dependencies from `adf-requirements.lock`. Provisioning is idempotent and lock-guarded.

Pre-warm:

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/tracker/jira/md_to_adf.py --setup
```

If setup fails, conversion fails loudly. Never fall back to raw Markdown.

The converter validates top-level ADF structure before emitting JSON. When write verification matters, inspect stored ADF through Jira REST rather than relying on legacy rendered-HTML endpoints.
