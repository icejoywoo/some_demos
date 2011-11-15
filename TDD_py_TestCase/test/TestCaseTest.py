'''
Created on 2011-1-5

@author: Administrator
'''
import TestCase
import WasRun
import TestResult
'''
TestCaseTest
'''
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
    def testRunning(self, result):
        self.test.run()
        assert(self.test.wasRun)
    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)
        assert("setUp testMethod " == self.test.log)
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)
        print "setUp testMethod tearDown " == test.log
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run();
        assert("1 run, 0 failed" == result.summary())
        print "1 run, 0 failed" == result.summary()
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run(result);
        assert("1 run, 1 failed" == result.summary())


result = TestResult()
TestCaseTest("testTemplateMethod").run(result)