from src.dados.ioperacoes_dados import IOperacaoDados
from typing import Generator, Tuple, TypeVar, Generic
from abc import abstractmethod
import os

T = TypeVar('T')


class Arquivo(IOperacaoDados, Generic[T]):
    def __init__(self, nome_arquivo: str = None, diretorio: str = None) -> None:
        """_summary_

        Args:
            nome_arquivo (str): nome do arquivo a ser aberto sem extensao 
        """
        self._nome_arquivo = nome_arquivo
        self._caminho_base = os.getcwd()
        self._diretorio = diretorio

        self._caminho_arquivo = os.path.join(
            self._caminho_base, self._diretorio, nome_arquivo) if nome_arquivo is not None else os.path.join(
            self._caminho_base, self._diretorio)

    @property
    def nome_arquivo(self):
        return self._nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo

    @property
    def diretorio(self):
        return self._diretorio

    @diretorio.setter
    def diretorio(self, diretorio):
        self._diretorio = diretorio

    @abstractmethod
    def abrir_arquivo(self) -> T:
        pass

    @abstractmethod
    def ler_valores(self) -> Generator[Tuple[str, str], None, None]:
        """Método para ler os dados de arquivo, banco

        Yields:
            Generator[Tuple[str, str], None, None]: Gerador que retorna a url e o nome do vídeo
        """
        pass

    @abstractmethod
    def gravar_dados(self, valores):
        """Método para gravar dados
        """
        pass
