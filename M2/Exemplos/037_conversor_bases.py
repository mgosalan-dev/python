"""
Exercício 037 - Conversor decimal para binário, octal ou hexadecimal
"""

def main():
    num = int(input("Número decimal: "))
    print("1 - Binário\n2 - Octal\n3 - Hexadecimal")
    escolha = input("Escolha a base: ")
    if escolha == '1':
        print(f"Binário: {bin(num)[2:]}")
    elif escolha == '2':
        print(f"Octal: {oct(num)[2:]}")
    elif escolha == '3':
        print(f"Hexadecimal: {hex(num)[2:]}")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
