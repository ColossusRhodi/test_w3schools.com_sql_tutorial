import unittest
from selenium import webdriver
from parameterized import parameterized
from test_data import urls


class TestBackToHomePageFirstPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')
        self.driver.get('https://www.w3schools.com/sql/default.asp')
        self.driver.maximize_window()

    def test_back_to_home_page_first_home_button(self):
        home_button = self.driver.find_element_by_css_selector('#main > div:nth-child(3) > a.w3-left.w3-btn')
        home_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def test_back_to_home_page_second_home_button(self):
        home_button = self.driver.find_element_by_css_selector('#main > div:nth-child(50) > a.w3-left.w3-btn')
        home_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def tearDown(self):
        self.driver.quit()


class TestBackToHomePageOtherPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    test_data = []
    for url in urls:
        test_data.append((url,))

    @parameterized.expand(test_data)
    def test_back_to_home_page_w3schools_button(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        w3schools_button = self.driver.find_element_by_css_selector('div.w3-container.top > a')
        w3schools_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    @parameterized.expand(test_data)
    def test_back_to_home_page_drawn_house_button(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        drawn_house_button = self.driver.find_element_by_css_selector('a[title="Home"]')
        drawn_house_button.click()
        page_title = self.driver.title
        self.assertEqual("W3Schools Online Web Tutorials", page_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
