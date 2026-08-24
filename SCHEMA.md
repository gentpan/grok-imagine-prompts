# 数据结构说明

本项目采用规范化的目录结构和数据格式，便于管理和使用。

## 目录结构

```
grok-imagine-prompts/
├── README.md                    # 项目说明
├── CONTRIBUTING.md              # 贡献指南
├── LICENSE                      # MIT 许可证
├── SCHEMA.md                    # 本文件：数据结构说明
├── sources.md                   # 数据来源详细说明
├── data/
│   └── prompts.jsonl           # 所有提示词的 JSONL 格式数据
├── prompts/                     # 提示词 Markdown 文件（按分类）
│   ├── 写实/                    # 写实肖像类
│   │   ├── 0001.md
│   │   ├── 0002.md
│   │   └── ...
│   ├── 电影/                    # 电影感类
│   │   ├── 0001.md
│   │   └── ...
│   ├── 动漫/                    # 动漫风格类
│   ├── 动作/                    # 动作视频类
│   ├── 动画/                    # 视频动画类
│   ├── 风景/                    # 自然风景类
│   ├── 科幻/                    # 科幻类
│   ├── 奇幻/                    # 奇幻类
│   ├── 抽象/                    # 抽象超现实类
│   ├── 编辑/                    # 编辑转换类
│   ├── 风格/                    # 风格氛围类
│   ├── 视频/                    # 视频生成类
│   └── 其它/                    # 其他类别
└── scripts/
    └── generate_images.py       # 图像生成脚本（存根）
```

## Markdown 文件格式

每个提示词文件（如 `prompts/电影/0001.md`）包含以下部分：

### 1. YAML Frontmatter

文件开头的 YAML 元数据块：

```yaml
---
id: 唯一标识符（8位哈希）
title_zh: 中文标题
title_en: English Title
category: 中文分类名
tags:
  - 标签1
  - 标签2
source_repo: 来源仓库全名
source_url: 来源完整 URL
source_license: 许可证类型
organizer:
  name: Yep
  github: gentpan
  note: 整理
---
```

### 2. 中文内容

```markdown
## 中文

**标题**

提示词内容（中文）
```

### 3. 英文内容

```markdown
## English

**Title**

Prompt content (English)
```

### 4. 页脚

```markdown
---

整理：Yep（[gentpan](https://github.com/gentpan)）  
来源：[仓库名](URL) (许可证)
```

## JSONL 数据格式

`data/prompts.jsonl` 文件中，每行是一个 JSON 对象：

```json
{
  "id": "唯一的8位哈希值",
  "title_zh": "中文标题",
  "title_en": "English Title",
  "prompt": "原始提示词文本",
  "prompt_zh": "中文提示词",
  "prompt_en": "English prompt",
  "tags": ["标签1", "标签2"],
  "source_repo": "owner/repository",
  "source_url": "https://github.com/...",
  "source_license": "MIT",
  "organizer": {
    "name": "Yep",
    "github": "gentpan",
    "note": "整理"
  }
}
```

## 字段说明

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 由提示词内容生成的唯一标识符（MD5 哈希前8位） |
| `title_zh` | string | 中文标题 |
| `title_en` | string | 英文标题 |
| `prompt` | string | 原始提示词文本（通常是英文） |
| `prompt_zh` | string | 中文提示词或中文说明 |
| `prompt_en` | string | 英文提示词 |
| `category` | string | 中文分类名（仅在 YAML 中） |
| `tags` | array | 标签列表，用于多维度分类 |
| `source_repo` | string | 来源 GitHub 仓库（格式：owner/repo） |
| `source_url` | string | 提示词的原始来源 URL |
| `source_license` | string | 原始内容的许可证类型 |
| `organizer` | object | 整理者信息 |

## 分类体系

采用中文目录名，便于中文用户浏览：

| 中文分类 | 英文对应 | 说明 |
|---------|---------|------|
| 写实 | Photorealistic | 写实风格肖像、照片 |
| 电影 | Cinematic | 电影感镜头、叙事 |
| 动漫 | Anime | 动漫、二次元风格 |
| 动作 | Action | 动作场景、运动 |
| 动画 | Animation | 视频动画效果 |
| 风景 | Nature/Landscape | 自然风景、户外 |
| 科幻 | Sci-Fi | 科幻场景、未来感 |
| 奇幻 | Fantasy | 奇幻、魔幻题材 |
| 抽象 | Abstract | 抽象艺术、超现实 |
| 编辑 | Editing | 编辑转换、特效 |
| 风格 | Styles | 风格化、氛围营造 |
| 视频 | Video | 视频生成技巧 |
| 其它 | Misc | 其他未分类内容 |

## 文件命名规范

- Markdown 文件：`0001.md`, `0002.md`, ... `9999.md`
- 使用4位数字编号，不足补零
- 按添加顺序或重要性排序
- 同一分类内保持连续编号

## 许可证信息

本项目整理内容采用 **MIT License**，原始提示词保留其来源许可证：

- **MIT License**: 可自由使用、修改、分发
- **CC BY 4.0**: 需注明原作者和来源
- 每个提示词的 `source_license` 字段标注其原始许可证

## 使用说明

### 读取 JSONL 数据

```python
import json

prompts = []
with open('data/prompts.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        prompts.append(json.loads(line))

print(f"总计 {len(prompts)} 个提示词")
```

### 按分类筛选

```python
# 获取所有电影类提示词
cinematic_prompts = [p for p in prompts if '电影' in p.get('tags', [])]
```

### 解析 Markdown 文件

```python
import yaml
from pathlib import Path

def parse_prompt_md(md_file):
    content = Path(md_file).read_text(encoding='utf-8')
    
    # 提取 YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        yaml_content = parts[1]
        md_content = parts[2]
        
        metadata = yaml.safe_load(yaml_content)
        return metadata, md_content
    
    return None, content

# 使用示例
metadata, content = parse_prompt_md('prompts/电影/0001.md')
print(metadata['title_zh'])
```

## 数据更新

如需添加新的提示词：

1. 为新提示词生成唯一 ID
2. 确定合适的分类
3. 创建对应的 Markdown 文件（编号递增）
4. 追加到 `data/prompts.jsonl`
5. 确保包含完整的双语内容和来源信息

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

**维护者**: Yep ([gentpan](https://github.com/gentpan))  
**最后更新**: 2026-08-24
