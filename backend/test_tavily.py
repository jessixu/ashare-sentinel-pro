#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试改进后的 Tavily 搜索结果"""

import os
import sys
import asyncio
from dotenv import load_dotenv

load_dotenv()

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.search_service import search_financial_news

async def test_search():
    print("=" * 80)
    print("测试改进后的 Tavily 搜索 - 杰瑞股份 (002353)")
    print("=" * 80)

    result = await search_financial_news("002353", "杰瑞", max_results=5)

    print("\n" + "=" * 80)
    print("搜索结果摘要:")
    print("=" * 80)
    print(result.get("summary", "无摘要"))

    print("\n" + "=" * 80)
    print(f"找到 {len(result.get('results', []))} 条高质量结果")
    print("=" * 80)

    for i, res in enumerate(result.get("results", []), 1):
        print(f"\n{i}. {res.get('title', 'N/A')}")
        print(f"   时间: {res.get('published_date', '未知')}")
        print(f"   来源: {res.get('url', 'N/A')}")
        print(f"   评分: {res.get('score', 0)}")
        content = res.get('content', 'N/A')
        if len(content) > 300:
            content = content[:300] + "..."
        print(f"   内容: {content}")

if __name__ == "__main__":
    asyncio.run(test_search())

