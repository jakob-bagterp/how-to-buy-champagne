from config.browser_extension import Browser
from config.cookie_banner import ACCEPT_COOKIES
from config.shopping_list import (BILLECART_SALMON_BRUT_RESERVE, FREREJEAN_FRERES_BLANC_DE_BLANCS,
                                  KRUG_ROSE_20TH_EDITION_MAGNUM, POL_COURONNE_BRUT)

if __name__ == "__main__":
    with Browser() as browser:
        browser.open.url("https://www.honestgrapes.co.uk/")
        browser.combo.cookie_banner(ACCEPT_COOKIES)
        browser.add_to_cart(20, POL_COURONNE_BRUT)
        browser.add_to_cart(10, FREREJEAN_FRERES_BLANC_DE_BLANCS)
        browser.add_to_cart(20, BILLECART_SALMON_BRUT_RESERVE)
        browser.add_to_cart(20, KRUG_ROSE_20TH_EDITION_MAGNUM)
        browser.check_out()
