import unittest
from selenium import webdriver


class TestOpenSQLTutorial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/')
        self.driver.maximize_window()

    def test_open_sql_tutorial_from_top_nav_bar(self):
        tutorials_menu = self.driver.find_element_by_css_selector('body > div:nth-child(5) > a:nth-child(2)')
        tutorials_menu.click()
        sql_tutorial_button = self.driver.find_element_by_css_selector('#nav_tutorials div:nth-child(3) > a:nth-child(2)')
        sql_tutorial_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def test_open_sql_tutorial_from_left_nav_bar(self):
        sql_tutorial_button = self.driver.find_element_by_css_selector('div.w3-bar-block > a:nth-child(20)')
        sql_tutorial_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
