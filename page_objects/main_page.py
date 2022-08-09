from selenium.webdriver.common.by import By


from unilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    __page_title = (By.XPATH, '//button[@aria-label= "Back to homepage"]/span[@class="mat-button-wrapper"]/span')

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.__page_title)