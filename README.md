# 检查avail空投资格的脚本，仅限evm钱包

## 安装扩展
+ pip install web3
+ pip install requests
+ pip install loguru

## 例子
```python
from main import Avail

seed = '' # 助记词或私钥
proxy = '' # 127.0.0.1:1087 # 代理，非必需
av = Avail(seed, proxy)
av.check()

```
