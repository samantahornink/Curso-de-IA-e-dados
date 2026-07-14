import requests

cep = input("Insira o seu CEP:  ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(f"Você mora na rua {resposta["logradouro"]}, no bairro {resposta["bairro"]}, na cidade de {resposta["localidade"]}, no estado de {resposta["estado"]}")
