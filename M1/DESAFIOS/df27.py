# df27 Primeiro e ultimo nome

def receber_nome() -> str:
    while True:
        nome = input("Digite seu nome completo: ").strip()
        if nome == "":
          print("O campo não pode estar vazio.")
        else:
          return nome
        
def verificar_nome(nome: str) -> None:
    nome_title = nome.title().split()
    print(f"Seu Primeiro nome é {nome_title[0]}")
    print(f"Seu último nome é {nome_title[-1]}")
    

def main():
  nome = receber_nome()
  verificar_nome(nome)
  
  
if __name__ == "__main__":
  main()