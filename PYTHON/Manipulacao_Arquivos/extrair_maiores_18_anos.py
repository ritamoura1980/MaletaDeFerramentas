def extrair_clientes_maioridade(arquivo):
    try:
        with open(arquivo, 'r') as file:
            clientes_maiores = []
            for linha in file:
                dados = linha.strip().split(',')  # Supondo que os dados são separados por vírgula
                if len(dados) >= 5:  # Assegurando que há pelo menos 5 campos
                    nome = dados[0]
                    idade = dados[1]
                    sexo = dados[2]
                    endereco = dados[3]

                    # Verifica se a idade é superior a 18
                    if idade.isdigit() and int(idade) > 18:
                        clientes_maiores.append((nome, idade, sexo, endereco))
        
        return clientes_maiores

    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

# Nome do arquivo a ser lido
arquivo_clientes = 'clientes.txt'
clientes_maiores = extrair_clientes_maioridade(arquivo_clientes)

# Exibindo os clientes maiores de idade
for cliente in clientes_maiores:
    print(cliente)