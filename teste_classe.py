from src.service.service_web_scraping import ServiceWebScaping
from src.utils.utils import salvar_imagem_local

sws = ServiceWebScaping()
sws.pesquisar_produto(codigo_produto='6364025019')
dados = sws.extrair_dados()

for url, imagem in sws.obter_imagens():
    print(url, imagem)

    salvar_imagem_local(url=url, nome_arquivo=imagem)
