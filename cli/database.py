import psycopg2

# Configuracoes de conexao
DB_HOST = "192.168.56.101"
DB_NAME = "produtostrab"
DB_USER = "julio"
DB_PASS = "123456"
DB_PORT = "5432"

def conectar():
    """Estabelece e retorna a conexao com o PostgreSQL."""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

def inicializar_banco():
    """Cria a tabela caso nao exista. O tipo SERIAL e usado para autoincremento."""
    try:
        with conectar() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS produtostrab (
                        codigo SERIAL PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        descricao TEXT NOT NULL
                    )
                ''')
            conn.commit()
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL no host {DB_HOST}. Verifique o servico e as credenciais. Detalhes: {e}")

def incluir(nome, descricao):
    with conectar() as conn:
        with conn.cursor() as cursor:
            # Correcao: Inserindo na tabela produtostrab
            cursor.execute('INSERT INTO produtostrab (nome, descricao) VALUES (%s, %s)', (nome, descricao))
        conn.commit()

def listar_todos():
    with conectar() as conn:
        with conn.cursor() as cursor:
            # Correcao: Lendo da tabela produtostrab
            cursor.execute('SELECT * FROM produtostrab ORDER BY codigo ASC')
            return cursor.fetchall()

def buscar_por_codigo(codigo):
    with conectar() as conn:
        with conn.cursor() as cursor:
            # Correcao: Buscando na tabela produtostrab
            cursor.execute('SELECT * FROM produtostrab WHERE codigo = %s', (codigo,))
            return cursor.fetchone()

def buscar_por_nome(nome):
    with conectar() as conn:
        with conn.cursor() as cursor:
            # Correcao: Buscando na tabela produtostrab
            cursor.execute('SELECT * FROM produtostrab WHERE nome ILIKE %s', ('%' + nome + '%',))
            return cursor.fetchall()

def alterar(codigo, novo_nome, nova_descricao):
    with conectar() as conn:
        with conn.cursor() as cursor:
            # Correcao: Atualizando a tabela produtostrab
            cursor.execute('UPDATE produtostrab SET nome = %s, descricao = %s WHERE codigo = %s', 
                           (novo_nome, nova_descricao, codigo))
        conn.commit()

def excluir(codigo):
    with conectar() as conn:
        with conn.cursor() as cursor:
            # Correcao: Excluindo da tabela produtostrab
            cursor.execute('DELETE FROM produtostrab WHERE codigo = %s', (codigo,))
        conn.commit()

# Executa a verificacao da tabela ao importar o modulo
inicializar_banco()
