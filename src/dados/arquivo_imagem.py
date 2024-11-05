from typing import Generator, Tuple, Any
from src.pacote_log.config_log import logger
from src.dados.arquivo import Arquivo
import requests


class ArquivoImagem(Arquivo[bytes]):
    def __init__(self, nome_arquivo=None, diretorio=None, url: str = None):
        self.__url = url
        super().__init__(nome_arquivo, diretorio)

    def ler_valores(self):
        pass

    def gravar_dados(self):
        self.__url = self.__url.replace('https', 'http')

        response = requests.get(self.__url, verify=False, timeout=10)
        if response.status_code == 200:
            with open(self.__arquivo._caminho_arquivo, "wb") as file:
                file.write(response.content)
