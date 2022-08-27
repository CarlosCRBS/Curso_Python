"""
Módulo de Entrada
Descrição: Este módulo lê os dados da operação digitados pelo usuário.
que operam sobre os 2 operadores recebidos.
Autor: Carlos Rafael Batista Santos
Data: 25/08/2022
Versão: 1.0.0
"""
# Definição de funções


def entra_dados():
    """Esta função (procedimento) lê dois números digitados pelo usuário."""
    
    op1 = float(input("\nDigite um número: "))
    op2 = float(input("\nDigite um número: "))
    
    operacao = input('''Informe o tipo de operação aritmética que deseja realizar:
            + para Adição
            - para Subtração
            * para Multiplicação
            / para Divisão
            ''')
    
    dados = {'tipoOperacao' : operacao, 'operador1' : op1, 'operador2' : op2}

    return dados

