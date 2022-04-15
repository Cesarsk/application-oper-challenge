import unittest
import warnings
from src import string_transform


class UnitTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    def tearDown(self):
        pass

    def test_transform(self):
        print("\n\nTesting transform text function")
        start = "fOoBar25"
        expected_result = "47RAbOoF"

        result = string_transform.transform(start)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
