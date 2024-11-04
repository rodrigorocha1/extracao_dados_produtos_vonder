import requests
import os


def salvar_imagem_local(url: str, nome_arquivo: str):
    caminho_base = os.getcwd()
    caminho_aquivo = os.path.join(caminho_base, 'img', nome_arquivo)

    response = requests.get(url)
    if response.status_code == 200:
        with open(caminho_aquivo, "wb") as file:
            file.write(response.content)
