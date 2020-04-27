from abc import ABC, abstractmethod
from typing import Callable
from fastapi_utils.inferring_router import InferringRouter


class BaseController(ABC):
    def __init__(self):
        self._router = InferringRouter()
        self._register_routes()

    @abstractmethod
    def _register_routes(self):
        pass

    @property
    def router(self) -> InferringRouter:
        return self._router

    def _get(self, path: str, endpoint: Callable, **kwargs):
        self.__add_route(path, endpoint, 'get', **kwargs)

    def _post(self, path: str, endpoint: Callable, **kwargs):
        self.__add_route(path, endpoint, 'post', **kwargs)

    def _put(self, path: str, endpoint: Callable, **kwargs):
        self.__add_route(path, endpoint, 'put', **kwargs)

    def _delete(self, path: str, endpoint: Callable, **kwargs):
        self.__add_route(path, endpoint, 'delete', **kwargs)

    def __add_route(self, path: str, endpoint: Callable, method: str, **kwargs):
        self._router.add_api_route(path, endpoint, methods=[method.upper()], **kwargs)
