from src.dados.ioperacoes_dados import IOperacaoDados
from typing import Generator, Iterable, Optional, Tuple, TypeVar, Generic
from abc import abstractmethod
import os

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class Arquivo(IOperacaoDados[T, U], Generic[T, U, V]):

    def __init__(self, nome_arquivo: Optional[str] = None, diretorio: Optional[str] = None) -> None:
        """_summary_

        Args:
            nome_arquivo (str): nome do arquivo a ser aberto sem extensão
        """
        self._nome_arquivo = nome_arquivo
        self._caminho_base = os.getcwd()
        self._diretorio = diretorio

        self._caminho_arquivo = os.path.join(
            self._caminho_base,
            self._diretorio or '',
            nome_arquivo or ''
        ) if nome_arquivo is not None else os.path.join(
            self._caminho_base,
            self._diretorio or ''
        )

    @property
    def nome_arquivo(self) -> Optional[str]:
        return self._nome_arquivo

    @nome_arquivo.setter
    def nome_arquivo(self, nome_arquivo: str):
        self._nome_arquivo = nome_arquivo

    @property
    def diretorio(self) -> Optional[str]:
        return self._diretorio

    @diretorio.setter
    def diretorio(self, diretorio: str):
        self._diretorio = diretorio

    @abstractmethod
    def ler_valores(self) -> T:
        pass

    @abstractmethod
    def abrir_arquivo(self) -> T:
        pass

    @abstractmethod
    def gravar_dados(self, valores: U) -> None:

        pass
