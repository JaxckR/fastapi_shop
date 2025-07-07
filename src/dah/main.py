from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


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
        root_path="/api",
        default_response_class=ORJSONResponse,
    )

    return app
