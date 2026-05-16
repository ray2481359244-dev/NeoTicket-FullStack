# NeoTicket-FullStack
一个简易的全栈项目
# 🎫 NeoTicket-FullStack

> **基于 Python Flask + MySQL + HTML5 构建的工业级全栈购票/退票事务控制系统原型。**
> 本项目核心展示了在全栈工程中，如何通过表现层、业务逻辑层与数据持久层的配合，实现高安全性的数据库原子性事务（ACID）控制。

---

## 🏗️ 系统三层架构设计 (Architecture)

本项目严格遵循经典的软件工程三层架构进行解耦开发：
1. **表现层 (Frontend / UI)**：采用响应式 HTML5 + CSS3（赛博朋克极客蓝风格），利用现代 JavaScript (Fetch API) 实现异步无刷新数据交互。
2. **业务逻辑层 (Backend / API)**：基于 Python Flask 框架搭建微服务网关，处理参数化解析、跨域防护（CORS）与核心业务流转。
3. **数据访问与持久层 (Database)**：采用 MySQL (InnoDB 引擎) 存储，通过强外键约束与事务锁机制确保底层数据参照完整性。

---

## 🚀 核心技术亮点 (Technical Highlights)

* **🛡️ 工业级 SQL 注入防御**：后端全面废除字符串拼接，强制采用 `PyMySQL` 的**参数化查询（Parameterized Queries）** 占位符机制，死守网络安全防线。
* **⚡ 严格的 ACID 事务控制**：退票业务（归还库存、修改订单状态）封装在单次数据库事务中，采用 `START TRANSACTION` 与 `COMMIT/ROLLBACK`，确保高并发下的“全成或全败”，严防超卖与数据孤儿现象。
* **🌐 跨域安全防护 (CORS)**：内嵌 `Flask-CORS` 拦截器，动态调校网络握手协议，安全掏通前后端异构端口的通信隧道。
* **🔤 字符集全链路优化**：统一全链路（Python 连接器与 MySQL 引擎）字符集为 `utf8mb4`，完美降伏中文字符串编解码乱码大魔王。

---

## 📂 仓库目录结构说明

```text
NeoTicket-FullStack/
├── frontend/             # 前端表现层
│   └── index.html        # 赛博朋克风售后控制台（含 Fetch 异步通信逻辑）
└── backend/              # 后端业务逻辑层
    └── main.py           # Flask 核心 Web 服务器（含连接池与 MySQL 事务源码）
