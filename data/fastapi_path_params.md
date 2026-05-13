路径参数 - FastAPI

](#path-parameters)

[Join the **FastAPI Cloud** waiting list 🚀](https://fastapicloud.com)

[**FastAPI Conf '26** — Oct 28, 2026, Amsterdam 🎤](https://fastapiconf.com)

[Follow **@fastapi** on **X (Twitter)** to stay updated](https://x.com/fastapi)

[Follow **FastAPI** on **LinkedIn** to stay updated](https://www.linkedin.com/company/fastapi)

[Subscribe to the **FastAPI and friends** newsletter 🎉](https://fastapi.tiangolo.com/newsletter/)

[sponsor
![](/img/sponsors/blockbee-banner.png)](https://blockbee.io?ref=fastapi "BlockBee Cryptocurrency Payment Gateway")

[sponsor
![](/img/sponsors/scalar-banner.svg)](https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=top-banner "Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files")

[sponsor
![](/img/sponsors/propelauth-banner.png)](https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=topbanner "Auth, user management and more for your B2B product")

[sponsor
![](/img/sponsors/liblab-banner.png)](https://liblab.com?utm_source=fastapi "liblab - Generate SDKs from FastAPI")

[sponsor
![](/img/sponsors/render-banner.svg)](https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi "Deploy & scale any full-stack web app on Render. Focus on building apps, not infra.")

[sponsor
![](/img/sponsors/coderabbit-banner.png)](https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=banner&utm_campaign=fastapi "Cut Code Review Time & Bugs in Half with CodeRabbit")

[sponsor
![](/img/sponsors/subtotal-banner.svg)](https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source "Making Retail Purchases Actionable for Brands and Developers")

[sponsor
![](/img/sponsors/railway-banner.png)](https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi "Deploy enterprise applications at startup speed")

[sponsor
![](/img/sponsors/serpapi-banner.png)](https://serpapi.com/?utm_source=fastapi_website "SerpApi: Web Search API")

[sponsor
![](/img/sponsors/greptile-banner.png)](https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page "Greptile: The AI Code Reviewer")

[![logo](../../img/icon-white.svg)](../.. "FastAPI")

FastAPI

路径参数

* [en - English](/)
* [de - Deutsch](/de/)
* [es - español](/es/)
* [fr - français](/fr/)
* [ja - 日本語](/ja/)
* [ko - 한국어](/ko/)
* [pt - português](/pt/)
* [ru - русский язык](/ru/)
* [tr - Türkçe](/tr/)
* [uk - українська мова](/uk/)
* [zh - 简体中文](/zh/)
* [zh-hant - 繁體中文](/zh-hant/)

正在初始化搜索引擎

[fastapi/fastapi](https://github.com/fastapi/fastapi "前往仓库")

* [FastAPI](../..)
* [特性](../../features/)
* [学习](../../learn/)
* [Reference](../../reference/)
* [FastAPI People](../../fastapi-people/)
* [资源](../../resources/)
* [关于](../../about/)
* [Release Notes](../../release-notes/)

[![logo](../../img/icon-white.svg)](../.. "FastAPI")
FastAPI

[fastapi/fastapi](https://github.com/fastapi/fastapi "前往仓库")

* [FastAPI](../..)
* [特性](../../features/)
* [学习](../../learn/)

  学习
  + [Python 类型提示简介](../../python-types/)
  + [并发 async / await](../../async/)
  + [环境变量](../../environment-variables/)
  + [虚拟环境](../../virtual-environments/)
  + [教程 - 用户指南](../)

    教程 - 用户指南
    - [第一步](../first-steps/)
    - 路径参数

      [路径参数](./)

      目录
      * [声明路径参数的类型](#path-parameters-with-types)
      * [数据转换](#data-conversion)
      * [数据校验](#data-validation)
      * [文档](#documentation)
      * [基于标准的好处，备选文档](#standards-based-benefits-alternative-documentation)
      * [Pydantic](#pydantic)
      * [顺序很重要](#order-matters)
      * [预设值](#predefined-values)

        + [创建 `Enum` 类](#create-an-enum-class)
        + [声明路径参数](#declare-a-path-parameter)
        + [查看文档](#check-the-docs)
        + [使用 Python 枚举](#working-with-python-enumerations)

          - [比较枚举成员](#compare-enumeration-members)
          - [获取枚举值](#get-the-enumeration-value)
          - [返回枚举成员](#return-enumeration-members)
      * [包含路径的路径参数](#path-parameters-containing-paths)

        + [OpenAPI 支持](#openapi-support)
        + [路径转换器](#path-convertor)
      * [小结](#recap)
    - [查询参数](../query-params/)
    - [请求体](../body/)
    - [查询参数和字符串校验](../query-params-str-validations/)
    - [路径参数和数值校验](../path-params-numeric-validations/)
    - [查询参数模型](../query-param-models/)
    - [请求体 - 多个参数](../body-multiple-params/)
    - [请求体 - 字段](../body-fields/)
    - [请求体 - 嵌套模型](../body-nested-models/)
    - [声明请求示例数据](../schema-extra-example/)
    - [额外数据类型](../extra-data-types/)
    - [Cookie 参数](../cookie-params/)
    - [Header 参数](../header-params/)
    - [Cookie 参数模型](../cookie-param-models/)
    - [Header 参数模型](../header-param-models/)
    - [响应模型 - 返回类型](../response-model/)
    - [更多模型](../extra-models/)
    - [响应状态码](../response-status-code/)
    - [表单数据](../request-forms/)
    - [表单模型](../request-form-models/)
    - [请求文件](../request-files/)
    - [请求表单与文件](../request-forms-and-files/)
    - [处理错误](../handling-errors/)
    - [路径操作配置](../path-operation-configuration/)
    - [JSON 兼容编码器](../encoder/)
    - [请求体 - 更新数据](../body-updates/)
    - [依赖项](../dependencies/)

      依赖项
      * [类作为依赖项](../dependencies/classes-as-dependencies/)
      * [子依赖项](../dependencies/sub-dependencies/)
      * [路径操作装饰器依赖项](../dependencies/dependencies-in-path-operation-decorators/)
      * [全局依赖项](../dependencies/global-dependencies/)
      * [使用 yield 的依赖项](../dependencies/dependencies-with-yield/)
    - [安全性](../security/)

      安全性
      * [安全 - 第一步](../security/first-steps/)
      * [获取当前用户](../security/get-current-user/)
      * [OAuth2 实现简单的 Password 和 Bearer 验证](../security/simple-oauth2/)
      * [使用密码（及哈希）的 OAuth2，基于 JWT 的 Bearer 令牌](../security/oauth2-jwt/)
    - [中间件](../middleware/)
    - [CORS（跨域资源共享）](../cors/)
    - [SQL（关系型）数据库](../sql-databases/)
    - [更大的应用 - 多个文件](../bigger-applications/)
    - [流式传输 JSON Lines](../stream-json-lines/)
    - [服务器发送事件（SSE）](../server-sent-events/)
    - [后台任务](../background-tasks/)
    - [元数据和文档 URL](../metadata/)
    - [静态文件](../static-files/)
    - [测试](../testing/)
    - [调试](../debugging/)
  + [高级用户指南](../../advanced/)

    高级用户指南
    - [流式数据](../../advanced/stream-data/)
    - [路径操作的高级配置](../../advanced/path-operation-advanced-configuration/)
    - [额外的状态码](../../advanced/additional-status-codes/)
    - [直接返回响应](../../advanced/response-directly/)
    - [自定义响应 - HTML、流、文件等](../../advanced/custom-response/)
    - [OpenAPI 中的附加响应](../../advanced/additional-responses/)
    - [响应Cookies](../../advanced/response-cookies/)
    - [响应头](../../advanced/response-headers/)
    - [响应 - 更改状态码](../../advanced/response-change-status-code/)
    - [高级依赖项](../../advanced/advanced-dependencies/)
    - [高级安全](../../advanced/security/)

      高级安全
      * [OAuth2 作用域](../../advanced/security/oauth2-scopes/)
      * [HTTP 基础授权](../../advanced/security/http-basic-auth/)
    - [直接使用 Request](../../advanced/using-request-directly/)
    - [使用数据类](../../advanced/dataclasses/)
    - [高级中间件](../../advanced/middleware/)
    - [子应用 - 挂载](../../advanced/sub-applications/)
    - [使用代理](../../advanced/behind-a-proxy/)
    - [模板](../../advanced/templates/)
    - [WebSockets](../../advanced/websockets/)
    - [生命周期事件](../../advanced/events/)
    - [测试 WebSockets](../../advanced/testing-websockets/)
    - [测试事件：lifespan 和 startup - shutdown](../../advanced/testing-events/)
    - [使用覆盖测试依赖项](../../advanced/testing-dependencies/)
    - [异步测试](../../advanced/async-tests/)
    - [设置和环境变量](../../advanced/settings/)
    - [OpenAPI 回调](../../advanced/openapi-callbacks/)
    - [OpenAPI 网络钩子](../../advanced/openapi-webhooks/)
    - [包含 WSGI - Flask，Django，其它](../../advanced/wsgi/)
    - [生成 SDK](../../advanced/generate-clients/)
    - [高级 Python 类型](../../advanced/advanced-python-types/)
    - [在 JSON 中使用 Base64 表示字节](../../advanced/json-base64-bytes/)
    - [严格的 Content-Type 检查](../../advanced/strict-content-type/)
  + [FastAPI CLI](../../fastapi-cli/)
  + [编辑器支持](../../editor-support/)
  + [部署](../../deployment/)

    部署
    - [关于 FastAPI 版本](../../deployment/versions/)
    - [FastAPI Cloud](../../deployment/fastapicloud/)
    - [关于 HTTPS](../../deployment/https/)
    - [手动运行服务器](../../deployment/manually/)
    - [部署概念](../../deployment/concepts/)
    - [在云服务商上部署 FastAPI](../../deployment/cloud/)
    - [服务器工作进程（Workers） - 使用 Uvicorn 的多工作进程模式](../../deployment/server-workers/)
    - [容器中的 FastAPI - Docker](../../deployment/docker/)
  + [如何操作 - 诀窍](../../how-to/)

    如何操作 - 诀窍
    - [通用 - 如何操作 - 诀窍](../../how-to/general/)
    - [从 Pydantic v1 迁移到 Pydantic v2](../../how-to/migrate-from-pydantic-v1-to-pydantic-v2/)
    - [GraphQL](../../how-to/graphql/)
    - [自定义 Request 和 APIRoute 类](../../how-to/custom-request-and-route/)
    - [按条件配置 OpenAPI](../../how-to/conditional-openapi/)
    - [扩展 OpenAPI](../../how-to/extending-openapi/)
    - [是否为输入和输出分别生成 OpenAPI JSON Schema](../../how-to/separate-openapi-schemas/)
    - [自托管自定义文档 UI 静态资源](../../how-to/custom-docs-ui-assets/)
    - [配置 Swagger UI](../../how-to/configure-swagger-ui/)
    - [测试数据库](../../how-to/testing-database/)
    - [使用旧的 403 认证错误状态码](../../how-to/authentication-error-status-code/)
* [Reference](../../reference/)

  Reference
  + [`FastAPI` class](../../reference/fastapi/)
  + [Request Parameters](../../reference/parameters/)
  + [Status Codes](../../reference/status/)
  + [`UploadFile` class](../../reference/uploadfile/)
  + [Exceptions - `HTTPException` and `WebSocketException`](../../reference/exceptions/)
  + [Dependencies - `Depends()` and `Security()`](../../reference/dependencies/)
  + [`APIRouter` class](../../reference/apirouter/)
  + [Background Tasks - `BackgroundTasks`](../../reference/background/)
  + [`Request` class](../../reference/request/)
  + [WebSockets](../../reference/websockets/)
  + [`HTTPConnection` class](../../reference/httpconnection/)
  + [`Response` class](../../reference/response/)
  + [Custom Response Classes - File, HTML, Redirect, Streaming, etc.](../../reference/responses/)
  + [Middleware](../../reference/middleware/)
  + [OpenAPI](../../reference/openapi/)

    OpenAPI
    - [OpenAPI `docs`](../../reference/openapi/docs/)
    - [OpenAPI `models`](../../reference/openapi/models/)
  + [Security Tools](../../reference/security/)
  + [Encoders - `jsonable_encoder`](../../reference/encoders/)
  + [Static Files - `StaticFiles`](../../reference/staticfiles/)
  + [Templating - `Jinja2Templates`](../../reference/templating/)
  + [Test Client - `TestClient`](../../reference/testclient/)
* [FastAPI People](../../fastapi-people/)
* [资源](../../resources/)

  资源
  + [帮助 FastAPI - 获取帮助](../../help-fastapi/)
  + [Development - Contributing](../../contributing/)
  + [FastAPI全栈模板](../../project-generation/)
  + [External Links](../../external-links/)
  + [FastAPI and friends newsletter](../../newsletter/)
  + [Repository Management Tasks](../../management-tasks/)
* [关于](../../about/)

  关于
  + [替代方案、灵感与对比](../../alternatives/)
  + [历史、设计、未来](../../history-design-future/)
  + [基准测试](../../benchmarks/)
  + [Repository Management](../../management/)
* [Release Notes](../../release-notes/)

目录

* [声明路径参数的类型](#path-parameters-with-types)
* [数据转换](#data-conversion)
* [数据校验](#data-validation)
* [文档](#documentation)
* [基于标准的好处，备选文档](#standards-based-benefits-alternative-documentation)
* [Pydantic](#pydantic)
* [顺序很重要](#order-matters)
* [预设值](#predefined-values)

  + [创建 `Enum` 类](#create-an-enum-class)
  + [声明路径参数](#declare-a-path-parameter)
  + [查看文档](#check-the-docs)
  + [使用 Python 枚举](#working-with-python-enumerations)

    - [比较枚举成员](#compare-enumeration-members)
    - [获取枚举值](#get-the-enumeration-value)
    - [返回枚举成员](#return-enumeration-members)
* [包含路径的路径参数](#path-parameters-containing-paths)

  + [OpenAPI 支持](#openapi-support)
  + [路径转换器](#path-convertor)
* [小结](#recap)

1. [FastAPI](../..)
2. [学习](../../learn/)
3. [教程 - 用户指南](../)

# 路径参数[¶](#path-parameters "Permanent link")

🌐 由 AI 与人类协作翻译



可能存在误解原意或不够自然等问题。🤖

你可以通过[帮助我们更好地引导 AI LLM](https://fastapi.tiangolo.com/zh/contributing/#translations)来改进此翻译。

[英文版本](https://fastapi.tiangolo.com/tutorial/path-params/)

你可以使用与 Python 字符串格式化相同的语法声明路径“参数”或“变量”：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```

路径参数 `item_id` 的值会作为参数 `item_id` 传递给你的函数。

运行示例并访问 <http://127.0.0.1:8000/items/foo>，可获得如下响应：

```
{"item_id":"foo"}
```

## 声明路径参数的类型[¶](#path-parameters-with-types "Permanent link")

使用 Python 标准类型注解，声明路径操作函数中路径参数的类型：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

本例把 `item_id` 的类型声明为 `int`。

检查

类型声明将为函数提供错误检查、代码补全等编辑器支持。

## 数据转换[¶](#data-conversion "Permanent link")

运行示例并访问 <http://127.0.0.1:8000/items/3>，返回的响应如下：

```
{"item_id":3}
```

检查

注意，函数接收并返回的值是 `3`（ `int`），不是 `"3"`（`str`）。

**FastAPI** 通过类型声明自动进行请求的解析。

## 数据校验[¶](#data-validation "Permanent link")

通过浏览器访问 <http://127.0.0.1:8000/items/foo>，接收如下 HTTP 错误信息：

```
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "path",
        "item_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "foo"
    }
  ]
}
```

这是因为路径参数 `item_id` 的值（`"foo"`）的类型不是 `int`。

值的类型不是 `int` 而是浮点数（`float`）时也会显示同样的错误，比如： <http://127.0.0.1:8000/items/4.2>

检查

**FastAPI** 使用同样的 Python 类型声明实现了数据校验。

注意，上面的错误清晰地指出了未通过校验的具体位置。

这在开发调试与 API 交互的代码时非常有用。

## 文档[¶](#documentation "Permanent link")

访问 <http://127.0.0.1:8000/docs>，查看自动生成的交互式 API 文档：

![](/img/tutorial/path-params/image01.png)

检查

还是使用 Python 类型声明，**FastAPI** 提供了（集成 Swagger UI 的）自动交互式文档。

注意，路径参数的类型是整数。

## 基于标准的好处，备选文档[¶](#standards-based-benefits-alternative-documentation "Permanent link")

**FastAPI** 使用 [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md) 生成概图，所以能兼容很多工具。

因此，**FastAPI** 还内置了 ReDoc 生成的备选 API 文档，可在此查看 <http://127.0.0.1:8000/redoc>：

![](/img/tutorial/path-params/image02.png)

同样，还有很多兼容工具，包括多种语言的代码生成工具。

## Pydantic[¶](#pydantic "Permanent link")

FastAPI 充分地利用了 [Pydantic](https://docs.pydantic.dev/) 的优势，用它在后台校验数据。众所周知，Pydantic 擅长的就是数据校验。

同样，`str`、`float`、`bool` 以及很多复合数据类型都可以使用类型声明。

接下来的章节会介绍其中的好几种。

## 顺序很重要[¶](#order-matters "Permanent link")

有时，*路径操作*中的路径是写死的。

比如要使用 `/users/me` 获取当前用户的数据。

然后还要使用 `/users/{user_id}`，通过用户 ID 获取指定用户的数据。

由于*路径操作*是按顺序依次运行的，因此，一定要在 `/users/{user_id}` 之前声明 `/users/me` ：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

否则，`/users/{user_id}` 将匹配 `/users/me`，FastAPI 会**认为**正在接收值为 `"me"` 的 `user_id` 参数。

同样，你不能重复定义一个路径操作：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
```

由于路径首先匹配，始终会使用第一个定义的。

## 预设值[¶](#predefined-values "Permanent link")

路径操作使用 Python 的 `Enum` 类型接收预设的路径参数。

### 创建 `Enum` 类[¶](#create-an-enum-class "Permanent link")

导入 `Enum` 并创建继承自 `str` 和 `Enum` 的子类。

通过从 `str` 继承，API 文档就能把值的类型定义为**字符串**，并且能正确渲染。

然后，创建包含固定值的类属性，这些固定值是可用的有效值：

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

提示

**AlexNet**、**ResNet**、**LeNet** 是机器学习模型的名字。

### 声明路径参数[¶](#declare-a-path-parameter "Permanent link")

使用 Enum 类（`ModelName`）创建使用类型注解的路径参数：

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

### 查看文档[¶](#check-the-docs "Permanent link")

API 文档会显示预定义路径参数的可用值：

![](/img/tutorial/path-params/image03.png)

### 使用 Python 枚举[¶](#working-with-python-enumerations "Permanent link")

路径参数的值是一个枚举成员。

#### 比较枚举成员[¶](#compare-enumeration-members "Permanent link")

可以将其与枚举类 `ModelName` 中的枚举成员进行比较：

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

#### 获取枚举值[¶](#get-the-enumeration-value "Permanent link")

使用 `model_name.value` 或通用的 `your_enum_member.value` 获取实际的值（本例中为 `str`）：

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

提示

使用 `ModelName.lenet.value` 也能获取值 `"lenet"`。

#### 返回枚举成员[¶](#return-enumeration-members "Permanent link")

即使嵌套在 JSON 请求体里（例如，`dict`），也可以从路径操作返回枚举成员。

返回给客户端之前，会把枚举成员转换为对应的值（本例中为字符串）：

Python 3.10+

```
from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

客户端中的 JSON 响应如下：

```
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```

## 包含路径的路径参数[¶](#path-parameters-containing-paths "Permanent link")

假设路径操作的路径为 `/files/{file_path}`。

但需要 `file_path` 中也包含路径，比如，`home/johndoe/myfile.txt`。

此时，该文件的 URL 是这样的：`/files/home/johndoe/myfile.txt`。

### OpenAPI 支持[¶](#openapi-support "Permanent link")

OpenAPI 不支持声明包含路径的路径参数，因为这会导致测试和定义更加困难。

不过，仍可使用 Starlette 内置工具在 **FastAPI** 中实现这一功能。

而且不影响文档正常运行，但是不会添加该参数包含路径的说明。

### 路径转换器[¶](#path-convertor "Permanent link")

直接使用 Starlette 的选项声明包含路径的路径参数：

```
/files/{file_path:path}
```

本例中，参数名为 `file_path`，结尾部分的 `:path` 说明该参数应匹配路径。

用法如下：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

提示

注意，包含 `/home/johndoe/myfile.txt` 的路径参数要以斜杠（`/`）开头。

本例中的 URL 是 `/files//home/johndoe/myfile.txt`。注意，`files` 和 `home` 之间要使用双斜杠（`//`）。

## 小结[¶](#recap "Permanent link")

通过简短、直观的 Python 标准类型声明，**FastAPI** 可以获得：

* 编辑器支持：错误检查，代码自动补全等
* 数据 "解析"
* 数据校验
* API 注解和自动文档

只需要声明一次即可。

这可能是除了性能以外，**FastAPI** 与其它框架相比的主要优势。



[上一页

第一步](../first-steps/)
[下一页

查询参数](../query-params/)

The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com) and is registered in the US and across other regions

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)