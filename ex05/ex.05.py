
def contar_numeros(vetor):
    positivos = 0
    negativos = 0
    zeros = 0

    for numero in vetor:
        if numero > 0:
            positivos += 1 
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1

    return positivos, negativos, zeros 

def main():
    vetor = []
    tamanho = int(input("Digite o tamanho do vetor: "))

    print("Digite os numeros do vetor: ")
    for i in range(tamanho):
        numero = int(input())
        vetor.append(numero)

    positivos, negativos, zeros = contar_numeros(vetor)

    print("\nResultados: ")
    print("\nNumeros positivos: ", positivos)
    print("\nNumeros negativos: ", negativos)
    print("\nZeros: ", zeros) 

if __name__ == "__main__":
    main()


















