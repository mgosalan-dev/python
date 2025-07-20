#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60€ por dia e 0,15€ por Km rodado.

from colorama import init, Fore, Style

init(autoreset=True)

def km_rodados() -> float:
  while True:
    try:
      km = float(input(Fore.CYAN + "🛞 informe quantos km foram rodados: "))
      if km <= 0 :
        print(Fore.RED + "❌ A kilometragem não pode ser 0 ou negativo.")
        continue
      return km
    except ValueError:
      print(Fore.RED + "❌ Por favor informar apenas valores numérico")
      
def dias_alugado()-> int:
  while True:
    try:
      dias = int(input(Fore.YELLOW + "🚗 Informe quantos dias foram utilizados: "))
      if dias <= 0:
        print(Fore.RED + "❌ A contagem de dias não pode ser 0. ")
        continue
      return dias
    except ValueError:
      print(Fore.RED + "❌ Insira apenas valores inteiros.")
    
def calcular_valor(dias: int, km: float) -> float:
  
  return (dias * 60) + (km * 0.15)

def main():
  print(Fore.CYAN + "📃 Calculadora de dias")
  dias = dias_alugado()
  km = km_rodados()
  total = calcular_valor(dias, km)
  
  print(Fore.GREEN + f"\n💶 valor total a pagar: €{total:.2f}")
  
if __name__ == "__main__":
  main()