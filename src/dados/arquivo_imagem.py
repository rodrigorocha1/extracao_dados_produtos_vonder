from typing import Generator, Generic, Optional, Tuple, Any, TypeVar
from src.pacote_log.config_log import logger
from src.dados.arquivo import Arquivo
import requests
import os
import io
from PIL import Image

T = TypeVar('T', Image.Image, Image.Image)
U = TypeVar('U', bytes, bytes)


class ArquivoImagem(Arquivo[bytes, Image.Image]):
    def __init__(self, nome_arquivo=None, diretorio=None):
        self.__url = None
        super().__init__(nome_arquivo, diretorio)

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    def abrir_arquivo(self) -> Image.Image:
        caminho_imagem = os.path.join(
            self._caminho_arquivo, self._nome_arquivo)

        imagem = Image.open(caminho_imagem)
        return imagem

    def ler_valores(self) -> bytes:
        url = self.__url.replace('https', 'http')

        response = requests.get(url, verify=False, timeout=10)

        return response.content

    # def gravar_dados(self, valores: bytes):
    #     valores_io = io.BytesIO(valores)
    #     imagem = Image.open(valores_io)
    #     caminho_imagem = os.path.join(
    #         self._caminho_arquivo, self._nome_arquivo)
    #     imagem.save(caminho_imagem)
