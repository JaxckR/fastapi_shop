from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from dah.presentation.http.v1.common.setup_routes import setup_routes
from dah.presentation.http.v1.routes.jinja2 import setup_static_root


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield None
    await app.state.dishka_container.close()


def get_app() -> FastAPI:
    app = FastAPI(
        title="DreamAndHigh",
        description="Shop site",
        version="1.0.0",
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )
    setup_routes(app)
    setup_static_root(app)

    return app
