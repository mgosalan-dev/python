import random

def coletar_nomes():
  print("✍️ Digite os nomes dos alunos (1 por linha). Para finalizar, pressicione Enter em uma linha vazia")
  alunos = []
  
  while True:
    nome = input("Nome do aluno: ").strip()
    if nome == "":
      break
    alunos.append(nome)
    
  return alunos

def verificar_lista(lista):
  if not lista:
    print("❌ A lista está vazia!")
    return False
  if not all(isinstance(nome, str)and nome.strip for nome in lista):
    print("❌ A lista contém valores inválidos!")
    return False
  return True

def sortear_aluno(lista):
  if verificar_lista(lista):
    sorteado = random.choice(lista)
    print(f"🎉 Aluno sorteado: {sorteado}")
  else:
    print("⚠️ Sorteio cancelado por dados inválidos.")
    
def main():
  
  alunos = coletar_nomes()
  sortear_aluno(alunos)
  
if __name__ == "__main__":
  main()
  
  