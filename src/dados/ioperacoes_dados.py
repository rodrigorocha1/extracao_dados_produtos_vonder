from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterable

# Definindo um TypeVar T que representará o tipo dos dados
T = TypeVar('T')
U = TypeVar('U')


class IOperacaoDados(ABC, Generic[T, U]):

    @abstractmethod
    def ler_valores(self) -> T:

        pass

    @abstractmethod
    def gravar_dados(self, valores: U) -> None:

        pass
