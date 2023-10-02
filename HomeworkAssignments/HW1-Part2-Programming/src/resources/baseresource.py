from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

KV = Dict[str, Any]

class BaseResource(ABC):
    @abstractmethod
    def get_all(self, filters: KV) -> List:
        pass

    @abstractmethod
    def get_by_id(self, _id) -> Optional:
        pass

    @abstractmethod
    def create(self, thing) -> bool:
        pass

    @abstractmethod
    def update(self, _id, thing) -> bool:
        pass

    @abstractmethod
    def delete(self, _id) -> bool:
        pass
