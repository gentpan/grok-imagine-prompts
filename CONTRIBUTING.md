# 贡献指南

感谢你考虑为 Grok Imagine 提示词收藏做出贡献！

## 📝 贡献内容

### 接受的内容

- ✅ Grok Imagine (xAI) 的视频生成提示词
- ✅ Grok Imagine 的图像生成提示词
- ✅ Grok Imagine 相关的技术文档和教程链接
- ✅ 提示词优化技巧和最佳实践

### 不接受的内容

- ❌ 其他模型的提示词（如 GPT Image 2, Nano Banana 等）
- ❌ NSFW（不适合工作场合）内容
- ❌ 违反法律法规的内容
- ❌ 侵犯版权的内容

## 🚀 如何贡献

### 1. 提交新提示词

#### 方式一：通过 Issue

1. 打开 [New Issue](https://github.com/gentpan/grok-imagine-prompts/issues/new)
2. 标题：`[新提示词] 简短描述`
3. 内容包括：
   - 中文标题
   - 英文标题
   - 提示词内容（中英文）
   - 分类（如：电影感、动漫、科幻等）
   - 来源（如果是转载）
   - 许可证信息

#### 方式二：通过 Pull Request

1. Fork 本仓库
2. 创建新分支：`git checkout -b add-new-prompts`
3. 添加你的提示词到 `data/prompts.jsonl`
4. 如果需要，在 `prompts/` 目录下创建或更新对应分类的 markdown 文件
5. 提交更改：`git commit -m "添加新提示词：描述"`
6. 推送到你的 Fork：`git push origin add-new-prompts`
7. 创建 Pull Request

### 2. 改进现有内容

- 修正错别字或翻译错误
- 改进提示词的描述或分类
- 补充来源信息或许可证

### 3. 报告问题

如果发现任何问题，请 [创建 Issue](https://github.com/gentpan/grok-imagine-prompts/issues/new)：

- 📝 错误的翻译
- 🔗 失效的链接
- ⚠️ 不适当的内容
- 📄 许可证相关问题

## 📋 提交格式

### 提示词数据格式

```json
{
  "id": "唯一的 8 位哈希值",
  "title_zh": "中文标题",
  "title_en": "English Title",
  "prompt": "原始提示词文本",
  "prompt_zh": "中文提示词或说明",
  "prompt_en": "English prompt",
  "tags": ["主分类", "子分类"],
  "source_repo": "来源仓库（如有）",
  "source_url": "来源 URL（如有）",
  "source_license": "许可证（如 MIT, CC BY 4.0）",
  "organizer": {
    "name": "你的名字",
    "github": "你的 GitHub 用户名",
    "note": "整理"
  }
}
```

### Markdown 文件格式

```markdown
## N. 中文标题

### 中文

**标题**: 中文标题

**提示词**: 中文提示词内容

### English

**Title**: English Title

**Prompt**: English prompt content

---

**整理**: 名字 ([GitHub用户名](https://github.com/用户名))

**来源**: [仓库名](来源链接) (许可证)
```

## ✅ 审核标准

提交的内容需要满足以下标准：

1. **准确性** - 提示词应该可以在 Grok Imagine 上正常使用
2. **双语** - 必须包含中文和英文版本
3. **来源** - 如果转载，必须注明来源和许可证
4. **分类** - 正确归类到合适的类别
5. **格式** - 遵循项目的数据格式规范
6. **SFW** - 内容适合所有年龄段和工作场合

## 📄 许可证

通过提交贡献，你同意你的内容将采用 [MIT License](LICENSE) 授权。

如果你提交的是转载内容，请确保：
- 原内容允许转载和二次分发
- 正确标注原始来源和许可证
- 遵守原始许可证的要求

## 🙏 感谢

感谢所有贡献者！你的每一份贡献都让这个项目变得更好。

---

有任何问题？欢迎通过 [Issues](https://github.com/gentpan/grok-imagine-prompts/issues) 或 [Discussions](https://github.com/gentpan/grok-imagine-prompts/discussions) 联系我们。
