import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = "https://www.staples.ca/collections/brother-ink-toner-8"


class StaplesProducts:
    closePromptXpath: str

    def __init__(self, driver):
        self.driver = driver
        self.itemClass = "ais-hits--item"
        self.itemTitleClass = "product-thumbnail__title"
        self.itemPriceClass = "money"
        self.nextPageText = "›"
        self.promptClass = "Modal__Header"
        self.closePromptClass = "icon--close"
        self.closePromptXpath = '//*[@id="bold-welcome-modal"]/div/div/header/div/span[2]'
        self.closePromptFullXpath = '/html/body/div[7]/div/div/header/div/span[2]'
        self.modalClosed = False

        # scheduled_works: site_captures_id date_time status_scheduled created_at updated_at
        # scrapper_results: site_captures_id sheduled_works_id brand glosa url price sale created_at updated_at scheduled_works_id site_captures_id
        # site_captures: name description url_site statu_size created_at updated_at

    def get_products_names(self):
        return self.productsNames

    def get_products_skus(self):
        return self.productsSKUs

    def get_products_prices(self):
        return self.productsPrices

    def get_items(self):
        self.wait_presence_by_class(5, self.itemClass)
        return self.driver.find_elements(By.CLASS_NAME, self.itemClass)

    def get_values_from_page(self, brand):
        parents = self.get_items()
        print("Reading page values...")
        pageurl = self.driver.current_url
        products = list()
        for parent in parents:
            title = parent.find_element(By.CLASS_NAME, self.itemTitleClass)
            price = parent.find_element(By.CLASS_NAME, self.itemPriceClass)
            url = title.get_attribute("href").removeprefix("https://www.staples.ca/products/")
            sale = None
            sku = url[0:url.index('-')]
            products.append((brand, title.text, pageurl, sku, price.text, sale))
        return products

    # def get_all_products(self, brand):
    #     canGoNextPage = True
    #     while canGoNextPage:
    #         self.wait_until_load()
    #         self.get_values_from_page(brand)
    #         canGoNextPage = self.click_next_page()

    def get_next_page(self):
        return self.driver.find_element(By.LINK_TEXT, self.nextPageText)

    def click_next_page(self):
        self.close_prompt()
        try:
            if self.get_next_page().is_displayed():
                self.get_next_page().click()
                print("Next page...")
                time.sleep(2)
                return True
            else:
                print("Last page...")
                return False
        except NoSuchElementException:
            print("Last page...")
            return False

    def wait_until_load(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def get_close_prompt(self):
        return self.driver.find_element(By.CLASS_NAME, self.closePromptClass)

    def close_prompt(self):
        if not self.modalClosed:
            self.driver.implicitly_wait(5)
            if self.driver.find_element(By.XPATH, self.closePromptXpath).is_displayed():
                self.driver.find_element(By.XPATH, self.closePromptXpath).click()
                self.modalClosed = True

    def wait_presence_by_class(self, time, locator):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, locator))
            )
        except:
            print("Element " + locator + " Not Found")

    def wait_element_clickeable_by_class(self, time, locator):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME, locator))
            )
        except:
            print("Element " + locator + " Was Not Clickeable")

    def wait_element_clickeable_by_class(self, time, locator):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.element_to_be_clickable((By.LINK_TEXT, locator))
            )
        except:
            print("Element " + locator + " Was Not Clickeable")

    def wait_presence_by_link_text(self, time, locator):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located((By.LINK_TEXT, locator))
            )
        except:
            print("Element " + locator + " Not Found")

    @staticmethod
    def get_base_url():
        return base_url
