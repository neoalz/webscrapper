import time
from src.Driver.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.staples.StaplesIndex import StaplesIndex
from src.PageObject.Pages.staples.StaplesProducts import StaplesProducts
from src.db import postgresql


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
        self.productsPage.get_all_products()

    def get_canon_products(self):
        print("Going for Canon products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_canon()
        self.productsPage.get_all_products()

    def get_samsung_products(self):
        print("Going for Samsung products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_samsung()
        self.productsPage.get_all_products()

    def get_epson_products(self):
        print("Going for Epson products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_epson()
        self.productsPage.get_all_products()

    def get_staples_products(self):
        print("Going for Staples products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_staples()
        self.productsPage.get_all_products()

    def get_fuzion_products(self):
        print("Going for Fuzion products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_fuzion()
        self.productsPage.get_all_products()

    def get_xerox_products(self):
        print("Going for Xerox products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_xerox()
        self.productsPage.get_all_products()

    def get_hp_products(self):
        print("Going for HP products")
        self.driver.setUp(StaplesIndex.get_base_url())
        self.indexPage.go_hp()
        self.productsPage.get_all_products()

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
        tableName = 'products'
        self.create_table(tableName)
        while canGoNextPage:
            self.productsPage.wait_until_load()
            products = self.productsPage.get_values_from_page(brand)
            self.insert_to_database(products)
            canGoNextPage = self.productsPage.click_next_page()

    def insert_to_database(self, products):
        postgresql.insert_values("products", products)

    def create_table(self, name):
        postgresql.create_table(name)
