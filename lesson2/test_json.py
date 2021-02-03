import unittest
from lesson2 import task2


class FileJsonTest(unittest.TestCase):

    def test_order_to_json1(self):
        self.assertEqual(task2.write_order_to_json('lamp', '12', '1500', 'John', '10.02.2021'),
                         {'orders': [{'товар': 'lamp', 'количество': '12', 'цена': '1500', 'покупатель': 'John',
                                      'дата': '10.02.2021'}]})

    def test_order_to_json2(self):
        self.assertEqual(task2.write_order_to_json('lamp2', '10', '1520', 'Smith', '11.12.2021'),
                         {'orders': [{'товар': 'lamp', 'количество': '12', 'цена': '1500', 'покупатель': 'John',
                                      'дата': '10.02.2021'},
                                     {'товар': 'lamp2', 'количество': '10', 'цена': '1520', 'покупатель': 'Smith',
                                      'дата': '11.12.2021'}]})

    def test_order_to_json3(self):
        self.assertEqual(task2.write_order_to_json('lamp4', '18', '1500', 'Jek', '13.12.2021'),
                         {'orders': [{'товар': 'lamp', 'количество': '12', 'цена': '1500', 'покупатель': 'John',
                                      'дата': '10.02.2021'},
                                     {'товар': 'lamp2', 'количество': '10', 'цена': '1520', 'покупатель': 'Smith',
                                      'дата': '11.12.2021'},
                                     {'товар': 'lamp4', 'количество': '18', 'цена': '1500', 'покупатель': 'Jek',
                                      'дата': '13.12.2021'}]})


if __name__ == "__main__":
    unittest.main()
