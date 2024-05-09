def verificar_multiplos_de_10(matriz):
    for linha in matriz:
        for elemento in linha:
            if elemento % 10 != 0:
                return False
    return True
def verificar_linhas_ordenadas(matriz):
    for linha in matriz:
        if linha != sorted(linha) and linha != sorted(linha, reverse=True):
            return False
    return True
def ler_matriz():
    linhas = int(input())
    colunas = int(input())
    matriz = []
    for _ in range(linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz
matriz = ler_matriz()
if verificar_multiplos_de_10(matriz) and verificar_linhas_ordenadas(matriz):
    print("SIM")
else:
    print("NAO")