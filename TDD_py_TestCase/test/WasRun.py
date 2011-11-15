'''
Created on 2011-1-5

@author: Administrator
'''
import TestCase
'''
WasRun
'''
class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase(name)
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "
    def tearDown(self):
        self.wasTearDown = 1
        self.log = self.log + "tearDown "
    def testBrokenMethod(self):
        raise Exception