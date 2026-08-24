#!/usr/bin/env python3
"""
Grok Imagine 图像/视频生成脚本

此脚本用于调用 Grok Imagine API 生成图像或视频。
目前为存根实现，需要配置 API 密钥和具体参数。

使用方法:
    python scripts/generate_images.py --prompt "your prompt here" --mode video

依赖:
    pip install requests

环境变量:
    GROK_API_KEY: xAI Grok Imagine API 密钥
"""

import argparse
import json
import sys
from pathlib import Path


def load_prompt_from_file(prompt_file):
    """从 markdown 文件加载提示词"""
    file_path = Path(prompt_file)
    
    if not file_path.exists():
        print(f"错误: 文件不存在 {prompt_file}", file=sys.stderr)
        return None
    
    content = file_path.read_text(encoding='utf-8')
    
    # 简单解析：提取 ## English 部分的内容
    if '## English' in content:
        parts = content.split('## English', 1)[1]
        # 移除标题行和页脚
        lines = parts.split('\n')
        prompt_lines = []
        for line in lines:
            if line.startswith('---') or line.startswith('整理：'):
                break
            if line.strip() and not line.startswith('**'):
                prompt_lines.append(line.strip())
        
        return ' '.join(prompt_lines)
    
    return None


def generate_image(prompt, **kwargs):
    """
    生成图像（存根实现）
    
    Args:
        prompt (str): 提示词
        **kwargs: 其他参数（aspect_ratio, resolution 等）
    
    Returns:
        dict: 生成结果
    """
    print(f"[存根] 生成图像")
    print(f"  提示词: {prompt[:100]}...")
    print(f"  参数: {kwargs}")
    print()
    print("提示: 此功能需要配置 xAI API 密钥")
    print("      export GROK_API_KEY='your-api-key'")
    print("      参考: https://docs.x.ai/")
    
    return {
        "status": "stub",
        "message": "这是存根实现，需要配置真实的 API"
    }


def generate_video(prompt, **kwargs):
    """
    生成视频（存根实现）
    
    Args:
        prompt (str): 提示词
        **kwargs: 其他参数（duration, aspect_ratio, resolution 等）
    
    Returns:
        dict: 生成结果
    """
    print(f"[存根] 生成视频")
    print(f"  提示词: {prompt[:100]}...")
    print(f"  参数: {kwargs}")
    print()
    print("提示: 此功能需要配置 xAI API 密钥")
    print("      export GROK_API_KEY='your-api-key'")
    print("      参考: https://docs.x.ai/developers/model-capabilities/video")
    
    return {
        "status": "stub",
        "message": "这是存根实现，需要配置真实的 API"
    }


def main():
    parser = argparse.ArgumentParser(
        description='使用 Grok Imagine 生成图像或视频',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 使用文本提示词生成图像
  python scripts/generate_images.py --prompt "A beautiful sunset" --mode image

  # 使用文件中的提示词生成视频
  python scripts/generate_images.py --file prompts/电影/0001.md --mode video

  # 指定参数
  python scripts/generate_images.py --prompt "..." --mode video --duration 10 --aspect-ratio 16:9
        """
    )
    
    parser.add_argument(
        '--prompt',
        type=str,
        help='直接指定提示词文本'
    )
    
    parser.add_argument(
        '--file',
        type=str,
        help='从 markdown 文件读取提示词'
    )
    
    parser.add_argument(
        '--mode',
        type=str,
        choices=['image', 'video'],
        default='image',
        help='生成模式：image 或 video（默认：image）'
    )
    
    parser.add_argument(
        '--duration',
        type=int,
        default=10,
        help='视频时长（秒），仅用于 video 模式（默认：10）'
    )
    
    parser.add_argument(
        '--aspect-ratio',
        type=str,
        default='16:9',
        help='宽高比，如 16:9, 9:16, 1:1（默认：16:9）'
    )
    
    parser.add_argument(
        '--resolution',
        type=str,
        choices=['480p', '720p', '1080p'],
        default='720p',
        help='分辨率（默认：720p）'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        help='输出文件路径'
    )
    
    args = parser.parse_args()
    
    # 获取提示词
    prompt = None
    if args.prompt:
        prompt = args.prompt
    elif args.file:
        prompt = load_prompt_from_file(args.file)
        if not prompt:
            print("错误: 无法从文件中提取提示词", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        print("\n错误: 必须指定 --prompt 或 --file", file=sys.stderr)
        sys.exit(1)
    
    # 准备参数
    kwargs = {
        'aspect_ratio': args.aspect_ratio,
        'resolution': args.resolution,
    }
    
    if args.mode == 'video':
        kwargs['duration'] = args.duration
    
    if args.output:
        kwargs['output'] = args.output
    
    # 生成
    if args.mode == 'image':
        result = generate_image(prompt, **kwargs)
    else:
        result = generate_video(prompt, **kwargs)
    
    # 输出结果
    print("\n结果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
