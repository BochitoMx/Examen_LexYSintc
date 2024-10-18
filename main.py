from flask import Flask, render_template, request, jsonify
from lexer import analizar_codigo
from parser import analizar_sintaxis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    codigo = request.json.get('code', '')

    resultado_lexico = analizar_codigo(codigo)
    resultado_sintactico = analizar_sintaxis(codigo)

    return jsonify({
        'lexical': resultado_lexico,
        'syntactic': resultado_sintactico if resultado_sintactico else "Error de sintaxis"
    })

if __name__ == '__main__':
    app.run(debug=True)
