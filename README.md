# Research Vault 检索技能

`research-vault-literature-retrieval` 是一个面向 `D:\ResearchVault` 的 Codex 技能。

它会把这个工作区中的绝大多数用户输入都当作 Vault 检索请求，然后：

- 先读取根目录索引页
- 再检索 Vault 中的相关笔记
- 优先使用已有精读笔记
- 只基于 Vault 证据回答
- 默认按照以下结构组织回答：
  - `结论`
  - `支持文献`
  - `差异/争议`
  - `对我研究的启发`

## 文件结构

```text
.
├─ SKILL.md
└─ agents/
   └─ openai.yaml
```

## 这个技能做什么

- 绑定到 `D:\ResearchVault`
- 优先按以下顺序读取索引页：
  - `文献索引.md`
  - `研究主题索引.md`
  - `研究方法索引.md`
  - `字段补全检查.md`
- 索引页缺失时直接跳过，不报错
- 用关键词方式检索 `D:\ResearchVault\note`
- 拒绝把外部知识当作 Vault 证据
- 当 Vault 无法支撑回答时，明确写出 `Vault 中未找到足够依据`

## 常见触发句式

- `告诉我第三空间的定义`
- `比较固定效应模型和空间计量两类论文的研究对象、核心变量和识别逻辑`
- `Vault 中有没有足够依据支持这个说法`
- `总结 Vault 里关于某个主题的结论`
- `这篇和前一篇有什么区别`

## 使用方式

可以这样调用：

```text
使用 $research-vault-literature-retrieval 检索 D:\ResearchVault，并且只基于已有阅读笔记回答问题。
```

也可以让它在这个工作区里作为默认技能自动运行。
