# crie um programa que leia quanto de dinheiro uma pessoa tem e mostre quantos dolares ele tem convertidos considere a cotação atual te vira

import requests

def obter_cotacao(base = "EUR", destino = "JPY", chave_api="82fad69e4cedf698b95653b3f39e57b7"):
  url = "https://api.currencystack.io/currency"
  params = {
    "base": base,
    "target": destino,
    "apikey": chave_api
  }
  
  try:
    resposta = requests.get(url, params=params)
    dados = resposta.json()
    
    if 'error' in dados:
      print(f"Erro na API: {dados['error']}")
      return None
    
    taxa = dados['data']['target_values']

    print(f"🪙 1{base} = {taxa:.4f} {destino}")
    return taxa
  
  except Exception as e:
    print("❌ Erro ao pegar cotação:", e)
    return None
  
def converter(valor, taxa):
    return valor * taxa
  
  
def main():
    chave_api = "82fad69e4cedf698b95653b3f39e57b7"
    print("\n💱 conversor de moeda (EUR → JPY)\n")
    
    valor_euro = float(input("Digite o valor em Euro (EUR): "))
    taxa = obter_cotacao("EUR", "JPY", chave_api)
    
    if taxa:
      valor_iene = converter(valor_euro, taxa)
      print(f"\n💶 {valor_euro:.2f} EUR = {valor_iene:.2f} JPY ")
    
    
if __name__ == "__main__":
    main()