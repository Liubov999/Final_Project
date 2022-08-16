from selenium.webdriver.common.by import By
import random

from selenium.webdriver.common.keys import Keys

from pythonProject.Final_Project_Juice.page_objects.login_page import LoginPage
from pythonProject.Final_Project_Juice.utilities.web_ua.base_page import BasePage


class MainPage(BasePage):
    __page_title = (By.XPATH, '//button[@aria-label= "Back to homepage"]/span[@class="mat-button-wrapper"]/span')
    __pagination_dropdown = (By.XPATH, "//mat-select[@role='combobox']")
    __product = (By.CSS_SELECTOR, "mat-card")
    __product_name = (By.CSS_SELECTOR, "[class='item-name']")
    __dismiss_button = (By.XPATH, "//*[text()='Dismiss']")
    __language_button = (By.XPATH, "//button[@aria-label='Language selection menu']")
    __language_radio_button = (By.XPATH, "//span[@class='mat-radio-label-content']/div")
    __items_header = (By.XPATH, "//app-search-result/div/div/div/div[@class='ng-star-inserted']")
    __search_icon = (By.XPATH, "//mat-icon[text() = ' search ']")
    __search_field = (By.XPATH, "//input[@type='text']")
    __search_result = (By.XPATH, "//div[@class='ng-star-inserted']")
    __not_found_search_result = (By.XPATH, "//span[@class = 'noResultText']")
    __account_button = (By.XPATH, "//button[@id = 'navbarAccount']")
    __login_button = (By.XPATH, "//button[@id = 'navbarLoginButton']")
    __test_locator = (By.XPATH, 'blablabla')

    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

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

    def click_search_icon(self):
        self.click(self.__search_icon)

    def search_existing_product(self, existing_product):
        return self.send_keys(self.__search_field, existing_product)

    def get_search_value(self):
        return self.get_text(self.__search_result)

    def get_not_found_search_value(self):
        return self.get_text(self.__not_found_search_result)

    def open_login_page(self):
        self.click(self.__account_button)
        self.click(self.__login_button)
        return LoginPage(self.driver)