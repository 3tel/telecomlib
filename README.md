# Python Package Telecomlib

ð¦ ä¸ä¸ªä¸ä¸º Telecom æé ç Python Packageã

> ä¸ä¼ å° PyPI åå¯ä»¥ä½¿ç¨ `pip install` å®è£ã
```shell
pip install telecomlib
```

## 1 ä½¿ç¨æ¹æ³



1. ç¼åä½ ç Package ä»£ç ï¼å¹¶è¿è¡æµè¯ã

    ```bash
    # å¨æ¬å°è¿è¡ååæµè¯
    bash scripts/local_test.sh
    ```

2. ä¸ä¼ å° PyPiï¼éè¦æ³¨åï¼ï¼åè[å¦ä½åå¸èªå·±çåå° pypi](https://www.v2ai.cn/2018/07/30/python/1-pypi/)ï¼

    ```bash
    bash scripts/upload_pypi.sh
    ```

3. æ´æ°å° Githubã

    ```bash
    git push
    ```

## 2 é¡¹ç®ç»æ

```
.
âââ package_name # é¡¹ç®åç§°
â    âââ shell # å¨å½ä»¤è¡ä¸­æ§è¡çä»£ç 
â    â    âââ __init__.py
â    â    âââ usage.py
â    âââ src # éæèµæº
â          âââ temp.txt
âââ scripts
â    âââ set_package_name.sh # æ¹éæ¿æ¢é»è®¤çé¡¹ç®åç§°
â    âââ local_install.sh
â    âââ local_test.sh
â    âââ upload_pypi.sh
âââ README.md # é¡¹ç®ææ¡£
âââ requirements.txt # åä¾èµ
âââ .gitignore # å¿½ç¥æä»¶
âââ MANIFEST.in # è¦åå«å¨ sdist å½ä»¤æå»ºçååä¸­çæä»¶åè¡¨ã
âââ LICENSE # è¿éé¢çåå®¹ä¸ºæ¬é¡¹ç®ç Licenseï¼ä½ éè¦æå¨æ¿æ¢å®ã
âââ setup.py # å®è£éç½®
```

## 3 TODO

- [ ] å¢å  test ç¸å³ä»£ç ã

## 4 è®¸å¯

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 5 åè

- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [å¦ä½ä»æ¨¡æ¿åå»ºä»åºï¼](https://docs.github.com/cn/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)
- [å¦ä½åå¸èªå·±çåå° pypi ï¼](https://www.v2ai.cn/2018/07/30/python/1-pypi/)
