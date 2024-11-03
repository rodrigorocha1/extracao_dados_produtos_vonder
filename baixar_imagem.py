import requests


url = "http://www.vonder.com.br/estatico/vonder/temp/320_7074000630.jpg"
# Nome do arquivo local onde a imagem será salva

filename = "imagem_vonder.jpg"
# Fazendo o download da imagem

filename = "imagem_vonder.jpg"

response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as file:
        file.write(response.content)
