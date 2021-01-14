from urllib.parse import ParseResult

from fastapi import FastAPI, Request, Response
from utils.config import Config

from .routes import router as ImplRouter

app = FastAPI(
    debug=Config["debug"].as_bool(),
    title="HibiAPI",
    version=Config["version"].as_str(),
    description="An alternative implement of Imjad API",
    docs_url="/docs/test",
    redoc_url="/docs",
)
app.include_router(ImplRouter, prefix="/api")


@app.get("/", include_in_schema=False)
async def redirect(request: Request, to: str = "/docs", code: int = 302):
    return Response(
        status_code=code,
        headers={
            "Location": ParseResult(
                scheme=request.url.scheme,
                netloc=request.url.netloc,
                path=to,
                params="",
                query=request.url.query,
                fragment=request.url.fragment,
            ).geturl()
        },
    )


"""
Temporary redirection solution below for #12
"""


@app.get("/qrcode/{path:path}", include_in_schema=False)
async def _qr_redirect(request: Request, path: str):
    return await redirect(request, to="/api/qrcode/" + path, code=301)


@app.get("/pixiv/{path:path}", include_in_schema=False)
async def _pixiv_redirect(request: Request, path: str):
    return await redirect(request, to="/api/pixiv/" + path, code=301)


@app.get("/netease/{path:path}", include_in_schema=False)
async def _netease_redirect(request: Request, path: str):
    return await redirect(request, to="/api/netease/" + path, code=301)


@app.get("/bilibili/{path:path}", include_in_schema=False)
async def _bilibili_redirect(request: Request, path: str):
    return await redirect(request, to="/api/bilibili/" + path, code=301)
