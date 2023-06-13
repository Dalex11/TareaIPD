import requests

url = 'http://localhost:5000/'

data = [
    {
        "fecha_inicial": "2020-01-02",
        "accion": "GOOGL",
        "fecha_final": "2020-01-05"
    },
    {
        "fecha_inicial": "2020-02-01",
        "accion": "AAPL",
        "fecha_final": "2020-02-10"
    },
    {
        "fecha_inicial": "2020-03-05",
        "accion": "MSFT",
        "fecha_final": "2020-03-10"
    }
]

error = 0

response = requests.get(url)
if response.status_code == 200:
    print("Respuesta del servidor del metodo get:")
    print(response.text)
else:
    print("Se produjo un error al realizar la solicitud GET")
    error += 1

for data_json in data:
    response = requests.post(url, json=data_json)
    if response.status_code == 200:
        print("Respuesta del servidor para la acción " + data_json["accion"] + ":")
        print(response.text)
    else:
        print("Se produjo un error al realizar la solicitud POST de la acción " + data_json["accion"])
        error += 1

if (error == 0):
    print("Todos las pruebas corrieron sin errores")
else:
    print("Ocurrió un error con " + str(error) + " prueba(s)")
