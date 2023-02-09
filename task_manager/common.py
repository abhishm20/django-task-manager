# -*- coding: utf-8 -*-
import logging
import sys

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s.%(msecs)03d] [%(name)s:%(levelname)s]"
            " [%(funcName)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "verbose",
        }
    },
    "loggers": {
        "task_manager": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

logger = logging.getLogger("task_manager")
