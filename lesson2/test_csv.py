import unittest
from lesson2 import task1


class FileCSVTest(unittest.TestCase):

    def test_header(self):
        self.assertEqual(task1.main_data, ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])

    def test_file1(self):
        self.assertEqual(task1.get_data('info_1.txt'),
                         ['LENOVO', 'Microsoft Windows 7 Профессиональная', '00971-OEM-1982661-00231', 'x64-based PC'])

    def test_file2(self):
        self.assertEqual(task1.get_data('info_2.txt'),
                         ['ACER', 'Microsoft Windows 10 Professional', '00971-OEM-1982661-00231', 'x64-based PC'])

    def test_file3(self):
        self.assertEqual(task1.get_data('info_3.txt'),
                         ['DELL', 'Microsoft Windows 8.1 Professional', '00971-OEM-1982661-00231', 'x86-based PC'])


if __name__ == "__main__":
    unittest.main()
