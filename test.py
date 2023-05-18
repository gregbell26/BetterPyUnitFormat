import unittest


class Test(unittest.TestCase):
    def test_failure(self):
        """This test should fail"""
        self.assertEquals(1, 2)

    def test_success(self):
        """This test should pass"""
        self.assertEquals(1, 1)

    def test_error(self):
        """This test will error"""
        0/0

    @unittest.skip("Skipping this test :)")
    def test_skip(self):
        """This test will be skipped"""
        self.assertEquals(1, 2)
