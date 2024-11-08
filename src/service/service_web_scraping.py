import re
from typing import Generator, Tuple, List
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException
)
from src.pacote_log.config_log import logger
from time import sleep


class ServiceWebScaping:
    def __init__(self):

        self.__servico = Service(ChromeDriverManager().install())
        self.__navegador = webdriver.Chrome(service=self.__servico)

    def __clicar_propaganda(self):
        try:
            self.__navegador.find_element(
                By.CLASS_NAME, 'campanha-popup-close').click()
        except Exception:
            pass

    def __abrir_navegador(self):

        try:
            self.__navegador.maximize_window()
        except Exception:
            pass

    def pesquisar_produto(self, codigo_produto: str):
        try:
            self.__abrir_navegador()
            url = f'https://www.vonder.com.br/busca/?departamento=%25%25&busca={codigo_produto}'
            self.__navegador.get(url)
            self.__clicar_propaganda()
            self.__navegador.find_element(By.CLASS_NAME, 'nomeProd').click()
        except NoSuchElementException as e:
            logger.error(
                f'Elemento não encontrado para extração de dados: {e}')
        except StaleElementReferenceException as e:
            logger.error(f'Elemento não está mais no DOM: {e}')
        except WebDriverException as e:
            logger.error(f'Erro do WebDriver ao extrair dados: {e}')

    def extrair_dados(self) -> List[str]:

        try:
            descricao_produto = self.__navegador.find_element(
                By.CLASS_NAME, 'descricaoProd').text.replace('\n', ' ')
            url_produto = self.__navegador.current_url
            descricao_titulo = self.__navegador.find_element(
                By.CLASS_NAME, 'nomeProduto').text.replace("\n", " ")
            conteudo_embalagem = self.__navegador.find_element(
                By.CLASS_NAME, 'descricaoProd').text.replace('\n', ' ')
            conteudo_embalagem_html = self.__navegador.find_element(
                By.CLASS_NAME, 'descricaoProd').get_attribute('outerHTML')
            detalhes_tecnicos = self.__navegador.find_element(
                By.CLASS_NAME, 'abaContent').text.replace(':\n', ': ')
            match = re.search(r'Certificados:.*', conteudo_embalagem)
            certificados = match.group(0) if match else ""
            certificados_html_descricao = self.__navegador.find_element(
                By.CLASS_NAME, 'descricaoProd').get_attribute('outerHTML')
            categoria = '|'.join(self.__navegador.find_element(
                By.CLASS_NAME, 'breadCrumb').text.split('|')[2:4]).replace('\n', '')

            return [descricao_produto, url_produto, descricao_titulo, conteudo_embalagem, conteudo_embalagem_html, detalhes_tecnicos, certificados, certificados_html_descricao, categoria]

        except NoSuchElementException as e:
            logger.error(
                f'Elemento não encontrado para extração de dados: {e}')
            return []
        except StaleElementReferenceException as e:
            logger.error(f'Elemento não está mais no DOM: {e}')
            return []
        except WebDriverException as e:
            logger.error(f'Erro do WebDriver ao extrair dados: {e}')
            return []

    def obter_imagens(self) -> Generator[Tuple[str, str], None, None]:

        try:
            imagens = self.__navegador.find_elements(By.CLASS_NAME, 'selected')
            if imagens:
                for imagem in imagens:
                    try:
                        imagem.find_element(By.TAG_NAME, 'img').click()
                        sleep(5)
                        url_imagem_grande = self.__navegador.find_element(
                            By.CLASS_NAME, 'zoomWrapperImage').find_element(By.TAG_NAME, 'img').get_attribute('src')

                        nome_arquivo = url_imagem_grande.split('/')[-1]
                        yield url_imagem_grande, nome_arquivo
                    except (NoSuchElementException, ElementNotInteractableException) as e:
                        logger.warning(f'Erro ao acessar imagem: {e}')
            else:
                url_imagem_grande = self.__navegador.find_element(
                    By.ID, 'imgProd1').get_attribute('src')
                nome_arquivo = url_imagem_grande.split('/')[-1]
                yield url_imagem_grande, nome_arquivo

        except NoSuchElementException as e:
            logger.error(f'Elemento de imagem não encontrado: {e}')
        except StaleElementReferenceException as e:
            logger.error(f'Elemento de imagem não está mais no DOM: {e}')
        except WebDriverException as e:
            logger.error(f'Erro do WebDriver ao obter imagens: {e}')

    def fechar_navegador(self):
        try:
            self.__navegador.quit()
        except WebDriverException as e:
            logger.error(f'Erro ao fechar o navegador: {e}')
