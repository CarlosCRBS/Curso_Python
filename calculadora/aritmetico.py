"""
Função soma
Requisitos: Esta função (procedimento) lê dois números digitados pelo usuário.
Autor: Nelson S. dos Santos
Data: 23/08/2022
Versão:0.9.0
"""
# Definição de funções

def adicao(numero_1, numero_2):
    """Esta função calcula a soma dos números
       numero_1 e numero_2."""
    return numero_1 + numero_2

def subtracao(numero_1, numero_2):
    """Esta função calcula a soma dos números
       numero_1 e numero_2."""
    return numero_1 - numero_2

def multiplicacao(numero_1, numero_2):
    """Esta função calcula a soma dos números
       numero_1 e numero_2."""
    return numero_1 * numero_2

def divisao(numero_1, numero_2):
    """Esta função calcula a soma dos números
       numero_1 e numero_2."""
    return numero_1 / numero_2
    
def calcula(operador, numero_1, numero_2):    
    if operador == '+':
        res = adicao(numero_1, numero_2)
        
    elif operador == '-':
        res = subtracao(numero_1, numero_2)

    elif operador == '*':
        res = multiplicacao(numero_1, numero_2)

    elif operador == '/':
        res = divisao(numero_1, numero_2)

    else:
        #res = print('You have not typed a valid operator, please run the program again.')
        return None
        
    return res