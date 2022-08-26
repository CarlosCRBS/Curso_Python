"""
Módulo Aritmético
Descrição: Este módulo possui as funções que fornecem as 4 operações aritméticas (adição, subtração, multiplicação e divisão)
que operam sobre os 2 operadores recebidos.
Autor: Carlos Rafael Batista Santos
Data: 25/08/2022
Versão: 1.0.0
"""
# Definição de funções

def adicao(numero_1, numero_2):
    return numero_1 + numero_2

def subtracao(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacao(numero_1, numero_2):
    return numero_1 * numero_2

def divisao(numero_1, numero_2):
    return numero_1 / numero_2
    
def calcula(valores):  
    operador = valores[0]
    numero_1 = valores[1]
    numero_2 = valores[2]
    
    if operador == '+':
        res = adicao(numero_1, numero_2)
        
    elif operador == '-':
        res = subtracao(numero_1, numero_2)

    elif operador == '*':
        res = multiplicacao(numero_1, numero_2)

    elif operador == '/':
        res = divisao(numero_1, numero_2)

    else:
       return None
        
    return res