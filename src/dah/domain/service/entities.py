from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import NewType

from dah.domain.common.entities import BaseEntity
from dah.domain.service import value_objects as vo


class CurrencyEnum(StrEnum):
    RUB = 'RUB'
    USD = 'USD'


ServiceID = NewType('ServiceID', int)


@dataclass(slots=True)
class Service(BaseEntity[ServiceID]):
    name: vo.Name
    image: vo.Image
    price: vo.Price
    currency: CurrencyEnum
    date_created: datetime
