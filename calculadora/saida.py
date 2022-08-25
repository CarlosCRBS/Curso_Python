"""
Módulo saida
Requisitos: Este módulo oferece uma função para colocar o resultado da operação
de adição.
Autor: Nelson S. dos Santos
Data: 23/08/2022
Versão:0.9.0
"""
# Definição de funções

def sai_dados(operador, numero_1, numero_2, resultado):
   if operador == '+':
      print(f"\nO resultado da soma de {numero_1} com o {numero_2} é igual a {resultado}.")
      print(f"{numero_1} + {numero_2} = {resultado}\n")
   
   elif operador == '-':
      print(f"\nO resultado da subtração de {numero_1} por {numero_2} é igual a {resultado}.")
      print(f"{numero_1} - {numero_2} = {resultado}\n")

   elif operador == '*':
      print(f"\nO resultado da multiplicação de {numero_1} por {numero_2} é igual a {resultado}.")
      print(f"{numero_1} * {numero_2} = {resultado}\n")

   elif operador == '/':
      print(f"\nO resultado da divisão de {numero_1} por {numero_2} é igual a {resultado}.")
      print(f"{numero_1} / {numero_2} = {resultado}\n")
      
   else:
      print(f"Você não digitou um operador válido, por favor execute o programa novamente.\n")