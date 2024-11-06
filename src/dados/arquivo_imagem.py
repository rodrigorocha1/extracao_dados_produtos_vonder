from typing import Generator, Tuple, Any
from src.pacote_log.config_log import logger
from src.dados.arquivo import Arquivo
import requests
import os


class ArquivoImagem(Arquivo[bytes]):
    def __init__(self, nome_arquivo=None, diretorio=None,):

        super().__init__(nome_arquivo, diretorio)

    def ler_valores(self):
        pass

    def gravar_dados(self, valores):
        valores = valores.replace('https', 'http')

        response = requests.get(valores, verify=False, timeout=10)
        if response.status_code == 200:
            with open(os.path.join(self._caminho_arquivo, self._nome_arquivo), "wb") as file:
                file.write(response.content)
