import unittest
import os
import sys
import json

from messager.common.utils import get_message, send_message, load_settings
from messager.server import handle_message

sys.path.append(os.path.join(os.getcwd(), '..'))


class TestServer(unittest.TestCase):
    CONFIGS = load_settings(is_server=True)

    error_messages = {
        CONFIGS['RESPONSE']: 400,
        CONFIGS['ERROR']: 'Bad Request'
    }
    success_messages = {
        CONFIGS['RESPONSE']: 200
    }

    def test_without_action(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['TIME']: '111111.111111',
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest'
                }
            }, self.CONFIGS),
            self.error_messages
        )

    def test_wrong_action(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: 'Wrong',
                self.CONFIGS['TIME']: '111111.111111',
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest'
                }
            }, self.CONFIGS),
            self.error_messages
        )

    def test_without_time(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: self.CONFIGS['PRESENCE'],
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest'
                }
            }, self.CONFIGS),
            self.error_messages
        )

    def test_without_user(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: self.CONFIGS['PRESENCE'],
                self.CONFIGS['TIME']: '111111.111111',
            }, self.CONFIGS),
            self.error_messages
        )

    def test_wrong_user(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: self.CONFIGS['PRESENCE'],
                self.CONFIGS['TIME']: '111111.111111',
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest1'
                }
            }, self.CONFIGS),
            self.error_messages
        )

    def test_success_messages(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: self.CONFIGS['PRESENCE'],
                self.CONFIGS['TIME']: '111111.111111',
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest'
                }
            }, self.CONFIGS),
            self.success_messages
        )


if __name__ == '__main__':
    unittest.main()
