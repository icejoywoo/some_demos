'''
Created on 2010-12-28

@author: icejoywoo
'''
import TestResult
'''
TestCase
'''
class TestCase:
    def __init__(self, name):
        self.name = name
    def setup(self):
        pass
    def run(self, result):
        result = TestResult()
        result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()
    def tearDown(self):
        pass