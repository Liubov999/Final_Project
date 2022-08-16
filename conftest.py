import pytest

from pythonProject.Final_Project_Juice.page_objects.main_page import MainPage
from pythonProject.Final_Project_Juice.utilities.driver_factory import DriverFactory


@pytest.fixture
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(create_driver):
    driver = create_driver
    driver.get('https://juiceshopppppppppppppppppppppp.herokuapp.com/')
    main_page = MainPage(driver)
    main_page.click_dismiss_button()
    return main_page


@pytest.fixture()
def open_login_page(open_main_page):
    return open_main_page.open_login_page()
