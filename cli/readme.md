# Sistema CRUD - CLI e GUI

Sistema de gerenciamento de dados interligado, operando com um banco de dados PostgreSQL centralizado.

* `database.py`: O "motor" do sistema. Cria as tabelas e gerencia as transações SQL.
* `cli.py`: Interface de Linha de Comando.
* `gui.py`: Interface Gráfica de Usuário.

## 1. Configuração do Banco de Dados (Servidor)

Ajuste as variáveis `DB_NAME`, `DB_USER` e `DB_PASS` no início do arquivo `database.py` com as informações do seu ambiente.

No servidor PostgreSQL, acesse o painel de administração:
> sudo -u postgres psql

Execute os seguintes comandos para estruturar o ambiente:
> CREATE DATABASE produtostrab;
> CREATE USER julio WITH PASSWORD '123456';
> GRANT ALL PRIVILEGES ON DATABASE produtostrab TO julio;
> \q

**Nota de Rede:** Garanta que o arquivo `pg_hba.conf` no servidor esteja configurado para aceitar conexões da rede do cliente via método `md5` ou `scram-sha-256`.

## 2. Preparação do Ambiente (Cliente Linux/Ubuntu)

Instale os pacotes base do sistema operacional necessários para a interface gráfica e para a criação do ambiente virtual:
> sudo apt update
> sudo apt install python3-tk python3-venv -y

Navegue até o diretório do projeto e isole as dependências:
> python3 -m venv env_crud
> source env_crud/bin/activate

Com o ambiente ativado, instale o driver do PostgreSQL:
> pip install psycopg2-binary

## 3. Execução

Mantenha o ambiente virtual ativado `(env_crud)`. 

Para iniciar a versão em Linha de Comando:
> python3 cli.py

Para iniciar a versão em Interface Gráfica:
> python3 gui.py
