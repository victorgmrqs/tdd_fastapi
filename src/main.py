from fastapi import FastAPI

from src.core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version=settings.PROJECT_VERSION,
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH,
        )


app = App()
