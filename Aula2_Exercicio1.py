"""
Programa MaiorQue10
Descrição: Este programa imprime na tela a informação de que o numero informado é maior, menor ou igual a 10
Requisitos
Autor: Carlos Rafael Batista Santos
Versão: 0.0.1
Data: 11/08/2022
"""

# Programação Sequencial
# Entrada de dados
numA = float(input("Informe um número: "))  



# Processamento de dados
# Estrutura de contraole de fluxo de esecução SELEÇÃO
if numA > 10:
    frase = "Este número é maior que 10"
    #print(f"O número {numA} é MAIOR que 10.\n")
elif numA < 10:
    frase = "Este número é menor que 10"
    #print(f"O número {numA} é MENOR que 10.\n")
else:
    frase = "Este número é igual a 10"    
    #print(f"O número {numA} é IGUAL que 10.\n")


# Saída de dados
print(frase)
