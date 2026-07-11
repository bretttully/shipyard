# Installing Shipyard

Shipyard is a Claude Code plugin. You **load** it, you do not symlink or copy it into `~/.claude`. Nothing about your global config changes; the plugin's skills, agents, and hooks become available under the `/sy:` namespace for as long as it is loaded.

Once loaded, configure the repo you want to use it in — see [`settings.md`](settings.md) (and [`github-setup.md`](github-setup.md) if you use the GitHub tracker). Then drive the loop as in [`usage.md`](usage.md).

## Load the plugin

Two ways, depending on whether you want it for one session or permanently.

### One session (local development / trying it out)

```bash
claude --plugin-dir /path/to/shipyard
```

The plugin is available only for that invocation — nothing is registered.

### Persistent (across sessions)

Persistent installs come from a **marketplace**: a directory or repo that contains a `.claude-plugin/marketplace.json` listing one or more plugins. This repo ships one (it lists the `sy` plugin at its root), so it is its own marketplace. Add the marketplace, then install the plugin from it — you can do this straight from GitHub without cloning, or from a local checkout.

**From GitHub (no clone).** `claude plugin marketplace add` accepts a GitHub `owner/repo` shorthand (or a full `https://`/`git@` URL); Claude Code clones it for you. Append `@<ref>` to pin a branch or tag, and private repos authenticate with your existing git credentials (`gh auth login`, SSH agent, or a credential helper).

```bash
claude plugin marketplace add bretttully/shipyard   # registers the marketplace, named "shipyard"
claude plugin install sy@shipyard                   # install the plugin from it
```

**From a local checkout.** Point the same command at the directory instead:

```bash
claude plugin marketplace add /path/to/shipyard
claude plugin install sy@shipyard
```

`claude plugin install` takes `<plugin>@<marketplace>`; here the plugin is `sy` and the marketplace is `shipyard` (the `name` in `marketplace.json`). Equivalently, run `/plugin` and enable **sy** from the `shipyard` marketplace in the interactive UI. Manage it later with `claude plugin list`, `claude plugin update sy`, and `claude plugin uninstall sy`.

Only `--plugin-dir` (the one-session dev mode above) needs a local checkout. Either way, the commands are namespaced by the plugin name (`sy`): `/sy:plan`, `/sy:spec`, `/sy:ship`, `/sy:spike`, `/sy:pr`, `/sy:ci`.

## `./install.sh` — validate and get load instructions

`./install.sh` does not copy anything. It runs `scripts/validate.py` (structure, frontmatter, the tracker seam, contract completeness, and the script self-tests), does a tracker-aware preflight against your environment, and prints the exact load instructions above for your checkout path. Run it after cloning and any time you want to confirm the plugin is intact:

```bash
cd /path/to/shipyard
./install.sh
```

The preflight warns (non-fatally, except where noted) when a tool the configured tracker needs is missing, when `CLAUDE_CODE_SUBAGENT_MODEL` is set (it overrides model routing and would reroute the reviewer — unset it), and when `SY_FRONTIER_MODEL` is unset (the reviewer falls back to `fable`). With `SY_TRACKER=github` it treats a missing `gh` as a hard error.

## Required tools

| Tool | Version | Used for | When you need it |
|---|---|---|---|
| Claude Code | plugin-capable | Loading the plugin; must support plugins, `hooks`, and `effort`/`model` in agent frontmatter | Always |
| Python | 3.10+, on `PATH`, invoked as `python` | Validation, usage accounting, the review guard, and the tracker helper scripts | Always |
| `gh` | ≥ 2.94.0, authenticated | The code host (PRs and CI, via `/sy:pr` and `/sy:ci`) for **every** tracker, and the transport for the GitHub tracker adapter | Always (the 2.94.0 floor is required by the GitHub tracker's sub-issue and dependency flags) |
| `acli` | Atlassian CLI | The Jira tracker adapter's transport | Jira tracker only (`SY_TRACKER=jira`) |
| `gitleaks` | any recent | Secret-scanning a rendered session transcript before it is attached (Jira) or gisted (GitHub) | Whenever ship attaches transcripts; without it, ship stops before publishing an unscanned transcript |

For the GitHub tracker, `gh` also needs `project` + `read:project` scopes (`gh auth refresh -s project,read:project`). See [`github-setup.md`](github-setup.md) for the one-time board setup.

## Next steps

- [`settings.md`](settings.md) — configure a repo (tracker choice, column names, model, tracker credentials).
- [`github-setup.md`](github-setup.md) — one-time GitHub Projects board and field setup (GitHub tracker only).
- [`usage.md`](usage.md) — the day-to-day `plan → spec → ship` loop.
