查询参数和字符串校验 - FastAPI

](#query-parameters-and-string-validations)

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

查询参数和字符串校验

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
    - [请求体](../body/)
    - 查询参数和字符串校验

      [查询参数和字符串校验](./)

      目录
      * [额外校验](#additional-validation)

        + [导入 `Query` 和 `Annotated`](#import-query-and-annotated)
      * [在 `q` 参数的类型中使用 `Annotated`](#use-annotated-in-the-type-for-the-q-parameter)
      * [在 `q` 的 `Annotated` 中添加 `Query`](#add-query-to-annotated-in-the-q-parameter)
      * [另一种（旧的）方式：把 `Query` 作为默认值](#alternative-old-query-as-the-default-value)

        + [在默认值中使用 `Query` 或在 `Annotated` 中使用 `Query`](#query-as-the-default-value-or-in-annotated)
        + [`Annotated` 的优势](#advantages-of-annotated)
      * [添加更多校验](#add-more-validations)
      * [添加正则表达式](#add-regular-expressions)
      * [默认值](#default-values)
      * [必填参数](#required-parameters)

        + [必填，但可以为 `None`](#required-can-be-none)
      * [查询参数列表 / 多个值](#query-parameter-list-multiple-values)

        + [具有默认值的查询参数列表 / 多个值](#query-parameter-list-multiple-values-with-defaults)

          - [只使用 `list`](#using-just-list)
      * [声明更多元数据](#declare-more-metadata)
      * [别名参数](#alias-parameters)
      * [弃用参数](#deprecating-parameters)
      * [从 OpenAPI 中排除参数](#exclude-parameters-from-openapi)
      * [自定义校验](#custom-validation)

        + [理解这段代码](#understand-that-code)

          - [字符串与 `value.startswith()`](#string-with-value-startswith)
          - [一个随机条目](#a-random-item)
      * [总结](#recap)
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

* [额外校验](#additional-validation)

  + [导入 `Query` 和 `Annotated`](#import-query-and-annotated)
* [在 `q` 参数的类型中使用 `Annotated`](#use-annotated-in-the-type-for-the-q-parameter)
* [在 `q` 的 `Annotated` 中添加 `Query`](#add-query-to-annotated-in-the-q-parameter)
* [另一种（旧的）方式：把 `Query` 作为默认值](#alternative-old-query-as-the-default-value)

  + [在默认值中使用 `Query` 或在 `Annotated` 中使用 `Query`](#query-as-the-default-value-or-in-annotated)
  + [`Annotated` 的优势](#advantages-of-annotated)
* [添加更多校验](#add-more-validations)
* [添加正则表达式](#add-regular-expressions)
* [默认值](#default-values)
* [必填参数](#required-parameters)

  + [必填，但可以为 `None`](#required-can-be-none)
* [查询参数列表 / 多个值](#query-parameter-list-multiple-values)

  + [具有默认值的查询参数列表 / 多个值](#query-parameter-list-multiple-values-with-defaults)

    - [只使用 `list`](#using-just-list)
* [声明更多元数据](#declare-more-metadata)
* [别名参数](#alias-parameters)
* [弃用参数](#deprecating-parameters)
* [从 OpenAPI 中排除参数](#exclude-parameters-from-openapi)
* [自定义校验](#custom-validation)

  + [理解这段代码](#understand-that-code)

    - [字符串与 `value.startswith()`](#string-with-value-startswith)
    - [一个随机条目](#a-random-item)
* [总结](#recap)

1. [FastAPI](../..)
2. [学习](../../learn/)
3. [教程 - 用户指南](../)

# 查询参数和字符串校验[¶](#query-parameters-and-string-validations "Permanent link")

🌐 由 AI 与人类协作翻译



可能存在误解原意或不够自然等问题。🤖

你可以通过[帮助我们更好地引导 AI LLM](https://fastapi.tiangolo.com/zh/contributing/#translations)来改进此翻译。

[英文版本](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)

**FastAPI** 允许你为参数声明额外的信息和校验。

让我们以下面的应用为例：

Python 3.10+

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

查询参数 `q` 的类型为 `str | None`，这意味着它是 `str` 类型，但也可以是 `None`。其默认值确实为 `None`，所以 FastAPI 会知道它不是必填的。

注意

FastAPI 会因为默认值 `= None` 而知道 `q` 的值不是必填的。

将类型标注为 `str | None` 能让你的编辑器提供更好的辅助和错误检测。

## 额外校验[¶](#additional-validation "Permanent link")

我们打算添加约束：即使 `q` 是可选的，但只要提供了该参数，**其长度不能超过 50 个字符**。

### 导入 `Query` 和 `Annotated`[¶](#import-query-and-annotated "Permanent link")

为此，先导入：

* 从 `fastapi` 导入 `Query`
* 从 `typing` 导入 `Annotated`

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

信息

FastAPI 在 0.95.0 版本中添加了对 `Annotated` 的支持（并开始推荐使用）。

如果你的版本更旧，使用 `Annotated` 会报错。

在使用 `Annotated` 之前，请确保先[升级 FastAPI 版本](../../deployment/versions/#upgrading-the-fastapi-versions)到至少 0.95.1。

## 在 `q` 参数的类型中使用 `Annotated`[¶](#use-annotated-in-the-type-for-the-q-parameter "Permanent link")

还记得我之前在[Python 类型简介](../../python-types/#type-hints-with-metadata-annotations)中说过可以用 `Annotated` 给参数添加元数据吗？

现在正是与 FastAPI 搭配使用它的时候。🚀

我们之前的类型标注是：

```
q: str | None = None
```

我们要做的是用 `Annotated` 把它包起来，变成：

```
q: Annotated[str | None] = None
```

这两种写法含义相同，`q` 是一个可以是 `str` 或 `None` 的参数，默认是 `None`。

现在进入更有趣的部分。🎉

## 在 `q` 的 `Annotated` 中添加 `Query`[¶](#add-query-to-annotated-in-the-q-parameter "Permanent link")

有了 `Annotated` 之后，我们就可以放入更多信息（本例中是额外的校验）。在 `Annotated` 中添加 `Query`，并把参数 `max_length` 设为 `50`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

注意默认值依然是 `None`，所以该参数仍是可选的。

但现在把 `Query(max_length=50)` 放到 `Annotated` 里，我们就在告诉 FastAPI，这个值需要**额外校验**，最大长度为 50 个字符。😎

提示

这里用的是 `Query()`，因为这是一个**查询参数**。稍后我们还会看到 `Path()`、`Body()`、`Header()` 和 `Cookie()`，它们也接受与 `Query()` 相同的参数。

FastAPI 现在会：

* 对数据进行**校验**，确保最大长度为 50 个字符
* 当数据无效时向客户端展示**清晰的错误**
* 在 OpenAPI 模式的*路径操作*中**记录**该参数（因此会出现在**自动文档 UI** 中）

## 另一种（旧的）方式：把 `Query` 作为默认值[¶](#alternative-old-query-as-the-default-value "Permanent link")

早期版本的 FastAPI（0.95.0 之前）要求你把 `Query` 作为参数的默认值，而不是放在 `Annotated` 里。你很可能会在别处看到这种写法，所以我也给你解释一下。

提示

对于新代码以及在可能的情况下，请按上文所述使用 `Annotated`。它有多项优势（如下所述），没有劣势。🍰

像这样把 `Query()` 作为函数参数的默认值，并把参数 `max_length` 设为 50：

Python 3.10+ - non-Annotated

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

由于这种情况下（不使用 `Annotated`）我们必须把函数中的默认值 `None` 替换为 `Query()`，因此需要通过参数 `Query(default=None)` 来设置默认值，它起到同样的作用（至少对 FastAPI 来说）。

所以：

```
q: str | None = Query(default=None)
```

...会让参数变成可选，默认值为 `None`，等同于：

```
q: str | None = None
```

但使用 `Query` 的版本会显式把它声明为一个查询参数。

然后，我们可以向 `Query` 传入更多参数。本例中是适用于字符串的 `max_length` 参数：

```
q: str | None = Query(default=None, max_length=50)
```

这会校验数据、在数据无效时展示清晰的错误，并在 OpenAPI 模式的*路径操作*中记录该参数。

### 在默认值中使用 `Query` 或在 `Annotated` 中使用 `Query`[¶](#query-as-the-default-value-or-in-annotated "Permanent link")

注意，当你在 `Annotated` 中使用 `Query` 时，不能再给 `Query` 传 `default` 参数。

相反，应使用函数参数本身的实际默认值。否则会不一致。

例如，下面这样是不允许的：

```
q: Annotated[str, Query(default="rick")] = "morty"
```

...因为不清楚默认值应该是 `"rick"` 还是 `"morty"`。

因此，你应该这样用（推荐）：

```
q: Annotated[str, Query()] = "rick"
```

...或者在旧代码库中你会见到：

```
q: str = Query(default="rick")
```

### `Annotated` 的优势[¶](#advantages-of-annotated "Permanent link")

**推荐使用 `Annotated`**，而不是把 `Query` 放在函数参数的默认值里，这样做在多方面都**更好**。🤓

函数参数的**默认值**就是**真正的默认值**，这与 Python 的直觉更一致。😌

你可以在**其他地方**不通过 FastAPI **直接调用**这个函数，而且它会**按预期工作**。如果有**必填**参数（没有默认值），你的**编辑器**会报错提示；如果在运行时没有传入必填参数，**Python** 也会报错。

当你不使用 `Annotated` 而是使用**（旧的）默认值风格**时，如果你在**其他地方**不通过 FastAPI 调用该函数，你必须**记得**给函数传参，否则得到的值会和预期不同（例如得到 `QueryInfo` 之类的对象而不是 `str`）。而你的编辑器不会报错，Python 也不会在调用时报错，只有在函数内部的操作出错时才会暴露问题。

由于 `Annotated` 可以包含多个元数据标注，你甚至可以用同一个函数与其他工具配合，例如 [Typer](https://typer.tiangolo.com/)。🚀

## 添加更多校验[¶](#add-more-validations "Permanent link")

你还可以添加 `min_length` 参数：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(default=None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## 添加正则表达式[¶](#add-regular-expressions "Permanent link")

你可以定义一个参数必须匹配的 正则表达式 `pattern`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None, min_length=3, max_length=50, pattern="^fixedquery$"
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

这个特定的正则表达式通过以下规则检查接收到的参数值：

* `^`：必须以接下来的字符开头，前面没有其他字符。
* `fixedquery`：值必须精确等于 `fixedquery`。
* `$`：到此结束，在 `fixedquery` 之后没有更多字符。

如果你对这些**「正则表达式」**概念感到迷茫，不必担心。对很多人来说这都是个难点。你仍然可以在不使用正则表达式的情况下做很多事情。

现在你知道了，一旦需要时，你可以在 **FastAPI** 中直接使用它们。

## 默认值[¶](#default-values "Permanent link")

当然，你也可以使用 `None` 以外的默认值。

假设你想要声明查询参数 `q` 的 `min_length` 为 `3`，并且默认值为 `"fixedquery"`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

注意

任何类型的默认值（包括 `None`）都会让该参数变为可选（非必填）。

## 必填参数[¶](#required-parameters "Permanent link")

当我们不需要声明更多校验或元数据时，只需不声明默认值就可以让查询参数 `q` 成为必填参数，例如：

```
q: str
```

而不是：

```
q: str | None = None
```

但现在我们用 `Query` 来声明它，例如：

```
q: Annotated[str | None, Query(min_length=3)] = None
```

因此，在使用 `Query` 的同时需要把某个值声明为必填时，只需不声明默认值：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

### 必填，但可以为 `None`[¶](#required-can-be-none "Permanent link")

你可以声明一个参数可以接收 `None`，但它仍然是必填的。这将强制客户端必须发送一个值，即使该值是 `None`。

为此，你可以声明 `None` 是有效类型，但不声明默认值：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## 查询参数列表 / 多个值[¶](#query-parameter-list-multiple-values "Permanent link")

当你用 `Query` 显式地定义查询参数时，你还可以声明它接收一个值列表，换句话说，接收多个值。

例如，要声明一个可在 URL 中出现多次的查询参数 `q`，你可以这样写：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items
```

然后，访问如下 URL：

```
http://localhost:8000/items/?q=foo&q=bar
```

你会在*路径操作函数*的*函数参数* `q` 中以一个 Python `list` 的形式接收到多个 `q` *查询参数* 的值（`foo` 和 `bar`）。

因此，该 URL 的响应将会是：

```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

提示

要声明类型为 `list` 的查询参数（如上例），你需要显式地使用 `Query`，否则它会被解释为请求体。

交互式 API 文档会相应更新，以支持多个值：

![](/img/tutorial/query-params-str-validations/image02.png)

### 具有默认值的查询参数列表 / 多个值[¶](#query-parameter-list-multiple-values-with-defaults "Permanent link")

你还可以定义在没有给定值时的默认 `list`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: list[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items
```

如果你访问：

```
http://localhost:8000/items/
```

`q` 的默认值将为：`["foo", "bar"]`，你的响应会是：

```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

#### 只使用 `list`[¶](#using-just-list "Permanent link")

你也可以直接使用 `list`，而不是 `list[str]`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items
```

注意

请记住，在这种情况下 FastAPI 不会检查列表的内容。

例如，`list[int]` 会检查（并记录到文档）列表的内容必须是整数。但仅用 `list` 不会。

## 声明更多元数据[¶](#declare-more-metadata "Permanent link")

你可以添加更多有关该参数的信息。

这些信息会包含在生成的 OpenAPI 中，并被文档用户界面和外部工具使用。

注意

请记住，不同的工具对 OpenAPI 的支持程度可能不同。

其中一些可能还不会展示所有已声明的额外信息，尽管在大多数情况下，缺失的功能已经在计划开发中。

你可以添加 `title`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(default=None, title="Query string", min_length=3),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

以及 `description`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## 别名参数[¶](#alias-parameters "Permanent link")

假设你想要参数名为 `item-query`。

像这样：

```
http://127.0.0.1:8000/items/?item-query=foobaritems
```

但 `item-query` 不是有效的 Python 变量名。

最接近的有效名称是 `item_query`。

但你仍然需要它在 URL 中就是 `item-query`...

这时可以用 `alias` 参数声明一个别名，FastAPI 会用该别名在 URL 中查找参数值：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str | None = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

## 弃用参数[¶](#deprecating-parameters "Permanent link")

现在假设你不再喜欢这个参数了。

由于还有客户端在使用它，你不得不保留一段时间，但你希望文档清楚地将其展示为已弃用。

那么将参数 `deprecated=True` 传给 `Query`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str | None = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
```

文档将会像下面这样展示它：

![](/img/tutorial/query-params-str-validations/image01.png)

## 从 OpenAPI 中排除参数[¶](#exclude-parameters-from-openapi "Permanent link")

要把某个查询参数从生成的 OpenAPI 模式中排除（从而也不会出现在自动文档系统中），将 `Query` 的参数 `include_in_schema` 设为 `False`：

Python 3.10+

```
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    hidden_query: str | None = Query(default=None, include_in_schema=False),
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
```

## 自定义校验[¶](#custom-validation "Permanent link")

有些情况下你需要做一些无法通过上述参数完成的**自定义校验**。

在这些情况下，你可以使用**自定义校验函数**，该函数会在正常校验之后应用（例如，在先校验值是 `str` 之后）。

你可以在 `Annotated` 中使用 [Pydantic 的 `AfterValidator`](https://docs.pydantic.dev/latest/concepts/validators/#field-after-validator) 来实现。

提示

Pydantic 还有 [`BeforeValidator`](https://docs.pydantic.dev/latest/concepts/validators/#field-before-validator) 等。🤓

例如，这个自定义校验器会检查条目 ID 是否以 `isbn-`（用于 ISBN 书号）或 `imdb-`（用于 IMDB 电影 URL 的 ID）开头：

Python 3.10+

```
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

信息

这在 Pydantic 2 或更高版本中可用。😎

提示

如果你需要进行任何需要与**外部组件**通信的校验，例如数据库或其他 API，你应该改用 **FastAPI 依赖项**，稍后你会学到它们。

这些自定义校验器用于只需检查请求中**同一份数据**即可完成的事情。

### 理解这段代码[¶](#understand-that-code "Permanent link")

关键点仅仅是：在 `Annotated` 中使用带函数的 **`AfterValidator`**。不感兴趣可以跳过这一节。🤸

---

但如果你对这个具体示例好奇，并且还愿意继续看，这里有一些额外细节。

#### 字符串与 `value.startswith()`[¶](#string-with-value-startswith "Permanent link")

注意到了吗？字符串的 `value.startswith()` 可以接收一个元组，它会检查元组中的每个值：

Python 3.10+

```
# Code above omitted 👆

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

# Code below omitted 👇
```

👀 Full file preview

Python 3.10+

```
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

#### 一个随机条目[¶](#a-random-item "Permanent link")

使用 `data.items()` 我们会得到一个包含每个字典项键和值的元组的 可迭代对象。

我们用 `list(data.items())` 把这个可迭代对象转换成一个真正的 `list`。

然后用 `random.choice()` 可以从该列表中获取一个**随机值**，也就是一个 `(id, name)` 的元组。它可能像 `("imdb-tt0371724", "The Hitchhiker's Guide to the Galaxy")` 这样。

接着我们把这个元组的**两个值**分别赋给变量 `id` 和 `name`。

所以，即使用户没有提供条目 ID，他们仍然会收到一个随机推荐。

...而我们把这些都放在**一行简单的代码**里完成。🤯 你不爱 Python 吗？🐍

Python 3.10+

```
# Code above omitted 👆

@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

👀 Full file preview

Python 3.10+

```
import random
from typing import Annotated

from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}
```

## 总结[¶](#recap "Permanent link")

你可以为参数声明额外的校验和元数据。

通用的校验和元数据：

* `alias`
* `title`
* `description`
* `deprecated`

字符串特有的校验：

* `min_length`
* `max_length`
* `pattern`

也可以使用 `AfterValidator` 进行自定义校验。

在这些示例中，你看到了如何为 `str` 值声明校验。

参阅下一章节，了解如何为其他类型（例如数值）声明校验。



[上一页

请求体](../body/)
[下一页

路径参数和数值校验](../path-params-numeric-validations/)

The FastAPI trademark is owned by [@tiangolo](https://tiangolo.com) and is registered in the US and across other regions

Made with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)