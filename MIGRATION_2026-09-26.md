# Underwrite repository reconciliation — 26 September 2026

The existing standalone repository is the authoritative working tree. The active manuscripts have been restored from `source_library/series/` to the Git-tracked `series/` layout. Frozen comparator material elsewhere in `source_library/` is preserved.

Three newer items were transferred from the ignored Mwendo integration copy: the additional pricing review, the collectability/re-verification feedback review, and its source image. Shared content was compared by SHA-256 before relocation. The standalone historical snapshots and hash list were retained, including its two additional snapshot manuscripts. The inner copy's path-specific hash list is preserved in the Mwendo archive.

The PDF build's project-root calculation now uses the parent of `series`, keeping scratch output inside this repository. No manuscript prose or research claims were rewritten by the layout repair.

Full pre-migration Git history, the original relocated series, and the retired integration copy are preserved under `C:/Users/Nevo/Downloads/insuretech & embedded finance/_archive/repository_migration_2026-09-26/`. The detailed comparison and transfer manifest are in the parent project's `docs/governance/migrations/2026-09-26/`.

Use this repository for subsequent Underwrite changes. Guest financial-material and business/blog website repositories were outside the migration's write boundary.
