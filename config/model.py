from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    url: str


@dataclass(frozen=True, slots=True)
class ItemPage:
    incremental_increase_amount_button: str
    add_to_cart_button: str
    confirmation_modal: str | None = None


@dataclass(frozen=True, slots=True)
class CheckOutPage:
    url: str
