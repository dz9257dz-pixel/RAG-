请求体 - FastAPI

](#request-body)

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

请求体

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
    - [路径参数](../path-params/)
    - [查询参数](../query-params/)
    - 请求体

      [请求体](./)

      目录
      * [导入 Pydantic 的 `BaseModel`](#import-pydantics-basemodel)
      * [创建数据模型](#create-your-data-model)
      * [声明为参数](#declare-it-as-a-parameter)
      * [结果](#results)
      * [自动文档](#automatic-docs)
      * [编辑器支持](#editor-support)
      * [使用模型](#use-the-model)
      * [请求体 + 路径参数](#request-body-path-parameters)
      * [请求体 + 路径 + 查询参数](#request-body-path-query-parameters)
      * [不使用 Pydantic](#without-pydantic)
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

* [导入 Pydantic 的 `BaseModel`](#import-pydantics-basemodel)
* [创建数据模型](#create-your-data-model)
* [声明为参数](#declare-it-as-a-parameter)
* [结果](#results)
* [自动文档](#automatic-docs)
* [编辑器支持](#editor-support)
* [使用模型](#use-the-model)
* [请求体 + 路径参数](#request-body-path-parameters)
* [请求体 + 路径 + 查询参数](#request-body-path-query-parameters)
* [不使用 Pydantic](#without-pydantic)

1. [FastAPI](../..)
2. [学习](../../learn/)
3. [教程 - 用户指南](../)

# 请求体[¶](#request-body "Permanent link")

🌐 由 AI 与人类协作翻译



可能存在误解原意或不够自然等问题。🤖

你可以通过[帮助我们更好地引导 AI LLM](https://fastapi.tiangolo.com/zh/contributing/#translations)来改进此翻译。

[英文版本](https://fastapi.tiangolo.com/tutorial/body/)

当你需要从客户端（比如浏览器）向你的 API 发送数据时，会把它作为**请求体**发送。

**请求体**是客户端发送给你的 API 的数据。**响应体**是你的 API 发送给客户端的数据。

你的 API 几乎总是需要发送**响应体**。但客户端不一定总是要发送**请求体**，有时它们只请求某个路径，可能带一些查询参数，但不会发送请求体。

使用 [Pydantic](https://docs.pydantic.dev/) 模型来声明**请求体**，能充分利用它的功能和优点。

信息

发送数据应使用以下之一：`POST`（最常见）、`PUT`、`DELETE` 或 `PATCH`。

规范中没有定义用 `GET` 请求发送请求体的行为，但 FastAPI 仍支持这种方式，只用于非常复杂/极端的用例。

由于不推荐，在使用 `GET` 时，Swagger UI 的交互式文档不会显示请求体的文档，而且中间的代理可能也不支持它。

## 导入 Pydantic 的 `BaseModel`[¶](#import-pydantics-basemodel "Permanent link")

从 `pydantic` 中导入 `BaseModel`：

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

## 创建数据模型[¶](#create-your-data-model "Permanent link")

把数据模型声明为继承 `BaseModel` 的类。

使用 Python 标准类型声明所有属性：

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

与声明查询参数一样，包含默认值的模型属性是可选的，否则就是必选的。把默认值设为 `None` 可使其变为可选。

例如，上述模型声明如下 JSON "object"（即 Python `dict`）：

```
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

...由于 `description` 和 `tax` 是可选的（默认值为 `None`），下面的 JSON "object" 也有效：

```
{
    "name": "Foo",
    "price": 45.2
}
```

## 声明为参数[¶](#declare-it-as-a-parameter "Permanent link")

使用与声明路径和查询参数相同的方式，把它添加至*路径操作*：

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
```

...并把其类型声明为你创建的模型 `Item`。

## 结果[¶](#results "Permanent link")

仅使用这些 Python 类型声明，**FastAPI** 就可以：

* 以 JSON 形式读取请求体。
* （在必要时）把请求体转换为对应的类型。
* 校验数据。
  + 数据无效时返回清晰的错误信息，并指出错误数据的确切位置和内容。
* 把接收的数据赋值给参数 `item`。
  + 因为你把函数中的参数类型声明为 `Item`，所以还能获得所有属性及其类型的编辑器支持（补全等）。
* 为你的模型生成 [JSON Schema](https://json-schema.org) 定义，如果对你的项目有意义，还可以在其他地方使用它们。
* 这些 schema 会成为生成的 OpenAPI Schema 的一部分，并被自动文档的 UIs 使用。

## 自动文档[¶](#automatic-docs "Permanent link")

你的模型的 JSON Schema 会成为生成的 OpenAPI Schema 的一部分，并显示在交互式 API 文档中：

![](/img/tutorial/body/image01.png)

并且，还会用于需要它们的每个*路径操作*的 API 文档中：

![](/img/tutorial/body/image02.png)

## 编辑器支持[¶](#editor-support "Permanent link")

在编辑器中，函数内部你会在各处得到类型提示与补全（如果接收的不是 Pydantic 模型，而是 `dict`，就不会有这样的支持）：

![](/img/tutorial/body/image03.png)

还支持检查错误的类型操作：

![](/img/tutorial/body/image04.png)

这并非偶然，整个框架都是围绕这种设计构建的。

并且在设计阶段、实现之前就进行了全面测试，以确保它能在所有编辑器中正常工作。

我们甚至对 Pydantic 本身做了一些改动以支持这些功能。

上面的截图来自 [Visual Studio Code](https://code.visualstudio.com)。

但使用 [PyCharm](https://www.jetbrains.com/pycharm/) 和大多数其他 Python 编辑器，你也会获得相同的编辑器支持：

![](/img/tutorial/body/image05.png)

提示

如果你使用 [PyCharm](https://www.jetbrains.com/pycharm/) 作为编辑器，可以使用 [Pydantic PyCharm 插件](https://github.com/koxudaxi/pydantic-pycharm-plugin/)。

它能改进对 Pydantic 模型的编辑器支持，包括：

* 自动补全
* 类型检查
* 代码重构
* 查找
* 代码审查

## 使用模型[¶](#use-the-model "Permanent link")

在*路径操作*函数内部直接访问模型对象的所有属性：

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
```

## 请求体 + 路径参数[¶](#request-body-path-parameters "Permanent link")

可以同时声明路径参数和请求体。

**FastAPI** 能识别与**路径参数**匹配的函数参数应该**从路径中获取**，而声明为 Pydantic 模型的函数参数应该**从请求体中获取**。

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
```

## 请求体 + 路径 + 查询参数[¶](#request-body-path-query-parameters "Permanent link")

也可以同时声明**请求体**、**路径**和**查询**参数。

**FastAPI** 会分别识别它们，并从正确的位置获取数据。

Python 3.10+

```
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
```

函数参数按如下规则进行识别：

* 如果该参数也在**路径**中声明了，它就是路径参数。
* 如果该参数是（`int`、`float`、`str`、`bool` 等）**单一类型**，它会被当作**查询**参数。
* 如果该参数的类型声明为 **Pydantic 模型**，它会被当作请求**体**。

注意

FastAPI 会根据默认值 `= None` 知道 `q` 的值不是必填的。

`str | None` 并不是 FastAPI 用来判断是否必填的依据；是否必填由是否有默认值 `= None` 决定。

但添加这些类型注解可以让你的编辑器提供更好的支持并检测错误。

## 不使用 Pydantic[¶](#without-pydantic "Permanent link")

即便不使用 Pydantic 模型也能使用 **Body** 参数。详见[请求体 - 多参数：请求体中的单值](../body-multiple-params/#singular-values-in-body)。



[上一页

查询参数](../query-params/)
[下一页

查询参数和字符串校验](../query-params-str-validations/)

The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com) and is registered in the US and across other regions

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)