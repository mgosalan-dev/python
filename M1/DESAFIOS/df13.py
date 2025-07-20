#faça um algoritimo que leia o salario de um funcionario e mostre o novo salario com 15% de desconto

from colorama import init, Fore, Style

init(autoreset=True)

def calcular_aumento(valor: float) -> float:
  
  return valor * 1.15

def solicitar_salario() -> float:
  while True:
    try:
      valor = float(input(Fore.CYAN + "Digite o seu salario (€): "))
      if valor <= 0:
        print(Fore.RED + "❌ o valor não pode ser zero ou negativo!")
        continue
      return valor
    except ValueError:
      print(Fore.RED + "❌ Entrada invalida. Digite apenas numeros!!")
      
def main():
  print(Fore.BLUE + "\n🧾 Calculadora de Salário com 15% de aumento\n" + Style.RESET_ALL)
  salario = solicitar_salario()
  novo_salario = calcular_aumento(salario)
  print(Fore.GREEN +f"\n💰 Seu novo salário com 15% de aumento será: €{novo_salario:.2f}\n")
if __name__ == "__main__":
  main()

