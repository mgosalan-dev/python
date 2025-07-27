def ler_segmento(msg: str) -> float:
    """Lê um valor positivo com tratamento de erro."""
    while True:
        try:
            valor = float(input(msg))
            if valor > 0:
                return valor
            else:
                print('\033[31m[ERRO] O valor deve ser maior que zero.\033[m')
        except ValueError:
            print('\033[31m[ERRO] Digite um número válido.\033[m')


def pode_formar_triangulo(a: float, b: float, c: float) -> bool:
    """Verifica se os segmentos podem formar um triângulo."""
    return a < b + c and b < a + c and c < a + b


def tipo_triangulo(a: float, b: float, c: float) -> str:
    """Retorna o tipo do triângulo."""
    if a == b == c:
        return 'Equilátero 🔺 (todos os lados iguais)'
    elif a == b or b == c or a == c:
        return 'Isósceles 🔻 (dois lados iguais)'
    else:
        return 'Escaleno 🛡️ (todos os lados diferentes)'


def main():
    print('=== Analisador de Triângulos ===')

    # Entrada com validação
    r1 = ler_segmento('Primeiro segmento: ')
    r2 = ler_segmento('Segundo segmento: ')
    r3 = ler_segmento('Terceiro segmento: ')

    # Verificação
    if pode_formar_triangulo(r1, r2, r3):
        print('\033[32mOs segmentos PODEM formar um triângulo.\033[m')
        print(f'Tipo do triângulo: {tipo_triangulo(r1, r2, r3)}')
    else:
        print('\033[31mOs segmentos NÃO podem formar um triângulo.\033[m')


if __name__ == '__main__':
    main()
