from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_elements_located(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def get_text(self, locator):
        element = self.wait_for_element_located(locator)
        return element.text

    def click(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def select_from_menu_content(self, value, locator):
        elements = self.wait_for_elements_located(locator)
        for element in elements:
            if element.text.strip() == value:
                element.click()
                break


            # if element.get_attribute('aria-label') == value:
            #     element.click()
            #     break
