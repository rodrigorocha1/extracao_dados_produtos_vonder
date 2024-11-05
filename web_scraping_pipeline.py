from src.service.service_web_scraping import ServiceWebScaping
from src.dados.arquivo_imagem import ArquivoImagem
from src.dados.excel_dados import ExcelDados


class WebScrapingPipeline:
    def __init__(self,):
        self.__servico_web_scraping = ServiceWebScaping()
        self.__arquivo_imagem = ArquivoImagem(
            diretorio='img',)
        self.__arquivo_excel = ExcelDados(
            diretorio='docs',  nome_arquivo='planilha_produtos.xlsx',)

    def rodar_servico(self):
        for dado in self.__arquivo_excel.ler_valores():
            codpro,  *resto = dado

        # self.__servico_web_scraping.pesquisar_produto(
        #     codigo_produto='6364025019')
        # dados = self.__servico_web_scraping.extrair_dados()

        # for url, imagem in self.__servico_web_scraping.obter_imagens():

        #     self.__utils.salvar_imagem_local(url=url, nome_arquivo=imagem)


if __name__ == '__main__':
    wsp = WebScrapingPipeline()
    wsp.rodar_servico()
