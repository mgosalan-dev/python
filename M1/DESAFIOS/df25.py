# df25 cria um programa que verifique que uma pessoa tenha  Silva no nome

def verificar_nome() -> str:
  while True:
      nome = input("Digite seu nome completo:" ).strip()
      if nome == "":
        print("O campo não pode estar vazio.")
        continue
      else:
        return nome
    
def verificar_silva(nome: str) -> None:
  
      if "silva" in nome.lower():
        print(f"O nome tem silva: {nome.title()}")
      else:
        print(f"não tem silva no seu nome: {nome.title()}")
        
      
def main():
  nome = verificar_nome()
  verificar_silva(nome)
  
if __name__ == "__main__":
  main()