import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
url = 'https://www.vonder.com.br/busca/?departamento=%25%25&busca=6220111211'
navegador.get(url)

navegador.find_element(By.CLASS_NAME, 'campanha-popup-close').click()

navegador.find_element(By.CLASS_NAME, 'nomeProd').click()


print(navegador.current_url)  # URL FORNECEDOR e código fornecedor


navegador.find_element(By.CLASS_NAME, 'nomeProduto').text.replace(
    "\n", " ")  # Descrição título

# Baixar imagem
# selected over


navegador.find_element(
    By.XPATH, '//*[@id="itensProd"]/div/div[1]/div[4]/p[2]/b').text

navegador.find_element(By.ID, 'imgProd1').get_attribute('src')


conteudo_embalagem = navegador.find_element(By.CLASS_NAME, 'descricaoProd').text.replace(
    '\n', ' ')  # CONTEUDO EMBALAGEM

partes = ' '.join(conteudo_embalagem.split('Certificados'))

navegador.find_element(By.CLASS_NAME, 'descricaoProd').get_attribute(
    'outerHTML')  # CONTEUDO EMBALAGEM HTML

navegador.find_element(By.CLASS_NAME, 'abaContent').text.replace(
    ':\n', ': ')  # Detalhes tecnicos


texto = "Conteúdo da Embalagem: 1 Escudo para solda. Acompanha lente incolor. Proteção facial, com visor fixo. Certificados: 3702 Indicada para proteção facial em processos de solda em geral. Garantia legal: 90 dias"
match = re.search(r'Certificados:.*', conteudo_embalagem)

resultado = match.group(
    0) if match else ""
print(resultado)

url = "http://www.vonder.com.br/estatico/vonder/temp/320_7074000630.jpg"


filename = "imagem_vonder.jpg"

response = requests.get(url)
if response.status_code == 200:
    with open(filename, "wb") as file:
        file.write(response.content)


navegador.find_element(By.CLASS_NAME, 'descricaoProd').text


elemento = navegador.find_element(By.CLASS_NAME, 'descricaoProd')

# Extrai o HTML do elemento
html_elemento = elemento.get_attribute('outerHTML')  # descrição html


elemento = navegador.find_element(By.CLASS_NAME, 'breadCrumb')

html_elemento = elemento.get_attribute('outerHTML')

'|'.join(navegador.find_element(By.CLASS_NAME,
                                'breadCrumb').text.split('|')[2:4]).replace('\n', '')  # categoria


imagens = navegador.find_elements(By.CLASS_NAME, 'selected')

imagem_teste = navegador.find_elements(By.CLASS_NAME, 'selected')

len(imagem_teste)
for chave, imagem in enumerate(imagens):
    imagem_pequena = imagem.find_element(By.TAG_NAME, 'img').click()
    imagem_grande = navegador.find_element(
        By.ID, 'imgPrinc_1').get_attribute('src')
    print(imagem_grande)
    if chave == 1:
        break


imagem_pequena = navegador.find_element(
    By.ID, 'imgProd1').get_attribute('src')


elementos = navegador.find_elements(By.CLASS_NAME, 'selected')
for elemento in elementos:
    images = elemento.find_elements(By.TAG_NAME, 'img')
    print(images)
    for img in images:
        # Aqui você pode fazer o que precisar com cada imagem
        print(img.get_attribute('src'))


navegador.find_element(
    By.CLASS_NAME, 'zoomWrapperImage').find_element(By.TAG_NAME, 'img').get_attribute('src')
