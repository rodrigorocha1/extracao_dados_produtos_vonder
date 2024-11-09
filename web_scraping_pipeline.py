from src.dados.arquivo_imagem import ArquivoImagem
from src.dados.excel_dados import ExcelDados
from src.service.service_web_scraping import ServiceWebScaping
from src.dados.ioperacoes_dados import IOperacaoDados


class WebScrapingPipeline:
    def __init__(self, servico_web_scraping: ServiceWebScaping, arquivo_imagem: IOperacaoDados, arquivo_excel: IOperacaoDados):
        self.__servico_web_scraping = servico_web_scraping
        self.__arquivo_imagem = arquivo_imagem
        self.__arquivo_excel = arquivo_excel

    def rodar_servico(self):
        for chave, dado in enumerate(self.__arquivo_excel.ler_valores()):
            codpro, *resto = dado
            print(codpro.value)
            if codpro.value is not None:
                self.__servico_web_scraping.pesquisar_produto(
                    codigo_produto=codpro.value)
                produtos = self.__servico_web_scraping.extrair_dados()
                print(produtos)
                print(len(produtos))
                self.__arquivo_excel.gravar_dados(valores=produtos)
                self.__arquivo_imagem.diretorio = 'img'
                if chave == 1:
                    print()
                for url, imagem in self.__servico_web_scraping.obter_imagens():
                    self.__arquivo_imagem.nome_arquivo = imagem
                    self.__arquivo_imagem.url = url
                    dados = self.__arquivo_imagem.ler_valores()

                    self.__arquivo_imagem.gravar_dados(dados)


if __name__ == '__main__':
    wsp = WebScrapingPipeline(
        servico_web_scraping=ServiceWebScaping(),
        arquivo_imagem=ArquivoImagem(
            diretorio='img',),
        arquivo_excel=ExcelDados(
            diretorio='docs',  nome_arquivo='planilha_produtos.xlsx',)
    )
    wsp.rodar_servico()
