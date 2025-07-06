# retoCargaAndEstres
# Se adjunta el archivo de prueba de carga y de estres
# se adjuntan los comandos para que se se ejecute el script de carga y de estres
# se no se adjunta el archivo de reporte de carga, pero se deja una evidencia de foto en el documento en PDF
#


# comando para prueba de carga sin interfaz grafica
# locust -f .\tasks\TestCarga.py --users 20 --spawn-rate 20 --run-time 1m --headless --csv=reports/carga/resultado_carga
# comando para prueba de carga con interfaz grafica
# locust -f .\tasks\TestCarga.py --users 20 --spawn-rate 20 --run-time 1m


# comando para prueba de estres 
# interfaz UI: locust -f .\tasks\TestEstresUI.py 