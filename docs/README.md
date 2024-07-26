# 巴布森校友+ 小程序 & 校友卡管理系统

## 项目介绍

### 巴布森校友+

巴布森校友+ 是巴布森学院在中国的官方校友会小程序。它提供了一个便捷的交流平台，供校友们获取学院资讯、参与活动、联系朋友并拓展人脉。

### 校友卡管理系统

这是一个基于 Streamlit 的校友卡管理系统。该系统允许用户查看项目文件结构，触发更新操作并查看更新日志。

## 目录结构

### 巴布森校友+ 小程序

- `app.js`: 小程序主入口文件。
- `app.json`: 全局配置文件。
- `pages/index/index.js`: 首页逻辑文件。
- `pages/index/index.wxml`: 首页结构文件。
- `pages/index/index.wxss`: 首页样式文件。
- `project.config.json`: 项目配置文件。
- `LICENSE`: 许可证文件。

### 校友卡管理系统

- `configs/config.yaml`: 配置文件，包含数据库、API 密钥和其他设置。
- `docs/README.md`: 项目说明文档。
- `pages/index/index.html`: 基本网页结构，展示个人中心和校友卡申领表单。
- `src/app.py`: Streamlit 应用的主脚本，集成文件展示和更新操作。
- `src/utils.py`: 实用工具模块，包含加载配置和数据库连接等函数。
- `temp/OneDC_Updater/update.log`: 更新操作的日志文件，记录每次更新的详细信息。
- `temp/OneDC_Updater/update.py`: 更新脚本，执行更新操作并记录日志。

## 运行

### 巴布森校友+ 小程序

1. 安装 [微信开发者工具](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)。
2. 导入项目目录到微信开发者工具。
3. 运行并调试小程序。

### 校友卡管理系统

1. 安装依赖：`pip install -r requirements.txt`
2. 运行应用：`streamlit run src/app.py`

## 使用方法

### 校友卡管理系统

运行应用后，可以在浏览器中查看项目文件结构，触发更新操作并查看更新日志。

## 许可证

本项目使用 MIT 许可证。有关详细信息，请参见 LICENSE 文件。
