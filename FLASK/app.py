from flask import Flask, render_template, request
from src.Ejercicio_6 import celciusToFahrenheit as converCtoF
from src.Ejercicio_17 import aleatorio as aleatorio
from src.Ejercicio_17 import adivinaNumero
from src.Ejercicio_16 import *
from src.Ejercicio4 import Area, Perimetro
app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# celcius a fahrenheit


@app.route('/Ejercicio_6', methods=['GET'])
def Ejercicio_6():
    return render_template('Ejercicio_6.html')


@app.route("/celciusToFahrenheit", methods=['POST'])
def celciusToFahrenheit():
    centigrados = float(request.form["centigrados"])
    fahrenheit = converCtoF(centigrados)
    return render_template('Ejercicio_6r.html', f=fahrenheit, c=centigrados)
# adivina numero


@app.route('/Ejercicio_17', methods=['GET'])
def Ejercicio_17():
    random = aleatorio()
    mensaje = "¡Que empiece el juego!"
    return render_template('Ejercicio_17.html', r=random, m=mensaje)


@app.route("/Ejercicio_17", methods=['POST'])
def advinar():
    random = int(request.form["hidden-input"])
    numero = int(request.form["adivinar"])
    mensaje = adivinaNumero(random, numero)
    return render_template('Ejercicio_17.html', r=random, m=mensaje)


@app.route('/Ejercicio_16', methods=['GET'])
def Ejercicio_16():
    numeros = ""
    media = ""
    return render_template('Ejercicio_16.html', m=media, n=numeros)


@app.route('/Ejercicio_16', methods=['POST'])
def aritmetica():
    numeros = stringToList(str(request.form["numeros"]))
    numeros = listStrToFloat(numeros)
    media = float(mediaAritmetica(numeros))
    numeros = ', '.join(str(i) for i in numeros)
    return render_template('Ejercicio_16.html', m=media, n=numeros)

@app.route('/Ejercicio_4', methods=['GET'])
def Ejercicio_4():
    return render_template('Ejercicio_4.html')

@app.route('/AreaYPerimetro', methods=['POST'])
def AreaYPerimetro():
    area=int(request.form["area"])
    perimetro=int(request.form["perimetro"])
    resultadoArea= Area(area)
    resultadoPerimetro= Perimetro(perimetro)
    return render_template('Ejercicio_4r.html',a=resultadoArea, p=resultadoPerimetro)

if __name__ == "__main__":
    app.run(debug=True)
