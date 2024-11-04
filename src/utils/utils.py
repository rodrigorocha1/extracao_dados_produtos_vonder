import requests
import os
from src.dados.arquivo import Arquivo


class Utils(Arquivo):
    def __init__(self, nome_arquivo=None, diretorio=None):
        super().__init__(nome_arquivo, diretorio)

    def salvar_dados(self, url: str):
        url = url.replace('https', 'http')

        response = requests.get(url, verify=False, timeout=10)
        if response.status_code == 200:
            with open(self._caminho_arquivo, "wb") as file:
                file.write(response.content)
