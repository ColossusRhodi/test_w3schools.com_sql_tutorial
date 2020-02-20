import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
from test_data import urls, answers


class TestOpenSQLExercises(unittest.TestCase):
    """Test case.

    Current test case checks opening SQL exercise pages.
    Method 'setUp' contains preconditions for each test.
    Method 'test_open_sql_exercises' checks the firts button to open page with SQL exercises from SQL lesson page.
    Method 'test_start_sql_exercises' checks the second button to open page with SQL exercises from SQL lesson page.
    Method  'test_start_sql_exercises_with_answer' checks if input information by user gose to SQL exercise page from SQL lesson page.
    Method 'tearDown' contains postconditions for each test.

    @parameterized.expand() transfers test data to each test.
    It takes a list of lists or tuples or tuple of lists or tuples with test data.
    @parameterized.expand(('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    or
    test_data = (('test data',), ('test data 1', 'test data 2' ... 'test data n'))
    @parameterized.expand(test_data)

    test_open_sql_exercises(self, url) and test_start_sql_exercises(self, url) take argument 'url' that goes from @parameterized.expand() modul.
    This argument must be a list or tuple with one string test data.
    test_open_sql_exercises(self, 'https://url.com/')

    test_start_sql_exercises_with_answer(self, url, *answer) takes takes two argument 'url' and '*answer' those go from @parameterized.expand() modul.
    'url' argument must be a list or tuple with one string test data.
    '*answer' argument must be a list or tuple with one or more test data.
    test_start_sql_exercises_with_answer(self, url, ('test data',), ('test data 1', 'test data 2' ... 'test data n'))

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    # Prepare test data for tests.
    test_data = []
    for url in urls:
        test_data.append((url,))

    # Pass test data to test.
    @parameterized.expand(test_data)
    def test_open_sql_exercises(self, url):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Get SQL query statement from lesson page.
        sql_query_statement = self.driver.find_element_by_css_selector('div.exercisewindow pre').text

        # Open exercise page.
        start_exercise = self.driver.find_element_by_css_selector('div.exercisewindow a')
        start_exercise.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Get SQL query statement from exercise page.
        sql_query_statement_to_validate = self.driver.find_element_by_css_selector('#assignmentcontainer').text

        # Validate if open page is correct by comparing SQL query statements from lesson page and exercise page.
        self.assertEqual(sql_query_statement, sql_query_statement_to_validate.replace('\n', ''))

    # Pass test data to test.
    @parameterized.expand(test_data)
    def test_start_sql_exercises(self, url):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Get SQL query statement from lesson page.
        sql_query_statement = self.driver.find_element_by_css_selector('div.exercisewindow pre').text

        # Open exercise page.
        submit_answer = self.driver.find_element_by_css_selector('div.exercisewindow button')
        submit_answer.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Get SQL query statement from exercise page.
        sql_query_statement_to_validate = self.driver.find_element_by_css_selector('#assignmentcontainer').text

        # Validate if open page is correct by comparing SQL query statements from lesson page and exercise page.
        self.assertEqual(sql_query_statement, sql_query_statement_to_validate.replace('\n', ''))

    # Prepare test data for test.
    urls_sql_exercises_with_answer = []
    urls_sql_exercises_with_answer.append(urls[0])
    urls_sql_exercises_with_answer.extend(urls[3:12])
    urls_sql_exercises_with_answer.append(urls[13])
    urls_sql_exercises_with_answer.extend(urls[14:22])
    urls_sql_exercises_with_answer.append(urls[23])
    urls_sql_exercises_with_answer.append(urls[27])

    test_data = []
    for answer in answers:
        index = answers.index(answer)
        temporary_list = []
        temporary_list.append(urls_sql_exercises_with_answer[index])
        for word in answer:
            temporary_list.append(word)
        test_data.append(temporary_list)

    # Pass test data to test.
    @parameterized.expand(test_data)
    def test_start_sql_exercises_with_answer(self, url, *answer):
        # Open url in browser.
        self.driver.get(url)
        self.driver.maximize_window()

        # Find input fields and send arguments.
        input_answer = self.driver.find_elements_by_css_selector('div.exercisewindow input')
        for field in input_answer:
            index = input_answer.index(field)
            field.send_keys(answer[index])

        # Open exercise page.
        submit_answer = self.driver.find_element_by_css_selector('div.exercisewindow button')
        submit_answer.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Validate if open page is correct by pressing on Submit Answer button.
        submit_answer = self.driver.find_element_by_css_selector('#answerbutton')
        submit_answer.click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div#assignmentCorrect[style="display: block;"]'))))

    def tearDown(self):
        # End the session.
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
