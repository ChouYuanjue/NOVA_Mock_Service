from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent.parent
SAMPLES = BASE / "samples"

def load_json(name: str):
    with open(SAMPLES / name, "r", encoding="utf-8") as f:
        return json.load(f)

app = FastAPI(title="Nova Mock Server")

def load_json(name: str):
    with open(SAMPLES / name, "r", encoding="utf-8") as f:
        return json.load(f)

# 文档相关
@app.get("/api/v1/docs")
async def list_docs():
    return JSONResponse(load_json("docs_list_success.json"))

@app.get("/api/v1/docs/{doc_id}")
async def get_doc(doc_id: str):
    data = load_json("doc_detail_success.json")
    data["data"]["id"] = doc_id
    return JSONResponse(data)

@app.post("/api/v1/docs")
async def create_doc():
    return JSONResponse({"code": 201, "msg": "created", "data": {"id": "doc_new"}})

@app.put("/api/v1/docs/{doc_id}")
async def update_doc(doc_id: str):
    return JSONResponse({"code": 200, "msg": "updated", "data": {"id": doc_id}})

@app.delete("/api/v1/docs/{doc_id}")
async def delete_doc(doc_id: str):
    return JSONResponse({"code": 200, "msg": "deleted", "data": None})

# 预处理相关
@app.post("/api/v1/preprocess/clean")
async def preprocess_clean():
    return JSONResponse(load_json("preprocess_clean_success.json"))

@app.post("/api/v1/preprocess/dedup")
async def preprocess_dedup():
    return JSONResponse(load_json("preprocess_dedup_success.json"))

@app.post("/api/v1/preprocess/tags")
async def preprocess_tags():
    return JSONResponse(load_json("preprocess_tags_success.json"))

# AI相关
@app.post("/api/v1/ai/summary")
async def ai_summary():
    return JSONResponse(load_json("ai_summary_success.json"))

@app.post("/api/v1/ai/classify")
async def ai_classify():
    return JSONResponse({"code": 200, "msg": "success", "data": {"category": "通知", "confidence": 0.95}})

@app.post("/api/v1/ai/recognize")
async def ai_recognize():
    return JSONResponse({"code": 200, "msg": "success", "data": {"type": "image", "result": {"text": "示例识别结果"}}})

# 推送相关
@app.post("/api/v1/push/webhook")
async def push_webhook():
    return JSONResponse(load_json("push_webhook_success.json"))

@app.post("/api/v1/push/email")
async def push_email():
    return JSONResponse(load_json("push_email_success.json"))

@app.get("/api/v1/push/rss")
async def get_rss(tag: str | None = None):
    xml = """<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<rss><channel><title>Nova Feed</title></channel></rss>"""
    return PlainTextResponse(xml, media_type="application/xml")

# 信息流与检索
@app.get("/api/v1/stream")
async def get_stream():
    return JSONResponse(load_json("stream_success.json"))

@app.get("/api/v1/search")
async def search_get():
    return JSONResponse(load_json("search_success.json"))

@app.post("/api/v1/search")
async def search_post():
    return JSONResponse(load_json("search_success.json"))

@app.get("/api/v1/views/{view_id}")
async def get_view(view_id: str):
    data = load_json("view_success.json")
    data["data"]["id"] = view_id
    return JSONResponse(data)

# 导入作业
@app.post("/api/v1/imports")
async def import_job():
    return JSONResponse(load_json("import_job_created.json"))

@app.get("/api/v1/imports/{job_id}")
async def import_job_status(job_id: str):
    data = load_json("import_job_status.json")
    data["data"]["job_id"] = job_id
    return JSONResponse(data)

# Bot 与 GraphQL
@app.post("/api/v1/bot/send")
async def bot_send():
    return JSONResponse(load_json("bot_send_success.json"))

@app.post("/graphql")
async def graphql():
    return JSONResponse(load_json("graphql_success.json"))

# 根路由
@app.get("/")
async def root():
    return {"msg": "Nova Mock is running"}
