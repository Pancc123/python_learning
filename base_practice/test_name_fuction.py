# -*- coding: utf-8 -*- 
import unittest
import time,os
from function_str import get_formatted_name1
import HTMLTestRunner


class NamesTestCase(unittest.TestCase):
    def test_first_last_name1(self):
            formatted_name = get_formatted_name1('janis','joplin')
            self.assertEqual(formatted_name, 'Janis Joplin')
            self.assertNotEqual(formatted_name, 'JanisJoplin')


def suite():
    LoginTestCase = unittest.makeSuite(NamesTestCase, "test")
    #alltest = unittest.TestSuite(LoginTestCase)
    return LoginTestCase


if __name__ == '__main__':
    #unittest.main()
    #runner = unittest.TextTestRunner()
    #runner.run(suite())
    fp = open(r'D:/python_work/report/test1.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=1,title='Iotplatform Login Test Report',
                                               description='Implementation Example with:')
    runner.run(suite())

