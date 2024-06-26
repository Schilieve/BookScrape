

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/"

driver.get(url)
time.sleep(1)

links = driver.find_elements(By.TAG_NAME,"a")
print(links)
print(len(links))

# os livros começam no 54 e terminam no 92 e vamos de 2 em 2

x = driver.find_elements(By.TAG_NAME,"a")[54].text
print(x)

y = driver.find_elements(By.TAG_NAME,"a")[54].get_attribute("title")
print(y)

print(driver.find_elements(By.TAG_NAME,"a")[54:94:2])
elementos_titulo = driver.find_elements(By.TAG_NAME,"a")[54:94:2]

lista_titulos = [title.get_attribute("title") for title in elementos_titulo]
print(lista_titulos)

elementos_titulo[1].click()
time.sleep(2)

stok = driver.find_element(By.CLASS_NAME,"instock").text
time.sleep(2)
print(stok)

estoque = int(stok.replace("In stock (","").replace("available)",""))
print(estoque)


driver.back()
lista_estoque = []

for titulo in elementos_titulo:
    titulo.click()
    time.sleep(1)
    qtd = int(driver.find_element(By.CLASS_NAME,"instock").text.replace("In stock (","").replace("available)",""))
    lista_estoque.append(qtd)
    driver.back()
    time.sleep(1)

print(lista_estoque)

data ={"Titulo":lista_titulos,"Estoque":lista_estoque}
print(pd.DataFrame(data))

dados = pd.DataFrame(data)

dados.to_excel("dados.xlsx")