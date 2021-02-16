import unittest
from lesson2 import task3


class FileYamlTest(unittest.TestCase):

    def test_read_from_yaml(self):
        self.assertEqual(task3.read_from_yaml(),
                         {'вложенный словарь': {'евро': '1000€', 'йена': '1000¥', 'рубль': '1000₽'},
                          'список': ['msg_1', 'msg_2', 'msg_3'], 'целое число': 122})


if __name__ == "__main__":
    unittest.main()
