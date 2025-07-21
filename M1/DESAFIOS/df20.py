# df20 Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

def nome_alunos():
  print("✍️ Digite o nome dos alunos (1 por linha). Para finalizar, pressione Enter em uma linha vazia,")
  alunos = []
  
  while True:
    nome = input("Nome do aluno: ").strip()
    if nome == "":
      break
    alunos.append(nome)
  return alunos

def verifica_lista(lista):
  if not lista:
    print("❌ A lista está vazia!")
    return False
  if not all(isinstance(nome, str) and nome.strip() for nome in lista):
    print("❌ A lista contém valores inválidos!")
    return False
  return True

def ordem_sorteio(lista):
  if verifica_lista(lista):
    random.shuffle(lista)
    print(f"🎉 Ordem sorteado: {lista}")
  else:
    print("⚠️ Sorteio cancelado por dados inválidos.")
    
def main():
  
  alunos = nome_alunos()
  ordem_sorteio(alunos)
  
if __name__ == "__main__":
  main()
    
    

