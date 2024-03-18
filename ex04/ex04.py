import numpy as np 

def matriz_transposta(matriz):
    return np.transpose(matriz)


matriz = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])


transposta = matriz_transposta(matriz)


print("Matriz original: \n", matriz)

print("\nTransposta da matriz: \n", transposta)
