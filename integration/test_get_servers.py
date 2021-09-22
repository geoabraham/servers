from http import HTTPStatus

import pytest
import requests


# Scenarios for GET /v1/servers
# Scenarios 01: Success
# Scenarios 02: Error - Invalid Customer ID
def test_get_servers_success(customer_id, servers_client):
    # When
    response = servers_client.get_servers(customer_id)

    # Then
    assert response.status_code == HTTPStatus.OK
    body = response.json()

    data = body["data"]
    meta = body["meta"]
    assert len(data) == meta["count"]


@pytest.mark.parametrize(
    "invalid_customer_id",
    [
        "not_uuid",
        "",
        123,
    ],
)
def test_get_servers_invalid_customer_id(invalid_customer_id, servers_client):
    # When
    response = servers_client.get_servers(invalid_customer_id)

    # Then
    assert response.status_code == HTTPStatus.BAD_REQUEST
    body = response.json()

    # Assert over the error body
    errors = body["errors"]
    assert len(errors) == 1

    assert errors[0]["code"] == "validation_error"
