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