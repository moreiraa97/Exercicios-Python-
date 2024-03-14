import numpy as np 

def organizar_vetor(vetor):
    
    #função sort para ordenar os elementos do vetor
    vetor_organizado = np.sort(vetor)
    return vetor_organizado 

vetor = np.array([4, 7, 9, 3, 6, 7, 8, 2, 1, 3])
vetor_organizado = organizar_vetor(vetor)

print("Vetor original: ", vetor)
print("Vetor organizado: ", vetor_organizado)

