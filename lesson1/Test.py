import unittest
import Dz


class MyTestCase(unittest.TestCase):
    def test_print_max_number(self):
        test_props = [
            {"numbers": [1, 2, 3], "result": 3},
            {"numbers": [555, 55, 6], "result": 555}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.print_max_number(test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_is_triangle(self):
        test_props = [
            {"points": [[1, 1], [2, 2], [3, 3]], "result": False},
            {"points": [[0, 0], [0, 10], [10, 10]], "result": True}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.is_triangle(test_prop["points"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_find_roots_in_square_case(self):
        test_props = [
            {"coefficients": [1, 2, 3], "result": False},
            {"coefficients": [-1, 7, 8], "result": [-1, 8]},
            {"coefficients": [4, 4, 1], "result": -0.5},
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.find_roots_in_square_case(*test_prop["coefficients"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))


if __name__ == '__main__':
    unittest.main()
