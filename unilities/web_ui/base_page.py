from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))



    def get_text(self, locator):
        element = self.wait_for_element_located(locator)
        return element.text

