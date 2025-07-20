# crie um programa que leia quanto de dinheiro uma pessoa tem e mostre quantos dolares ele tem convertidos considere a cotação atual te vira

import requests

def obter_cotacao(base="EUR", destino="JPY"):
    url = f"https://api.frankfurter.app/latest?from={base}&to={destino}"
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        taxa = dados["rates"][destino]
        
        return taxa
    except Exception as e:
        print("❌ Erro ao pegar cotação:", e)
        return None

def converter(valor, taxa):
    return valor * taxa

def main():
    print("\n💱 Conversor de Moeda (EUR → JPY)\n")
    try:
        valor = float(input("Digite o valor em Euro (EUR): "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    taxa = obter_cotacao("EUR", "JPY")
    if taxa:
        convertido = converter(valor, taxa)
        print(f"\n💶 {valor:.2f} EUR = {convertido:.2f} JPY")

if __name__ == "__main__":
    main()



