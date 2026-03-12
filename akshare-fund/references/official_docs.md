# AKShare 官方文档索引

本文档汇总 AKShare 官方资源和常用参考链接。

## 官方资源

| 资源 | 链接 |
|------|------|
| 官方文档 | https://akshare.akfamily.xyz |
| GitHub 仓库 | https://github.com/akfamily/akshare |
| PyPI | https://pypi.org/project/akshare |
| 问题反馈 | https://github.com/akfamily/akshare/issues |

## 文档目录

### 基金数据
- **公募基金数据**: https://akshare.akfamily.xyz/data/fund/fund_public.html
- **私募基金数据**: https://akshare.akfamily.xyz/data/fund/fund_public.html#id6


### 行情数据
- **ETF基金实时行情-东财**: https://akshare.akfamily.xyz/data/fund/fund_public.html#etf
- **ETF基金实时行情-同花顺**: https://akshare.akfamily.xyz/data/fund/fund_public.html#id7

### 板块数据
- **基金实时行情-同花顺**: https://akshare.akfamily.xyz/data/stock/stock.html#id4


## 安装和更新

```bash
# 安装
pip install akshare

# 更新到最新版
pip install akshare --upgrade

# 查看版本
python -c "import akshare; print(akshare.__version__)"
```

## 常见问题

### 1. 接口报错或返回空数据
- 检查 akshare 版本是否最新
- 部分接口可能暂时不可用，等待官方修复
- 检查网络连接

### 2. 接口限流
- 批量请求时添加 `time.sleep(0.5)` 延时
- 使用本 skill 的缓存功能避免重复请求

### 3. 数据字段变化
- AKShare 接口可能随时更新字段名
- 建议使用 try-except 处理字段缺失

## 接口更新记录

关注官方 GitHub Releases 获取最新接口变更：
https://github.com/akfamily/akshare/releases

## 推荐用法

1. 使用本 skill 封装的脚本而非直接调用接口
2. 开启数据缓存减少重复请求
3. 定期更新 akshare 到最新版本
