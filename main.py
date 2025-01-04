from tasks.automate_login import login
from tasks.automate_extracao_dados import extracao_dados
def tarefa():
    # executa o processo de login
    login()

    # Executa o outro processo
    extracao_dados()

if __name__ == "__main__":
    tarefa()