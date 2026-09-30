# Research Vault Literature Retrieval

This repository is the standalone release mirror of the Retrieval Skill in the canonical workflow repository:

**Canonical implementation:** [`Zotero-Analytical-Workflow-Skills/skills/research-vault-literature-retrieval`](https://github.com/cheneternity/Zotero-Analytical-Workflow-Skills/tree/main/skills/research-vault-literature-retrieval)

The published `SKILL.md`, `agents/openai.yaml`, and `references/retrieval-routing.md` are copied from that canonical directory. Do not develop a separate behavior version here. A CI check compares these files to the canonical source to prevent version drift.

## Install

Clone this repository and copy the repository folder into your agent's Skills directory, for example:

```text
.codex/skills/research-vault-literature-retrieval/
├── SKILL.md
├── agents/openai.yaml
└── references/retrieval-routing.md
```

No Python package, Zotero database, MinerU install, or local Vault path is required by this Skill. Use it in an agent session where the target ResearchVault is available as the active project/workspace. New content follows `02vault/` for Analytical Notes, `03fulltext/` for Fulltext, and `01knowledge/` for derived Knowledge; existing legacy paths are read only when resolving existing links during migration.

## Update policy

Update the canonical Skill in `Zotero-Analytical-Workflow-Skills` first, then copy the three mirrored files to this repository in the same release. Run the synchronization check locally:

```text
python tools/check_sync.py --canonical-dir <path-to-main-repo>/skills/research-vault-literature-retrieval
```

The GitHub workflow checks the matching pull-request branch in the canonical repository, so the two changes can be reviewed and checked together. Keep the branch name in both repositories aligned during a paired release.
