from dataclasses import dataclass

from dah.domain.services.exceptions import (
    EmptyPriceError,
    PriceNegativeError,
    EmptyNameError,
    EmptyImageError,
)


@dataclass(slots=True)
class Price:
    value: int

    def __post_init__(self) -> None:
        if self.value is None:
            raise EmptyPriceError

        if self.value < 0:
            raise PriceNegativeError


@dataclass(slots=True)
class Name:
    value: str

    def __post_init__(self) -> None:
        if self.value is None:
            raise EmptyNameError


@dataclass(slots=True)
class Image:
    value: str

    def __post_init__(self) -> None:
        if self.value is None:
            raise EmptyImageError
