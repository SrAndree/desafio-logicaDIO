# Sistema de Classificação de Heróis com Input do Usuário

print("=== CLASSIFICADOR DE NÍVEL DE HERÓIS ===")

# Laço principal (permite cadastrar múltiplos heróis)
while True:
    # Input do nome (validação para não ser vazio)
    nome = input("\nDigite o nome do herói: ").strip()
    while not nome:
        print("Nome inválido! Digite novamente.")
        nome = input("Digite o nome do herói: ").strip()

    # Input do XP (validação para ser número positivo)
    while True:
        try:
            xp = int(input("Digite a quantidade de XP do herói: "))
            if xp >= 0:
                break
            else:
                print("XP não pode ser negativo!")
        except ValueError:
            print("Digite um número válido!")

    # Estrutura de decisão para determinar o nível
    if xp < 1000:
        nivel = "Ferro"
    elif 1001 <= xp <= 2000:
        nivel = "Bronze"
    elif 2001 <= xp <= 5000:
        nivel = "Prata"
    elif 5001 <= xp <= 7000:
        nivel = "Ouro"
    elif 7001 <= xp <= 8000:
        nivel = "Platina"
    elif 8001 <= xp <= 9000:
        nivel = "Ascendente"
    elif 9001 <= xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"  # XP > 10000

    # Saída formatada
    print(f"\n→ O Herói {nome} tem {xp} XP e está no nível {nivel}!")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja cadastrar outro herói? (s/n): ").strip().lower()
    if continuar != 's':
        print("\nPor hoje é só pessoal!")
        break