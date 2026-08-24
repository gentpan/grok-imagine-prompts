# Grok Imagine 提示词收藏

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Prompts](https://img.shields.io/badge/Prompts-213-blue.svg)](data/prompts.jsonl)

> 精心整理的 Grok Imagine (xAI) 视频生成提示词集合。中英文双语，保留来源，仅收录 SFW 内容。

**整理者**: Yep ([gentpan](https://github.com/gentpan))

---

## 📖 关于本项目

本项目收集和整理来自社区的高质量 **Grok Imagine** (xAI) 提示词，专注于视频生成场景。

### 特点

- ✅ **双语支持** - 每个提示词都包含中文和英文版本
- ✅ **来源追溯** - 保留每个提示词的原始来源和许可证信息
- ✅ **分类清晰** - 按主题分类，便于查找和使用
- ✅ **SFW 内容** - 仅收录安全、适合工作场合的内容
- ✅ **结构化数据** - 提供 JSONL 格式的机器可读数据

### 内容范围

本项目**仅收录** Grok Imagine (xAI) 的提示词，不包括：
- ❌ GPT Image 2 (OpenAI)
- ❌ Nano Banana 或其他图像生成模型

---

## 📊 统计信息

| 指标 | 数量 |
|------|------|
| 总提示词数 | **213** |
| 分类数 | **13** |
| 数据来源 | **10** |

---

## 🗂️ 分类目录

| 分类 | 提示词数 | 目录 |
|------|---------|------|
| 写实 | 33 | [prompts/写实/](prompts/写实/) |
| 电影 | 31 | [prompts/电影/](prompts/电影/) |
| 视频 | 25 | [prompts/视频/](prompts/视频/) |
| 动画 | 23 | [prompts/动画/](prompts/动画/) |
| 编辑 | 16 | [prompts/编辑/](prompts/编辑/) |
| 其它 | 14 | [prompts/其它/](prompts/其它/) |
| 科幻 | 13 | [prompts/科幻/](prompts/科幻/) |
| 风景 | 12 | [prompts/风景/](prompts/风景/) |
| 动漫 | 10 | [prompts/动漫/](prompts/动漫/) |
| 奇幻 | 10 | [prompts/奇幻/](prompts/奇幻/) |
| 动作 | 9 | [prompts/动作/](prompts/动作/) |
| 抽象 | 9 | [prompts/抽象/](prompts/抽象/) |
| 风格 | 8 | [prompts/风格/](prompts/风格/) |

---

## 🚀 快速开始

### 浏览提示词

1. 访问 [prompts](prompts/) 目录查看所有分类
2. 每个分类文件包含该类别的所有提示词（中英文双语）
3. 选择感兴趣的提示词，复制并在 Grok Imagine 中使用

### 使用数据

```bash
# 克隆仓库
git clone https://github.com/gentpan/grok-imagine-prompts.git
cd grok-imagine-prompts

# 查看 JSONL 数据
cat data/prompts.jsonl
```

### 数据格式

每个提示词文件（如 `prompts/电影/0001.md`）包含 YAML frontmatter 和双语内容：

```yaml
---
id: 唯一标识
title_zh: 中文标题
title_en: English Title
category: 分类名
tags: [标签1, 标签2]
source_repo: 来源仓库
source_url: 来源 URL
source_license: 许可证
organizer:
  name: Yep
  github: gentpan
  note: 整理
---

## 中文
**标题**
提示词内容

## English
**Title**
Prompt content

---
整理：Yep（gentpan）  
来源：[仓库](URL) (许可证)
```

详细说明见 [SCHEMA.md](SCHEMA.md)。

---

## 📚 数据来源

本项目整理自以下开源项目（详见 [sources.md](sources.md)）：

1. **that-cod/awesome-grok-imagine-prompts** (MIT) - 183 个
2. **seaimagine/awesome-grok-imagine-1-5-prompts** (MIT) - 40 个原创
3. **YouMind-OpenLab/awesome-grok-imagine-prompts** (CC BY 4.0) - 精选
4. **imagineVid/awesome-grok-imagine-video-prompts-and-skills** (MIT) - 24 个
5. **thoxakihiko/grok-imagine-prompt-1.5-guide** (CC BY 4.0) - 技术指南
6. **medicinalsheep/grokmusicvideoprompt** (MIT) - 音乐视频
7. **Roulandu/dance-i2v-prompt** (MIT) - 舞蹈图生视频
8. **langgptai/awesome-grok-prompts** (MIT) - 综合提示词
9. **Rion-Wu-tech/grok-video-workflow** (MIT) - 视频工作流
10. **love1106/grok-imagine-toolkit** (MIT) - 工具包

感谢所有原作者的贡献！

---

## 🤝 参与贡献

欢迎提交新的 Grok Imagine 提示词！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 贡献要求

- ✅ 仅限 Grok Imagine (xAI) 提示词
- ✅ 必须是 SFW 内容
- ✅ 提供中英文版本
- ✅ 注明来源和许可证

---

## 📄 许可证

本项目采用 [MIT License](LICENSE)。

各来源内容保留其原始许可证：
- that-cod/awesome-grok-imagine-prompts: MIT
- seaimagine/awesome-grok-imagine-1-5-prompts: MIT
- YouMind-OpenLab/awesome-grok-imagine-prompts: CC BY 4.0

---

## 🔗 相关链接

- [Grok Imagine 官方文档](https://docs.x.ai/developers/model-capabilities/imagine)
- [xAI 官网](https://x.ai/)
- [Grok Imagine Video 1.5 发布说明](https://x.ai/news/grok-imagine-video-1-5)

---

**整理**: Yep ([gentpan](https://github.com/gentpan)) | **最后更新**: 2026-08-24
