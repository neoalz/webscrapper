from selenium import webdriver
import urllib3

chrome_driver_path = '.\\src\\Driver\\chromedriver.exe'

class WebDriverSetup():
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def setUp(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
