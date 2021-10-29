import unittest
import Dz


class MyTestCase(unittest.TestCase):
    def test_evc(self):
        test_props = [
            {"numbers": [78, 78*4], "result": 78},
            {"numbers": [142, 71*71], "result": 71}
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.evc(*test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))

    def test_evc_max(self):
        test_props = [
            {"numbers": [78, 294, 570, 36], "result": 6},
            {"numbers": [555, 5555, 25], "result": 5},
            {"numbers": [150, 75], "result": 75},
            {"numbers": [23], "result": 23},
        ]

        for test_prop in test_props:
            self.assertEqual(Dz.evc_max(*test_prop["numbers"]),
                             test_prop["result"], "Should be " + str(test_prop["result"]))


if __name__ == '__main__':
    unittest.main()
