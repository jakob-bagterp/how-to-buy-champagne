import time

from browserist import Browser

from config.item_page import ITEM_PAGE
from config.model import CheckOutPage, Item


def buy(browser: Browser, amount: int, item: Item):
    browser.open.url(item.url)
    for _ in range(amount - 1):  # The item count always starts at 1.
        browser.click.button(ITEM_PAGE.incremental_increase_amount_button)
        time.sleep(0.1)
    browser.click.button(ITEM_PAGE.add_to_cart_button)
    if ITEM_PAGE.confirmation_modal:
        browser.wait.for_element(ITEM_PAGE.confirmation_modal)
        time.sleep(1)


def check_out(browser: Browser, check_out_page: CheckOutPage):
    browser.open.url(check_out_page.url)
