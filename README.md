# Nova Mock Service 使用说明

## 目录结构
- `contracts/`         —— OpenAPI 契约文件（openapi.yaml）
- `samples/`           —— 各接口的 Golden JSON 示例数据
- `samples/ndjson/`    —— 批量导入用 NDJSON 示例
- `server/`            —— FastAPI Mock 服务代码

## 快速启动

### 方式一：Prism（推荐，自动按契约 Mock）
1. 安装 Node.js
2. 全局安装 Prism：
   ```pwsh
   npm i -g @stoplight/prism-cli
   ```
3. 启动 Mock 服务（在 mock-service 目录下）：
   ```pwsh
   prism mock contracts/openapi.yaml --port 4010
   ```
4. 访问接口：
   - http://localhost:4010/api/v1/docs
   - http://localhost:4010/api/v1/ai/summary
   - ...（所有契约中定义的端点均可访问）

### 方式二：FastAPI 轻量 Mock
1. 安装 Python 3.10+
2. 安装依赖：
   ```pwsh
   pip install fastapi uvicorn pydantic
   ```
3. 启动服务（在 mock-service/server 目录下）：
   ```pwsh
   uvicorn server:app --port 4011
   ```
4. 访问接口：
   - http://localhost:4011/api/v1/docs
   - http://localhost:4011/api/v1/ai/summary
   - http://localhost:4011/api/v1/preprocess/clean
   - http://localhost:4011/api/v1/imports/imp_123
   - http://localhost:4011/api/v1/bot/send
   - http://localhost:4011/graphql

## 如何扩展
- 新增接口：
  1. 在 contracts/openapi.yaml 中补充端点和 schema。
  2. 在 samples/ 下增加对应的 JSON 示例。
  3. FastAPI 方案下，在 server/server.py 补充路由。
- 新增批量导入样例：
  - 在 samples/ndjson/ 下添加 NDJSON 文件。

## 调试说明

建议使用 [Apifox](https://apifox.com/) 进行接口调试和测试。

### 使用步骤
1. **导入 OpenAPI 契约**：
   - 打开 Apifox，创建或选择项目。
   - 导入 `contracts/openapi.yaml` 文件。
2. **验证接口**：
   - 在 Apifox 中查看并测试所有定义的接口。
   - 确保接口响应与契约一致。
3. **Mock 数据测试**：
   - 使用 Apifox 的 Mock 功能，快速验证接口的响应数据。

通过 Apifox，可以更高效地进行接口调试和契约验证，提升开发与联调效率。

## 说明
- 所有接口响应结构、字段、示例均与《协作对接方案（草案）》保持一致。
- 推荐优先用 Prism 方式，自动 Mock，便于契约驱动开发。
- FastAPI 方案适合需要自定义逻辑或特殊响应的场景。

如有问题或需补充端点，欢迎在本目录下补充样例、契约或脚本，并在主文档中同步说明。
