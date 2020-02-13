import unittest
from test_open_sql_tutorial import TestOpenSQLTutorial
from test_back_to_home_page import TestBackToHomePage
from test_navigation_in_sql_tutorial import TestNavigationInSQLTutorial


test_open_sql_tutorial = unittest.TestLoader().loadTestsFromTestCase(TestOpenSQLTutorial)
test_back_to_home_page = unittest.TestLoader().loadTestsFromTestCase(TestBackToHomePage)
test_navigation_in_sql_tutorial = unittest.TestLoader().loadTestsFromTestCase(TestNavigationInSQLTutorial)

test_suite = unittest.TestSuite([
    test_open_sql_tutorial,
    test_back_to_home_page,
    test_navigation_in_sql_tutorial
    ])

unittest.TextTestRunner(verbosity=2).run(test_suite)
