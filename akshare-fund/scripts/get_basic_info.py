# -*- coding: utf-8 -*-
"""
获取基金基本信息

用法:
    python get_basic_info.py 000001
"""
import argparse
import sys
import warnings
warnings.filterwarnings('ignore')

try:
    import akshare as ak
    import pandas as pd
except ImportError:
    print("请先安装依赖: pip install akshare pandas")
    sys.exit(1)

from cache_manager import cache_get, cache_set


def get_basic_info(code: str, Use_markdown: bool = True, use_cache: bool = True):
    """获取基金基本信息"""
    print("正在获取基金基本信息...")
    
    # 尝试从缓存获取 (全量市场数据)
    df = None
    if use_cache:
        cached_data = cache_get('basic', 'market_spot')
        if cached_data:
            # print("从缓存加载市场数据...")
            df = pd.DataFrame(cached_data)
    
    if df is None:
        try:
            df = ak.fund_overview_em(symbol=code)
            # 写入缓存
            if use_cache:
                cache_set('basic', df.to_dict('records'), 'market_spot')
        except Exception as e:
            print(f"获取失败: {e}")
            return
    
    if df is not None:
        if len(df) > 0:
            if Use_markdown:
                print(df.to_markdown(index=False))
            else:
                print(df.to_string(index=False))
        else:
            print(f"未找到代码: {code}")


def main():
    parser = argparse.ArgumentParser(description='获取基本信息')
    parser.add_argument('code', help='基金代码')
    parser.add_argument('--no-cache', action='store_false', help='不使用缓存')
    
    args = parser.parse_args()
    
    get_basic_info(args.code, use_cache=not args.no_cache)


if __name__ == '__main__':
    main()
