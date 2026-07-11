---
name: pr
description: >-
  Create, promote, or clean up the GitHub PR for the current branch; keep the description
  brutally short, preserve durable acceptance evidence in comments, and handle review threads.
  Never carries transcripts — the exported /sy:ship session is attached to the task by /sy:ship,
  not posted to the PR.
argument-hint: "[optional emphasis or draft]"
---

Create/update the GitHub PR for the **current branch**. `$ARGUMENTS` may provide emphasis or `draft`.

This skill inherits caller model/effort. Assess scope before reading: a handful of short comments can be read directly; long review/thread tails go to `sy:sweep` and return briefs.

## 1. Detect state

Never operate on `main`. Confirm branch and PR state.

- **No PR** ⇒ create; push first if needed.
- **Draft exists** ⇒ promote/refresh when caller requests readiness.
- **Open non-draft exists** ⇒ cleanup/update. If called directly by a human, ask before rewriting mutable metadata; when `/sy:ship` explicitly invokes promotion/refresh, that invocation is authorization for that operation.

## 2. Description contract

Base on real diff/log. Keep the mutable PR body concise:

- why and why this approach;
- 2–4 single-line summary bullets;
- no redundant file/function inventory;
- caveats only when reviewers cannot infer them from the diff;
- manual-only test plan; omit if none;
- optional small table only when genuinely clearer;
- image placeholder only when needed;
- no AI self-credit/co-author lines.

**Acceptance criteria/evidence never live only in the mutable description.** `/sy:ship` posts them as a dedicated PR comment so promotion/refresh cannot erase them.

Title: `<TICKET> - <imperative summary>` when branch carries a ticket key.

## 3. Review threads

Every relevant review thread gets an answer; push back on bad trade-offs instead of rubber-stamping.

- small thread set ⇒ read directly;
- long auto-reviewer/multi-round tail ⇒ `sy:sweep` brief with open suggestion, target `file:line`, and addressed/unaddressed state.

Caller reads decisive threads and writes replies. Stage each reply body as a file, then post it by **reading the file** — never by handing `@path` to a literal-string flag:

- inline thread reply ⇒ `gh api --method POST repos/<o>/<r>/pulls/<pr>/comments/<id>/replies -F body=@<file>` (or `--input <file>`);
- top-level PR comment ⇒ `gh pr comment <pr> --body-file <file>`;
- edit an existing comment ⇒ `gh api --method PATCH repos/<o>/<r>/pulls/comments/<id> -F body=@<file>`.

`gh api -F/--raw-field key=@file` reads the file; `-f/--field key=@file` posts the literal `@file` — a silent-corruption trap. After posting, read the stored body back (`gh api .../comments/<id> --jq .body`) and confirm it is the intended prose, not a value starting with `@`.

## 4. Merge (verified-head only)

Merging is `/sy:ship`'s explicit-authorization path (`ship/references/merge-accounting.md`), not part of the normal create/promote/cleanup flow. Whenever a merge runs, gate it on the exact validated commit:

- `gh pr merge <pr> --squash --match-head-commit <CI-green + reviewed SHA>` — `--match-head-commit` aborts the merge if the head moved since validation, so only the reviewed/CI-green commit can land, never a race-pushed one.
- add `--admin` only to clear a ruleset the author cannot satisfy alone (e.g. a required approval the author can't self-give), and only with the owner's explicit go-ahead — it bypasses the ruleset, not CI/review freshness.

This skill never runs tests or review; `/sy:ci` and `sy:gate` own those gates, and session transcripts belong on the task via `/sy:ship`. End by printing the PR URL and what state change/comment action occurred.
