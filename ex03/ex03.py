def contar_palavras(texto):

    # Converte todo o texto para minúsculas para ignorar diferenças de maiúsculas e minúsculas
    texto = texto.lower()
    
    # Divide o texto em palavras
    palavras = texto.split()

    # Cria um dicionário para armazenar as contagens de cada palavra
    contagem_palavras = {}

   
    for palavra in palavras:

        # Remove pontuações das palavras 
        palavra = palavra.strip('.,!?;:()[]{}\'"')

        # Incrementa a contagem para a palavra atual no dicionário
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    return contagem_palavras

texto = "Este texto e um teste para contagem de palavras que serao inseridas em um vetor e serao lidas e segmentadas em um dicionario apenas em letras minusculas"
contagem = contar_palavras(texto)
print("Contagem de palavras:")
for palavra, frequencia in contagem.items():
    print(f"{palavra}: {frequencia}")