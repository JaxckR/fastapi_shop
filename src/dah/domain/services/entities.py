from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import NewType
from uuid import UUID

from dah.domain.common.entities import BaseEntity
from dah.domain.services import value_objects as vo


class CurrencyEnum(StrEnum):
    RUB = 'RUB'
    USD = 'USD'


ServicesID = NewType('ServiceID', UUID)


@dataclass(slots=True)
class Services(BaseEntity[ServicesID]):
    name: vo.Name
    image: vo.Image
    price: vo.Price
    currency: CurrencyEnum
    date_created: datetime
