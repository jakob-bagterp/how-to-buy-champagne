from browserist import Browser as BrowserDefault

from helper import action

from .check_out_page import CHECK_OUT_PAGE_HONEST_GRAPES_CO_UK
from .model import CheckOutPage, Item


class Browser(BrowserDefault):
    def __init__(self) -> None:
        super().__init__()

    def buy(self, amount: int, item: Item) -> None:
        action.buy(self, amount, item)

    def check_out(self, check_out_page: CheckOutPage = CHECK_OUT_PAGE_HONEST_GRAPES_CO_UK) -> None:
        action.check_out(self, check_out_page)
