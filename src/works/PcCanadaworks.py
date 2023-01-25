import time
from src.Driver.WebDriverSetup import WebDriverSetup
from src.db import postgresql
from src.PageObject.Pages.pccanada.PcCanadaIndex import PcCanada
table_name = "scrapper_results"


def insert_to_database(products):
    postgresql.insert_values(table_name, products)


def create_table():
    postgresql.create_table(table_name)


class PcCanadaWorks:

    def __init__(self):
        self.driver = WebDriverSetup()
        self.indexPage = PcCanada(self.driver.driver)

    def go_to_ink_toner(self):
        self.driver.setUp(PcCanada.get_base_url())
        self.indexPage.click_shop_product()
        self.indexPage.click_ink_toner()

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
