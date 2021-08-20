import logging

_logger = logging.getLogger("unit-test-suite")


def pytest_sessionstart(session):  # pylint: disable=unused-argument
    _logger.warning("Starting unit test suite!!")
