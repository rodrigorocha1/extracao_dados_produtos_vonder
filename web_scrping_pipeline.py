from src.service.service_web_scraping import ServiceWebScaping
from src.utils.utils import Utils


class WebScrapingPipeline:
    def __init__(self):
        self.__servico_web_scraping = ServiceWebScaping()
        self.__utils = Utils()

    def rodar_servico(self):

        self.__servico_web_scraping.pesquisar_produto(
            codigo_produto='6364025019')
        dados = self.__servico_web_scraping.extrair_dados()
        for url, imagem in self.__servico_web_scraping.obter_imagens():
            print(url, imagem)

            self.__utils(url=url, nome_arquivo=imagem)
