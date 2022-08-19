# Python Package Telecomlib

📦 一个专为 Telecom 打造的 Python Package。

> 上传到 PyPI 后可以使用 `pip install` 安装。
```shell
pip install telecomlib
```

## 1 使用方法



1. 编写你的 Package 代码，并进行测试。

    ```bash
    # 在本地进行充分测试
    bash scripts/local_test.sh
    ```

2. 上传到 PyPi（需要注册），参考[如何发布自己的包到 pypi](https://www.v2ai.cn/2018/07/30/python/1-pypi/)；

    ```bash
    bash scripts/upload_pypi.sh
    ```

3. 更新到 Github。

    ```bash
    git push
    ```

## 2 项目结构

```
.
├── package_name # 项目名称
│    ├── shell # 在命令行中执行的代码
│    │    ├── __init__.py
│    │    └── usage.py
│    └── src # 静态资源
│          └── temp.txt
├── scripts
│    ├── set_package_name.sh # 批量替换默认的项目名称
│    ├── local_install.sh
│    ├── local_test.sh
│    └── upload_pypi.sh
├── README.md # 项目文档
├── requirements.txt # 包依赖
├── .gitignore # 忽略文件
├── MANIFEST.in # 要包含在 sdist 命令构建的分发中的文件列表。
├── LICENSE # 这里面的内容为本项目的 License，你需要手动替换它。
└── setup.py # 安装配置
```

## 3 TODO

- [ ] 增加 test 相关代码。

## 4 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 5 参考

- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [如何从模板创建仓库？](https://docs.github.com/cn/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)
- [如何发布自己的包到 pypi ？](https://www.v2ai.cn/2018/07/30/python/1-pypi/)
