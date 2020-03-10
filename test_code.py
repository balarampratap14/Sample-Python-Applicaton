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
