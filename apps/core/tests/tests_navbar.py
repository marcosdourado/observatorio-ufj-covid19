from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class NavbarTestCase(TestCase):
    
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.driver.close()
    
    def test_pag_default(self):
        self.driver.get('http://127.0.0.1:8000/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == True 
        assert is_active_grafico == False  
        assert is_active_tendencias == False 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    def test_pag_grafico_jatai(self):
        self.driver.get('http://127.0.0.1:8000/graficos/jatai/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == True  
        assert is_active_tendencias == False 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    
    
    def test_pag_grafico_mineiros(self):
        self.driver.get('http://127.0.0.1:8000/graficos/mineiros/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == True  
        assert is_active_tendencias == False 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False
    
    def test_pag_grafico_rioverde(self):
        self.driver.get('http://127.0.0.1:8000/graficos/rioverde/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == True  
        assert is_active_tendencias == False 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    def test_pag_comparacao(self):
        self.driver.get('http://127.0.0.1:8000/comparacao/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == True  
        assert is_active_tendencias == False 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    def test_pag_como_sao_criados(self):
        self.driver.get('http://127.0.0.1:8000/como-sao-criados/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == True  
        assert is_active_tendencias == False 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    def test_pag_tendencias_jatai(self):
        self.driver.get('http://127.0.0.1:8000/tendencias/jatai/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == True 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    def test_pag_tendencias_rioverde(self):
        self.driver.get('http://127.0.0.1:8000/tendencias/rioverde/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == True 
        assert is_active_simulacao == False
        assert is_active_saiba_mais == False

    def test_pag_simulacao(self):
        self.driver.get('http://127.0.0.1:8000/simulacao')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == False 
        assert is_active_simulacao == True
        assert is_active_saiba_mais == False
    
    def test_pag_sobre(self):
        self.driver.get('http://127.0.0.1:8000/sobre/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == False
        assert is_active_simulacao == False
        assert is_active_saiba_mais == True
    
    def test_pag_equipe(self):
        self.driver.get('http://127.0.0.1:8000/equipe/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == False
        assert is_active_simulacao == False
        assert is_active_saiba_mais == True
    
    def test_pag_na_midia(self):
        self.driver.get('http://127.0.0.1:8000/na-midia/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == False
        assert is_active_simulacao == False
        assert is_active_saiba_mais == True

    def test_pag_colabore(self):
        self.driver.get('http://127.0.0.1:8000/colabore/')

        is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais = self.__carrega_status_menus()

        assert is_active_main == False 
        assert is_active_grafico == False 
        assert is_active_tendencias == False
        assert is_active_simulacao == False
        assert is_active_saiba_mais == True

    def __carrega_status_menus(self):
        principal_element = self.driver.find_element_by_xpath('//*[@id="navbarColor01"]/ul/li[1]')
        grafico_element= self.driver.find_element_by_id("navbarDropdownGraficos")
        tendencia_element= self.driver.find_element_by_id("navbarDropdownTendencias")
        simulacao_element= self.driver.find_element_by_id("navbarMenuSimulacao")
        saiba_mais_element= self.driver.find_element_by_id("navbarDropdownConhecaMais")

        is_active_main = "active" in principal_element.get_attribute("class")
        is_active_grafico = "active" in grafico_element.get_attribute("class")
        is_active_tendencias = "active" in tendencia_element.get_attribute("class")
        is_active_simulacao = "active" in simulacao_element.get_attribute("class")
        is_active_saiba_mais = "active" in saiba_mais_element.get_attribute("class")
        return is_active_main, is_active_grafico, is_active_tendencias, is_active_simulacao, is_active_saiba_mais