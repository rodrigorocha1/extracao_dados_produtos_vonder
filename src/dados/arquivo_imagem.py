from typing import Generator, Optional, Tuple, Any
from src.pacote_log.config_log import logger
from src.dados.arquivo import Arquivo
import requests
import os
import io
from PIL import Image


class ArquivoImagem(Arquivo[Image.Image]):
    def __init__(self, nome_arquivo=None, diretorio=None):
        self.__url = None
        super().__init__(nome_arquivo, diretorio)

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    def abrir_arquivo(self) -> Optional[Image.Image]:
        caminho_imagem = os.path.join(
            self._caminho_arquivo, self._nome_arquivo)
        if os.path.exists(caminho_imagem):
            imagem = Image.open(caminho_imagem)
            return imagem
        return None

    def ler_valores(self) -> Optional[bytes]:
        url = self.__url.replace('https', 'http')

        response = requests.get(url, verify=False, timeout=10)
        if response.status_code == 200:
            return response.content
        return None

    def gravar_dados(self, valores: bytes):
        valores = io.BytesIO(valores)
        imagem = Image.open(valores)
        caminho_imagem = os.path.join(
            self._caminho_arquivo, self._nome_arquivo)
        imagem.save(caminho_imagem)
