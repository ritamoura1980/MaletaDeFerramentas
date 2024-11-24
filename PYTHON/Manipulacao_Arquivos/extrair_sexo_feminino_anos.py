def extrair_clientes_femininos(arquivo):
    try:
        with open(arquivo, 'r') as file:
            clientes_femininos = []
            for linha in file:
                dados = linha.strip().split(',') # Supondo que os dados são separados por vírgula
                if len(dados) >= 5:  # Assegurando que há pelo menos 5 campos
                    nome = dados[0]
                    idade = dados[1]
                    sexo = dados[2]
                    endereco = dados[3]
                    
                    # Verifica se o sexo é feminino
                    if sexo.lower() == 'feminino':
                        clientes_femininos.append((nome, idade, sexo, endereco))
        
        return clientes_femininos

    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

# Nome do arquivo a ser lido
arquivo_clientes = 'clientes.txt'
clientes_femininos = extrair_clientes_femininos(arquivo_clientes)

# Exibindo os clientes do sexo feminino
for cliente in clientes_femininos:
    print(cliente)