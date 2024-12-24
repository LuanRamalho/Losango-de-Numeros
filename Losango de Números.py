def exibir_losango(n):
    # Parte superior do losango
    for i in range(1, n + 1):
        # Espaços à esquerda
        print(" " * (n - i), end="")
        # Números da linha
        print(" ".join(str(j) for j in range(1, i + 1)))
    
    # Parte inferior do losango
    for i in range(n - 1, 0, -1):
        # Espaços à esquerda
        print(" " * (n - i), end="")
        # Números da linha
        print(" ".join(str(j) for j in range(1, i + 1)))

# Exemplo de uso
linhas = int(input("Digite o número de linhas para o losango: "))
exibir_losango(linhas)
input()