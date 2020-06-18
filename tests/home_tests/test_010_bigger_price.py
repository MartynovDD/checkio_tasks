import unittest
from home.task_010_bigger_price import bigger_price


class TestBiggerPrice(unittest.TestCase):

    def test_two_goods(self):
        self.assertEqual(bigger_price(2, [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1}
        ]), [
                             {"name": "wine", "price": 138},
                             {"name": "bread", "price": 100}
                         ], "Two most expensive goods")

    def test_one_good(self):
        self.assertEqual(bigger_price(1, [
            {"name": "pen", "price": 5},
            {"name": "whiteboard", "price": 170}
        ]), [{"name": "whiteboard", "price": 170}], "One most expensive good")

    def test_limit_out_of_range(self):
        self.assertEqual(bigger_price(10, [
            {"name": "iphone", "price": 200},
            {"name": "samsung", "price": 150},
            {"name": "meizu", "price": 100}
        ]), [
                             {"name": "iphone", "price": 200},
                             {"name": "samsung", "price": 150},
                             {"name": "meizu", "price": 100}
                         ], "Limit out of range")

    def test_negative_index(self):
        self.assertEqual(bigger_price(-1, [
            {"name": "pen", "price": 5},
            {"name": "whiteboard", "price": 170}
        ]), [{"name": "whiteboard", "price": 170}], "Negative index")

    def test_zero_limit(self):
        self.assertEqual(bigger_price(0, [
            {"name": "Eggs", "price": 82}
        ]), [], "Limit not given")

    def test_no_price(self):
        self.assertEqual(bigger_price(1, [
            {"name": "spam"}
        ]), [{"name": "spam"}], "No price")


if __name__ == "__main__":
    unittest.main()
