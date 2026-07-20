# Standalone accounting logs

Machine accounting is separate from human narrative. Post each log as its own small Jira comment; never embed it inside retrospectives, execution plans, decomposition comments, or Epic checkpoints.

## Usage log

Generate from the Claude JSONL transcript tree with `session_usage.py`. The report recursively includes the main session and nested subagent transcript files and groups usage by agent type/model where mapping is available.

Comment shape:

````text
# Claude Code usage

```json
{
  "schema": "shipyard.claude_usage.v1",
  "phase": "ship",
  "session_id": "...",
  "scope": "main_plus_subagents",
  "transcripts": {"main": 1, "subagents": 6},
  "totals": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 0
  },
  "by_agent": []
}
```
````

Do not hand-calculate or infer missing token counts. `unknown_subagent` is preferable to false attribution; its usage still belongs in totals.

## Ship metrics log

Comment shape:

````text
# Claude Code ship metrics

```json
{
  "schema": "shipyard.ship_metrics.v1",
  "task": "PROJ-123",
  "pr_url": "...",
  "plan_divergence_count": 0,
  "ci_fix_rounds": 0,
  "review_findings_accepted": 0,
  "review_findings_rejected": 0,
  "human_review_defects": 0,
  "post_merge_defect": null,
  "rollback": null,
  "lead_time_seconds": null,
  "transcript_attachment": "ship-session-....txt"
}
```
````

Use JSON `null` for unknown values. Do not convert unknowns to zero. In the `light` process tier no transcript is attached and `transcript_attachment` is `null`.
