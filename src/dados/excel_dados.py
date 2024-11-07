from typing import Generator, Tuple
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Workbook
from openpyxl.styles import Font, Border, Side, Alignment, PatternFill
from src.pacote_log.config_log import logger
from src.dados.arquivo import Arquivo

import os


class ExcelDados(Arquivo[Workbook]):

    def __init__(self, nome_arquivo=None, diretorio=None):
        super().__init__(nome_arquivo, diretorio)
        self.__planilha = self._abrir_arquivo()
        self.__nome_aba = self.__planilha.active.title
        self.__aba = self.__planilha[self.__nome_aba]
        self.__ultima_linha = self.__aba.max_row

    def formatar_linhas(self, cell):
        """Método para formatar tabela"""
        cell.font = Font(bold=True, color="000000")
        cell.border = Border(left=Side(style='thin'), right=Side(style='thin'),
                             top=Side(style='thin'), bottom=Side(style='thin'))
        cell.alignment = Alignment(horizontal="justify", vertical="center")

    def __encontrar_proxima_linha_em_branco(self, coluna: str = 'B') -> int:
        """Encontra a próxima linha em branco a partir de uma coluna específica.

        Args:
            coluna (str): A coluna onde verificar as células em branco.

        Returns:
            int: Número da próxima linha em branco.
        """
        for linha in range(2, self.__ultima_linha + 1):
            if self.__aba[f"{coluna}{linha}"].value is None:
                return linha

        return self.__ultima_linha + 1

    def abrir_arquivo(self) -> Workbook:
        """Método para abrir a planilha

        Returns:
            Workbook: uma planilha
        """
        try:
            planilha = load_workbook(self._caminho_arquivo)
            return planilha
        except FileNotFoundError:
            logger.error('Arquivo não encontrado')
            exit()
        except Exception as e:
            logger.critical(f'FALHA TOTAL: {e}')

    def ler_valores(self) -> Generator[Tuple[str], None, None]:
        """Método para ler os dados de arquivo, banco

        Yields:
            Generator[Tuple[str, str], None, None]: Gerador que retorna a url e o nome do vídeo
        """
        return self.__aba.iter_rows(min_row=2)

    def __formatar_tabela(self, coluna_inicial, valores, linha_para_escrever):
        for col in range(coluna_inicial, coluna_inicial + len(valores)):
            col_letter = self.__aba.cell(row=1, column=col).column_letter

            self.__aba.column_dimensions[col_letter].width = 40
        self.__aba.row_dimensions[linha_para_escrever].height = 300

    def __escrever_dados(self, valores):
        try:

            coluna_inicial = 2
            linha_para_escrever = self.__encontrar_proxima_linha_em_branco()

            self.__formatar_tabela(coluna_inicial=coluna_inicial,
                                   valores=valores, linha_para_escrever=linha_para_escrever)

            for i, valor in enumerate(valores):

                self.formatar_linhas(self.__planilha.active.cell(row=linha_para_escrever,
                                                                 column=coluna_inicial + i, value=valor))
            self.__ultima_linha = max(self.__ultima_linha, linha_para_escrever)
        except Exception as e:
            logger.critical(f'ERRO FATAL: {e}')
            exit()

    def gravar_dados(self, valores):
        """_summary_

        Args:
            valores (_type_): _description_
        """
        try:
            self.__escrever_dados(valores)
            self.__planilha.save(self._caminho_arquivo)

        except OSError as e:
            logger.error(f'Erro de sistema ao salvar o arquivo: {e}')
            exit()
        except Exception as e:
            logger.error(f'Erro ao salvar o arquivo: {e}')
            exit()

    def __del__(self):
        self.__planilha.close()
