import json
import logging
import time
import socket
import sys

from messager.common.utils import get_message, send_message, load_settings
from messager.logs import client_log_config

CONFIGS = dict()
CLIENT_LOGGER = logging.getLogger('client')


def create_presence_message(account_name, CONFIGS):
    message = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.time(),
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): account_name
        }
    }
    CLIENT_LOGGER.info('Создание сообщения для отправки на сервер')
    return message


def handle_response(message, CONFIGS):
    CLIENT_LOGGER.info('Обработка сообщения от сервера')
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] == 200:
            CLIENT_LOGGER.info('Успешная обработка сообщения от сервера')
            return '200: OK'
        CLIENT_LOGGER.critical('Обработка сообщения от сервера провалилась')
        return f'400: {message[CONFIGS.get("ERROR")]}'
    raise ValueError


def main():
    global CONFIGS
    CONFIGS = load_settings(is_server=False)
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
    except ValueError:
        CLIENT_LOGGER.critical('Порт должен быть в диапазоне от 1024 до 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    presence_message = create_presence_message('Guest', CONFIGS)
    CLIENT_LOGGER.info('Отправка сообщения серверу')
    send_message(transport, presence_message, CONFIGS)

    try:
        response = get_message(transport, CONFIGS)
        handled_response = handle_response(response, CONFIGS)
        CLIENT_LOGGER.debug(f'Ответ от сервера: {response}')
        CLIENT_LOGGER.info(f'Обработанный ответ сервера: {handled_response}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.critical('Ошибка декодирования сообщения')


if __name__ == "__main__":
    main()
