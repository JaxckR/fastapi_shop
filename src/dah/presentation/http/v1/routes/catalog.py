from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from dah.presentation.http.v1.routes.jinja2 import templates

router = APIRouter(
    tags=["Catalog"],
)


@router.get(
    "/",
    response_class=HTMLResponse,
    name="home",
)
async def home(
        request: Request,
) -> HTMLResponse:
    return templates.TemplateResponse(
        "catalog/index.html", {
            "request": request
        }
    )
