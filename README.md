# 基于 Pytest + Requests 的接口自动化测试框架

## 📖 项目简介
本项目是一个基于 Python 语言，采用 Pytest 测试框架、Requests 请求库、Allure 报告工具，并接入 MySQL 数据库校验的企业级接口自动化测试框架。被测系统采用 DummyJSON 开源 API 靶场。

## 🛠️ 技术栈
- **语言**: Python 3.11
- **测试框架**: Pytest
- **请求库**: Requests
- **数据驱动**: PyYAML
- **数据库**: PyMySQL
- **测试报告**: Allure

## 📁 目录结构
```text
api_auto_test/
├── apis/            # 接口层（封装请求）
├── data/            # 数据层（YAML 测试数据）
├── testcases/       # 用例层（业务断言）
├── utils/           # 工具类（如数据库连接）
├── conftest.py      # 全局 Fixture（Session、数据库连接等）
├── pytest.ini       # Pytest 配置文件
└── requirements.txt # 依赖清单
```

## 🚀 核心特性
- 数据驱动：测试数据与测试代码分离，采用 YAML 文件管理。

- 鉴权自动化：利用 Session 保持登录态，自动注入 Token。

- 数据库联动：支持接口调用后直接查库断言，实现业务闭环。

- 高颜值报告：生成 Allure 可视化测试报告，支持挂载响应报文和数据库结果附件。

## 💻 快速开始
安装依赖：

- bash
pip install -r requirements.txt
配置环境：修改 utils/db_utils.py 中的数据库连接信息（账号、密码等）。


- 运行测试：

bash
pytest --alluredir=./allure-results
- 查看报告：

bash
allure serve ./allure-results