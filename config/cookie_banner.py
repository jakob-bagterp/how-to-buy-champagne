from browserist import CookieBannerSettings

from .url import URL_HONEST_GRAPES_CO_UK

ACCEPT_COOKIES = CookieBannerSettings(
    button_xpath="//button[@id='btn-cookie-allow']",
    url=URL_HONEST_GRAPES_CO_UK
)
