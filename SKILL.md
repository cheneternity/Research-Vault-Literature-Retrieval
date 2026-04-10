---
name: research-vault-literature-retrieval
description: "D:\\ResearchVault 的默认工作区 skill。Treat any user question, request, follow-up, fragment, or ordinary statement in this workspace as a trigger for vault retrieval first, unless it is completely impossible to ground an answer in vault contents. 检索和比较该工作区中已有论文笔记，并仅基于现有精读内容回答问题。Start by reading the root index pages 文献索引.md, 研究主题索引.md, 研究方法索引.md, and 字段补全检查.md in that order, skip missing files without error, then locate relevant notes and answer only from existing reading notes."
---

# Research Vault Literature Retrieval

Use this skill as the default behavior inside `D:\ResearchVault`.

## Activation Policy

- In this workspace, treat every user input as a retrieval trigger first.
- Include direct questions, short prompts, follow-up fragments, casual wording, and incomplete phrases.
- Typical trigger shapes include:
  - `告诉我第三空间的定义`
  - `比较这几篇论文`
  - `有没有足够依据`
  - `帮我看看这个说法`
  - `第三空间`
  - `空间计量`
  - `这几篇呢`
  - `为什么`
- Do not wait for the user to explicitly say `检索` or `搜索`.
- Only after completing the index-first search flow may you conclude that the vault cannot support an answer.
- When support is insufficient, still respond through this skill and say `Vault 中未找到足够依据`.

## Workspace Scope

- Bind this skill to the current workspace `D:\ResearchVault`.
- Do not generalize its file assumptions to other vaults or folders unless the user explicitly asks.

## Compressed Workspace Map

```text
D:\ResearchVault
├─ AGENTS.md
├─ 文献索引.md
├─ 研究主题索引.md
├─ 研究方法索引.md
├─ 字段补全检查.md
├─ .obsidian\
├─ note\
│  ├─ .codex\
│  ├─ .obsidian\
│  ├─ 创新\
│  ├─ 创新经济地理\
│  ├─ 能耗\
│  └─ 街景识别\
└─ 模板\
```

## Workflow

1. Stay inside the vault.
   - Work only in `D:\ResearchVault`.
   - Default to read-only.
   - Modify files only when the user explicitly asks.

2. Read root index pages first, in this order.
   - `文献索引.md`
   - `研究主题索引.md`
   - `研究方法索引.md`
   - `字段补全检查.md`
   - If a page is missing, skip it without error.
   - On Windows PowerShell, read with UTF-8 to avoid garbled Chinese text.

3. Locate relevant notes.
   - Use the index pages first to narrow likely note titles, themes, or methods.
   - Then search `D:\ResearchVault\note` with `rg`.
   - Search both Chinese and English keywords, plus likely aliases for methods, variables, regions, and paper titles.

4. Read evidence notes.
   - Prefer single-paper reading notes and completed精读笔记.
   - If only broad review notes, unfinished notes, or weak matches exist, say so explicitly.
   - Do not fill gaps with outside memory or general knowledge.

5. Answer from vault evidence only.
   - Base every conclusion on note content that is actually present.
   - If evidence is insufficient, say `Vault 中未找到足够依据` before any limited answer.
   - For multi-paper comparison, compare only what the notes explicitly state about research object, core variables, method, findings, limits, or implications.

6. Use the default answer structure.
   1. `结论`
   2. `支持文献`
   3. `差异/争议`
   4. `对我研究的启发`
   - Cite specific note titles.
   - Keep conclusions aligned with supporting notes.

## Search Pattern

Use UTF-8 reads in PowerShell:

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Get-Content -LiteralPath 'D:\ResearchVault\文献索引.md' -Encoding UTF8 -Raw
```

Search candidate notes with `rg`:

```powershell
rg -n --glob '*.md' "关键词1|keyword2|method|variable" D:\ResearchVault\note
```

Then open the most relevant 1-3 notes fully before answering.

## Guardrails

- Do not fabricate paper content, author claims, or definitions.
- Do not treat outside knowledge as vault evidence.
- Do not infer that a note is a精读笔记 unless the note content shows that clearly.
- If the user asks for a definition and the vault has only one supporting note, state that the definition is based on the current Vault note(s), not a universal definition.
- Even if the user message is vague, still run the retrieval workflow before deciding there is no answer.
- Do not modify notes, indexes, or `AGENTS.md` unless the user explicitly requests edits.

## Common Uses

- Compare two methods or paper groups already covered by the vault.
- Define a concept from existing notes, such as `第三空间`.
- Summarize what the vault says about a theme, method, variable, or region.
- Check whether the vault contains enough evidence before answering.

## Example Triggers

- `比较固定效应模型和空间计量两类论文的研究对象、核心变量和识别逻辑`
- `告诉我第三空间的定义`
- `总结 Vault 里关于极端高温影响经济增长的结论`
- `比较这几篇论文对高温冲击的识别策略有什么不同`
- `Vault 中有没有足够依据支持“经济联系会放大灾害溢出”这个说法`
- `找一下 Vault 里有没有讨论创新区第三空间的精读笔记`
- `基于现有精读笔记，比较高温、灾害和创新三类研究怎么定义核心变量`
- `用“结论—支持文献—差异/争议—对我研究的启发”回答这个问题`
- `这个概念怎么理解`
- `帮我看看`
- `这篇和前一篇有什么区别`
- `这个说法在 Vault 里站得住吗`
