def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc_calculado = calcular_imc(peso, altura)
print("O IMC é:", imc_calculado)
# p = 85
# a = 1.72
# imc = calc_imc(p,a)

# print(imc)

# print (calc_imc(85, 1.72))
from math import pi
"""
    Função que caucula a area de uma figura geometrica plana
"""
def calc_area(base, altura, tipo):
    resultado = None

    if tipo == "R":                #R = Retangulo
        resultado = base * altura
    elif tipo == "T":       # T = Triangulo
        resultado = base * altura / 2
    elif tipo == "E":               #E = Elipse
        resultado = (base / 2) * (altura / 2) * pi
    else: #forma invalida ou desconhecida
        resultado = None

    return resultado 
print("Retangulo 20x30: ", calc_area(20, 30, "R"))
print("Triangulo 45x32: ", calc_area(45, 32, "T"))
print("Elipse 10x15: ", calc_area(10, 15, "E"))
print("Desconhecido 12x16: ", calc_area(12, 16, "X"))