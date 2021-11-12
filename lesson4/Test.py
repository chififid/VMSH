import unittest
import Dz


class MyTestCase(unittest.TestCase):
    def test_bin_rec(self):
        nums = [2, 3, 4, 11, 12, 14, 23, 24, 34, 46, 78]

        test_props = [
            {"numbers": nums, "x": 23, "result": 6},
            {"numbers": nums, "x": 2, "result": 0},
            {"numbers": nums, "x": 78, "result": 10},
            {"numbers": nums, "x": 7008, "result": -1},
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.bin_rec(test_prop["numbers"], test_prop["x"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_gnome_sort(self):
        test_props = [
            {"numbers": [14, 11, 78, 3, 12, 2, 23, 24, 34, 46, 4], "result": [2, 3, 4, 11, 12, 14, 23, 24, 34, 46, 78]},
            {"numbers": [555, 5555, 25], "result": [25, 555, 5555]},
            {"numbers": [1, 3, 2, 4, 7, 6, 5, 9, 8, 0], "result": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
            {"numbers": [23], "result": [23]},
            {"numbers": [], "result": []},
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.gnome_sort(test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))


if __name__ == '__main__':
    unittest.main()
