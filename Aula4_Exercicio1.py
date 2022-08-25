"""
Programa Listas
Descrição: 
Autor: Carlos Rafael Batista Santos
Versão: 0.0.1
Data: 18/08/2022
"""

lista = []
lista_aux = []


while True:
    elemento = input("Digite um valor inteiro (X para terminar): ")
    if elemento.upper() == 'X':
        break
    lista.append(elemento)


print(f"A lista possui {len(lista)} elementos, são eles: ", lista)

for elemento in lista:
    if elemento not in lista_aux:
        lista_aux.append(elemento)



print(f"A lista possui {len(lista_aux)} elementos, são eles: ", lista_aux)

