from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from scalar_fastapi import get_scalar_api_reference
from core.fastapi.middlewares import SQLAlchemyMiddleware
from app.health import api_router as health_router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(health_router, tags=["Health"])


# def init_listeners(app_: FastAPI) -> None:
#     # Exception handler
#     @app_.exception_handler(CustomException)
#     async def custom_exception_handler(request: Request, exc: CustomException):
#         return JSONResponse(
#             status_code=exc.code,
#             content={"error_code": exc.error_code, "message": exc.message},
#         )


# def on_auth_error(request: Request, exc: Exception):
#     status_code, error_code, message = 401, None, str(exc)
#     if isinstance(exc, CustomException):
#         status_code = int(exc.code)
#         error_code = exc.error_code
#         message = exc.message

#     return JSONResponse(
#         status_code=status_code,
#         content={"error_code": error_code, "message": message},
#     )


def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        # Middleware(
        #     AuthenticationMiddleware,
        #     backend=AuthBackend(),
        #     on_error=on_auth_error,
        # ),
        Middleware(SQLAlchemyMiddleware),
        # Middleware(ResponseLogMiddleware),
    ]
    return middleware


# def init_cache() -> None:
#     Cache.init(backend=RedisBackend(), key_maker=CustomKeyMaker())


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None,
        redoc_url=None,
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    # init_listeners(app_=app_)
    # init_cache()
    return app_


app = create_app()


@app.get("/docs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url if app.openapi_url else "/openapi.json",
        title=app.title,
    )
