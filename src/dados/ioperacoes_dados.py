from abc import ABC, abstractmethod
from typing import Generator, Iterable, Tuple


class IOperacaoDados(ABC):

    @abstractmethod
    def ler_valores(self) -> Generator[Tuple[str, str], None, None]:
        """Método para ler os dados de arquivo, banco

        Yields:
            Generator[Tuple[str, str], None, None]: Gerador que retorna a url e o nome do vídeo
        """

        pass

    @abstractmethod
    def gravar_dados(self, **kwargs):
        """Método para gravar dados
        """
        pass
