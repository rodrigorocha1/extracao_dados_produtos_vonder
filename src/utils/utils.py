import requests
import os
from src.dados.arquivo import Arquivo


class Utils:

    def salvar_dados(self, url: str):
        url = url.replace('https', 'http')

        response = requests.get(url, verify=False, timeout=10)
        if response.status_code == 200:
            # with open(self.__arquivo._caminho_arquivo, "wb") as file:
            #     file.write(response.content)
            print(type(response.content))
            return response.content
