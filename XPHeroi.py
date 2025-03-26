herois = [
    {"nome": "Aragorn", "xp": 7500},
    {"nome": "Legolas", "xp": 2500},
    {"nome": "Gandalf", "xp": 10000},
    {"nome": "Frodo", "xp": 500},
    {"nome": "Gimli", "xp": 6000}
]

# Laço de repetição (for) para processar cada herói
for heroi in herois:
    nome = heroi["nome"]
    xp = heroi["xp"]
    
    # Estruturas de decisão (if/elif/else) para determinar o nível
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
    
    # Operadores de formatação (f-string) para exibir o resultado
    print(f"O Herói {nome} tem {xp} XP e está no nível {nivel}!")