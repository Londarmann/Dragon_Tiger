import motor.motor_asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from beanie import init_beanie


from .config import settings
from dragon.apps.documents.document import Round, Game, GamePlayer
from dragon.apps.routers.game import router
from dragon.apps.server.server import sio, s_app


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(router)
    app.mount("/ws", s_app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.on_event("startup")
    async def startup_event():
        client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
        await init_beanie(database=client[settings.MONGODB_DATABASE_NAME], document_models=[Game, Round, GamePlayer])

    return app
