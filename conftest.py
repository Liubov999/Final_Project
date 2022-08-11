import pytest

from page_objects.main_page import MainPage
from unilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_driver):
    driver = create_driver
    driver.get('http://localhost:3000/')
    main_page = MainPage(driver)
    main_page.click_dismiss_button()
    return main_page
