# Importando Bibliotecas e métodos

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Pichau\Downloads\Python Impressionador\Arquivos Notas",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

import os
import time


# Passo 1: Entrar no navegador

caminho = os.getcwd()
arquivo = caminho + r"\login.html"
navegador.get(arquivo)

# Passo 2: Preencher login e senha

navegador.find_element(By.XPATH, "/html/body/div/form/input[1]").send_keys('Thais', Keys.TAB, '123')
time.sleep(1)
navegador.find_element(By.XPATH, "/html/body/div/form/button").click()

# Passo 3/4/5: Preencher os campos do sistema para cada linha da tabela e finalizar o programa

import pandas as pd 

tabela_notas = pd.read_excel("NotasEmitir.xlsx")

for linha in tabela_notas.index:
    #Nome/Razão Social
    navegador.find_element(By.NAME, 'nome').send_keys(tabela_notas.loc[linha, "Cliente"])
    time.sleep(1)
    #Endereço
    navegador.find_element(By.NAME, 'endereco').send_keys(tabela_notas.loc[linha, "Endereço"])
    #Bairro
    navegador.find_element(By.NAME, 'bairro').send_keys(tabela_notas.loc[linha, "Bairro"])
    #Município
    navegador.find_element(By.NAME,'municipio').send_keys(tabela_notas.loc[linha, "Municipio"])
    #CEP
    navegador.find_element(By.NAME, 'cep').send_keys(str(tabela_notas.loc[linha, "CEP"]))
    #UF
    navegador.find_element(By.NAME, 'uf').send_keys(tabela_notas.loc[linha, "UF"])
    #CPF/CNPJ
    navegador.find_element(By.NAME, 'cnpj').send_keys(str(tabela_notas.loc[linha, "CPF/CNPJ"]))
    #Inscrição Estadual
    navegador.find_element(By.NAME, 'inscricao').send_keys(str(tabela_notas.loc[linha, "Inscricao Estadual"]))
    #Descrição
    texto = tabela_notas.loc[linha, "Descrição"]
    navegador.find_element(By.NAME, 'descricao').send_keys(texto)
    # Quantidade
    navegador.find_element(By.NAME, 'quantidade').send_keys(str(tabela_notas.loc[linha, "Quantidade"]))
    #Valor Unitário
    navegador.find_element(By.NAME, 'valor_unitario').send_keys(str(tabela_notas.loc[linha, "Valor Unitario"]))
    #Valor Total
    navegador.find_element(By.NAME, 'total').send_keys(str(tabela_notas.loc[linha, "Valor Total"]))
    
    #Clicar em Emitir Nota Fiscal
    navegador.find_element(By.CLASS_NAME, 'registerbtn').click()
    
    #Recarregar página para limpar formulário
    navegador.refresh()

navegador.quit()

