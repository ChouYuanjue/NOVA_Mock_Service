---
title: Nova 信息流 API v1.0.0
language_tabs:
  - python: Python
language_clients:
  - python: ""
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="nova-api">Nova 信息流 API v1.0.0</h1>

> Generator: Widdershins v4.0.1
> 
> Scroll down for code samples, example requests and responses. 

面向协作与 Mock 的契约。统一响应结构：{"code", "msg", "data", "trace_id?"}

Base URLs:

* <a href="http://localhost:4010">http://localhost:4010</a>

* <a href="http://localhost:8000">http://localhost:8000</a>

<h1 id="nova-api-ai">Ai</h1>

Auto-generated tag for Ai

## post_api_v1_ai_summary

<a id="opIdpost_api_v1_ai_summary"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/ai/summary', headers = headers)

print(r.json())

```

`POST /api/v1/ai/summary`

*生成摘要*

TODO: add description.

> Body parameter

```json
{
  "content": "string"
}
```

<h3 id="post_api_v1_ai_summary-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AiSummaryRequest](#schemaaisummaryrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "summary": "string"
  }
}
```

<h3 id="post_api_v1_ai_summary-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[AiSummaryResponse](#schemaaisummaryresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_ai_classify

<a id="opIdpost_api_v1_ai_classify"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/ai/classify', headers = headers)

print(r.json())

```

`POST /api/v1/ai/classify`

*文本分类*

TODO: add description.

> Body parameter

```json
{
  "content": "string"
}
```

<h3 id="post_api_v1_ai_classify-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AiClassifyRequest](#schemaaiclassifyrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "category": "通知",
    "confidence": 0.95
  }
}
```

<h3 id="post_api_v1_ai_classify-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[AiClassifyResponse](#schemaaiclassifyresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_ai_recognize

<a id="opIdpost_api_v1_ai_recognize"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/ai/recognize', headers = headers)

print(r.json())

```

`POST /api/v1/ai/recognize`

*图片/表格/公式识别*

TODO: add description.

> Body parameter

```json
{
  "file": "string"
}
```

<h3 id="post_api_v1_ai_recognize-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AiRecognizeRequest](#schemaairecognizerequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "type": "image",
    "result": {}
  }
}
```

<h3 id="post_api_v1_ai_recognize-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[AiRecognizeResponse](#schemaairecognizeresponse)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-bot">Bot</h1>

Auto-generated tag for Bot

## post_api_v1_bot_send

<a id="opIdpost_api_v1_bot_send"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/bot/send', headers = headers)

print(r.json())

```

`POST /api/v1/bot/send`

*Bot 发送消息*

TODO: add description.

> Body parameter

```json
{
  "platform": "qq",
  "target": "group:123456",
  "content": "string"
}
```

<h3 id="post_api_v1_bot_send-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BotSendRequest](#schemabotsendrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}
```

<h3 id="post_api_v1_bot_send-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdOk](#schemastdok)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-docs">Docs</h1>

Auto-generated tag for Docs

## get_api_v1_docs

<a id="opIdget_api_v1_docs"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/docs', headers = headers)

print(r.json())

```

`GET /api/v1/docs`

*获取文档列表*

TODO: add description.

<h3 id="get_api_v1_docs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|none|
|size|query|integer|false|none|
|tag|query|string|false|none|
|source|query|string|false|none|
|sort|query|string|false|none|
|fields|query|string|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|source|yuque|
|source|wechat|
|source|qq|
|source|web|

> Example responses

> success

```json
{
  "code": 200,
  "msg": "success",
  "data": [
    {
      "id": "doc_1",
      "source_id": "yuque:1",
      "source": "yuque",
      "title": "A",
      "summary": "...",
      "tags": [
        "通知"
      ],
      "created_at": "2025-10-10T09:00:00Z"
    },
    {
      "id": "doc_2",
      "source_id": "web:2",
      "source": "web",
      "title": "B",
      "summary": "...",
      "tags": [
        "活动"
      ],
      "created_at": "2025-10-09T09:00:00Z"
    }
  ]
}
```

<h3 id="get_api_v1_docs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdListResponseDoc](#schemastdlistresponsedoc)|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_docs

<a id="opIdpost_api_v1_docs"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/docs', headers = headers)

print(r.json())

```

`POST /api/v1/docs`

*新增文档*

TODO: add description.

> Body parameter

```json
{
  "title": "新文档",
  "content": "正文内容",
  "tags": [
    "通知"
  ],
  "source": "yuque"
}
```

<h3 id="post_api_v1_docs-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateDocRequest](#schemacreatedocrequest)|true|none|

> Example responses

> created

```json
{
  "code": 201,
  "msg": "created",
  "data": {
    "id": "doc_123"
  }
}
```

<h3 id="post_api_v1_docs-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|created|[StdCreatedId](#schemastdcreatedid)|

<aside class="success">
This operation does not require authentication
</aside>

## get_api_v1_docs_id

<a id="opIdget_api_v1_docs_id"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/docs/{id}', headers = headers)

print(r.json())

```

`GET /api/v1/docs/{id}`

*获取单个文档*

TODO: add description.

<h3 id="get_api_v1_docs_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> success

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": "doc_1",
    "source_id": "yuque:1",
    "source": "yuque",
    "title": "示例标题",
    "content": "这是正文...",
    "summary": "摘要...",
    "tags": [
      "通知"
    ],
    "author": "张三",
    "url": "https://...",
    "created_at": "2025-10-10T09:00:00Z",
    "updated_at": "2025-10-10T10:00:00Z"
  }
}
```

> not found

```json
{
  "code": 404,
  "msg": "not found",
  "data": null
}
```

<h3 id="get_api_v1_docs_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdResponseDoc](#schemastdresponsedoc)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|not found|[StdError](#schemastderror)|

<aside class="success">
This operation does not require authentication
</aside>

## put_api_v1_docs_id

<a id="opIdput_api_v1_docs_id"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('http://localhost:4010/api/v1/docs/{id}', headers = headers)

print(r.json())

```

`PUT /api/v1/docs/{id}`

*更新文档（整体）*

TODO: add description.

> Body parameter

```json
{
  "title": "string",
  "content": "string",
  "tags": [
    "string"
  ],
  "source": "string"
}
```

<h3 id="put_api_v1_docs_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|
|body|body|[UpdateDocRequest](#schemaupdatedocrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": "string"
  }
}
```

<h3 id="put_api_v1_docs_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|updated|[StdUpdatedId](#schemastdupdatedid)|

<aside class="success">
This operation does not require authentication
</aside>

## delete_api_v1_docs_id

<a id="opIddelete_api_v1_docs_id"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('http://localhost:4010/api/v1/docs/{id}', headers = headers)

print(r.json())

```

`DELETE /api/v1/docs/{id}`

*删除文档*

TODO: add description.

<h3 id="delete_api_v1_docs_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "deleted",
  "data": null
}
```

<h3 id="delete_api_v1_docs_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|deleted|[StdDeleted](#schemastddeleted)|

<aside class="success">
This operation does not require authentication
</aside>

## get_api_v1_docs_doc_id_versions

<a id="opIdget_api_v1_docs_doc_id_versions"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/docs/{doc_id}/versions', headers = headers)

print(r.json())

```

`GET /api/v1/docs/{doc_id}/versions`

*获取文档的历史版本列表*

TODO: add description.

<h3 id="get_api_v1_docs_doc_id_versions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|doc_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "versions": [
      {
        "version_id": "string",
        "message": "string",
        "author": "string",
        "timestamp": "string"
      }
    ]
  }
}
```

<h3 id="get_api_v1_docs_doc_id_versions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|Inline|

<h3 id="get_api_v1_docs_doc_id_versions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer|false|none|none|
|» msg|string|false|none|none|
|» data|object|false|none|none|
|»» versions|[object]|false|none|none|
|»»» version_id|string|false|none|none|
|»»» message|string|false|none|none|
|»»» author|string|false|none|none|
|»»» timestamp|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get_api_v1_docs_doc_id_versions_commit_hash

<a id="opIdget_api_v1_docs_doc_id_versions_commit_hash"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/docs/{doc_id}/versions/{commit_hash}', headers = headers)

print(r.json())

```

`GET /api/v1/docs/{doc_id}/versions/{commit_hash}`

*获取文档的特定历史版本*

TODO: add description.

<h3 id="get_api_v1_docs_doc_id_versions_commit_hash-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|doc_id|path|string|true|none|
|commit_hash|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "content": "string"
  }
}
```

<h3 id="get_api_v1_docs_doc_id_versions_commit_hash-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|Inline|

<h3 id="get_api_v1_docs_doc_id_versions_commit_hash-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer|false|none|none|
|» msg|string|false|none|none|
|» data|object|false|none|none|
|»» content|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## get_api_v1_docs_doc_id_diff

<a id="opIdget_api_v1_docs_doc_id_diff"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/docs/{doc_id}/diff', params={
  'from_commit': 'string',  'to_commit': 'string'
}, headers = headers)

print(r.json())

```

`GET /api/v1/docs/{doc_id}/diff`

*获取文档的版本差异*

TODO: add description.

<h3 id="get_api_v1_docs_doc_id_diff-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|doc_id|path|string|true|none|
|from_commit|query|string|true|none|
|to_commit|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "diff": "string"
  }
}
```

<h3 id="get_api_v1_docs_doc_id_diff-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|Inline|

<h3 id="get_api_v1_docs_doc_id_diff-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer|false|none|none|
|» msg|string|false|none|none|
|» data|object|false|none|none|
|»» diff|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_docs_doc_id_revert

<a id="opIdpost_api_v1_docs_doc_id_revert"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/docs/{doc_id}/revert', headers = headers)

print(r.json())

```

`POST /api/v1/docs/{doc_id}/revert`

*回滚文档到指定版本*

TODO: add description.

> Body parameter

```json
{
  "commit_hash": "string",
  "message": "string"
}
```

<h3 id="post_api_v1_docs_doc_id_revert-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|doc_id|path|string|true|none|
|body|body|object|true|none|
|» commit_hash|body|string|false|none|
|» message|body|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "new_version": "string"
  }
}
```

<h3 id="post_api_v1_docs_doc_id_revert-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|reverted|Inline|

<h3 id="post_api_v1_docs_doc_id_revert-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» code|integer|false|none|none|
|» msg|string|false|none|none|
|» data|object|false|none|none|
|»» new_version|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-graphql">Graphql</h1>

Auto-generated tag for Graphql

## post_graphql

<a id="opIdpost_graphql"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/graphql', headers = headers)

print(r.json())

```

`POST /graphql`

*GraphQL 端点（支持查询和检索）*

TODO: add description.

> Body parameter

```json
{
  "query": "string",
  "variables": {}
}
```

<h3 id="post_graphql-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» query|body|string|false|none|
|» variables|body|object|false|none|

> Example responses

> success

```json
{
  "data": {
    "stream": {
      "items": [
        {
          "id": "doc_1",
          "title": "A"
        },
        {
          "id": "doc_2",
          "title": "B"
        }
      ]
    }
  }
}
```

<h3 id="post_graphql-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|Inline|

<h3 id="post_graphql-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-imports">Imports</h1>

Auto-generated tag for Imports

## post_api_v1_imports

<a id="opIdpost_api_v1_imports"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/imports', headers = headers)

print(r.json())

```

`POST /api/v1/imports`

*提交导入作业*

TODO: add description.

> Body parameter

```json
{
  "path": "s3://bucket/folder/docs-20251010.ndjson.gz",
  "format": "ndjson",
  "schema_version": "1.0.0",
  "source": "yuque"
}
```

<h3 id="post_api_v1_imports-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ImportJobRequest](#schemaimportjobrequest)|true|none|

> Example responses

> 201 Response

```json
{
  "code": 201,
  "msg": "created",
  "data": {
    "job_id": "imp_123"
  }
}
```

<h3 id="post_api_v1_imports-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|created|[StdCreatedJob](#schemastdcreatedjob)|

<aside class="success">
This operation does not require authentication
</aside>

## get_api_v1_imports_job_id

<a id="opIdget_api_v1_imports_job_id"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/imports/{job_id}', headers = headers)

print(r.json())

```

`GET /api/v1/imports/{job_id}`

*查询导入作业*

TODO: add description.

<h3 id="get_api_v1_imports_job_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|job_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "status": "queued",
    "processed": 5000,
    "failed": 3,
    "next_cursor": "string"
  }
}
```

<h3 id="get_api_v1_imports_job_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[ImportJobStatus](#schemaimportjobstatus)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-preprocess">Preprocess</h1>

Auto-generated tag for Preprocess

## post_api_v1_preprocess_clean

<a id="opIdpost_api_v1_preprocess_clean"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/preprocess/clean', headers = headers)

print(r.json())

```

`POST /api/v1/preprocess/clean`

*文本清洗*

TODO: add description.

> Body parameter

```json
{
  "content": "【广告】同学们大家好！\n活动时间：..."
}
```

<h3 id="post_api_v1_preprocess_clean-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PreprocessCleanRequest](#schemapreprocesscleanrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "cleaned_content": "string"
  }
}
```

<h3 id="post_api_v1_preprocess_clean-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[PreprocessCleanResponse](#schemapreprocesscleanresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_preprocess_dedup

<a id="opIdpost_api_v1_preprocess_dedup"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/preprocess/dedup', headers = headers)

print(r.json())

```

`POST /api/v1/preprocess/dedup`

*去重检测*

TODO: add description.

> Body parameter

```json
{
  "content": "string"
}
```

<h3 id="post_api_v1_preprocess_dedup-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PreprocessDedupRequest](#schemapreprocessdeduprequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "is_duplicate": true,
    "similar_id": "string"
  }
}
```

<h3 id="post_api_v1_preprocess_dedup-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[PreprocessDedupResponse](#schemapreprocessdedupresponse)|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_preprocess_tags

<a id="opIdpost_api_v1_preprocess_tags"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/preprocess/tags', headers = headers)

print(r.json())

```

`POST /api/v1/preprocess/tags`

*分词与标签提取*

TODO: add description.

> Body parameter

```json
{
  "content": "string"
}
```

<h3 id="post_api_v1_preprocess_tags-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PreprocessTagsRequest](#schemapreprocesstagsrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "tags": [
      "string"
    ],
    "keywords": [
      "string"
    ]
  }
}
```

<h3 id="post_api_v1_preprocess_tags-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[PreprocessTagsResponse](#schemapreprocesstagsresponse)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-push">Push</h1>

Auto-generated tag for Push

## post_api_v1_push_webhook

<a id="opIdpost_api_v1_push_webhook"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/push/webhook', headers = headers)

print(r.json())

```

`POST /api/v1/push/webhook`

*推送到 Webhook*

TODO: add description.

> Body parameter

```json
{
  "target_url": "string",
  "payload": {}
}
```

<h3 id="post_api_v1_push_webhook-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[WebhookPushRequest](#schemawebhookpushrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}
```

<h3 id="post_api_v1_push_webhook-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdOk](#schemastdok)|

<aside class="success">
This operation does not require authentication
</aside>

## get_api_v1_push_rss

<a id="opIdget_api_v1_push_rss"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/xml'
}

r = requests.get('http://localhost:4010/api/v1/push/rss', headers = headers)

print(r.json())

```

`GET /api/v1/push/rss`

*生成 RSS（示意，不在 Mock 返回 XML）*

TODO: add description.

<h3 id="get_api_v1_push_rss-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tag|query|string|false|none|

> Example responses

> 200 Response

<h3 id="get_api_v1_push_rss-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|xml feed|string|

<aside class="success">
This operation does not require authentication
</aside>

## post_api_v1_push_email

<a id="opIdpost_api_v1_push_email"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://localhost:4010/api/v1/push/email', headers = headers)

print(r.json())

```

`POST /api/v1/push/email`

*邮件推送*

TODO: add description.

> Body parameter

```json
{
  "to": "string",
  "subject": "string",
  "content": "string"
}
```

<h3 id="post_api_v1_push_email-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EmailPushRequest](#schemaemailpushrequest)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}
```

<h3 id="post_api_v1_push_email-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdOk](#schemastdok)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-search">Search</h1>

Auto-generated tag for Search

## get_api_v1_search

<a id="opIdget_api_v1_search"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/search', headers = headers)

print(r.json())

```

`GET /api/v1/search`

*检索（短查询）*

TODO: add description.

<h3 id="get_api_v1_search-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|q|query|string|false|none|
|tag|query|string|false|none|
|mode|query|string|false|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|mode|vector|
|mode|precise|
|mode|hybrid|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "tags": [
        "string"
      ],
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}
```

<h3 id="get_api_v1_search-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdListResponseSearchItem](#schemastdlistresponsesearchitem)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-stream">Stream</h1>

Auto-generated tag for Stream

## get_api_v1_stream

<a id="opIdget_api_v1_stream"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/stream', headers = headers)

print(r.json())

```

`GET /api/v1/stream`

*获取信息流*

TODO: add description.

<h3 id="get_api_v1_stream-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|none|
|size|query|integer|false|none|

> Example responses

> 200 Response

```json
{
  "code": 0,
  "msg": "string",
  "data": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "tags": [
        "string"
      ],
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}
```

<h3 id="get_api_v1_stream-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[StdListResponseStreamItem](#schemastdlistresponsestreamitem)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="nova-api-views">Views</h1>

Auto-generated tag for Views

## get_api_v1_views_id

<a id="opIdget_api_v1_views_id"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://localhost:4010/api/v1/views/{id}', headers = headers)

print(r.json())

```

`GET /api/v1/views/{id}`

*获取保存的视图*

TODO: add description.

<h3 id="get_api_v1_views_id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|none|

> Example responses

> success

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": "view_001",
    "name": "最近通知",
    "query": {
      "tag": "通知",
      "sort": "created_at:desc"
    }
  }
}
```

<h3 id="get_api_v1_views_id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|success|[ViewResponse](#schemaviewresponse)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_StdOk">StdOk</h2>
<!-- backwards compatibility -->
<a id="schemastdok"></a>
<a id="schema_StdOk"></a>
<a id="tocSstdok"></a>
<a id="tocsstdok"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object¦null|false|none|none|

<h2 id="tocS_StdError">StdError</h2>
<!-- backwards compatibility -->
<a id="schemastderror"></a>
<a id="schema_StdError"></a>
<a id="tocSstderror"></a>
<a id="tocsstderror"></a>

```json
{
  "code": 400,
  "msg": "bad request",
  "data": {},
  "trace_id": "f3e0..."
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object¦null|false|none|none|
|trace_id|string|false|none|none|

<h2 id="tocS_StdCreatedId">StdCreatedId</h2>
<!-- backwards compatibility -->
<a id="schemastdcreatedid"></a>
<a id="schema_StdCreatedId"></a>
<a id="tocSstdcreatedid"></a>
<a id="tocsstdcreatedid"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "id": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» id|string|false|none|none|

<h2 id="tocS_StdUpdatedId">StdUpdatedId</h2>
<!-- backwards compatibility -->
<a id="schemastdupdatedid"></a>
<a id="schema_StdUpdatedId"></a>
<a id="tocSstdupdatedid"></a>
<a id="tocsstdupdatedid"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": "string"
  }
}

```

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[StdOk](#schemastdok)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» data|object|false|none|none|
|»» id|string|false|none|none|

<h2 id="tocS_StdDeleted">StdDeleted</h2>
<!-- backwards compatibility -->
<a id="schemastddeleted"></a>
<a id="schema_StdDeleted"></a>
<a id="tocSstddeleted"></a>
<a id="tocsstddeleted"></a>

```json
{
  "code": 200,
  "msg": "deleted",
  "data": null
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|any|false|none|none|

<h2 id="tocS_Doc">Doc</h2>
<!-- backwards compatibility -->
<a id="schemadoc"></a>
<a id="schema_Doc"></a>
<a id="tocSdoc"></a>
<a id="tocsdoc"></a>

```json
{
  "id": "doc_123",
  "source_id": "yuque:abc123",
  "source": "yuque",
  "title": "string",
  "content": "string",
  "summary": "string",
  "tags": [
    "string"
  ],
  "author": "string",
  "url": "string",
  "avatar": "string",
  "created_at": "2019-08-24T14:15:22Z",
  "updated_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|none|
|source_id|string|true|none|none|
|source|string|false|none|none|
|title|string|true|none|none|
|content|string|false|none|none|
|summary|string|false|none|none|
|tags|[string]|false|none|none|
|author|string|false|none|none|
|url|string|false|none|none|
|avatar|string|false|none|none|
|created_at|string(date-time)|true|none|none|
|updated_at|string(date-time)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|source|yuque|
|source|wechat|
|source|qq|
|source|web|

<h2 id="tocS_StreamItem">StreamItem</h2>
<!-- backwards compatibility -->
<a id="schemastreamitem"></a>
<a id="schema_StreamItem"></a>
<a id="tocSstreamitem"></a>
<a id="tocsstreamitem"></a>

```json
{
  "id": "string",
  "title": "string",
  "summary": "string",
  "tags": [
    "string"
  ],
  "created_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|title|string|false|none|none|
|summary|string|false|none|none|
|tags|[string]|false|none|none|
|created_at|string(date-time)|false|none|none|

<h2 id="tocS_CreateDocRequest">CreateDocRequest</h2>
<!-- backwards compatibility -->
<a id="schemacreatedocrequest"></a>
<a id="schema_CreateDocRequest"></a>
<a id="tocScreatedocrequest"></a>
<a id="tocscreatedocrequest"></a>

```json
{
  "title": "string",
  "content": "string",
  "tags": [
    "string"
  ],
  "source": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|content|string|true|none|none|
|tags|[string]|false|none|none|
|source|string|true|none|none|

<h2 id="tocS_UpdateDocRequest">UpdateDocRequest</h2>
<!-- backwards compatibility -->
<a id="schemaupdatedocrequest"></a>
<a id="schema_UpdateDocRequest"></a>
<a id="tocSupdatedocrequest"></a>
<a id="tocsupdatedocrequest"></a>

```json
{
  "title": "string",
  "content": "string",
  "tags": [
    "string"
  ],
  "source": "string"
}

```

### Properties

*None*

<h2 id="tocS_PreprocessCleanRequest">PreprocessCleanRequest</h2>
<!-- backwards compatibility -->
<a id="schemapreprocesscleanrequest"></a>
<a id="schema_PreprocessCleanRequest"></a>
<a id="tocSpreprocesscleanrequest"></a>
<a id="tocspreprocesscleanrequest"></a>

```json
{
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|true|none|none|

<h2 id="tocS_PreprocessCleanResponse">PreprocessCleanResponse</h2>
<!-- backwards compatibility -->
<a id="schemapreprocesscleanresponse"></a>
<a id="schema_PreprocessCleanResponse"></a>
<a id="tocSpreprocesscleanresponse"></a>
<a id="tocspreprocesscleanresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "cleaned_content": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» cleaned_content|string|false|none|none|

<h2 id="tocS_PreprocessDedupRequest">PreprocessDedupRequest</h2>
<!-- backwards compatibility -->
<a id="schemapreprocessdeduprequest"></a>
<a id="schema_PreprocessDedupRequest"></a>
<a id="tocSpreprocessdeduprequest"></a>
<a id="tocspreprocessdeduprequest"></a>

```json
{
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|true|none|none|

<h2 id="tocS_PreprocessDedupResponse">PreprocessDedupResponse</h2>
<!-- backwards compatibility -->
<a id="schemapreprocessdedupresponse"></a>
<a id="schema_PreprocessDedupResponse"></a>
<a id="tocSpreprocessdedupresponse"></a>
<a id="tocspreprocessdedupresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "is_duplicate": true,
    "similar_id": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» is_duplicate|boolean|false|none|none|
|» similar_id|string|false|none|none|

<h2 id="tocS_PreprocessTagsRequest">PreprocessTagsRequest</h2>
<!-- backwards compatibility -->
<a id="schemapreprocesstagsrequest"></a>
<a id="schema_PreprocessTagsRequest"></a>
<a id="tocSpreprocesstagsrequest"></a>
<a id="tocspreprocesstagsrequest"></a>

```json
{
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|true|none|none|

<h2 id="tocS_PreprocessTagsResponse">PreprocessTagsResponse</h2>
<!-- backwards compatibility -->
<a id="schemapreprocesstagsresponse"></a>
<a id="schema_PreprocessTagsResponse"></a>
<a id="tocSpreprocesstagsresponse"></a>
<a id="tocspreprocesstagsresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "tags": [
      "string"
    ],
    "keywords": [
      "string"
    ]
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» tags|[string]|false|none|none|
|» keywords|[string]|false|none|none|

<h2 id="tocS_AiSummaryRequest">AiSummaryRequest</h2>
<!-- backwards compatibility -->
<a id="schemaaisummaryrequest"></a>
<a id="schema_AiSummaryRequest"></a>
<a id="tocSaisummaryrequest"></a>
<a id="tocsaisummaryrequest"></a>

```json
{
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|true|none|none|

<h2 id="tocS_AiSummaryResponse">AiSummaryResponse</h2>
<!-- backwards compatibility -->
<a id="schemaaisummaryresponse"></a>
<a id="schema_AiSummaryResponse"></a>
<a id="tocSaisummaryresponse"></a>
<a id="tocsaisummaryresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "summary": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» summary|string|false|none|none|

<h2 id="tocS_AiClassifyRequest">AiClassifyRequest</h2>
<!-- backwards compatibility -->
<a id="schemaaiclassifyrequest"></a>
<a id="schema_AiClassifyRequest"></a>
<a id="tocSaiclassifyrequest"></a>
<a id="tocsaiclassifyrequest"></a>

```json
{
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|content|string|true|none|none|

<h2 id="tocS_AiClassifyResponse">AiClassifyResponse</h2>
<!-- backwards compatibility -->
<a id="schemaaiclassifyresponse"></a>
<a id="schema_AiClassifyResponse"></a>
<a id="tocSaiclassifyresponse"></a>
<a id="tocsaiclassifyresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "category": "通知",
    "confidence": 0.95
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» category|string|false|none|none|
|» confidence|number(float)|false|none|none|

<h2 id="tocS_AiRecognizeRequest">AiRecognizeRequest</h2>
<!-- backwards compatibility -->
<a id="schemaairecognizerequest"></a>
<a id="schema_AiRecognizeRequest"></a>
<a id="tocSairecognizerequest"></a>
<a id="tocsairecognizerequest"></a>

```json
{
  "file": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|file|string|true|none|base64 或 文件链接|

<h2 id="tocS_AiRecognizeResponse">AiRecognizeResponse</h2>
<!-- backwards compatibility -->
<a id="schemaairecognizeresponse"></a>
<a id="schema_AiRecognizeResponse"></a>
<a id="tocSairecognizeresponse"></a>
<a id="tocsairecognizeresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "type": "image",
    "result": {}
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» type|string|false|none|none|
|» result|object|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|type|image|
|type|table|
|type|formula|

<h2 id="tocS_SearchRequest">SearchRequest</h2>
<!-- backwards compatibility -->
<a id="schemasearchrequest"></a>
<a id="schema_SearchRequest"></a>
<a id="tocSsearchrequest"></a>
<a id="tocssearchrequest"></a>

```json
{
  "query": "string",
  "category": "string",
  "tag": "string",
  "mode": "vector"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|query|string|false|none|none|
|category|string|false|none|none|
|tag|string|false|none|none|
|mode|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|mode|vector|
|mode|precise|
|mode|hybrid|

<h2 id="tocS_SearchItem">SearchItem</h2>
<!-- backwards compatibility -->
<a id="schemasearchitem"></a>
<a id="schema_SearchItem"></a>
<a id="tocSsearchitem"></a>
<a id="tocssearchitem"></a>

```json
{
  "id": "string",
  "title": "string",
  "summary": "string",
  "tags": [
    "string"
  ],
  "created_at": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|title|string|false|none|none|
|summary|string|false|none|none|
|tags|[string]|false|none|none|
|created_at|string(date-time)|false|none|none|

<h2 id="tocS_WebhookPushRequest">WebhookPushRequest</h2>
<!-- backwards compatibility -->
<a id="schemawebhookpushrequest"></a>
<a id="schema_WebhookPushRequest"></a>
<a id="tocSwebhookpushrequest"></a>
<a id="tocswebhookpushrequest"></a>

```json
{
  "target_url": "string",
  "payload": {}
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|target_url|string|true|none|none|
|payload|object|true|none|none|

<h2 id="tocS_EmailPushRequest">EmailPushRequest</h2>
<!-- backwards compatibility -->
<a id="schemaemailpushrequest"></a>
<a id="schema_EmailPushRequest"></a>
<a id="tocSemailpushrequest"></a>
<a id="tocsemailpushrequest"></a>

```json
{
  "to": "string",
  "subject": "string",
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|to|string|true|none|none|
|subject|string|true|none|none|
|content|string|true|none|none|

<h2 id="tocS_ImportJobRequest">ImportJobRequest</h2>
<!-- backwards compatibility -->
<a id="schemaimportjobrequest"></a>
<a id="schema_ImportJobRequest"></a>
<a id="tocSimportjobrequest"></a>
<a id="tocsimportjobrequest"></a>

```json
{
  "path": "s3://bucket/folder/docs-20251010.ndjson.gz",
  "format": "ndjson",
  "schema_version": "1.0.0",
  "source": "yuque"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|path|string|true|none|none|
|format|string|true|none|none|
|schema_version|string|true|none|none|
|source|string|true|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|format|ndjson|
|format|parquet|

<h2 id="tocS_StdCreatedJob">StdCreatedJob</h2>
<!-- backwards compatibility -->
<a id="schemastdcreatedjob"></a>
<a id="schema_StdCreatedJob"></a>
<a id="tocSstdcreatedjob"></a>
<a id="tocsstdcreatedjob"></a>

```json
{
  "code": 201,
  "msg": "created",
  "data": {
    "job_id": "imp_123"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» job_id|string|false|none|none|

<h2 id="tocS_ImportJobStatus">ImportJobStatus</h2>
<!-- backwards compatibility -->
<a id="schemaimportjobstatus"></a>
<a id="schema_ImportJobStatus"></a>
<a id="tocSimportjobstatus"></a>
<a id="tocsimportjobstatus"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "status": "queued",
    "processed": 5000,
    "failed": 3,
    "next_cursor": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» status|string|false|none|none|
|» processed|integer|false|none|none|
|» failed|integer|false|none|none|
|» next_cursor|string¦null|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|queued|
|status|running|
|status|succeeded|
|status|failed|
|status|partial|

<h2 id="tocS_ViewResponse">ViewResponse</h2>
<!-- backwards compatibility -->
<a id="schemaviewresponse"></a>
<a id="schema_ViewResponse"></a>
<a id="tocSviewresponse"></a>
<a id="tocsviewresponse"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "id": "string",
    "name": "string",
    "query": {}
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|object|false|none|none|
|» id|string|false|none|none|
|» name|string|false|none|none|
|» query|object|false|none|none|

<h2 id="tocS_BotSendRequest">BotSendRequest</h2>
<!-- backwards compatibility -->
<a id="schemabotsendrequest"></a>
<a id="schema_BotSendRequest"></a>
<a id="tocSbotsendrequest"></a>
<a id="tocsbotsendrequest"></a>

```json
{
  "platform": "qq",
  "target": "group:123456",
  "content": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|platform|string|true|none|none|
|target|string|true|none|none|
|content|string|true|none|none|

<h2 id="tocS_StdResponseDoc">StdResponseDoc</h2>
<!-- backwards compatibility -->
<a id="schemastdresponsedoc"></a>
<a id="schema_StdResponseDoc"></a>
<a id="tocSstdresponsedoc"></a>
<a id="tocsstdresponsedoc"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": {
    "id": "doc_123",
    "source_id": "yuque:abc123",
    "source": "yuque",
    "title": "string",
    "content": "string",
    "summary": "string",
    "tags": [
      "string"
    ],
    "author": "string",
    "url": "string",
    "avatar": "string",
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|[Doc](#schemadoc)|false|none|none|

<h2 id="tocS_StdListResponseDoc">StdListResponseDoc</h2>
<!-- backwards compatibility -->
<a id="schemastdlistresponsedoc"></a>
<a id="schema_StdListResponseDoc"></a>
<a id="tocSstdlistresponsedoc"></a>
<a id="tocsstdlistresponsedoc"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": [
    {
      "id": "doc_123",
      "source_id": "yuque:abc123",
      "source": "yuque",
      "title": "string",
      "content": "string",
      "summary": "string",
      "tags": [
        "string"
      ],
      "author": "string",
      "url": "string",
      "avatar": "string",
      "created_at": "2019-08-24T14:15:22Z",
      "updated_at": "2019-08-24T14:15:22Z"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|[[Doc](#schemadoc)]|false|none|none|

<h2 id="tocS_StdListResponseStreamItem">StdListResponseStreamItem</h2>
<!-- backwards compatibility -->
<a id="schemastdlistresponsestreamitem"></a>
<a id="schema_StdListResponseStreamItem"></a>
<a id="tocSstdlistresponsestreamitem"></a>
<a id="tocsstdlistresponsestreamitem"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "tags": [
        "string"
      ],
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|[[StreamItem](#schemastreamitem)]|false|none|none|

<h2 id="tocS_StdListResponseSearchItem">StdListResponseSearchItem</h2>
<!-- backwards compatibility -->
<a id="schemastdlistresponsesearchitem"></a>
<a id="schema_StdListResponseSearchItem"></a>
<a id="tocSstdlistresponsesearchitem"></a>
<a id="tocsstdlistresponsesearchitem"></a>

```json
{
  "code": 0,
  "msg": "string",
  "data": [
    {
      "id": "string",
      "title": "string",
      "summary": "string",
      "tags": [
        "string"
      ],
      "created_at": "2019-08-24T14:15:22Z"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|none|
|msg|string|false|none|none|
|data|[[SearchItem](#schemasearchitem)]|false|none|none|

