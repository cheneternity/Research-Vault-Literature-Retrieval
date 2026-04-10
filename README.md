# Research Vault Literature Retrieval

`research-vault-literature-retrieval` is a Codex skill for `D:\ResearchVault`.

It treats the vault as the default evidence source for almost every user message in that workspace, then:

- reads root index pages first
- searches relevant notes inside the vault
- prefers existing reading notes
- answers only from vault evidence
- uses the default response structure:
  - `结论`
  - `支持文献`
  - `差异/争议`
  - `对我研究的启发`

## Files

```text
.
├─ SKILL.md
└─ agents/
   └─ openai.yaml
```

## What This Skill Does

- binds itself to `D:\ResearchVault`
- reads these index pages first, in order:
  - `文献索引.md`
  - `研究主题索引.md`
  - `研究方法索引.md`
  - `字段补全检查.md`
- skips missing index pages without error
- searches `D:\ResearchVault\note` with keyword-based retrieval
- refuses to use outside knowledge as vault evidence
- says `Vault 中未找到足够依据` when the vault cannot support the answer

## Typical Triggers

- `告诉我第三空间的定义`
- `比较固定效应模型和空间计量两类论文的研究对象、核心变量和识别逻辑`
- `Vault 中有没有足够依据支持这个说法`
- `总结 Vault 里关于某个主题的结论`
- `这篇和前一篇有什么区别`

## Usage

Invoke it as:

```text
Use $research-vault-literature-retrieval to search D:\ResearchVault and answer only from existing reading notes.
```

Or let it act as the default skill inside that workspace.
