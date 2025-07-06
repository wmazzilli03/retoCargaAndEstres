from locust import HttpUser, task, between
from config.url import BASE_URL, RUTA_GUIA

class TestCarga(HttpUser):
    wait_time = between(0.5, 0.5) 
    host = BASE_URL

    @task
    def consultar_guia(self):
        self.client.get(RUTA_GUIA)
