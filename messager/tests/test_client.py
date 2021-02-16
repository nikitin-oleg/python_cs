import unittest
import os
import sys

from messager.client import create_presence_message, handle_response
from messager.common.utils import get_message, send_message, load_settings

sys.path.append(os.path.join(os.getcwd(), '..'))


class TestClass(unittest.TestCase):
    CONFIGS = load_settings()

    def test_presence(self):
        test = create_presence_message('Guest', CONFIGS=self.CONFIGS)
        test[self.CONFIGS['TIME']] = '1.1'
        self.assertEqual(
            test,
            {
                self.CONFIGS['ACTION']: self.CONFIGS['PRESENCE'],
                self.CONFIGS['TIME']: '1.1',
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest'
                }
            }
        )

    def test_correct_answer(self):
        self.assertEqual(
            handle_response({self.CONFIGS['RESPONSE']: 200}, self.CONFIGS),
            '200: OK'
        )

    def test_bad_request(self):
        self.assertEqual(
            handle_response({
                self.CONFIGS['RESPONSE']: 400,
                self.CONFIGS['ERROR']: 'Bad Request',
            }, self.CONFIGS),
            '400: Bad Request'
        )

    def test_no_response(self):
        self.assertRaises(
            ValueError,
            handle_response,
            {self.CONFIGS['ERROR']: 'Bad Request'},
            self.CONFIGS
        )


if __name__ == '__main__':
    unittest.main()
