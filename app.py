from flask import Flask, render_template, request
from src.Ejercicio_6 import celciusToFahrenheit as converCtoF
app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/Ejercicio_6', methods=['GET'])
def Ejercicio_6():
    return render_template('Ejercicio_6.html')


@app.route("/celciusToFahrenheit", methods=['POST'])
def celciusToFahrenheit():
    centigrados = float(request.form["centigrados"])
    fahrenheit = converCtoF(centigrados)
    return render_template('Ejercicio_6r.html', f=fahrenheit, c=centigrados)


if __name__ == "__main__":
    app.run(debug=True)
