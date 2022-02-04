"""Декораторы"""

import sys
import logging
import logs.config_server_log
import logs.config_client_log

# метод определения модуля, источника запуска.

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}')
        return ret
    return log_saver
