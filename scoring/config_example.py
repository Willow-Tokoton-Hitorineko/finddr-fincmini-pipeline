"""
配置文件示例
复制此文件为 config.py 并填入您的配置
"""

import os

# OpenAI API 配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# 可选：指定OpenAI API Base URL（如使用代理或本地模型）
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", None)

# 默认评估模型
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4")

# 默认阈值
DEFAULT_THRESHOLD = float(os.getenv("DEFAULT_THRESHOLD", "0.5"))

# 设置环境变量
if OPENAI_API_KEY and OPENAI_API_KEY != "your_openai_api_key_here":
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

if OPENAI_API_BASE:
    os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE

