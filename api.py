import os
import requests
import csv
from flask import Flask, jsonify


########### DESAFIO PARTE 2{  ###########

# URl
url = "https://jsonplaceholder.typicode.com/comments"

# REquisição GET.
response = requests.get(url)

# Verificar requesição.
if response.status_code == 200:

    comments_data = response.json()

    # Nome arquivo CSV gerado.
    csv_filename = "orbitDF.csv"

    # Caminho de saida do arquivo.
    output_folder = "./saida"

    # Caso o caminho de saida não exista, será criado.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Caminho do arquivo CSV.
    csv_filepath = os.path.join(output_folder, csv_filename)

    # Abrir o arquivo CSV em modo de escrita.
    with open(csv_filepath, mode="w", newline="", encoding="utf-8") as csv_file:

        csv_writer = csv.writer(csv_file)

        # Escreve o cabeçalho do arquivo CSV.
        csv_writer.writerow(["postId", "id", "name", "email", "body"])

        # Escreve cada linha no arquivo CSV
        for comment in comments_data:
            csv_writer.writerow([comment["postId"], comment["id"],
                                comment["name"], comment["email"], comment["body"]])

    print(f"Os dados foram exportados para {csv_filepath}")
else:
    print(f"Erro na requisição. Código de status: {response.status_code}")

########### FIM DESAFIO PARTE 2 } ###########


########### DESAFIO PARTE 3 { ###########

## API ##
app = Flask(__name__)


@app.route('/api/comments', methods=['GET'])
def get_comments():
    # Caminho do arquivo CSV.
    csv_file = "./saida/orbitDF.csv"

    # ler arquivo CSV.
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        comments_data = [row for row in csv_data]

    return jsonify(comments_data)


if __name__ == '__main__':
    app.run()

########### FIM DESAFIO PARTE 3 } ###########
