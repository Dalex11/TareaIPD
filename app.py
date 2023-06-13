from flask import Flask, request
from datetime import datetime
import read_value_yf

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        json_data = request.get_json()
        return read_value_yf.get_stock_data(json_data["fecha_inicial"], json_data["accion"], json_data["fecha_final"]).to_json()
    else:
        return read_value_yf.test().to_html()

if __name__ == "__main__":
    print(f"{datetime.now()}")
    app.run(host="0.0.0.0")