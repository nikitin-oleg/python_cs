import json
import os
import sys
import logging

CLIENT_LOGGER = logging.getLogger('client')
SERVER_LOGGER = logging.getLogger('server')


def get_message(opened_socket, CONFIGS):
    response = opened_socket.recv(CONFIGS.get('MAX_PACKAGE_LENGTH'))
    if isinstance(response, bytes):
        json_response = response.decode(CONFIGS.get('ENCODING'))
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError()


def send_message(opened_socket, message, CONFIGS):
    json.message = json.dumps(message)
    response = json.message.encode(CONFIGS.get('ENCODING'))
    opened_socket.send(response)


def load_settings(is_server=True):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(base_dir, 'settings.json')
    config_keys = [
        "DEFAULT_PORT",
        "MAX_CONNECTIONS",
        "MAX_PACKAGE_LENGTH",
        "ENCODING",
        "ACTION",
        "TIME",
        "USER",
        "ACCOUNT_NAME",
        "PRESENCE",
        "RESPONSE",
        "ERROR"
    ]
    if not is_server:
        config_keys.append('DEFAULT_IP_ADDRESS')
    if not os.path.exists(path):
        CLIENT_LOGGER.critical('Файл конфигурации не найден')
        sys.exit(1)
    with open(path) as config_file:
        CONFIGS = json.load(config_file)
    loaded_configs_keys = list(CONFIGS.keys())
    for key in config_keys:
        if key not in loaded_configs_keys:
            SERVER_LOGGER.critical(f'В файле конфигурации не хватает ключа: {key}')
            sys.exit(1)
    return CONFIGS
