from dataclasses import dataclass
from typing import TypeVar, Generic

OIDType = TypeVar('OIDType')


@dataclass(slots=True)
class BaseEntity(Generic[OIDType]):
    oid: OIDType
