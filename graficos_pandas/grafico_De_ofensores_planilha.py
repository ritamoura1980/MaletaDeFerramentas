import pandas as pd
import matplotlib.pyplot as plt

# Função para ler o arquivo Excel e processar os dados
def processar_dados(arquivo):
    # Lê o arquivo Excel
    df = pd.read_excel(arquivo)

    # Agrupa os dados pela coluna 'Ofensor' e soma as quantidades
    resumo = df.groupby('Ofensor')['Quantidade'].sum().reset_index()

    return resumo

# Função para gerar o gráfico
def gerar_grafico(resumo):
    plt.figure(figsize=(10, 6))
    plt.bar(resumo['Ofensor'], resumo['Quantidade'], color='blue')
    plt.xlabel('Ofensor')
    plt.ylabel('Quantidade de Problemas')
    plt.title('Quantidade de Problemas por Ofensor')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Exibe o gráfico
    plt.tight_layout()
    plt.show()

def main():
    # Nome do arquivo Excel
    arquivo = 'problemas.xlsx'

    # Processa os dados e gera o gráfico
    resumo = processar_dados(arquivo)
    gerar_grafico(resumo)

if __name__ == "__main__":
    main()