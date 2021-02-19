import unittest
import os
import sys
import json
from messager.common.utils import get_message, send_message, load_settings


sys.path.append(os.path.join(os.getcwd(), '..'))


class TestSocket:
    CONFIGS = load_settings()

    def __init__(self, test_message):
        self.test_message = test_message
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_message)
        self.encoded_message = json_test_message.encode(self.CONFIGS['ENCODING'])
        self.received_message = message_to_send

    def recv(self, max_len):
        json_test_message = json.dumps(self.test_message)
        return json_test_message.encode(self.CONFIGS['ENCODING'])


class Test(unittest.TestCase):
    CONFIGS = load_settings()

    test_message_send = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): '111111.111111',
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): 'test_test'
        }
    }

    test_success_receive = {CONFIGS['RESPONSE']: 200}
    test_error_receive = {
        CONFIGS['RESPONSE']: 400,
        CONFIGS['ERROR']: 'Bad Request'
    }

    def test_send_message(self):
        test_socket = TestSocket(self.test_message_send)
        send_message(test_socket, self.test_message_send, self.CONFIGS)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)
        with self.assertRaises(Exception):
            send_message(test_socket, test_socket, self.CONFIGS)

    def test_get_message(self):
        test_sock_ok = TestSocket(self.test_success_receive)
        test_sock_err = TestSocket(self.test_error_receive)
        self.assertEqual(get_message(test_sock_ok, self.CONFIGS), self.test_success_receive)
        self.assertEqual(get_message(test_sock_err, self.CONFIGS), self.test_error_receive)


if __name__ == '__main__':
    unittest.main()
