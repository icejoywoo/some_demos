'''
Created on 2011-1-8

@author: Administrator
'''
class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        
class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount +  1
    def testReault(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
        print result.summary()
    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)

class TestSuite:
    def __init__(self):
        self.tests = []
    def add(self, test):
        self.tests.append(test)
    def run(self, result):
        for test in self.tests:
            test.run(result)

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "
    def tearDown(self):
        self.log = self.log + "tearDown "
    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "
    def testBrokenMethod(self):
        raise Exception

class TestCaseTest(TestCase):
    def setUp(self):
        self.result = TestResult()
    def testTemplateMethod(self):   
        test = WasRun("testMethod")   
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):   
        test = WasRun("testMethod")   
        test.run(self.result)   
        assert("1 run, 0 failed" == self.result.summary())   
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

# test run
suite = TestSuite()
suite.add(TestCaseTest("testTemplateMethod"))
suite.add(TestCaseTest("testResult"))
suite.add(TestCaseTest("testFailedResult"))
suite.add(TestCaseTest("testFailedResultFormatting"))
suite.add(TestCaseTest("testSuite"))
result = TestResult()
suite.run(result)
print result.summary()
