from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id, is_headless=False):
        if DriverFactory.CHROME == driver_id:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
             #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        return driver