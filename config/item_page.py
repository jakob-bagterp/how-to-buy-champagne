from .model import ItemPage

ITEM_PAGE = ITEM_PAGE_HONEST_GRAPES_CO_UK = ItemPage(
    incremental_increase_amount_button="//*[@id='super-product-table']/tbody[1]/tr/td[2]/div/button[2]",
    add_to_cart_button="//*[@id='super-product-table']/tbody[1]/tr/td[3]/button[1]",
    confirmation_modal="//*[@id='mb-ajaxcart-wrapper']"
)
