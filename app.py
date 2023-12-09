from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

# Caminho para a pasta com os arquivos JSON
DATA_FOLDER = os.path.join('finals_data')

@app.route('/')
def index():
    # Renderiza o index.html que deve estar na pasta 'templates'
    return render_template('index.html')

@app.route('/api-endpoint', methods=['POST'])
def get_finals_data():
    # Pega o JSON enviado pelo JavaScript
    data = request.get_json()

    # Pega o ano da final do JSON recebido
    year = data.get('ano_da_final')

    # Caminho para o arquivo JSON baseado no ano recebido
    data_file = os.path.join(DATA_FOLDER, f'{year}.json')

    # Verifica se o arquivo existe
    if os.path.isfile(data_file):
        # Abre o arquivo JSON e retorna o conteúdo
        with open(data_file, 'r', encoding='utf-8') as file:
            final_data = json.load(file)
            return jsonify(final_data)
    else:
        # Se o arquivo não existir, retorna um erro 404
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
