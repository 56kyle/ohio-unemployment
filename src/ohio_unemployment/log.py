"""Module containing logic for logging used throughout the ohio_unemployment package."""

from pathlib import Path

from loguru import logger

from ohio_unemployment.constants import _FILE_SAFE_DATETIME_FORMAT
from ohio_unemployment.constants import APP_START_TIME
from ohio_unemployment.constants import USER_LOG_FOLDER


_FILE_SAFE_DATETIME_SLUG: str = APP_START_TIME.strftime(_FILE_SAFE_DATETIME_FORMAT)

LOG_PATH: Path = USER_LOG_FOLDER / f"log_{_FILE_SAFE_DATETIME_SLUG}.log"


logger.add(LOG_PATH, serialize=True)
