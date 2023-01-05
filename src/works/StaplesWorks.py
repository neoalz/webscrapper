import time
from src.Driver.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.staples.StaplesIndex import StaplesIndex
from src.PageObject.Pages.staples.StaplesProducts import StaplesProducts
from src.db import postgresql

table_name = "scrapper_results"


def insert_to_database(products):
    postgresql.insert_values(table_name, products)


def create_table():
    postgresql.create_table(table_name)


class StaplesWorks:

    def __init__(self):
        self.driver = WebDriverSetup()
        self.indexPage = StaplesIndex(self.driver.driver)
        self.productsPage = StaplesProducts(self.driver.driver)

    def get_brother_products(self):
        print("Going for Brother products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_brother()
        self.get_all_products("BROTHER")

    def get_lexmark_products(self):
        print("Going for Lexmark products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_lexmark()
        self.get_all_products("LEXMARK")

    def get_canon_products(self):
        print("Going for Canon products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_canon()
        self.get_all_products("CANON")

    def get_samsung_products(self):
        print("Going for Samsung products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_samsung()
        self.get_all_products("SAMSUNG")

    def get_epson_products(self):
        print("Going for Epson products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_epson()
        self.get_all_products("EPSON")

    def get_staples_products(self):
        print("Going for Staples products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_staples()
        self.get_all_products("STAPLES")

    def get_fuzion_products(self):
        print("Going for Fuzion products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_fuzion()
        self.get_all_products("FUZION")

    def get_xerox_products(self):
        print("Going for Xerox products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_xerox()
        self.get_all_products("XEROX")

    def get_hp_products(self):
        print("Going for HP products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_hp()
        self.get_all_products("HP")

    def present_values(self):
        productsNames = self.productsPage.get_products_names()
        productsSkus = iter(self.productsPage.get_products_skus())
        productsPrices = iter(self.productsPage.get_products_prices())
        total = 0
        for i, prod in enumerate(productsNames):
            productName = "Product: " + prod
            productSku = "| SKU: " + next(productsSkus)
            productPrice = " | Price: " + next(productsPrices)
            print(productName + productSku + productPrice)
            total = i + 1
        print("Total products captured: " + str(total))

    def get_all_products(self, brand):
        canGoNextPage = True
        # create_table()
        while canGoNextPage:
            self.productsPage.wait_until_load()
            products = self.productsPage.get_values_from_page(brand)
            insert_to_database(products)
            canGoNextPage = self.productsPage.click_next_page()
