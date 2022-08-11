import random

from selenium.webdriver.common.by import By


from unilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    __page_title = (By.XPATH, '//button[@aria-label= "Back to homepage"]/span[@class="mat-button-wrapper"]/span')
    __pagination_dropdown = (By.XPATH, "//mat-select[@role='combobox']")
    __product = (By.CSS_SELECTOR, "mat-card")
    __product_name = (By.CSS_SELECTOR, "[class='item-name']")
    __dismiss_button = (By.XPATH, "//*[text()='Dismiss']")
    __language_button = (By.XPATH, "//button[@aria-label='Language selection menu']")
    __language_radio_button = (By.XPATH, "//span[@class='mat-radio-label-content']/div")
    __items_header = (By.XPATH, "//app-search-result/div/div/div/div[@class='ng-star-inserted']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.__page_title)

    def get_pagination_value(self):
        return self.get_text(self.__pagination_dropdown)

    def get_products_quantity(self):
        return len(self.wait_for_elements_located(self.__product))

    def click_dismiss_button(self):
        self.click(self.__dismiss_button)

    def select_language(self, language):
        self.click(self.__language_button)
        self.select_from_menu_content(language, self.__language_radio_button)

    def get_items_header(self):
        return self.get_text(self.__items_header)

    def choose_random_product(self):
        products = self.wait_for_elements_located(self.__product_name)
        random_product = random.choice(products)
        return random_product.text

