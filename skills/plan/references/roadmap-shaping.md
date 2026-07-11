# Roadmap shaping

## Find seams

Locate low-coupling cut points and real dependency order. Use parallel `sy:sweep` briefs for large surfaces; escalate only genuinely unresolved boundaries to `sy:seam`.

Hunt hidden serialization: shared schemas/tables/config, generated artifacts, migrations, deployment order, or API/format compatibility that make apparently parallel work sequential.

## Build the ladder backwards

- Name the capabilities composing the North Star; let conceptual fan-out follow reality.
- Sequence the critical path and identify the parallel-safe set.
- Pick the near horizon using critical-path pressure and uncertainty reduction.
- Existing active work counts against the cap of four.

## Create only near executable leaves

Create only PR-sized Tasks/Bugs ready for `/sy:spec`. Each needs goal, boundary, adjacent interfaces, blockers/dependencies, and enough project context to explain how it fits. Create direct under the Epic in `backlog`; record dependencies with the tracker's `add-dependency`.

If the near horizon would exceed four active leaves, create only the critical/uncertainty-reducing subset and keep the rest conceptual in the Epic.

When shape decisions are settled, load `checkpoint-handoff.md`.
