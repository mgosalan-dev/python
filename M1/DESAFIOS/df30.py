#df30 verificando se um valor é par ou impar

def par_impar(numero: int) -> None :
  if numero % 2 == 0:
        print("✅ É um número **par**.")
  else:
        print("🔢 É um número **ímpar**.")
    
def validar_inpu() -> int:
  while True:
    try:
      return int(input("Digite um numero inteiro: "))
    except ValueError:
      print("❌ Entrada inválida! Digite apenas números inteiros.")
    
def main():
  numero = validar_inpu()
  par_impar(numero)
  
if __name__ == "__main__":
  main()