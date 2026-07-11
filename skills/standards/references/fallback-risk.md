# Shipyard fallback and risk lenses

Use fallback standards only when no repository authority applies:

- correctness and explicit failure over silent corruption;
- reuse established project/platform primitives before invention;
- specific error handling that preserves root causes;
- tests proportional to behavioural risk and acceptance criteria;
- public interface documentation and compatibility consideration;
- resource/performance claims measured or reasoned quantitatively;
- match surrounding language/framework conventions.

Do not invent repo-specific preferences such as dataframe library, path API, type syntax, member ordering, formatter, or binding choice.

## Risk-lens catalogue

Activate only lenses justified by the changed surface:

- security/trust boundaries, authn/authz, injection, secrets, sensitive data;
- migration/backfill, dual read/write compatibility, rollback/recovery;
- public API, serialization, file-format, protocol, CLI compatibility;
- concurrency, retries, idempotency, duplicate execution, races, ordering;
- performance/resource goals with explicit metrics and realistic shapes;
- operational visibility: logs, metrics, alerts, actionable failure modes;
- data integrity and irreversible mutation;
- deployment/config compatibility and staged rollout.

Pass only activated lenses into implementation and correctness review. `/sy:spec` converts each activated lens into an explicit verification obligation: claim plus named evidence.
