"""
Módulo Principal
Descrição: Este módulo realizada a chamada das funções dos outros módulos para realizar a leitura dos dados 
fornecidos pelo usuário, calcular estes dados conforme a operação aritmética escolhida (adição, subtração, 
multiplicação ou divisão), e printar o resultado na tela.
Autor: Carlos Rafael Batista Santos
Data: 25/08/2022
Versão: 1.0.0
"""

# Importação de módulos

import entrada 
import aritmetico
import saida


# Definição de funções



def main():
    # Entrada
    dados = entrada.entra_dados()

    # Processamento
    resultado = aritmetico.calcula(dados)

    # Saída
    saida.sai_dados(dados, resultado)
    

 
# Execução do programa

if __name__ == "__main__":
    main()