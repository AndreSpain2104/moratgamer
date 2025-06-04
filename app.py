from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Cargar preguntas desde JSON
with open('data/preguntas.json', encoding='utf-8') as f:
    preguntas = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", preguntas=preguntas)

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.get_json()
    seleccion = data.get("seleccion")
    correcta = data.get("correcta")

    resultado = seleccion == correcta
    return jsonify({"correcto": resultado})

if __name__ == "__main__":
    app.run(debug=True)
