# RESTful API接口标准

这是一份未完成的草案。我真的非常希望大家一起来修改完善这个文档（我好像经常这么说但是没有人理我qwq）

## 通用规范

### 1. 基本规范
- 所有接口均采用HTTP/HTTPS协议，数据格式统一为JSON。（除了特殊情况，如返回更适用于RSS的xml格式）
- 路径命名采用小写、短横线分隔，资源名用复数。
- 支持标准HTTP方法：GET（查询）、POST（创建）、PUT/PATCH（更新）、DELETE（删除）。
- 状态码规范：200（成功）、201（创建成功）、400（参数错误）、401（未授权）、403（禁止）、404（未找到）、500（服务器错误）。

### 2. 认证与安全
- 推荐采用Token认证，所有敏感信息存储于.env文件，严禁提交至公开仓库。（如有需要可以私下交流）
- API请求需携带Authorization头，后端统一校验。
- 数据传输建议加密（可暂缓），敏感操作需权限校验。

### 3. 数据结构与响应格式
- 所有接口返回统一结构：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {...}
  }
  ```
- 错误响应需明确code与msg，便于前端处理。
- 资源对象设计参考面向对象原则，字段命名统一、语义清晰。
- `data`字段里一定要为每条数据分配唯一固定的原始id，方便我们进行对应、反向搜索以及索引等等。

### 4. 版本管理
- 接口需支持版本号，如`/api/v1/docs`，便于后续升级和兼容。

---

## 数据采集模块

### 1. 获取文档/消息列表
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": [
      {
        "id": "string",
        "title": "string",
        "author": "string",
        "source": "yuque|wechat|qq|web",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    ]
  }
  ```
- 不同信息来源可在格式上略有区别。比如加入头像数据、微信号/QQ号、网页具体链接等等。

### 2. 获取单个文档/消息内容
- `GET /api/v1/docs/{id}`
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "id": "string",
      "title": "string",
      "content": "markdown/string/image",
      "tags": ["string"],
      "source": "yuque|wechat|qq|web",
      "created_at": "datetime"
    }
  }
  ```

### 3. 新增文档（采集/上传）
- `POST /api/v1/docs`
- 请求体：
    ```json
    {
    "title": "string",
    "content": "string",
    "tags": ["string"],
    "source": "string"
    }
    ```
- 返回：
    ```json    
    {
        "code": 201,
        "msg": "created",
        "data": {
            "id": "string"
        }
    }
    ```

### 4. 更新/删除文档

- `PUT /api/v1/docs/{id}`
- 请求体：
  ```json
  {
    "title": "string",
    "content": "string",
    "tags": ["string"],
    "source": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "updated",
    "data": {
      "id": "string"
    }
  }
  ```

- `DELETE /api/v1/docs/{id}`
- 返回：
  ```json
  {
    "code": 200,
    "msg": "deleted"
  }
  ```
---

## 数据预处理模块

### 1. 文本清洗
- `POST /api/v1/preprocess/clean`
- 请求体：
  ```json
  {
    "content": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "cleaned_content": "string"
    }
  }
  ```

请求/响应 JSON Schema：

请求体（PreprocessCleanRequest）：

```json
{
  "type": "object",
  "required": ["content"],
  "properties": {
    "content": {"type": "string"}
  }
}
```

成功响应（PreprocessCleanResponse）：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "cleaned_content": {"type": "string"}
      }
    }
  }
}
```

### 2. 去重检测
- `POST /api/v1/preprocess/dedup`
- 请求体：
  ```json
  {
    "content": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "is_duplicate": true,
      "similar_id": "string"
    }
  }
  ```

请求/响应 JSON Schema：

请求体（PreprocessDedupRequest）：

```json
{
  "type": "object",
  "required": ["content"],
  "properties": {"content": {"type": "string"}}
}
```

成功响应（PreprocessDedupResponse）：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "is_duplicate": {"type": "boolean"},
        "similar_id": {"type": ["string","null"]}
      }
    }
  }
}
```

### 3. 分词与标签提取
- `POST /api/v1/preprocess/tags`
- 请求体：
  ```json
  {
    "content": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "tags": ["string"],
      "keywords": ["string"]
    }
  }
  ```

请求/响应 JSON Schema：

请求体（PreprocessTagsRequest）：

```json
{
  "type": "object",
  "required": ["content"],
  "properties": {"content": {"type": "string"}}
}
```

成功响应（PreprocessTagsResponse）：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "tags": {"type": "array", "items": {"type": "string"}},
        "keywords": {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```

---

## 信息推送模块

### 1. 推送消息到Webhook
- `POST /api/v1/push/webhook`
- 请求体：
  ```json
  {
    "target_url": "string",
    "payload": { ... }
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success"
  }
  ```

请求/响应 JSON Schema（Webhook）：

请求体（WebhookPushRequest）：

```json
{
  "type": "object",
  "required": ["target_url","payload"],
  "properties": {
    "target_url": {"type": "string"},
    "payload": {"type": "object", "additionalProperties": true}
  }
}
```

成功响应：标准返回结构（StdOk）

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer", "example": 200},
    "msg": {"type": "string", "example": "success"},
    "data": {"type": ["object","null"]}
  }
}
```

### 2. 生成RSS订阅源
- `GET /api/v1/push/rss?tag=xxx`
- 返回：
  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <rss>
    <!-- RSS内容 -->
  </rss>
  ```

请求/响应 JSON Schema：

查询参数：

```json
{
  "type": "object",
  "properties": {"tag": {"type": "string"}}
}
```

响应为 XML（示意），Mock 或文档中可返回 application/xml。此接口在 Mock 中不返回 JSON。

### 3. 邮件推送
- `POST /api/v1/push/email`
- 请求体：
  ```json
  {
    "to": "string",
    "subject": "string",
    "content": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success"
  }
  ```

请求/响应 JSON Schema（EmailPushRequest）：

```json
{
  "type": "object",
  "required": ["to","subject","content"],
  "properties": {
    "to": {"type": "string"},
    "subject": {"type": "string"},
    "content": {"type": "string"}
  }
}
```

成功响应同 StdOk。

---

## 前端交互模块

### 1. 获取信息流
- `GET /api/v1/stream`
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": [
      {
        "id": "string",
        "title": "string",
        "summary": "string",
        "tags": ["string"],
        "created_at": "datetime"
      }
    ]
  }
  ```
- 信息流作用是为前端或用户提供统一的内容展示入口。它将采集、处理后的各类文档、消息、摘要等内容，按时间或相关性聚合成列表，方便用户浏览、检索和获取最新动态。简单来说，就是把所有有价值的信息集中展示，类似于首页。就像我之前和黄同学说的一样，一个展示原始信息的漂亮界面非常重要。


### 2. 检索/过滤/提问
- `GET /api/v1/search?q=xxx&tag=xxx`（查询文本较短时）
- `POST /api/v1/search`（查询文本较长时）
- 请求体：
  ```json
  {
    "query": "string",
    "category": "string",
    "tag": "string",
    "mode": "vector|precise|hybrid"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": [
      {
        "id": "string",
        "title": "string",
        "summary": "string",
        "tags": ["string"],
        "created_at": "datetime"
      }
    ]
  }
  ```

请求/响应 JSON Schema（信息流）：

查询参数:

```json
{
  "type": "object",
  "properties": {
    "page": {"type": "integer", "default": 1},
    "size": {"type": "integer", "default": 20}
  }
}
```

成功响应（StdListResponseStreamItem）：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "title": {"type": "string"},
          "summary": {"type": "string"},
          "tags": {"type": "array", "items": {"type": "string"}},
          "created_at": {"type": "string", "format": "date-time"}
        }
      }
    }
  }
}
```
  - 具体采用什么方式检索可以考虑我上周文档中提出的方案。比如通过向量数据库实现自然语言提问，通过例如SQL之类的数据库实现精确检索，或者采用混合检索等等，这些可分别作为不同的mode参数供调用

请求/响应 JSON Schema（Search）：

GET 查询参数示例（短查询）:

```json
{
  "type": "object",
  "properties": {
    "q": {"type": "string"},
    "tag": {"type": "string"},
    "mode": {"type": "string", "enum": ["vector","precise","hybrid"]}
  }
}
```

POST 请求体（SearchRequest，长查询）:

```json
{
  "type": "object",
  "properties": {
    "query": {"type": "string"},
    "category": {"type": "string"},
    "tag": {"type": "string"},
    "mode": {"type": "string", "enum": ["vector","precise","hybrid"]}
  }
}
```

成功响应（StdListResponseSearchItem）同上，data 为 SearchItem 数组：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {"type": "array", "items": {"$ref": "#/components/schemas/SearchItem"}}
  }
}
```


## AI处理模块

### 1. 文本分类
- `POST /api/v1/ai/classify`
- 请求体：
  ```json
  {
    "content": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "category": "string",
      "confidence": 0.95
    }
  }
  ```

请求/响应 JSON Schema（AiClassify）：

请求体（AiClassifyRequest）：

```json
{
  "type": "object",
  "required": ["content"],
  "properties": {"content": {"type": "string"}}
}
```

成功响应（AiClassifyResponse）：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "category": {"type": "string"},
        "confidence": {"type": "number"}
      }
    }
  }
}
```

### 2. 内容摘要
- `POST /api/v1/ai/summary`
- 请求体：
  ```json
  {
    "content": "string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "summary": "string"
    }
  }
  ```

请求/响应 JSON Schema（AiSummary）：

请求体（AiSummaryRequest）：

```json
{
  "type": "object",
  "required": ["content"],
  "properties": {"content": {"type": "string"}}
}
```

成功响应（AiSummaryResponse）：

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {"type": "object", "properties": {"summary": {"type": "string"}}}
  }
}
```

### 3. 图片/表格/公式识别
- `POST /api/v1/ai/recognize`
- 请求体：
  ```json
  {
    "file": "base64/string"
  }
  ```
- 返回：
  ```json
  {
    "code": 200,
    "msg": "success",
    "data": {
      "type": "image|table|formula",
      "result": { ... }
    }
  }
  ```

请求/响应 JSON Schema（AiRecognize）：

请求体 (AiRecognizeRequest):

```json
{
  "type": "object",
  "required": ["file"],
  "properties": {"file": {"type": "string", "description": "base64 或 文件链接"}}
}
```

成功响应 (AiRecognizeResponse):

```json
{
  "type": "object",
  "properties": {
    "code": {"type": "integer"},
    "msg": {"type": "string"},
    "data": {
      "type": "object",
      "properties": {
        "type": {"type": "string", "enum": ["image","table","formula"]},
        "result": {"type": "object"}
      }
    }
  }
}
```

## 其他讨论
- 图片最好支持两种形式的传输，base64编码和图链（或者索引到本地图片地址），但后者在我们需要通过不同服务器部署时不太方便，租用图床也不太方便。不过这些是后话。
- 有一些具体的环节还没有补充。比如适用于QQbot的端口、适用于企业微信的端口、监视文档访问数据/点赞情况的端口等等，还有很多同学们已经实现的功能，大家都可以自己往这个文档里补充，我容易写着写着就混乱了，一次性没法把大家的工作都统计进来，而且大家自己更清楚需要什么样的数据。
- 这些只是最终希望达到的格式，不包含技术细节，也不包含具体的分组指示。大家可以进行各种各样的操作去达到这个目的，中间可能还需要其他端口，大家再修改协调一下。
- 王恩成同学的面向对象方法在什么地方集成进去我还没有想好，这部分工作得麻烦一下王同学了。
- 我在上一份文档提到的builder和王同学在文档里提到的builder可以说分别对应json的构建和解析，我们可能需要在初期把这两个builder给搓好，因为这是比较底层的依赖工具。