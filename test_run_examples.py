import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class TestRunSQLExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/sql/default.asp')
        self.driver.maximize_window()

    def test_run_examples(self):
        main_window = self.driver.current_window_handle

        try_it_yourself_button = self.driver.find_element_by_css_selector('#main > div.w3-example > a')
        try_it_yourself_button.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        page_title = self.driver.find_element_by_css_selector('#tryitform > h3')
        self.assertEqual("SQL Statement:", page_title.text)
        run_sql_button = self.driver.find_element_by_css_selector('button.w3-green.w3-btn')
        run_sql_button.click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#divResultSQL table'))))
        self.driver.close()

        self.driver.switch_to.window(window_name=main_window)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
