import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.PageObject.Pages.common import CommonPage

base_url = "https://www.123ink.ca/"


class One23InkIndex(CommonPage):
    def __init__(self,driver):
        self.driver = driver
        self.ink_cartridges_selector = (By.XPATH, "//ul[@class='display-flex']/li[2]/a")
        self.hp_ink_cartridges_selector = (By.XPATH, "//ul/li/a[@title='HP Ink Cartridges']")
        self.item_product_selector = (By.XPATH, "//a[@class='product_item_track product-title']")
        self.Precio_Oferta_selector = (By.XPATH, "//span[@class='price']")
        self.Precio_Real_selector = (By.XPATH, "//span[@class='market-price former-price']")
        self.nextPageText = 1
    def ink_hover(self):
        a = ActionChains(self.driver)
        ink = self.get_element(self.ink_cartridges_selector,10)
        a.move_to_element(ink).perform()
        time.sleep(2)

    def click_hp_cartridges(self):
        self.get_element(self.hp_ink_cartridges_selector, 10).click()

    def get_names(self):
        return self.get_elements(self.item_product_selector)
    def get_precio_real(self):
        return self.get_elements(self.Precio_Real_selector)

    def get_precio_oferta(self):
        return self.get_elements(self.Precio_Oferta_selector)
    @staticmethod
    def get_base_url():
        return base_url
    def get_products_names(self):
        return self.productsNames

    def get_products_prices(self):
        return self.productsPrices
    def click_next_page(self):
        try:
            self.nextPageText = 1 + self.nextPageText
            locator = (By.LINK_TEXT, str(self.nextPageText))
            if self.get_element(locator).is_displayed():
                self.get_element(locator).click()
                print("Next page...")
                time.sleep(2)
                return True
            else:
                print("Last page...")
                return False
        except NoSuchElementException:
            print("Last page...")
            return False

    def get_values_from_page(self, brand):
        names = self.get_names()
        precios_original = iter(self.get_precio_real())
        precios_ofertas = iter(self.get_precio_oferta())
        print("Reading page values...")
        products = list()
        for name in names:
            title = name.text
            price_text = next(precios_original).text
            url = name.get_attribute("href")
            sale = next(precios_ofertas).text
            created_at = time.strftime("%Y_%m_%d_%H%M%S", time.gmtime())  # 2019_08_24_111757
            updated_at = time.strftime("%Y_%m_%d_%H%M%S", time.gmtime())  # 2019_08_24_111757
            temp = url.removeprefix("https://www.123ink.ca/p-")
            sku = temp[0:temp.index('-')]
            products.append(
                (brand, title, url, price_text.replace('$', ''), sale.replace('$', ''), created_at, updated_at, sku))
        return products

