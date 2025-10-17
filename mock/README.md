# 本地 Mock 服务（示例）

这里给两种方式：

## 方案 A：Prism（OpenAPI Mock）
- 前置：安装 Node.js
- 安装 Prism（一次性）
  npm i -g @stoplight/prism-cli
- 启动：
  prism mock ../contracts/openapi.yaml --port 4010
- 访问：
  http://localhost:4010/api/v1/docs

说明：
- Prism 会根据 openapi.yaml 里的 schema 与 examples 自动返回示例。
- 如需固定返回 samples 下的 JSON，可以用 --dynamic=false 或在 OpenAPI 中增加固定 examples。

## 方案 B：Python 轻量 Mock（FastAPI）
- 前置：Python 3.10+
- 安装：
  pip install fastapi uvicorn pydantic
- 运行：
  uvicorn server:app --port 4011

文件说明：
- server.py：返回 samples/ 下的固定 JSON，方便前端/调用方本地联调。
