import os         
import vlc       
from tabulate import tabulate  

# Função que busca até 'limite' músicas (.mp3) numa pasta específica, pra mostrar no preview
def buscar_musicas_pasta(pasta, limite=5):
    musicas = []
    # Caminho da pasta dentro do diretório do usuário (ex: C:/Users/SeuUser/Music)
    caminho = os.path.join(os.path.expanduser("~"), pasta)

    # Se a pasta existir, listamos os arquivos .mp3 nela
    if os.path.exists(caminho):
        arquivos = [f for f in os.listdir(caminho) if f.endswith(".mp3")]

        # Só pega até o limite de arquivos para não lotar a tela
        musicas.extend(arquivo for i, arquivo in enumerate(arquivos[:limite], start=1))
    else:
        # Se não existir, já avisa o user — nada de fail silencioso, né? 
        print(f"Pasta não encontrada: {caminho}")
    return musicas

# Função que busca TODAS as músicas na pasta, pra mostrar e tocar depois
def buscar_todas_musicas(pasta):
    musicas = []
    caminho = os.path.join(os.path.expanduser("~"), pasta)

    if os.path.exists(caminho):
        arquivos = [f for f in os.listdir(caminho) if f.endswith(".mp3")]

        # Monta uma lista de dicionários, com id, nome e caminho completo da música
        musicas.extend(
            {
                "id": i,
                "nome": arquivo,
                "caminho": os.path.join(caminho, arquivo),
            }
            for i, arquivo in enumerate(arquivos, start=1)
        )
    else:
        print(f"Pasta não encontrada: {caminho}")
    return musicas

# Mostra o resumo das pastas com as primeiras músicas, num formato tabela bonitão
def exibir_resumo(pastas, musicas_por_pasta, limite=5):
    tabela = []
    # Para cada pasta, monta uma linha da tabela com infos importantes
    for i, pasta in enumerate(pastas, start=1):
        lista_musicas = musicas_por_pasta[pasta]          # músicas preview
        qtd_total = len(buscar_todas_musicas(pasta))      # quantidade total na pasta
        
        # Se tiver mais músicas que o limite, corta só pra mostrar o preview
        musicas_display = lista_musicas if len(lista_musicas) < limite else lista_musicas[:limite]
        musicas_str = ", ".join(musicas_display)          # transforma lista em string
        
        # Monta a linha da tabela
        tabela.append([i, pasta, qtd_total, musicas_str])
    
    # Print da tabela formatada usando o tabulate (fancy_grid deixa mais style)
    print(tabulate(tabela, headers=["Número", "Pasta", "Qtd Total", f"Até {limite} músicas na pasta"], tablefmt="fancy_grid"))

# Mostra a lista completa de músicas pra o usuário escolher qual quer tocar
def exibir_lista(musicas):
    tabela = [[m["id"], m["nome"]] for m in musicas]
    print(tabulate(tabela, headers=["Número", "Música"], tablefmt="fancy_grid"))

# Função que cria o player, toca o arquivo, e espera o user dar enter pra parar
def tocar_musica(caminho):
    player = vlc.MediaPlayer(caminho)  # Cria player VLC com o arquivo especificado
    player.play()                      # Começa a tocar
    input("\n▶️ Pressione Enter para parar a música...\n")  # Pausa até o user apertar enter
    player.stop()                      # Para a música

# Função principal — o coração do programa
def main():
    # Pastas padrão onde vamos procurar as músicas (pode adicionar mais!)
    pastas = ["Music", "Downloads"]
    
    # Pra cada pasta, busca as músicas para exibir no resumo (preview)
    musicas_para_resumo = {}
    for pasta in pastas:
        musicas_para_resumo[pasta] = buscar_musicas_pasta(pasta)

    print("\n🎵 Pastas com músicas MP3 (preview até 5 músicas):\n")
    exibir_resumo(pastas, musicas_para_resumo, limite=5)

    try:
        # Pergunta qual pasta o user quer abrir pra escolher música
        escolha_pasta = int(input("\nEscolha a pasta para abrir (número): "))
        
        # Valida o input (se não estiver no intervalo válido, cancela)
        if escolha_pasta not in range(1, len(pastas)+1):
            print("Número inválido, saindo...")
            return

        # Pasta escolhida
        pasta_escolhida = pastas[escolha_pasta - 1]
        
        # Busca TODAS as músicas da pasta escolhida (lista completa)
        musicas = buscar_todas_musicas(pasta_escolhida)

        # Se não achou nenhuma música, já avisa e termina
        if not musicas:
            print(f"Nenhuma música encontrada na pasta {pasta_escolhida}.")
            return

        # Mostra as músicas disponíveis pra escolha
        print(f"\n🎶 Músicas em {pasta_escolhida}:")
        exibir_lista(musicas)

        # Pergunta qual música tocar (pelo número)
        escolha_musica = int(input("\nDigite o número da música para tocar: "))
        
        # Procura a música selecionada na lista
        selecionada = next((m for m in musicas if m["id"] == escolha_musica), None)
        
        if selecionada:
            print(f"\n▶️ Tocando: {selecionada['nome']}\n")
            tocar_musica(selecionada["caminho"])
        else:
            print("Número inválido. Nenhuma música selecionada.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Aquele clássico: roda a main só se o script for executado diretamente
if __name__ == "__main__":
    main()
