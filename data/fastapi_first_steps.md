第一步 - FastAPI

](#first-steps)

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

第一步

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
    - 第一步

      [第一步](./)

      目录
      * [查看](#check-it)
      * [交互式 API 文档](#interactive-api-docs)
      * [可选的 API 文档](#alternative-api-docs)
      * [OpenAPI](#openapi)

        + [「模式」](#schema)
        + [API「模式」](#api-schema)
        + [数据「模式」](#data-schema)
        + [OpenAPI 和 JSON Schema](#openapi-and-json-schema)
        + [查看 `openapi.json`](#check-the-openapi-json)
        + [OpenAPI 的用途](#what-is-openapi-for)
      * [在 `pyproject.toml` 中配置应用 `entrypoint`](#configure-the-app-entrypoint-in-pyproject-toml)
      * [`fastapi dev` 带路径](#fastapi-dev-with-path)
      * [部署你的应用（可选）](#deploy-your-app-optional)
      * [分步概括](#recap-step-by-step)

        + [步骤 1：导入 `FastAPI`](#step-1-import-fastapi)
        + [步骤 2：创建一个 `FastAPI`「实例」](#step-2-create-a-fastapi-instance)
        + [步骤 3：创建一个*路径操作*](#step-3-create-a-path-operation)

          - [路径](#path)
          - [操作](#operation)
          - [定义一个*路径操作装饰器*](#define-a-path-operation-decorator)
        + [步骤 4：定义**路径操作函数**](#step-4-define-the-path-operation-function)
        + [步骤 5：返回内容](#step-5-return-the-content)
        + [步骤 6：部署](#step-6-deploy-it)

          - [关于 FastAPI Cloud](#about-fastapi-cloud)
          - [部署到其他云服务商](#deploy-to-other-cloud-providers)
      * [总结](#recap)
    - [路径参数](../path-params/)
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

* [查看](#check-it)
* [交互式 API 文档](#interactive-api-docs)
* [可选的 API 文档](#alternative-api-docs)
* [OpenAPI](#openapi)

  + [「模式」](#schema)
  + [API「模式」](#api-schema)
  + [数据「模式」](#data-schema)
  + [OpenAPI 和 JSON Schema](#openapi-and-json-schema)
  + [查看 `openapi.json`](#check-the-openapi-json)
  + [OpenAPI 的用途](#what-is-openapi-for)
* [在 `pyproject.toml` 中配置应用 `entrypoint`](#configure-the-app-entrypoint-in-pyproject-toml)
* [`fastapi dev` 带路径](#fastapi-dev-with-path)
* [部署你的应用（可选）](#deploy-your-app-optional)
* [分步概括](#recap-step-by-step)

  + [步骤 1：导入 `FastAPI`](#step-1-import-fastapi)
  + [步骤 2：创建一个 `FastAPI`「实例」](#step-2-create-a-fastapi-instance)
  + [步骤 3：创建一个*路径操作*](#step-3-create-a-path-operation)

    - [路径](#path)
    - [操作](#operation)
    - [定义一个*路径操作装饰器*](#define-a-path-operation-decorator)
  + [步骤 4：定义**路径操作函数**](#step-4-define-the-path-operation-function)
  + [步骤 5：返回内容](#step-5-return-the-content)
  + [步骤 6：部署](#step-6-deploy-it)

    - [关于 FastAPI Cloud](#about-fastapi-cloud)
    - [部署到其他云服务商](#deploy-to-other-cloud-providers)
* [总结](#recap)

1. [FastAPI](../..)
2. [学习](../../learn/)
3. [教程 - 用户指南](../)

# 第一步[¶](#first-steps "Permanent link")

🌐 由 AI 与人类协作翻译



可能存在误解原意或不够自然等问题。🤖

你可以通过[帮助我们更好地引导 AI LLM](https://fastapi.tiangolo.com/zh/contributing/#translations)来改进此翻译。

[英文版本](https://fastapi.tiangolo.com/tutorial/first-steps/)

最简单的 FastAPI 文件可能像下面这样：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

将其复制到 `main.py` 文件中。

运行实时服务器：

```
$ <font color="#4E9A06">fastapi</font> dev

  <span style="background-color:#009485"><font color="#D3D7CF"> FastAPI </font></span>  Starting development server 🚀

             Searching for package file structure from directories
             with <font color="#3465A4">__init__.py</font> files
             Importing from <font color="#75507B">/home/user/code/</font><font color="#AD7FA8">awesomeapp</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> module </font></span>  🐍 main.py

     <span style="background-color:#007166"><font color="#D3D7CF"> code </font></span>  Importing the FastAPI app object from the module with
             the following code:

             <u style="text-decoration-style:solid">from </u><u style="text-decoration-style:solid"><b>main</b></u><u style="text-decoration-style:solid"> import </u><u style="text-decoration-style:solid"><b>app</b></u>

      <span style="background-color:#007166"><font color="#D3D7CF"> app </font></span>  Using import string: <font color="#3465A4">main:app</font>

   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Server started at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font>
   <span style="background-color:#007166"><font color="#D3D7CF"> server </font></span>  Documentation at <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000/docs</u></font>

      <span style="background-color:#007166"><font color="#D3D7CF"> tip </font></span>  Running in development mode, for production use:
             <b>fastapi run</b>

             Logs:

     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Will watch for changes in these directories:
             <b>[</b><font color="#4E9A06">&apos;/home/user/code/awesomeapp&apos;</font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Uvicorn running on <font color="#729FCF"><u style="text-decoration-style:solid">http://127.0.0.1:8000</u></font> <b>(</b>Press CTRL+C
             to quit<b>)</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started reloader process <b>[</b><font color="#34E2E2"><b>383138</b></font><b>]</b> using WatchFiles
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Started server process <b>[</b><font color="#34E2E2"><b>383153</b></font><b>]</b>
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Waiting for application startup.
     <span style="background-color:#007166"><font color="#D3D7CF"> INFO </font></span>  Application startup complete.
```

在输出中，会有一行信息像下面这样：

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

该行显示了你的应用在本机所提供服务的 URL 地址。

### 查看[¶](#check-it "Permanent link")

打开浏览器访问 <http://127.0.0.1:8000>。

你将看到如下的 JSON 响应：

```
{"message": "Hello World"}
```

### 交互式 API 文档[¶](#interactive-api-docs "Permanent link")

跳转到 <http://127.0.0.1:8000/docs>。

你将会看到自动生成的交互式 API 文档（由 [Swagger UI](https://github.com/swagger-api/swagger-ui) 提供）：

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### 可选的 API 文档[¶](#alternative-api-docs "Permanent link")

前往 <http://127.0.0.1:8000/redoc>。

你将会看到可选的自动生成文档 （由 [ReDoc](https://github.com/Rebilly/ReDoc) 提供）：

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

### OpenAPI[¶](#openapi "Permanent link")

**FastAPI** 使用定义 API 的 **OpenAPI** 标准将你的所有 API 转换成「模式」。

#### 「模式」[¶](#schema "Permanent link")

「模式」是对事物的一种定义或描述。它并非具体的实现代码，而只是抽象的描述。

#### API「模式」[¶](#api-schema "Permanent link")

在这种场景下，[OpenAPI](https://github.com/OAI/OpenAPI-Specification) 是一种规定如何定义 API 模式的规范。

「模式」的定义包括你的 API 路径，以及它们可能使用的参数等等。

#### 数据「模式」[¶](#data-schema "Permanent link")

「模式」这个术语也可能指的是某些数据比如 JSON 的结构。

在这种情况下，它可以表示 JSON 的属性及其具有的数据类型，等等。

#### OpenAPI 和 JSON Schema[¶](#openapi-and-json-schema "Permanent link")

OpenAPI 为你的 API 定义 API 模式。该模式中包含了你的 API 发送和接收的数据的定义（或称为「模式」），这些定义通过 JSON 数据模式标准 **JSON Schema** 所生成。

#### 查看 `openapi.json`[¶](#check-the-openapi-json "Permanent link")

如果你对原始的 OpenAPI 模式长什么样子感到好奇，FastAPI 自动生成了包含所有 API 描述的 JSON（模式）。

你可以直接在：<http://127.0.0.1:8000/openapi.json> 看到它。

它将显示以如下内容开头的 JSON：

```
{
    "openapi": "3.1.0",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "paths": {
        "/items/": {
            "get": {
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {

...
```

#### OpenAPI 的用途[¶](#what-is-openapi-for "Permanent link")

驱动 FastAPI 内置的 2 个交互式文档系统的正是 OpenAPI 模式。

并且还有数十种替代方案，它们全部都基于 OpenAPI。你可以轻松地将这些替代方案中的任何一种添加到使用 **FastAPI** 构建的应用程序中。

你还可以使用它自动生成与你的 API 进行通信的客户端代码。例如 web 前端，移动端或物联网嵌入程序。

### 在 `pyproject.toml` 中配置应用 `entrypoint`[¶](#configure-the-app-entrypoint-in-pyproject-toml "Permanent link")

你可以在 `pyproject.toml` 文件中配置应用的位置，例如：

```
[tool.fastapi]
entrypoint = "main:app"
```

该 `entrypoint` 会告诉 `fastapi` 命令按如下方式导入应用：

```
from main import app
```

如果你的代码结构如下：

```
.
├── backend
│   ├── main.py
│   ├── __init__.py
```

那么你可以将 `entrypoint` 设置为：

```
[tool.fastapi]
entrypoint = "backend.main:app"
```

这等价于：

```
from backend.main import app
```

### `fastapi dev` 带路径[¶](#fastapi-dev-with-path "Permanent link")

你也可以把文件路径传给 `fastapi dev` 命令，它会尝试推断要使用的 FastAPI 应用对象：

```
$ fastapi dev main.py
```

但这样每次调用 `fastapi` 命令时都需要记得传入正确的路径。

另外，其他工具可能无法找到它，例如 [VS Code 扩展](../../editor-support/) 或 [FastAPI Cloud](https://fastapicloud.com)，因此推荐在 `pyproject.toml` 中使用 `entrypoint`。

### 部署你的应用（可选）[¶](#deploy-your-app-optional "Permanent link")

你可以选择将 FastAPI 应用部署到 [FastAPI Cloud](https://fastapicloud.com)，如果还没有，先去加入候补名单。🚀

如果你已经拥有 **FastAPI Cloud** 账户（我们从候补名单邀请了你 😉），你可以用一条命令部署应用。

部署前，先确保已登录：

```
$ fastapi login

You are logged in to FastAPI Cloud 🚀
```

然后部署你的应用：

```
$ fastapi deploy

Deploying to FastAPI Cloud...

✅ Deployment successful!

🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev
```

就这些！现在你可以通过该 URL 访问你的应用了。✨

## 分步概括[¶](#recap-step-by-step "Permanent link")

### 步骤 1：导入 `FastAPI`[¶](#step-1-import-fastapi "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

`FastAPI` 是一个为你的 API 提供了所有功能的 Python 类。

技术细节

`FastAPI` 是直接从 `Starlette` 继承的类。

你可以通过 `FastAPI` 使用所有的 [Starlette](https://www.starlette.dev/) 的功能。

### 步骤 2：创建一个 `FastAPI`「实例」[¶](#step-2-create-a-fastapi-instance "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

这里的变量 `app` 会是 `FastAPI` 类的一个「实例」。

这个实例将是创建你所有 API 的主要交互对象。

### 步骤 3：创建一个*路径操作*[¶](#step-3-create-a-path-operation "Permanent link")

#### 路径[¶](#path "Permanent link")

这里的「路径」指的是 URL 中从第一个 `/` 起的后半部分。

所以，在一个这样的 URL 中：

```
https://example.com/items/foo
```

...路径会是：

```
/items/foo
```

Info

「路径」也通常被称为「端点」或「路由」。

开发 API 时，「路径」是用来分离「关注点」和「资源」的主要手段。

#### 操作[¶](#operation "Permanent link")

这里的「操作」指的是一种 HTTP「方法」。

下列之一：

* `POST`
* `GET`
* `PUT`
* `DELETE`

...以及更少见的几种：

* `OPTIONS`
* `HEAD`
* `PATCH`
* `TRACE`

在 HTTP 协议中，你可以使用以上的其中一种（或多种）「方法」与每个路径进行通信。

---

在开发 API 时，你通常使用特定的 HTTP 方法去执行特定的行为。

通常使用：

* `POST`：创建数据。
* `GET`：读取数据。
* `PUT`：更新数据。
* `DELETE`：删除数据。

因此，在 OpenAPI 中，每一个 HTTP 方法都被称为「操作」。

我们也打算称呼它们为「操作」。

#### 定义一个*路径操作装饰器*[¶](#define-a-path-operation-decorator "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

`@app.get("/")` 告诉 **FastAPI** 在它下方的函数负责处理如下访问请求：

* 请求路径为 `/`
* 使用 `get` 操作

`@decorator` 信息

`@something` 语法在 Python 中被称为「装饰器」。

像一顶漂亮的装饰帽一样，将它放在一个函数的上方（我猜测这个术语的命名就是这么来的）。

装饰器接收位于其下方的函数并且用它完成一些工作。

在我们的例子中，这个装饰器告诉 **FastAPI** 位于其下方的函数对应着**路径** `/` 加上 `get` **操作**。

它是一个「**路径操作装饰器**」。

你也可以使用其他的操作：

* `@app.post()`
* `@app.put()`
* `@app.delete()`

以及更少见的：

* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

Tip

你可以随意使用任何一个操作（HTTP方法）。

**FastAPI** 没有强制要求操作有任何特定的含义。

此处提供的信息仅作为指导，而不是要求。

比如，当使用 GraphQL 时通常你所有的动作都通过 `POST` 一种方法执行。

### 步骤 4：定义**路径操作函数**[¶](#step-4-define-the-path-operation-function "Permanent link")

这是我们的「**路径操作函数**」：

* **路径**：是 `/`。
* **操作**：是 `get`。
* **函数**：是位于「装饰器」下方的函数（位于 `@app.get("/")` 下方）。

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

这是一个 Python 函数。

每当 **FastAPI** 接收一个使用 `GET` 方法访问 URL「`/`」的请求时这个函数会被调用。

在这个例子中，它是一个 `async` 函数。

---

你也可以将其定义为常规函数而不使用 `async def`:

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

Note

如果你不知道两者的区别，请查阅 [并发: *赶时间吗？*](../../async/#in-a-hurry)。

### 步骤 5：返回内容[¶](#step-5-return-the-content "Permanent link")

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

你可以返回一个 `dict`、`list`，像 `str`、`int` 一样的单个值，等等。

你还可以返回 Pydantic 模型（稍后你将了解更多）。

还有许多其他将会自动转换为 JSON 的对象和模型（包括 ORM 对象等）。尝试下使用你最喜欢的一种，它很有可能已经被支持。

### 步骤 6：部署[¶](#step-6-deploy-it "Permanent link")

用一条命令将你的应用部署到 **[FastAPI Cloud](https://fastapicloud.com)**：`fastapi deploy`。🎉

#### 关于 FastAPI Cloud[¶](#about-fastapi-cloud "Permanent link")

**[FastAPI Cloud](https://fastapicloud.com)** 由 **FastAPI** 的作者和团队打造。

它以最小的投入简化了 **构建**、**部署** 和 **访问** API 的流程。

它把使用 FastAPI 构建应用的相同**开发者体验**带到了将应用**部署**到云端的过程。🎉

FastAPI Cloud 是 *FastAPI 及其朋友们* 开源项目的主要赞助和资金提供方。✨

#### 部署到其他云服务商[¶](#deploy-to-other-cloud-providers "Permanent link")

FastAPI 是开源并基于标准的。你可以将 FastAPI 应用部署到你选择的任何云服务商。

按照你的云服务商的指南部署 FastAPI 应用即可。🤓

## 总结[¶](#recap "Permanent link")

* 导入 `FastAPI`。
* 创建一个 `app` 实例。
* 编写一个**路径操作装饰器**，如 `@app.get("/")`。
* 定义一个**路径操作函数**，如 `def root(): ...`。
* 使用命令 `fastapi dev` 运行开发服务器。
* 可选：使用 `fastapi deploy` 部署你的应用。



[上一页

教程 - 用户指南](../)
[下一页

路径参数](../path-params/)

The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com) and is registered in the US and across other regions

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)