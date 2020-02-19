import unittest
from test_open_sql_tutorial import TestOpenSQLTutorial
from test_back_to_home_page import TestBackToHomePageFirstPage, TestBackToHomePageOtherPages
from test_navigation_in_sql_tutorial import TestNavigationInSQLTutorial
from test_open_and_run_sql_examples import TestOpenSQLExamples, TestRunSQLExamples


open_sql_tutorial = unittest.TestLoader().loadTestsFromTestCase(TestOpenSQLTutorial)
back_to_home_page_first_page = unittest.TestLoader().loadTestsFromTestCase(TestBackToHomePageFirstPage)
back_to_home_page_other_pages = unittest.TestLoader().loadTestsFromTestCase(TestBackToHomePageOtherPages)
navigation_in_sql_tutorial = unittest.TestLoader().loadTestsFromTestCase(TestNavigationInSQLTutorial)
open_sql_examples = unittest.TestLoader().loadTestsFromTestCase(TestOpenSQLExamples)
run_sql_examples = unittest.TestLoader().loadTestsFromTestCase(TestRunSQLExamples)

test_suite = unittest.TestSuite([
    open_sql_tutorial,
    back_to_home_page_first_page,
    back_to_home_page_other_pages,
    navigation_in_sql_tutorial,
    open_sql_examples,
    run_sql_examples
    ])

unittest.TextTestRunner(verbosity=2).run(test_suite)
