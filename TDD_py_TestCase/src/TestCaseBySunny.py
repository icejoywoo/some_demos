'''''  
created on 2010-10-3  
 
@author: sunny  
'''  
  
  
class testcase:   
    def __init__(self, name):   
        self.name = name   
       
    def setup(self):   
        pass  
           
    def run(self, result):   
        result.teststarted()   
        self.setup()   
        try:   
            method = getattr(self, self.name)   
            method()   
        except:   
            result.testfailed()   
        self.teardown()   
           
    def teardown(self):   
        pass  
           
  
class wasrun(testcase):   
    def __init__(self, name):   
        testcase.__init__(self, name)   
           
    def setup(self):   
        self.wasrun = None  
        self.wassetup = 1  
        self.log = "setup ";   
           
    def testmethod(self):   
        self.wasrun = 1  
        self.log = self.log + "testmethod ";   
           
    def testbrokenmethod(self):   
        raise Exception
           
    def teardown(self):   
        self.log = self.log + "teardown "   
  
  
class testresult:   
    def __init__(self):   
        self.runcount = 0  
        self.errorcount = 0  
           
    def teststarted(self):   
        self.runcount = self.runcount + 1  
           
    def testfailed(self):   
        self.errorcount = self.errorcount + 1  
           
    def summary(self):   
        return "%d run, %d failed" % (self.runcount, self.errorcount)   
  
  
class testsuite:   
    def __init__(self):   
        self.tests = []   
           
    def add(self, test):   
        self.tests.append(test)   
       
    def run(self, result):   
        for test in self.tests:   
            test.run(result)   
  
  
class testcasetest(testcase):   
    def setup(self):   
        self.result = testresult()   
           
    def testtemplatemethod(self):   
        test = wasrun("testmethod")   
        test.run(self.result)   
        assert("setup testmethod teardown " == test.log)   
           
    def testresult(self):   
        test = wasrun("testmethod")   
        test.run(self.result)   
        assert("1 run, 0 failed" == self.result.summary())   
       
    def testfailedresult(self):   
        test = wasrun("testbrokenmethod")   
        test.run(self.result)   
        assert("1 run, 1 failed" == self.result.summary())   
           
    def testfailedresultformatting(self):   
        self.result.teststarted()   
        self.result.testfailed()   
        assert("1 run, 1 failed" == self.result.summary())   
           
    def testsuite(self):   
        suite = testsuite()   
        suite.add(wasrun("testmethod"))   
        suite.add(wasrun("testbrokenmethod"))   
        suite.run(self.result)   
        assert("2 run, 1 failed" == self.result.summary())   
       
    def teardown(self):   
        pass  
  
suite = testsuite()   
suite.add(testcasetest("testtemplatemethod"))   
suite.add(testcasetest("testresult"))   
suite.add(testcasetest("testfailedresult"))   
suite.add(testcasetest("testfailedresultformatting"))   
suite.add(testcasetest("testsuite"))   
result = testresult()   
suite.run(result)   
print(result.summary())
