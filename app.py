from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/Ejercicio_6', methods=['GET'])
def Ejercicio_6():
    return render_template('Ejercicio_6.html')


if __name__ == "__main__":
    app.run(debug=True)
