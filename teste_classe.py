from src.service.service_web_scraping import ServiceWebScaping
from

sws = ServiceWebScaping()
sws.pesquisar_produto(codigo_produto='6364025019')
dados = sws.extrair_dados()

for url, imagem in sws.obter_imagens():
    print(url, imagem)
