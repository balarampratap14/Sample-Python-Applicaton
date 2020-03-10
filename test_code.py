#!/usr/bin/env python
import unittest
import application

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        #self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World! Your Python Application Is succesfully Up and Running.\n Created and Written By Balaram Pratap')
    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        #self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World! Your Python Application Is succesfully Up and Running.\n Created and Written By Balaram Pratap')

    def test_hello_name(self):
        #name = 'Balaram_Pratap'
        rv = self.app.get('/hello/Balaram_Pratap/')
        #self.assertEqual(rv.status, '200 OK')
        self.assertEqual('HEY! Hello Balaram_Pratap!\n. Welcome to my UserPage.!!!!!', 'HEY! Hello Balaram_Pratap!\n. Welcome to my UserPage.!!!!!')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
