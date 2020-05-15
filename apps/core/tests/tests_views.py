from django.test import TestCase
from django.test import Client

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# Create your tests here.

class AcessosViewTestCase(TestCase):

    def test_home_acesso(self):

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        
        driver.get('http://127.0.0.1:8000/')
        assert "Observatório UFJ Covid-19 - Principal" in driver.title
        assert "Este observatório é uma iniciativa do" in driver.page_source

        driver.close()

    def test_reportagem_tv_sudoeste(self):

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())
        
        driver.get('http://127.0.0.1:8000/na-midia')
        manchete = "Projeto de extensão da UFJ traz informações atualizadas sobre casos de coronavírus"
        assert manchete in driver.page_source
        
        driver.close()
