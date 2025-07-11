from typing import cast
from datetime import datetime

from dah.domain.services.entities import CurrencyEnum, ServicesID, Services
from dah.domain.services import value_objects as vo


class ServicesService:
    def __init__(self):
        ...

    def create(
            self,
            oid: ServicesID,
            name: str,
            image: str,
            price: int,
            currency: CurrencyEnum,
    ):
        return Services(
            oid=oid,
            name=vo.Name(name),
            image=vo.Image(image),
            price=vo.Price(price),
            currency=currency,
            date_created=cast("datetime", cast("object", None))
        )
