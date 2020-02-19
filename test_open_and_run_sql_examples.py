import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
from test_data import sql_query_examples


class TestOpenSQLExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    test_data = sql_query_examples

    @parameterized.expand(test_data)
    def test_open_examples(self, sql_query_example, url):
        self.driver.get(url)
        self.driver.maximize_window()
        sql_query_examples = self.driver.find_elements_by_css_selector('div.w3-example')
        for text in sql_query_examples:
            if sql_query_example in text.text:
                try_it_yourself_button = text.find_element_by_css_selector('a')
                try_it_yourself_button.send_keys(Keys.CONTROL + Keys.RETURN)
                self.driver.switch_to.window(self.driver.window_handles[1])
                sql_query_example_to_validate = self.driver.find_element_by_css_selector('div.CodeMirror-code').text
                self.assertEqual(sql_query_example, sql_query_example_to_validate.rstrip())
                break

    def tearDown(self):
        self.driver.quit()


class TestRunSQLExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    test_data = sql_query_examples

    @parameterized.expand(test_data)
    def test_run__examples(self, sql_query_example, url):
        self.driver.get(url)
        self.driver.maximize_window()
        sql_query_examples = self.driver.find_elements_by_css_selector('div.w3-example')
        for text in sql_query_examples:
            if sql_query_example in text.text:
                try_it_yourself_button = text.find_element_by_css_selector('a')
                try_it_yourself_button.send_keys(Keys.CONTROL + Keys.RETURN)
                self.driver.switch_to.window(self.driver.window_handles[1])
                run_sql_button = self.driver.find_element_by_css_selector('button.w3-green.w3-btn')
                run_sql_button.click()
                self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#divResultSQL table'))))
                break

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
