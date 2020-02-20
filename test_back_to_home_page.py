import unittest
from selenium import webdriver
from parameterized import parameterized
from test_data import urls


class TestBackToHomePageFirstPage(unittest.TestCase):
    """Test case.

    Current test case checks if app goes back to home page from first page in SQL tutorial.
    Method 'setUp' contains preconditions for each test.
    Method 'test_back_to_home_page_first_home_button' checks if app goes back to home page use the first "Home" button.
    Method 'test_back_to_home_page_second_home_button' checks if app goes back to home page use the second "Home" button.
    Method 'tearDown' contains postconditions for each test.

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/sql/default.asp')
        self.driver.maximize_window()

    def test_back_to_home_page_first_home_button(self):
        # Go back to home page.
        home_button = self.driver.find_element_by_css_selector('#main > div:nth-child(3) > a.w3-left.w3-btn')
        home_button.click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page test data title and current page title.
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def test_back_to_home_page_second_home_button(self):
        # Go back to home page.
        home_button = self.driver.find_element_by_css_selector('#main > div:nth-child(50) > a.w3-left.w3-btn')
        home_button.click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page test data title and current page title.
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def tearDown(self):
        # End the session.
        self.driver.quit()


class TestBackToHomePageOtherPages(unittest.TestCase):
    """Test case.

    Current test case checks opening SQL example pages.
    Method 'setUp' contains preconditions for each test.
    Method 'test_back_to_home_page_w3schools_button' checks if app goes back to home page use "w3schools" link in all pages.
    Method 'test_back_to_home_page_drawn_house_button' checks if app goes back to home page use "Drawn house" button in all pages.
    Method 'tearDown' contains postconditions for each test.

    @parameterized.expand() transfers test data to each test.
    It takes a list of lists or tuples or tuple of lists or tuples with test data.
    @parameterized.expand(('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    or
    test_data = (('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    @parameterized.expand(test_data)

    All tests take one argument 'url' this go from @parameterized.expand() modul.
    'url' argument must be a list or tuple with one string test data.
    test_start_sql_exercises_with_answer(self, 'https://url.com/')

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    # Prepare test data for test.
    test_data = []
    for url in urls:
        test_data.append((url,))

    # Pass test data to test.
    @parameterized.expand(test_data)
    def test_back_to_home_page_w3schools_button(self, url):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Go back to home page.
        w3schools_button = self.driver.find_element_by_css_selector('div.w3-container.top > a')
        w3schools_button.click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page test data title and current page title.
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    @parameterized.expand(test_data)
    def test_back_to_home_page_drawn_house_button(self, url):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Go back to home page.
        drawn_house_button = self.driver.find_element_by_css_selector('a[title="Home"]')
        drawn_house_button.click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page test data title and current page title.
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def tearDown(self):
        # End the session.
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
