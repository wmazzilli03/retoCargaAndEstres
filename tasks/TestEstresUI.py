from locust import HttpUser, task, constant_pacing
from locust.shape import LoadTestShape 
from config.url import BASE_URL, RUTA_GUIA

class TestEstresUI(HttpUser):
    wait_time = constant_pacing(0.1)  # 10 req/s por usuario x segudo.
    host = BASE_URL

    @task
    def consultar_guia(self):
        with self.client.get(RUTA_GUIA, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"ERROR {response.status_code}: {response.text}")


class SimulacionDeEstres(LoadTestShape):
    """
    Curva de carga personalizada: incrementa usuarios cada 15 segundos hasta 250.
    """
    def tick(self):
        run_time = self.get_run_time()

        if run_time < 15:
            return (100, 100)
        elif run_time < 30:
            return (150, 150)
        elif run_time < 45:
            return (200, 200)
        elif run_time < 60:
            return (250, 250)
        else:
            return None 
