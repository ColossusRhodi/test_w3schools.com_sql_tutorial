import unittest
from selenium import webdriver


class TestOpenSQLTutorial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/')
        self.driver.maximize_window()

    def test_open_sql_tutorial_from_top_navbar(self):
        tutorials_menu = self.driver.find_element_by_css_selector('#navbtn_tutorials')
        tutorials_menu.click()
        sql_tutorial_button = self.driver.find_element_by_css_selector('#nav_tutorials a[href="/sql/default.asp"]')
        sql_tutorial_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def test_open_sql_tutorial_from_left_navbar(self):
        sql_tutorial_button = self.driver.find_element_by_css_selector('#mySidenav a[href="/sql/default.asp"]')
        sql_tutorial_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
