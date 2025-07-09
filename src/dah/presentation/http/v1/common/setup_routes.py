from fastapi import FastAPI, APIRouter

from dah.presentation.http.v1.routes.catalog import router as catalog_router
from dah.presentation.http.v1.routes.healthcheck import router as healthcheck_router


def setup_routes(app: FastAPI) -> None:
    router = APIRouter()
    router.include_router(healthcheck_router)
    router.include_router(catalog_router)

    app.include_router(router)
