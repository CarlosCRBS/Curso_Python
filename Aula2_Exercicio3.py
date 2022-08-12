"""
Programa Soma
Descrição: Este programa soma dois números dados pelo usuário
Requisitos
Autor: Carlos Rafael Batista Santos
Versão: 0.0.1
Data: 11/08/2022
"""

# Programação Sequencial
# Entrada de dados
numeros = []
i = 0

while i < 2:
    numeros.append(int(input("Informe um número: ")))
    i += 1

# Processamento de dados
soma = numeros[0] + numeros[1]

# Saída de dados
print(f"A soma de {numeros[0]} com {numeros[1]} é {soma}. ")
