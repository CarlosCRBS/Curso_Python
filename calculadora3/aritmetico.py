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
    
def calcula(dados):  
    operador = dados.get('tipoOperacao')
    numero_1 = dados.get('operador1')
    numero_2 = dados.get('operador2')
    
    if operador == '+':
        res = adicao(numero_1, numero_2)
        
    elif operador == '-':
        res = subtracao(numero_1, numero_2)

    elif operador == '*':
        res = multiplicacao(numero_1, numero_2)

    elif operador == '/':
        res = divisao(numero_1, numero_2)

    else:
        dados.update({'resultado' : None})
        return dados 

    dados.update({'resultado' : res})
    return dados