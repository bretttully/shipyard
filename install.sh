#!/usr/bin/env bash
# Validate the Shipyard plugin and print how to load it. Shipyard is a Claude Code plugin, so it is
# not symlinked into ~/.claude; it is loaded with --plugin-dir (dev) or via a marketplace (install).
set -euo pipefail

PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

command -v python >/dev/null 2>&1 || { echo "ERROR: python not found on PATH" >&2; exit 1; }

echo "Validating Shipyard plugin..."
python "$PLUGIN_ROOT/scripts/validate.py"

TRACKER="${SY_TRACKER:-jira}"
case "$TRACKER" in
  jira)
    command -v acli >/dev/null 2>&1 || echo "NOTE: SY_TRACKER=jira but 'acli' (Atlassian CLI) is not on PATH." >&2
    ;;
  github)
    command -v gh >/dev/null 2>&1 || { echo "ERROR: SY_TRACKER=github requires 'gh' >= 2.94.0 on PATH" >&2; exit 1; }
    ;;
  *)
    echo "ERROR: SY_TRACKER must be 'jira' or 'github' (got '$TRACKER')" >&2; exit 1
    ;;
esac

command -v gitleaks >/dev/null 2>&1 || \
  echo "NOTE: gitleaks not installed; transcript attachment stops before publish until a deterministic scanner is available." >&2

if [[ -n "${CLAUDE_CODE_SUBAGENT_MODEL:-}" ]]; then
  echo "WARNING: CLAUDE_CODE_SUBAGENT_MODEL is set; it overrides model routing and would reroute the reviewer. Unset it." >&2
fi
if [[ -z "${SY_FRONTIER_MODEL:-}" ]]; then
  echo "NOTE: set SY_FRONTIER_MODEL in settings.json env; gate defaults to fable when unset." >&2
fi

cat <<EOF

Shipyard validated (tracker: $TRACKER). To load it:

  Local development (this session only):
    claude --plugin-dir "$PLUGIN_ROOT"

  Persistent install (this repo ships a marketplace manifest; add it, then install):
    claude plugin marketplace add "$PLUGIN_ROOT"
    claude plugin install sy@shipyard      # or run /plugin and enable "sy"

Commands are namespaced:  /sy:plan  /sy:spec  /sy:ship  /sy:spike  /sy:pr  /sy:ci
EOF
