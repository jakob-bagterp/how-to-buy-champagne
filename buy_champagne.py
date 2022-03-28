from config.browser_extension import Browser
from config.cookie_banner import ACCEPT_COOKIES
from config.shopping_list import POL_COURONNE_BRUT

if __name__ == "__main__":
    with Browser() as browser:
        browser.open.url("https://www.honestgrapes.co.uk/")
        browser.combo.cookie_banner(ACCEPT_COOKIES)
        browser.add_to_cart(10, POL_COURONNE_BRUT)
        browser.check_out()
