# python -m pip install selenium
# para rodar = python aula10_04_2026/desafio_robt.py


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time


#________ fase 1__________

opcoes = Options()

opcoes.add_argument("--headless=new")
opcoes.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=opcoes)

print("🌍 🌎 🌏")

driver.get("https://the-internet.herokuapp.com/dropdown")
print(f"👽 {driver.title} aberta com sucesso!!")

driver.implicitly_wait(10)


#_____ trocar abas_____

driver.execute_script("window.open('https://the-internet.herokuapp.com/dynamic_loading/2')")


WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

#delay para trocar abas
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

driver.execute_script("window.open('https://pt.wikipedia.org')")

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
driver.switch_to.window(driver.window_handles[2])

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
driver.switch_to.window(driver.window_handles[0])

menu_suspenso = driver.find_element(By.ID, "dropdown")
menu = Select(menu_suspenso)
menu.select_by_visible_text("Option 1")

opcao_selecionada = menu.first_selected_option
valor_opcao = opcao_selecionada.get_attribute("value")

print("Start selecionado 🚀")
print(opcao_selecionada.text)
print(valor_opcao)

driver.switch_to.window(driver.window_handles[1])

botao_start = driver.find_element(By.CSS_SELECTOR, "#start button")
botao_start.click()

elemento_secreto = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

print(elemento_secreto.text)

driver.switch_to.window(driver.window_handles[2])

barra_pesquisa = driver.find_element(By.NAME, "search")
barra_pesquisa.send_keys("Automacao")

link_lateral = driver.find_element(By.CSS_SELECTOR, "#p-navigation li a")

print(link_lateral.text)
print(link_lateral.get_attribute("href"))

driver.save_screenshot("evidencia_wiki.png")

driver.quit()
