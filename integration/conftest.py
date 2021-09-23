import logging
import os
import time
import uuid

import pytest
import requests

from integration.clients.servers import ServersClient

_logger = logging.getLogger("integration-test-suite")

_RETRY_ATTEMPTS = 10

SERVERS_BASE_URL = os.getenv("SERVERS_BASE_URL", "http://localhost:5000")


def pytest_sessionstart(session):
    _ensure_service_is_up()


def _is_service_up():
    try:
        response = requests.get(f"{SERVERS_BASE_URL}/health", timeout=1)
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


@pytest.fixture(name="customer_id")
def get_customer_id():
    return str(uuid.uuid4())


@pytest.fixture(scope="session", name="servers_base_url")
def get_servers_base_url():
    return SERVERS_BASE_URL


@pytest.fixture(scope="session", name="servers_client")
def get_servers_client(servers_base_url):
    return ServersClient(servers_base_url)
