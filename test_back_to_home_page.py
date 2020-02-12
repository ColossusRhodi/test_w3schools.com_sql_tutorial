import unittest
from selenium import webdriver


class TestBackToHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/sql/default.asp')
        self.driver.maximize_window()

    def test_back_to_home_page_use_w3schools_button(self):
        w3schools_button = self.driver.find_element_by_css_selector('div.w3-container.top > a')
        w3schools_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def test_back_to_home_page_use_drawn_house_button(self):
        drawn_house_button = self.driver.find_element_by_css_selector('#topnav a:nth-child(2)')
        drawn_house_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def test_back_to_home_page_use_first_home_button(self):
        home_button = self.driver.find_element_by_css_selector('#main > div:nth-child(3) > a')
        home_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def test_back_to_home_page_use_second_home_button(self):
        home_button = self.driver.find_element_by_css_selector('#main > div:nth-child(50) > a')
        home_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
