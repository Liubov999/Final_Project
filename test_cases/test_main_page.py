def test_check_title(open_main_page):
    """
    @test description: Test verifies that page title is correct
    @test steps:
        1. Open main Page.
        2. Verify page title.
    @expected: main page title >>>
    """
    home_page = open_main_page
    home_page_title = home_page.get_page_title()
    assert home_page_title == 'OWASP Juice Shop', f'Expected: OWASP Juice Shop \n Actual: {home_page_title}'


def test_check_default_item_per_page(open_main_page):
    """
    @test description: Test verifies default elements quantity per pager
    @test steps:
        1. Open main page
        2. Observe "Items per page" drowpdown value
        3. Observe number of Juices on page
    @expected:
        1. "Items per page" drowpdown value is 12
        2. Number of Juices on page is 12
    """
    home_page = open_main_page
    pagination_value = home_page.get_pagination_value()
    assert pagination_value == '12', f"\nActual: {pagination_value}\nExpected: 12"
    products_count = home_page.get_products_quantity()
    assert products_count == int(pagination_value), f"\nActual: {products_count}\nExpected: {pagination_value}"


def test_verify_language_change(open_main_page):
    """
    @test description: test verifies that language can be changed
    @test steps:
        1. open main page
        2. select German language from dropdown
        3. observe items header
    @expected:
        1. items header is "Alle Produkte"
    """
    home_page = open_main_page
    home_page.select_language('Deutsch')
    actual_text = home_page.get_items_header()
    assert actual_text == "Alle Produkte"


def test_verify_searching(open_main_page):
    """
    @test description: test verifies searching
    @test steps:
        1. open main page
        2. get random available product from main page
        3. search for product
        4. search for partial name product
        5. search for incorrect product
    @expected:
        1. search result page contains one product
        2. search resutl page displays "No results found"
        3. search resutl page displays "Try adjusting your search to find what you're looking for."
    """
    home_page = open_main_page
    product = home_page.choose_random_product()
    # 'Only 1 left\nBest Juice Shop Salesman Artwork\n5000¤'


def test_open_login_page(open_main_page):
    """
    @test description: test verifies that login page can be opened
    @test steps:
        1. open main page
        2. click "Account" button
        3. click "Login" button
    @expected:
        1. user redirected to Login page

    """
