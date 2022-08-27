"""
Módulo de Saída
Descrição: Este módulo printa o resultado da operação na tela.
Autor: Carlos Rafael Batista Santos
Data: 25/08/2022
Versão: 1.0.0
"""
# Definição de funções

def sai_dados(dados):
   operador = dados.get('tipoOperacao')
   numero_1 = dados.get('operador1')
   numero_2 = dados.get('operador2')
   resultado = dados.get('resultado')


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