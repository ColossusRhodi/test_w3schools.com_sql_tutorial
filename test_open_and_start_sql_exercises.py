import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from parameterized import parameterized
from test_data import urls, answers


class TestOpenSQLExercises(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('D:\chromedriver.exe')

    test_data = []
    for url in urls:
        test_data.append((url,))

    @parameterized.expand(test_data)
    def test_open_sql_exercises(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        sql_query_statement = self.driver.find_element_by_css_selector('div.exercisewindow pre').text
        start_exercise = self.driver.find_element_by_css_selector('div.exercisewindow a')
        start_exercise.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sql_query_statement_to_validate = self.driver.find_element_by_css_selector('#assignmentcontainer').text
        self.assertEqual(sql_query_statement, sql_query_statement_to_validate.replace('\n', ''))

    @parameterized.expand(test_data)
    def test_start_sql_exercises(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        sql_query_statement = self.driver.find_element_by_css_selector('div.exercisewindow pre').text
        submit_answer = self.driver.find_element_by_css_selector('div.exercisewindow button')
        submit_answer.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sql_query_statement_to_validate = self.driver.find_element_by_css_selector('#assignmentcontainer').text
        self.assertEqual(sql_query_statement, sql_query_statement_to_validate.replace('\n', ''))

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

    @parameterized.expand(test_data)
    def test_start_sql_exercises_with_answer(self, url, *answer):
        self.driver.get(url)
        self.driver.maximize_window()
        input_answer = self.driver.find_elements_by_css_selector('div.exercisewindow input')
        for field in input_answer:
            index = input_answer.index(field)
            field.send_keys(answer[index])
        submit_answer = self.driver.find_element_by_css_selector('div.exercisewindow button')
        submit_answer.send_keys(Keys.CONTROL + Keys.RETURN)
        self.driver.switch_to.window(self.driver.window_handles[1])
        submit_answer = self.driver.find_element_by_css_selector('#answerbutton')
        submit_answer.click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'div#assignmentCorrect[style="display: block;"]'))))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
