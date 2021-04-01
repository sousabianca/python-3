frase = 'Curso em Vídeo Python'
#fatiamento
'''print(frase[3:13]) #não chega até o 13 elemento e sim até o 12
print(frase[:13])
print(frase[13:])
print(frase[1:15:2]) # vai do 1 ao 14 pulando de 2 em 2
print(frase[1::2]) #não identifiquei o final então vai do 1 ao último de 2 em 2
print(frase[::2]) # vai pegar a str inteira pulando de 2 em 2'''
#Análise e transformação
'''print(frase.count('o')) #irá contar na frase quantos o minúsculo tem'''
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase.upper().count('O'))
print(frase.capitalize())
print(frase.title())
