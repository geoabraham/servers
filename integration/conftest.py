import logging
import time

import pytest
import requests

_logger = logging.getLogger("integration-test-suite")

_RETRY_ATTEMPTS = 10


def pytest_sessionstart(session):
    _ensure_service_is_up()


def _is_service_up():
    try:
        response = requests.get(f"http://localhost:5000/health", timeout=1)
        response.raise_for_status()
    except Exception as err:  # pylint: disable=broad-except
        _logger.warning(err)
        return False
    return True


def _ensure_service_is_up():
    for i in range(_RETRY_ATTEMPTS):
        _logger.info(f"Check if service is up. Attempt {i + 1}/{_RETRY_ATTEMPTS}")

        if _is_service_up():
            _logger.info("Service is up. Enjoy!")
            return

        _logger.warning("Service is not up.")
        time.sleep(5)

    pytest.exit("Service is not running or is unreachable.")
