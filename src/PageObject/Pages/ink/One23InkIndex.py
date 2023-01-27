import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from src.PageObject.Pages.common import Common

base_url = "https://www.123ink.ca/"


class One23InkIndex(Common):
    def __init__(self,driver):
        self.driver = driver
        self.ink_cartridges_selector = (By.XPATH, "//ul[@class='display-flex']/li[2]/a")
        self.hp_ink_cartridges_selector = (By.XPATH, "//ul/li/a[@title='HP Ink Cartridges']")
        self.item_product_selector = (By.XPATH, "//a[@class='product_item_track product-title']")
        self.product_prices_selector = (By.XPATH, "//div[@class='product-list-price']")
        self.sale_price_selector = (By.XPATH, "//span[@class='price']")
        self.original_price_selector = (By.XPATH, "//span[@class='market-price former-price']")
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
    def get_products_prices(self):
        return self.get_elements(self.product_prices_selector)
    def get_original_prices(self):
        return self.get_elements(self.original_price_selector)

    def get_sales_prices(self):
        return self.get_elements(self.sale_price_selector)
    @staticmethod
    def get_base_url():
        return base_url
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
        precios_productos = iter(self.get_products_prices())
        # precios_original = iter(self.get_original_prices())
        # precios_ofertas = iter(self.get_sales_prices())
        print("Reading page values...")
        products = list()
        for name in names:
            title = name.text
            product_prices = next(precios_productos).text.split("\n")
            # print(str(product_prices[0]))
            # print(str(product_prices[1]))
            price_text = str(product_prices[0])
            if len(product_prices)==2:
                sale = str(product_prices[1])
            else :
                sale = ''
            url = name.get_attribute("href")
            created_at = time.strftime("%Y_%m_%d_%H%M%S", time.gmtime())  # YYYY_mm_dd_HHMMSS
            updated_at = time.strftime("%Y_%m_%d_%H%M%S", time.gmtime())  # 2019_08_24_111757
            temp = url.removeprefix("https://www.123ink.ca/p-")
            sku = temp[0:temp.index('-')]
            # sku = temp[temp.index('sku')]
            products.append(
                (brand, title, url, price_text.replace('$', ''), sale.replace('$', ''), created_at, updated_at, sku))
        return products



