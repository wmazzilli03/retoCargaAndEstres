from locust import HttpUser, task, between
from config.url import BASE_URL, RUTA_GUIA


class TestCarga(HttpUser):
    wait_time = between(0.5, 0.5) 
    host = BASE_URL

    @task
    def consultar_guia(self):
        with self.client.get(RUTA_GUIA, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error {response.status_code}: {response.text}")