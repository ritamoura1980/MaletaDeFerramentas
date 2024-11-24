import cx_Oracle
import time

def ler_credenciais(arquivo):
    with open(arquivo, 'r') as f:
        credenciais = [linha.strip().split(',') for linha in f.readlines()]
    return credenciais

def monitorar_conexao(dsn, usuario, senha):
    try:
        connection = cx_Oracle.connect(usuario, senha, dsn)
        print(f"Conexão bem-sucedida com {dsn}.")
        return connection
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Erro ao conectar ao {dsn}: {error.message}")
        return None

def verificar_status(connection, dsn):
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1 FROM DUAL")
            result = cursor.fetchone()
            print(f"Status da conexão para {dsn}: Ativa")
            return True
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            print(f"Erro ao verificar o status da conexão para {dsn}: {error.message}")
            return False
        finally:
            cursor.close()
    else:
        print(f"Conexão não está disponível para {dsn}.")
        return False

def main():
    arquivo_credenciais = "credenciais.txt"
    credenciais = ler_credenciais(arquivo_credenciais)
    
    conexoes = {}
    
    # Estabelecendo conexões
    for dsn, usuario, senha in credenciais:
        conn = monitorar_conexao(dsn, usuario, senha)
        conexoes[dsn] = conn

    while True:
        time.sleep(10)  # Espera 10 segundos entre verificações
        for dsn, connection in conexoes.items():
            verificar_status(connection, dsn)

if __name__ == "__main__":
    main()