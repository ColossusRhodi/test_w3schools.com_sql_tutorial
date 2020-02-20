import unittest
from selenium import webdriver


class TestOpenSQLTutorial(unittest.TestCase):
    """Test case.

    Current test case checks opening app.
    Method 'setUp' contains preconditions for each test.
    Method 'test_open_sql_tutorial_from_top_navbar' checks app if it opens from top drop-down menu.
    Method 'test_open_sql_tutorial_from_left_navbar' checks app if it opens from left menu.
    Method 'tearDown' contains postconditions for each test.

    """
    def setUp(self):
        # Create a new session.
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/')
        self.driver.maximize_window()

    def test_open_sql_tutorial_from_top_navbar(self):
        # Open top drop-down menu.
        tutorials_menu = self.driver.find_element_by_css_selector('#navbtn_tutorials')
        tutorials_menu.click()

        # Open SQL Tutorial.
        sql_tutorial_button = self.driver.find_element_by_css_selector('#nav_tutorials a[href="/sql/default.asp"]')
        sql_tutorial_button.click()

        # Validate if open page is correct.
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def test_open_sql_tutorial_from_left_navbar(self):
        # Open SQL Tutorial.
        sql_tutorial_button = self.driver.find_element_by_css_selector('#mySidenav a[href="/sql/default.asp"]')
        sql_tutorial_button.click()

        # Validate if open page is correct.
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def tearDown(self):
        # End the session.
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
