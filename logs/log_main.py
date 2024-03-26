import logging
import os
import json
import sys
from logging.handlers import TimedRotatingFileHandler


class RotatingFileLogger:
    def __init__(self, config_file='logs/log_settings_base.json'):
        with open(config_file, 'r') as f:
            config = json.load(f)

        self.log_dir = config.get('log_dir', 'logs/base')
        self.log_file_format = config.get('log_file_format', '%Y-%m-%d.log')
        self.max_bytes = config.get('max_bytes', 200000000)
        self.backup_count = config.get('backup_count', 7)

        self.logger = logging.getLogger(name=config.get('log_name', None))
        self.logger.setLevel(logging.INFO)

        self.setup_logging()

        if self.log_dir == 'logs/base':
            sys.excepthook = self.handle_exception

    def setup_logging(self):
        """Настройки логгирования, ротация"""
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        handler = TimedRotatingFileHandler(
            filename=os.path.join(self.log_dir, 'olvpnbot.log'),
            when='midnight',
            interval=1,
            backupCount=self.backup_count,
            encoding='utf-8',
            delay=False,
            utc=True
        )
        handler.suffix = self.log_file_format
        handler.extMatch = r'^\d{4}-\d{2}-\d{2}.log$'

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        self.logger.error("Необработанное исключение", exc_info=(exc_type, exc_value, exc_traceback))

    def log(self, level: str, message: str) -> None:
        """
        Записывает сообщение в лог с заданным уровнем.

        :param level: Уровень логирования.
        :param message: Сообщение для записи в лог.
        :return: None
        """
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        else:
            raise ValueError('Некорретный уровень логирования')


if __name__ == "__main__":
    logger = RotatingFileLogger()
    logger.log('info', 'Информационное сообщение')
    logger.log('error', 'Сообщение об ошибке')
    value_first = 1 / 2
    print(value_first)
    value_second = 1 / 0
    print(value_second)
