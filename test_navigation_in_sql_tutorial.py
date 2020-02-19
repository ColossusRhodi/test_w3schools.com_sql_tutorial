import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
from test_data import titles, urls


class TestNavigationInSQLTutorial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    test_data_next_buttons = []
    for url in urls:
        index = urls.index(url)
        test_data_next_buttons.append((url, titles[1:][index]))

    @parameterized.expand(test_data_next_buttons)
    def test_navigation_first_next_button(self, url, title):
        self.driver.get(url)
        self.driver.maximize_window()
        next_buttons = self.driver.find_elements_by_css_selector('div.w3-clear.nextprev > a.w3-right.w3-btn')
        next_buttons[0].click()
        page_title = self.driver.title
        self.assertEqual(title, page_title)

    @parameterized.expand(test_data_next_buttons)
    def test_navigation_second_next_button(self, url, title):
        self.driver.get(url)
        self.driver.maximize_window()
        next_buttons = self.driver.find_elements_by_css_selector('div.w3-clear.nextprev > a.w3-right.w3-btn')
        next_buttons[1].click()
        page_title = self.driver.title
        self.assertEqual(title, page_title)

    test_data_previous_buttons = []
    for title in titles[:-2]:
        index = titles[:-2].index(title)
        test_data_previous_buttons.append((urls[1:][index], title))

    @parameterized.expand(test_data_previous_buttons)
    def test_navigation_first_previous_button(self, url, title):
        self.driver.get(url)
        self.driver.maximize_window()
        previous_buttons = self.driver.find_elements_by_css_selector('div.w3-clear.nextprev > a.w3-left.w3-btn')
        previous_buttons[0].click()
        page_title = self.driver.title
        self.assertEqual(title, page_title)

    @parameterized.expand(test_data_previous_buttons)
    def test_navigation_use_second_previous_button(self, url, title):
        self.driver.get(url)
        self.driver.maximize_window()
        previous_buttons = self.driver.find_element_by_css_selector('div.w3-clear.nextprev > a.w3-left.w3-btn')
        previous_buttons[1].click()
        page_title = self.driver.title
        self.assertEqual(title, page_title)

    test_data_left_nav_bar = []
    for url in urls:
        test_data_left_nav_bar.append((url, titles[:-1]))

    @parameterized.expand(test_data_left_nav_bar)
    def test_navigation_left_nav_bar(self, url, title):
        self.driver.get(url)
        self.driver.maximize_window()
        main_window = self.driver.current_window_handle
        nav_bar_buttons = self.driver.find_elements_by_css_selector('#leftmenuinnerinner > a')[:37]
        for button in nav_bar_buttons:
            index = nav_bar_buttons.index(button)
            button.send_keys(Keys.CONTROL + Keys.RETURN)
            self.driver.switch_to.window(self.driver.window_handles[1])
            page_title = self.driver.title
            self.assertEqual(title[index], page_title)
            self.driver.close()
            self.driver.switch_to.window(window_name=main_window)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
