from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def sanitizar(texto):
    # Simplificado para o exemplo
    texto = re.sub(r'\b[1235689]\d{8}\b', '[NIF BLOQUEADO]', texto)
    texto = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[EMAIL BLOQUEADO]', texto)
    return texto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    msg_usuario = request.json.get('mensagem')
    msg_protegida = sanitizar(msg_usuario)
    return jsonify({"original": msg_usuario, "filtrada": msg_protegida})

if __name__ == '__main__':
    app.run(debug=True)