def calcular_rank(vitorias, derrotas):
    """
    Calcula o saldo e determina o nível do jogador baseado nas vitórias.
    
    Args:
        vitorias (int): Número de vitórias
        derrotas (int): Número de derrotas
    
    Returns:
        tuple: (saldo, nivel)
    """
    saldo = vitorias - derrotas
    
    # Determinação do nível com base nas vitórias (intervalos corrigidos)
    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return saldo, nivel

def obter_entrada_valida(mensagem):
    """
    Obtém uma entrada numérica válida do usuário.
    
    Args:
        mensagem (str): Mensagem a ser exibida
    
    Returns:
        int: Número válido inserido pelo usuário
    """
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Por favor, insira um número não negativo.")
                continue
            return valor
        except ValueError:
            print("Por favor, insira apenas números inteiros.")

def main():
    """Função principal do programa."""
    print("🎮 Calculadora de Partidas Ranqueadas")
    print("=" * 40)
    
    while True:
        print("\n" + "─" * 40)
        
        # Obter entradas válidas
        vitorias = obter_entrada_valida("Digite a quantidade de vitórias: ")
        derrotas = obter_entrada_valida("Digite a quantidade de derrotas: ")
        
        # Calcular rank
        saldo, nivel = calcular_rank(vitorias, derrotas)
        
        # Exibir resultado
        print(f"\n📊 RESULTADO:")
        print(f"   Vitórias: {vitorias}")
        print(f"   Derrotas: {derrotas}")
        print(f"   Saldo: {saldo:+d}")  # Mostra + ou - no saldo
        print(f"   Nível: {nivel}")
        
        # Perguntar se quer continuar
        print("\n" + "─" * 40)
        continuar = input("Deseja calcular novamente? (s/n): ").lower().strip()
        
        if continuar not in ['s', 'sim', 'y', 'yes']:
            print("\n👋 Encerrando a calculadora. Até logo!")
            break

if __name__ == "__main__":
    main()
