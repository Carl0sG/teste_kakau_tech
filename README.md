instruçôes para a execução da tarefa


passo 1: criação do ambiente virtual

- escolha um diretorio de sua preferencia, abra um terminal nesse diretorio e execute o comando:

    python -m venv env


passo 2: ativar o ambiente virtual

- ativação em SO windows

    abra um terminal onde o ambiente virtual esta instalado e execute o comando:

        .\env\Scripts\activate

- ativação em SO linux

    abra um terminal onde o ambiente virtual esta instalado e execute o comando:

        source ./env/bin/activate


passo 3: instalar as bibliotecas necessarias

    pip install -r requirements.txt


passo 4: executar o arquivo main.py

    python main.py