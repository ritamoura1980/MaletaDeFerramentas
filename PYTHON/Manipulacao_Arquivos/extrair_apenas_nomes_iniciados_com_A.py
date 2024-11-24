def extrair_clientes_nome_a(arquivo):
    try:
        with open(arquivo, 'r') as file:
            clientes_nome_a = []
            for linha in file:
                dados = linha.strip().split(',')  # Supondo que os dados são separados por vírgula
                if len(dados) >= 5:  # Assegurando que há pelo menos 5 campos
                    nome = dados[0]
                    idade = dados[1]
                    sexo = dados[2]
                    endereco = dados[3]
                    email = dados[4]

                    # Verifica se o nome começa com a letra 'A'
                    if nome.startswith('A'):
                        clientes_nome_a.append((nome, idade, sexo, endereco, email))
        
        return clientes_nome_a

    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

# Nome do arquivo a ser lido
arquivo_clientes = 'clientes.txt'
clientes_nome_a = extrair_clientes_nome_a(arquivo_clientes)

# Exibindo os clientes com o nome que começa com a letra 'A'
for cliente in clientes_nome_a:
    print(cliente)