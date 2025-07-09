from typing import override

from dah.domain.common.exceptions import DomainError


class EmptyPriceError(DomainError):

    @property
    @override
    def message(self) -> str:
        return "Price can't be empty"


class PriceNegativeError(DomainError):

    @property
    @override
    def message(self) -> str:
        return "Price can't be negative"


class EmptyNameError(DomainError):

    @property
    @override
    def message(self) -> str:
        return "Name can't be empty"


class EmptyImageError(DomainError):

    @property
    @override
    def message(self) -> str:
        return "Image can't be empty"
