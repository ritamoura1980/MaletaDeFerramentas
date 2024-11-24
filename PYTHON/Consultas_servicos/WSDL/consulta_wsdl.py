import requests

def consultar_cliente(url, cpf):
    try:
        # Monta a URL com o CPF como parâmetro de consulta
        response = requests.get(url, params={'cpf': cpf})

        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()
        
        # Retorna a resposta JSON, se o serviço retornar JSON
        return response.json()

    except requests.exceptions.HTTPError as errh:
        print(f"Erro de HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Erro de Conexão: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Ocorreu um erro: {err}")
    except ValueError:
        print("Resposta não é um JSON válido.")

    return None

def main():
    url = 'http://endereco?wsdl'  # Substitua pelo URL real do serviço
    cpf = '12345678901'  # Substitua pelo CPF que deseja consultar

    resposta = consultar_cliente(url, cpf)

    if resposta:
        print("Resposta do serviço:", resposta)

if __name__ == "__main__":
    main()