from password import Password
import unittest
import re


class GeneratorTest(unittest.TestCase):

    def testGenerator(self):
        result = Password.generate_password(16, 0, 1, 1, 1)
        test_regex = re.compile('^[a-zA-Z!@#$%^&*()_+=-]{16}$')
        self.assertRegex(result, test_regex)
        result = Password.generate_password(16, 1, 0, 1, 1)
        test_regex = re.compile('^[A-Z0-9!@#$%^&*()_+=-]{16}$')
        self.assertRegex(result, test_regex)
        result = Password.generate_password(16, 1, 1, 0, 1)
        test_regex = re.compile('^[a-z0-9!@#$%^&*()_+=-]{16}$')
        self.assertRegex(result, test_regex)
        result = Password.generate_password(16, 1, 1, 1, 0)
        test_regex = re.compile('^[a-zA-Z0-9]{16}$')
        self.assertRegex(result, test_regex)
        result = Password.generate_password(16, 1, 1, 1, 1)
        test_regex = re.compile('^[a-zA-Z0-9!@#$%^&*()_+=-]{16}$')
        self.assertRegex(result, test_regex)


if __name__ == "__main__":
    unittest.main()
