from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from datetime import datetime

def extracao_dados():
    # abrir o navegador
    navegador = webdriver.Chrome()

    try:
        # acessar a página
        navegador.get("https://tradingeconomics.com/matrix")
        
        # colocar navegador em tela cheia
        navegador.maximize_window()
        
        # procurar a tabela
        tabela = navegador.find_element(By.ID, "matrix")
        
        # certificar que esta na tela
        navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", tabela)
        espera = WebDriverWait(navegador, 10)
        espera.until(EC.presence_of_element_located((By.ID, "matrix")))

        # pegando os nomes das colunas
        header_row = tabela.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "th")
        header = [col.text for col in header_row]

        # pegando as linhas da tabela
        rows = tabela.find_elements(By.TAG_NAME, "tr")
        data_tabela = []

        # adicionando os dados
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")  # colunas
            if cols:
                data_tabela.append([col.text for col in cols])  # adiciona o texto

        # escrevendo os dados no arquivo CSV
        with open('csv//extracted_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # escreve o cabeçalho da tabela
            writer.writerow(header)
            
            # escreve as linhas de dados
            writer.writerows(data_tabela)

        print("Dados salvos no arquivo 'extracted_data.csv' com sucesso.")

    except Exception as e:
        print(f"ocorreu um erro: {e}")
        with open('log//log.txt', 'a') as file:
            file.write(f'{datetime.now().strftime('%Y-%m-%d %H:%m')} Ocorreu um erro durante o processo de login: {e}\n')
        navegador.quit()
    finally:
        # Fechar o navegador
        navegador.quit()
