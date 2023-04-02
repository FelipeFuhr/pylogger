# -*- coding: utf-8 -*-
"""
Logger for the application .
"""

from logging import INFO, Logger, StreamHandler, getLogger
from os import environ

from pythonjsonlogger import jsonlogger


class Logger:
    """
    Logger class to handle logger related functionalities .

    Methods
    -------
    get_logger(application_name: str) -> Logger
        Sets up logger for the application .

    """

    @staticmethod
    def get_logger(
        application_name: str,
    ) -> Logger:
        """
        Sets up logger for the application .

        Parameters
        ----------
        application_name : str
            Application name for the logger .

        Returns
        -------
        Logger
            Logger to be used .

        """
        # Create logger and handler objects
        logger = getLogger()
        handler = StreamHandler()

        # Modify handler's formatter
        formatter = jsonlogger.JsonFormatter(
            "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] "
            + "%(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Set logger level to info
        level = environ.get("LOG_LEVEL", INFO)
        logger.setLevel(level)

        return logger


# Logger object for the application
log = Logger.get_logger(
    application_name=__name__,
)
