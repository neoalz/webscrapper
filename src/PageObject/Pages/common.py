from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.Driver.WebDriverSetup import WebDriverSetup
from src.db import postgresql
table_name = "scrapper_results"

class CommonPage:

    def __init__(self):
        self.driver = WebDriverSetup().driver

    def wait_presence(self, time, locator):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located(locator)
            )
        except:
            print('element with selector '+str(locator)+' not found')
            # self.tearDown()

    def get_element(self, locator, wait=5):
        self.wait_presence(wait, locator)
        return self.driver.find_element(locator[0],locator[1])

    def get_elements(self, locator, wait=5):
        self.wait_presence(wait, locator)
        return self.driver.find_elements(locator[0],locator[1])

    def wait_until_load(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def insert_to_database(products):
        postgresql.insert_values(table_name, products)