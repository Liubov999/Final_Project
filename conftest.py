import pytest

from page_objects.main_page import MainPage
from unilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_driver):
    driver = create_driver
    driver.get('http://localhost:3000/')
    return MainPage(driver)

