from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

PATH = Path(__file__).parent

templates = Jinja2Templates(directory=PATH / 'frontend/templates')


def setup_static_root(app: FastAPI) -> None:
    app.mount(
        "/static",
        StaticFiles(directory=PATH / "frontend/static"),
        name="static"
    )
