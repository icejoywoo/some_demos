'''
Created on 2011-1-8

@author: Administrator
'''
class WasRun:
    def __init__(self, name):
        self.wasRun = None
        self.name = name
    def testMethod(self):
        self.wasRun = 1
    def run(self):
        method = getattr(self, self.name)
        method()

test =  WasRun("testMethod")
print test.wasRun
test.run()
print test.wasRun