import unittest
import test
from BetterPyUnitFormat import BetterPyUnitTestRunner

if __name__ == "__main__":
    testSuite = unittest.loader.makeSuite(test.Test)
    runner = BetterPyUnitTestRunner()
    runner.run(testSuite)
