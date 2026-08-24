# Grok Imagine 提示词收藏

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Prompts](https://img.shields.io/badge/Prompts-197-blue.svg)](data/prompts.jsonl)

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
| 总提示词数 | **197** |
| 分类数 | **12** |
| 数据来源 | **3** |

---

## 🗂️ 分类目录

| 分类 | 提示词数 | 文件 |
|------|---------|------|
| 电影感 (Cinematic) | 34 | [cinematic.md](prompts/cinematic.md) |
| 写实肖像 (Photorealistic Portraits) | 33 | [photorealistic_potraits.md](prompts/photorealistic_potraits.md) |
| 视频动画 (Video Animation) | 26 | [video_animation.md](prompts/video_animation.md) |
| 编辑转换 (Editing & Transformation) | 16 | [editing_transformation.md](prompts/editing_transformation.md) |
| 抽象超现实 (Abstract & Surreal) | 13 | [abstract_surreal.md](prompts/abstract_surreal.md) |
| 科幻 (Sci-Fi) | 13 | [sci_fi.md](prompts/sci_fi.md) |
| 杂项 (Misc) | 13 | [misc.md](prompts/misc.md) |
| 奇幻 (Fantasy) | 12 | [fantasy.md](prompts/fantasy.md) |
| 自然 (Nature) | 11 | [nature.md](prompts/nature.md) |
| 动漫赛博朋克 (Anime & Cyberpunk) | 9 | [anime_cyberpunk.md](prompts/anime_cyberpunk.md) |
| 动作视频 (Action Videos) | 9 | [action_videos.md](prompts/action_videos.md) |
| 风格氛围 (Styles & Moods) | 8 | [styles_moods.md](prompts/styles_moods.md) |

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

每个提示词记录包含以下字段：

```json
{
  "id": "唯一标识",
  "title_zh": "中文标题",
  "title_en": "English Title",
  "prompt": "原始提示词",
  "prompt_zh": "中文提示词（或说明）",
  "prompt_en": "English prompt",
  "tags": ["标签1", "标签2"],
  "source_repo": "来源仓库",
  "source_url": "来源 URL",
  "source_license": "许可证",
  "organizer": {
    "name": "Yep",
    "github": "gentpan",
    "note": "整理"
  }
}
```

---

## 📚 数据来源

本项目整理自以下开源项目（详见 [sources.md](sources.md)）：

1. **that-cod/awesome-grok-imagine-prompts** (MIT)
   - 197 个提示词
   - 已跳过 NSFW 内容

2. **seaimagine/awesome-grok-imagine-1-5-prompts** (MIT)
   - 约 40 个原创提示词
   - 分类清晰的生产级内容

3. **YouMind-OpenLab/awesome-grok-imagine-prompts** (CC BY 4.0)
   - 精选提示词预览
   - 2500+ 提示词库

感谢原作者的贡献！

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
