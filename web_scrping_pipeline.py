from src.service.service_web_scraping import ServiceWebScaping
from src.utils.utils import Utils


class WebScrapingPipeline:
    def __init__(self, servico_web_scraping: ServiceWebScaping,  utils:  Utils):
        self.__servico_web_scraping = servico_web_scraping
        self.__utils = utils

    def rodar_servico(self):

        self.__servico_web_scraping.pesquisar_produto(
            codigo_produto='6364025019')
        dados = self.__servico_web_scraping.extrair_dados()
        for url, imagem in self.__servico_web_scraping.obter_imagens():

            self.__utils.salvar_imagem_local(url=url, nome_arquivo=imagem)


if __name__ == '__main__':
    wsp = WebScrapingPipeline(
        servico_web_scraping=ServiceWebScaping()
        utils=Utils()
    )
