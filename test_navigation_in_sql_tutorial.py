import unittest
from selenium import webdriver


class NavigationInSQLTutorial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/sql/sql_intro.asp')
        self.driver.maximize_window()

    def test_navigation_use_first_next_button(self):
        next_button = self.driver.find_element_by_css_selector('#main > div:nth-child(3) > a:nth-child(2)')
        next_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Syntax", page_title)

    def test_navigation_use_second_next_button(self):
        next_button = self.driver.find_element_by_css_selector('#main > div:nth-child(32) > a:nth-child(2)')
        next_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Syntax", page_title)

    def test_navigation_use_first_previous_button(self):
        previous_button = self.driver.find_element_by_css_selector('#main > div:nth-child(3) > a:nth-child(1)')
        previous_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def test_navigation_use_second_previous_button(self):
        previous_button = self.driver.find_element_by_css_selector('#main > div:nth-child(32) > a:nth-child(1)')
        previous_button.click()
        page_title = self.driver.title
        self.assertEqual("SQL Tutorial", page_title)

    def test_navigation_use_left_nav_bar(self):
        file_page_titles = open('page_titles.txt', 'r', encoding='utf8')
        page_titles = file_page_titles.readlines()
        file_page_titles.close()

        for title in page_titles:
            index = page_titles.index(title)
            nav_bar_buttons = self.driver.find_elements_by_css_selector('#leftmenuinnerinner > a')
            nav_bar_buttons[index].click()
            page_title = self.driver.title
            self.assertEqual(title.rstrip(), page_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
