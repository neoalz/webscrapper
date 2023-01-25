import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

base_url = "https://www.pc-canada.com/"

class PcCanada:
    def __init__(self, driver):
        self.driver = driver
        self.promptClass = "//*[@id=\"navbarNav\"]/ul/li[3]/a"
        self.shopproductsselecctor = (By.LINK_TEXT,"Shop Products")
        self.ink_toner =(By.LINK_TEXT,"Ink & Toner")

    def wait_presence(self, time, locator):
        try:
            WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located(locator)
            )
        except:
            self.driver.tearDown()

    def get_element(self, locator):
        self.wait_presence(100,locator)
        return self.driver.find_element(locator)

    def click_shop_product(self):
        self.get_element(self.shopproductsselecctor).click()
        # self.driver.implicitly_wait(1)

    def click_ink_toner(self):
        self.get_element(self.ink_toner).click()
        # self.driver.implicitly_wait(1)


    def wait_prompt(self):
        self.wait_presence_by_class(15,self.promptClass)
        self.close_prompt()
        self.driver.implicitly_wait(1)

    def close_prompt(self):
        self.driver.find_element(By.CLASS_NAME, self.closePromptClass).click()

    def click_shop(self):
        self.get_shop().click()
        # self.driver.implicitly_wait(1)

    def get_brother(self):
        self.wait_presence_by_link_text(5,self.brotherLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.brotherLinkText)

    def click_brother(self):
        self.get_brother().click()

    def go_brother(self):
        self.click_shop()
        self.click_brother()

    def get_lexmark(self):
        self.wait_presence_by_link_text(5,self.LexmarkLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.LexmarkLinkText)

    def click_lexmark(self):
        self.get_lexmark().click()

    def go_lexmark(self):
        self.click_shop()
        self.click_lexmark()

    def get_canon(self):
        self.wait_presence_by_link_text(5,self.canonLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.canonLinkText)

    def click_canon(self):
        self.get_canon().click()

    def go_canon(self):
        self.click_shop()
        self.click_canon()

    def get_samsung(self):
        self.wait_presence_by_link_text(5,self.samsungLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.samsungLinkText)

    def click_samsung(self):
        self.get_samsung().click()

    def go_samsung(self):
        self.click_shop()
        self.click_samsung()

    def get_epson(self):
        self.wait_presence_by_link_text(5,self.epsonLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.epsonLinkText)

    def click_epson(self):
        self.get_epson().click()

    def go_epson(self):
        self.click_shop()
        self.click_epson()

    def get_staples(self):
        self.wait_presence_by_link_text(5,self.staplesLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.staplesLinkText)

    def click_staples(self):
        self.get_staples().click()

    def go_staples(self):
        self.click_shop()
        self.click_staples()

    def get_fuzion(self):
        self.wait_presence_by_link_text(5,self.fuzionLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.fuzionLinkText)

    def click_fuzion(self):
        self.get_fuzion().click()

    def go_fuzion(self):
        self.click_shop()
        self.click_fuzion()

    def get_xerox(self):
        self.wait_presence_by_link_text(5,self.xeroxLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.xeroxLinkText)

    def click_xerox(self):
        self.get_xerox().click()

    def go_xerox(self):
        self.click_shop()
        self.click_xerox()

    def get_hp(self):
        self.wait_presence_by_link_text(5,self.hpLinkText)
        return self.driver.find_element(By.LINK_TEXT, self.hpLinkText)

    def click_hp(self):
        self.get_hp().click()

    def go_hp(self):
        self.click_shop()
        self.click_hp()

    @staticmethod
    def get_base_url():
        return base_url
