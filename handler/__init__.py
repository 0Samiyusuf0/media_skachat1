from aiogram import Router
from .users import start, help, check

def setup_message_routers() -> Router:

    router = Router()

    # users
    router.include_router(start.router)
    router.include_router(help.router)
    router.include_router(check.router)


    # groups

    return router