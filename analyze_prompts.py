#!/usr/bin/env python3
"""分析所有 prompt 文件，识别需要修复的问题"""

import os
import re
from pathlib import Path
from typing import Dict, List

def analyze_file(filepath: Path) -> Dict:
    """分析单个文件，返回问题列表"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 检查占位符
    if '[技术性 prompt 集合' in content or '[完整文档]' in content:
        issues.append('placeholder')
    
    # 检查 frontmatter 中的 organizer
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        if 'organizer: Yep' in frontmatter:
            issues.append('organizer_yep')
        elif 'organizer:' not in frontmatter:
            issues.append('missing_organizer')
    
    # 检查中文部分是否为英文或混杂
    chinese_match = re.search(r'## 中文\n\n(.*?)(?=\n## English|\Z)', content, re.DOTALL)
    if chinese_match:
        chinese_section = chinese_match.group(1).strip()
        # 去掉标题行
        chinese_lines = [l for l in chinese_section.split('\n') if l.strip() and not l.startswith('**')]
        if chinese_lines:
            chinese_text = ' '.join(chinese_lines)
            # 简单检查：如果中文区90%是ASCII字符（除空格外），可能有问题
            non_space_chars = chinese_text.replace(' ', '').replace('\n', '')
            if non_space_chars:
                ascii_ratio = sum(1 for c in non_space_chars if ord(c) < 128) / len(non_space_chars)
                if ascii_ratio > 0.7:
                    issues.append('chinese_section_english')
    
    # 检查是否过短（English部分少于80字符，排除标题）
    english_match = re.search(r'## English\n\n(.*?)(?=\n---|\Z)', content, re.DOTALL)
    if english_match:
        english_section = english_match.group(1).strip()
        # 去掉标题行和整理行
        english_lines = [l for l in english_section.split('\n') 
                        if l.strip() and not l.startswith('**') and not l.startswith('整理：')]
        english_text = ' '.join(english_lines)
        if len(english_text) < 80:
            issues.append('too_short')
    
    # 检查页脚
    if '整理：Yep' in content or '整理：[Yep]' in content:
        issues.append('footer_yep')
    
    return {
        'path': str(filepath),
        'issues': issues
    }

def main():
    prompts_dir = Path('/workspace/prompts')
    results = []
    
    for md_file in sorted(prompts_dir.rglob('*.md')):
        result = analyze_file(md_file)
        if result['issues']:
            results.append(result)
    
    print(f"总文件数: {len(list(prompts_dir.rglob('*.md')))}")
    print(f"有问题的文件数: {len(results)}")
    print()
    
    # 按问题类型分组
    issue_counts = {}
    for r in results:
        for issue in r['issues']:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
    
    print("问题类型统计:")
    for issue, count in sorted(issue_counts.items()):
        print(f"  {issue}: {count}")
    print()
    
    print("需要修复的文件列表:")
    for r in results:
        print(f"{r['path']}: {', '.join(r['issues'])}")

if __name__ == '__main__':
    main()
