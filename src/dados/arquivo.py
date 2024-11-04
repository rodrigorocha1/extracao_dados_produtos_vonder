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

        self._caminho_arquivo = os.path.join(
            self._caminho_base, diretorio, nome_arquivo) if nome_arquivo is not None else os.path.join(
            self._caminho_base, diretorio)

    @abstractmethod
    def ler_valores(self) -> Generator[Tuple[str, str], None, None]:
        """Método para ler os dados de arquivo, banco

        Yields:
            Generator[Tuple[str, str], None, None]: Gerador que retorna a url e o nome do vídeo
        """
        pass

    @abstractmethod
    def _abrir_arquivo(self) -> T:
        """_summary_

        Returns:
            T: Retorna o arquivo aberto
        """
        pass

    @abstractmethod
    def gravar_dados(self):
        """Método para gravar dados
        """
        pass

    @abstractmethod
    def salvar_dados(self):

        pass
