#LISTAS
#Listas são uma forma de armazenar mais de um valor em uma
#Unica variavel. Os valores podem ser de tipos diferentes

#Uma lista de numero
valores = [2, 3, 5, 7, 9, 11]

#Uma lista de valores variados
mix = ["batata", 1.25, True, "Tomate"]

#Lista de strings
legumes = ["batata", "beterraba", "Brocolis", "Pipino"]

#OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: Significa percorrer a lista do pimeiro ao 
#ultimo alemento, fazendo algo com cada um deles.

# Imprimindo cada um dos elementos da lista, um por um
for val in valores:
    print(val)

print("-" * 40) #Traço de 40 Hifens

#Imprimindo o dobro do valor de cada elemento em listas
for x in valores:
    print(x * 2)

# 2) INSERINDO UM NOVO ELEMENTO NO FIM DA LISTA

valores.append(13)
legumes.append("cebola")

print(valores)
print(legumes)

# 3) INSERINDO UM NOV ELEMENTO EM UMA POSIÇÃO ESPECIFICADA
# Parametros:
# 1) a posiçãoonde sera inserido o novo elemento
# 2) o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "repolho")
print(legumes)

print("-" * 40)     # Traços de 40 hifens

# 4) 
print("Elemto na QUARTA posição:", valores[3])
print("Elemento na Primeira posição:", valores[0])
print("Elemto na ULTIMA posição:", valores[-1])
print("Elemento na PENULTIM posição:", valores[-2])

print("-" * 40)

#5)SUBSTITUINDO VALORES EXISTENTES
print("Antes", legumes)
legumes[3] = "vagem"

legumes[0] = "mandica"

legumes[-1] = "milho"

print("Depois ", legumes)

print("-" * 40)

#6)
print("Numero de eementos na lista de valores: ", len(valores))
print("Numeros de elementos na lista de legumes: ", len(legumes))

print("-" * 40)

#7)
print("Antes: ", valores)
removido = valores.pop()
print("Valor removido: ", removido)
print("Depois: ", valores)

print("-" * 40)

#8)
removido = valores.pop(3)
print("Valor removido da posição 3: ", removido)
print(valores)
removido = valores.pop(0)
print("Valore removido da primeira posição: ", removido)
print(valores)

print("-" * 40)

#9)
print("Antes: ", legumes)
legumes.remove("abobrinha")
print("Apos remoção de abobrinha: ",legumes)

print("-" * 40)

#Arecentando algun legumes para aumentar a lista

legumes.append("beterraba")
legumes.append("abobrinha")
legumes.append("batata doce")
legumes.append("mandioquinha")
legumes.append("cará")
legumes.append("nabo")

#10)
#Falin significa copiar uma parte da lista (uma sublista)

print(legumes)

#Cria uma sublista qu contenha os elementos da posição 2 e posição 7

sublista2_7 = legumes[2:8]
print("Sublista de 2 a 7: ", sublista2_7)

sublista0_5 = legumes[:6]
print("Sublista de 0 a 5: ", sublista0_5)

sublista8_fim = legumes[8:]
print("Sublista do 8 ao fim: ", sublista8_fim)
