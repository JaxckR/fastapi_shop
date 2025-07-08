from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from dah.presentation.http.v1.routes.jinja2 import templates

router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
)


@router.get("")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/template", response_class=HTMLResponse)
async def healthcheck(
        request: Request,
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
        }
    )
