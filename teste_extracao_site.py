import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()
url = 'https://www.vonder.com.br/busca/?departamento=%25%25&busca=3662254000'
navegador.get(url)

navegador.find_element(By.CLASS_NAME, 'campanha-popup-close').click()

navegador.find_element(By.CLASS_NAME, 'nomeProd').click()


print(navegador.current_url)  # URL FORNECEDOR e código fornecedor


navegador.find_element(By.CLASS_NAME, 'nomeProduto').text.replace(
    "\n", " ")  # Descrição título

# Baixar imagem
# selected over

if navegador.find_element(By.ID, 'thumblist') is None:
    print('Vazio')


navegador.find_element(By.ID, 'imgProd1').get_attribute('src')


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
len(imagens)
for chave, imagem in enumerate(imagens):
    imagem_pequena = imagem.find_element(By.TAG_NAME, 'img').click()
    imagem_grande = navegador.find_element(
        By.ID, 'imgProd1').get_attribute('src')
    print(imagem_grande)
    if chave == 1:
        break
