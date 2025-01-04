from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def login():
    # abrir o navegador
    navegador = webdriver.Chrome()

    try:
        # acessar a pagina
        navegador.get("https://practicetestautomation.com/practice-test-login/")

        # colocar navegador em tela cheia
        navegador.maximize_window()

        # preencher o formulario
        navegador.find_element(By.ID, "username").send_keys("student")
        navegador.find_element(By.ID, "password").send_keys("Password123")

        # procurar botao submit
        botao_confirmar = navegador.find_element(By.ID, "submit")

        # scroll pra certificar que o botao esta na tela
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", botao_confirmar)
        espera = WebDriverWait(navegador, 5)
        espera.until(EC.element_to_be_clickable((By.ID, "submit")))
        botao_confirmar.click()

        # Exemplo 2: Verificar a presença de um elemento específico pós-login
        mensagem_sucesso = espera.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Logged In Successfully')]"))
            ) 
        if mensagem_sucesso:
            print("Login bem-sucedido!")
            
    except Exception as e:
        print(f"Ocorreu um erro durante o processo de login: {e}")
        with open('log\\log.txt', 'a') as file:
            file.write(f'{datetime.now().strftime('%Y-%m-%d %H:%m')} Ocorreu um erro durante o processo de login: {e}\n')
        navegador.quuit()
        
    finally:
        # aguardar um tempo antes de fechar
        time.sleep(5)
        # Fechar o navegador
        navegador.quit()
