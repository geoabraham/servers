from http import HTTPStatus

import pytest


# Scenarios for POST /v1/servers
# Scenarios 01: Success
# Scenarios 02: Error - Invalid Customer ID
def test_post_servers_success(customer_id, servers_client):
    # Given
    hostname = "my-awesome-server"
    server_os = "linux"
    cpu = "intel"
    ram = 250

    # When
    create_response = servers_client.create_server(
        customer_id=customer_id,
        hostname=hostname,
        server_os=server_os,
        cpu=cpu,
        ram=ram,
    )

    # Then
    assert create_response.status_code == HTTPStatus.CREATED
    create_body = create_response.json()
    assert not create_body

    get_response = servers_client.get_servers(customer_id)
    assert get_response.status_code == HTTPStatus.OK
    get_body = get_response.json()

    assert len(get_body["data"]) == 1


@pytest.mark.parametrize(
    "invalid_customer_id",
    [
        "not_uuid",
        "",
        123,
    ],
)
def test_post_servers_invalid_customer_id(invalid_customer_id, servers_client):
    # Given
    hostname = "my-awesome-server"
    server_os = "linux"
    cpu = "intel"
    ram = 250

    # When
    create_response = servers_client.create_server(
        customer_id=invalid_customer_id,
        hostname=hostname,
        server_os=server_os,
        cpu=cpu,
        ram=ram,
    )

    # Then
    assert create_response.status_code == HTTPStatus.BAD_REQUEST
    body = create_response.json()

    # Assert over the error body
    errors = body["errors"]
    assert len(errors) == 1

    assert errors[0]["code"] == "validation_error"
