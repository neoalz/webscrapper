from selenium import webdriver
import platform
import urllib3

chrome_driver_path_windows = '.\\src\\Driver\\chromedriverwindows.exe'
chrome_driver_path_linux = './src/Driver/chromedriverlinux'


class WebDriverSetup:
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if 'Windows' == platform.system():
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path_windows)
        else:
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path_linux)

    def setUp(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
