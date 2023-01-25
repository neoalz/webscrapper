import time
from src.Driver.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.ink.One23InkIndex import One23InkIndex
from src.db import postgresql


class One23InkWorks:

    def __init__(self):
        self.driver = WebDriverSetup()
        self.indexPage = One23InkIndex(self.driver.driver)

    def go_to_hp(self):
        print("Go for ink")
        self.driver.setUp(self.indexPage.get_base_url())
        self.indexPage.ink_hover()
        self.indexPage.click_hp_cartridges()
        time.sleep(5)

    def get_all_products(self, brand):
        canGoNextPage = True
        # create_table()
        while canGoNextPage:
            self.indexPage.wait_until_load()
            products = self.indexPage.get_values_from_page(brand)
#           insert_to_database(products)
            self.present_values(products)
            canGoNextPage = self.indexPage.click_next_page()

    def present_values(self, products):
        total = 0
        for i, prod in enumerate(products):
            print(prod)
            total = i + 1
        print("Total products captured: " + str(total))
