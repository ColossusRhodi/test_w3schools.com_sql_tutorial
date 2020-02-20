import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
from test_data import titles, urls


class TestNavigationInSQLTutorial(unittest.TestCase):
    """Test case.

    Current test case checks opening SQL example pages.
    Method 'setUp' contains preconditions for each test.
    Method 'test_navigation_first_next_button' checks if open page is correct while forward navigation.
    Method 'test_navigation_second_next_button' checks if open page is correct while forward navigation.
    Method 'test_navigation_first_previous_button' checks if open page is correct while back navigation.
    Method 'test_navigation_second_previous_button' checks if open page is correct while back navigation.
    Method 'test_navigation_left_nav_bar' checks if open page is correct while navigation from main page.
    Method 'tearDown' contains postconditions for each test.

    @parameterized.expand() transfers test data to each test.
    It takes a list of lists or tuples or tuple of lists or tuples with test data.
    @parameterized.expand(('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    or
    test_data = (('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    @parameterized.expand(test_data)

    All tests take two arguments 'url' and 'title' those go from @parameterized.expand() modul.
    'url' argument must be a list or tuple with one string test data.
    'title' argument must be a list or tuple with one string test data.
    test_start_sql_exercises_with_answer(self, 'https://url.com/', 'SQL Tutorial')

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    # Prepare test data for test.
    test_data_next_buttons = []
    for url in urls:
        index = urls.index(url)
        test_data_next_buttons.append((url, titles[1:][index]))

    # Pass test data to test.
    @parameterized.expand(test_data_next_buttons)
    def test_navigation_first_next_button(self, url, title):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Go through SQL tutorial by clicking on the first "Next" button.
        next_buttons = self.driver.find_elements_by_css_selector('div.w3-clear.nextprev > a.w3-right.w3-btn')
        next_buttons[0].click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page title from test data and current page.
        self.assertEqual(title, page_title)

    # Pass test data to test.
    @parameterized.expand(test_data_next_buttons)
    def test_navigation_second_next_button(self, url, title):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Go through SQL tutorial by clicking on the second "Next" button.
        next_buttons = self.driver.find_elements_by_css_selector('div.w3-clear.nextprev > a.w3-right.w3-btn')
        next_buttons[1].click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page title from test data and current page.
        self.assertEqual(title, page_title)

    # Prepare test data for test.
    test_data_previous_buttons = []
    for title in titles[:-2]:
        index = titles[:-2].index(title)
        test_data_previous_buttons.append((urls[1:][index], title))

    # Pass test data to test.
    @parameterized.expand(test_data_previous_buttons)
    def test_navigation_first_previous_button(self, url, title):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Go through SQL tutorial by clicking on the first "Previous" button.
        previous_buttons = self.driver.find_elements_by_css_selector('div.w3-clear.nextprev > a.w3-left.w3-btn')
        previous_buttons[0].click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page title from test data and current page.
        self.assertEqual(title, page_title)

    # Pass test data to test.
    @parameterized.expand(test_data_previous_buttons)
    def test_navigation_second_previous_button(self, url, title):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Go through SQL tutorial by clicking on the second "Previous" button.
        previous_buttons = self.driver.find_element_by_css_selector('div.w3-clear.nextprev > a.w3-left.w3-btn')
        previous_buttons[1].click()

        # Get page title from current page.
        page_title = self.driver.title

        # Validate if open page is correct by comparing page title from test data and current page.
        self.assertEqual(title, page_title)

    # Prepare test data for test.
    test_data_left_nav_bar = []
    for url in urls:
        test_data_left_nav_bar.append((url, titles[:-1]))

    # Pass test data to test.
    @parameterized.expand(test_data_left_nav_bar)
    def test_navigation_left_nav_bar(self, url, title):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Remember a main browser tab.
        main_window = self.driver.current_window_handle

        # Go through SQL tutorial by clicking on links in left navigation menu.
        nav_bar_buttons = self.driver.find_elements_by_css_selector('#leftmenuinnerinner > a')[:37]
        for button in nav_bar_buttons:
            index = nav_bar_buttons.index(button)
            button.send_keys(Keys.CONTROL + Keys.RETURN)
            self.driver.switch_to.window(self.driver.window_handles[1])

            # Get page title from current page.
            page_title = self.driver.title

            # Validate if open page is correct by comparing page title from test data and current page.
            self.assertEqual(title[index], page_title)

            # Close current page and switch to the main browser tab.
            self.driver.close()
            self.driver.switch_to.window(window_name=main_window)

    def tearDown(self):
        # End the session.
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
