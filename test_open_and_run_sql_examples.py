import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
from test_data import sql_query_examples


class TestOpenSQLExamples(unittest.TestCase):
    """Test case.

    Current test case checks opening SQL example pages.
    Method 'setUp' contains preconditions for each test.
    Method 'test_open_examples' checks if open page with SQL example is correct.
    Method 'tearDown' contains postconditions for each test.

    @parameterized.expand() transfers test data to each test.
    It takes a list of lists or tuples or tuple of lists or tuples with test data.
    @parameterized.expand(('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    or
    test_data = (('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    @parameterized.expand(test_data)

    test_open_examples(self, sql_query_example, url) takes takes two arguments 'sql_query_example' and 'url' those go from @parameterized.expand() modul.
    'sql_query_example' argument must be a list or tuple with one string test data.
    'url' argument must be a list or tuple with one string test data.
    test_start_sql_exercises_with_answer(self, 'SELECT * FROM Customers;','https://url.com/')

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    # Prepare test data for test.
    test_data = sql_query_examples

    # Pass test data to test.
    @parameterized.expand(test_data)
    def test_open_examples(self, sql_query_example, url):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Get all SQL query examples on a page and compare if it's into test data.
        sql_query_examples = self.driver.find_elements_by_css_selector('div.w3-example')
        for text in sql_query_examples:
            if sql_query_example in text.text:
                # Open example page.
                try_it_yourself_button = text.find_element_by_css_selector('a')
                try_it_yourself_button.send_keys(Keys.CONTROL + Keys.RETURN)
                self.driver.switch_to.window(self.driver.window_handles[1])

                # Validate if open page is correct by comparing SQL query example from test data and example page.
                sql_query_example_to_validate = self.driver.find_element_by_css_selector('div.CodeMirror-code').text
                self.assertEqual(sql_query_example, sql_query_example_to_validate.rstrip())
                break

    def tearDown(self):
        # End the session.
        self.driver.quit()


class TestRunSQLExamples(unittest.TestCase):
    """Test case.

    Current test case checks opening SQL example pages.
    Method 'setUp' contains preconditions for each test.
    Method 'test_run__examples' checks if run SQL example.
    Method 'tearDown' contains postconditions for each test.

    @parameterized.expand() transfers test data to each test.
    It takes a list of lists or tuples or tuple of lists or tuples with test data.
    @parameterized.expand(('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    or
    test_data = (('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    @parameterized.expand(test_data)

    test_run_examples(self, sql_query_example, url) takes takes two argument 'sql_query_example' and 'url' those go from @parameterized.expand() modul.
    'sql_query_example' argument must be a list or tuple with one string test data.
    'url' argument must be a list or tuple with one string test data.
    test_start_sql_exercises_with_answer(self, 'SELECT * FROM Customers;','https://url.com/')

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    # Prepare test data for test.
    test_data = sql_query_examples

    # Pass test data to test.
    @parameterized.expand(test_data)
    def test_run_examples(self, sql_query_example, url):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Get all SQL query examples on a page and compare if it's into test data.
        sql_query_examples = self.driver.find_elements_by_css_selector('div.w3-example')
        for text in sql_query_examples:
            if sql_query_example in text.text:
                # Open example page.
                try_it_yourself_button = text.find_element_by_css_selector('a')
                try_it_yourself_button.send_keys(Keys.CONTROL + Keys.RETURN)
                self.driver.switch_to.window(self.driver.window_handles[1])

                # Run SQL query example.
                run_sql_button = self.driver.find_element_by_css_selector('button.w3-green.w3-btn')
                run_sql_button.click()

                # Validate if current function is work by appear a table with data from database.
                self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#divResultSQL table'))))
                break

    def tearDown(self):
        # End the session.
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
