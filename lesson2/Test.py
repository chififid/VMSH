import unittest
import Dz


class MyTestCase(unittest.TestCase):
    def test_middle_num(self):
        print("Задача 1")
        test_props = [
            {"numbers": [1, 2, 3], "result": 2},
            {"numbers": [555, 55, 2], "result": 204},
            {"numbers": [100, 50], "result": 75},
            {"numbers": Dz.input_numbers(), "result": float(input("Результат: "))}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.middle_num(test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_middle_num_rec(self):
        print("Задача 2")

        test_props_count = 2
        for _ in range(test_props_count):
            self.assertEqual(Dz.middle_num_rec(),
                             float(input("Результат: ")), "Wrong!!")

    def test_alternation_lists_re(self):
        test_props = [
            {"lists": [[1, 2], [3, 4]], "result": [1, 3, 2, 4]},
            {"lists": [[1, 3, 5, 7], [2, 4, 6, 8]], "result": [1, 2, 3, 4, 5, 6, 7, 8]},
            {"lists": [[1, 2], [1, 2], [3, 4]], "result": [1, 1, 3, 2, 2, 4]}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.alternation_lists_re(*test_prop["lists"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_max_min(self):
        test_props = [
            {"numbers": [-1, 2, 3, -55, 66], "result": {"min": -55, "max": 66}},
            {"numbers": [-1, 2, -2, 5, 3], "result": {"min": -2, "max": 5}}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.max_min(test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_max_increasing_part(self):
        test_props = [
            {"numbers": [1, 2, 3], "result": {"from": 0, "to": 3, "len": 3}},
            {"numbers": [-1, -2, 3, 2, 3, 4, 3, 2], "result": {"from": 3, "to": 6, "len": 3}},
            {"numbers": [-1, -2, -3, -4, -5, 1, 2, 3], "result": {"from": 4, "to": 8, "len": 4}}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.max_increasing_part(test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))


if __name__ == '__main__':
    unittest.main()
