import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt

def conectar_banco(usuario, senha, dsn):
    try:
        connection = cx_Oracle.connect(usuario, senha, dsn)
        print("Conexão bem-sucedida ao banco de dados.")
        return connection
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Erro ao conectar ao banco de dados: {error.message}")
        return None

def buscar_clientes_por_estado(connection):
    query = """
    SELECT estado, COUNT(*) as quantidade
    FROM clientes
    GROUP BY estado
    ORDER BY quantidade DESC
    FETCH FIRST 10 ROWS ONLY
    """
    
    df = pd.read_sql(query, connection)
    return df

def gerar_grafico(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['estado'], df['quantidade'], color='blue')
    plt.xlabel('Estado')
    plt.ylabel('Número de Clientes')
    plt.title('Top 10 Estados com Mais Clientes')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Exibir gráfico
    plt.tight_layout()
    plt.show()

def main():
    # Defina suas credenciais e dados de conexão
    usuario = 'seu_usuario'
    senha = 'sua_senha'
    dsn = 'seu_dsn'  # Ex: 'localhost/XE' ou outro DSN

    # Conecta ao banco de dados
    connection = conectar_banco(usuario, senha, dsn)

    if connection:
        # Realiza a busca e gera o gráfico
        df_clientes = buscar_clientes_por_estado(connection)
        gerar_grafico(df_clientes)

        # Fecha a conexão
        connection.close()

if __name__ == "__main__":
    main()