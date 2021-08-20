from http import HTTPStatus

import requests


# Scenarios for GET /v1/servers
# Scenarios 01: Success
def test_get_servers_success():
    # Given
    customer_id = "218e7c3b-8adc-4104-9691-38e06e6efcd9"
    query_params = {"customer_id": customer_id}

    # When
    response = requests.get("localhost:8000/v1/servers", params=query_params)

    # Then
    assert response.status_code == HTTPStatus.OK
