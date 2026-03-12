# -*- coding: utf-8 -*-
"""
获取基金实时行情

用法:
    python get_realtime_quote.py 000001
    python get_realtime_quote.py 000001 000002
"""
import argparse
import sys
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')

try:
    import akshare as ak
    import pandas as pd
except ImportError:
    print("请先安装依赖: pip install akshare pandas")
    sys.exit(1)

from cache_manager import cache_get, cache_set


def get_realtime_quote(codes: list, use_markdown: bool = True, use_cache: bool = True):
    """获取实时行情"""
    print("正在获取实时行情...")
    
    # 尝试从缓存获取 (全量市场数据)
    df = None
    if use_cache:
        cached_data = cache_get('realtime', 'market_spot')
        if cached_data:
            # print("从缓存加载市场数据...")
            df = pd.DataFrame(cached_data)
    
    if df is None:
        try:
            df = ak.fund_etf_spot_em()
            # 写入缓存
            if use_cache:
                cache_set('realtime', df.to_dict('records'), 'market_spot')
        except Exception as e:
            print(f"东财网获取失败: {e}")
            try:
                from datetime import datetime
                df = ak.fund_etf_spot_ths(datetime.now().strftime('%Y%m%d'))
            except Exception as e:
                print(f"同花顺获取失败: {e}")
                return

    if df is not None:
        # 处理可能的列名差异，兼容不同数据源的列名
        code_col = '代码' if '代码' in df.columns else '基金代码'
        result = df[df[code_col].isin(codes)]
        if len(result) > 0:
            if use_markdown:
                print(result.to_markdown(index=False))
            else:
                print(result.to_string(index=False))
        else:
            print(f"未找到代码: {codes}")


def main():
    parser = argparse.ArgumentParser(description='获取实时行情')
    parser.add_argument('codes', nargs='+', help='基金代码列表')
    parser.add_argument('--no-cache', action='store_false', help='不使用缓存')
    
    args = parser.parse_args()
    
    get_realtime_quote(args.codes, use_cache=not args.no_cache)


if __name__ == '__main__':
    main()
