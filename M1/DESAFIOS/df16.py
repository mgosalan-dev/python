#DF016 - Parte inteira de um número
from colorama import init, Fore, Style
from math import trunc

init(autoreset=True)

def dividindo_valor(numero: float) -> int:
  
  return (trunc(numero))

def verificacao_de_valor():
  while True:
    try:
      valor = float(input(Fore.BLUE + "Digite um Valor: "))
      
      return valor
    except ValueError:
      print(Fore.RED + "❌ O campo não pode estar em branco.")

def main():
  numero = verificacao_de_valor()
  print(Fore.CYAN + f"Analisando o numero {numero} \n")
  valor = dividindo_valor(numero)
  print(Fore.GREEN + f"O valor inteiro de {Fore.YELLOW}{numero}{Style.RESET_ALL} é {Fore.MAGENTA}{valor}")
if __name__ == "__main__":
  main()