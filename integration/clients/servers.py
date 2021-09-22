import requests


class ServersClient:
    def __init__(self, base_url):
        self._url = base_url

    def get_servers(self, customer_id):
        query_params = {"customer_id": customer_id}
        return requests.get(
            f"{self._url}/servers",
            params=query_params,
        )

    def create_server(self, customer_id, hostname, server_os, ram, cpu):
        body = dict(
            customer_id=customer_id,
            hostname=hostname,
            os=server_os,
            ram=ram,
            cpu=cpu,
        )
        return requests.post(
            f"{self._url}/servers",
            json=body,
        )
