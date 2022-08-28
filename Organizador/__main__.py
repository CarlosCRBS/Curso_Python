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

import os
import shutil

lista_planilhas = []
lista_documentos = []

# Definição de funções



def main():
    # Entrada
    
    lista_arquivos = os.listdir('Pasta/')
    print(f"Arquivos no diretório Pasta/", os.listdir('Pasta/'))

    # Processamento

    for arquivo in lista_arquivos:
        if ".xls" in arquivo:
            lista_planilhas.append(arquivo)
        if ".doc" in arquivo:        
            lista_documentos.append(arquivo)                
                
    if len(lista_planilhas) > 0:
        os.makedirs('Planilhas/')
        for arquivo in lista_planilhas:
            shutil.move(f"Pasta/{arquivo}", f"Planilhas/{arquivo}")
    if len(lista_documentos) > 0:
        os.makedirs('Documentos/')
        for arquivo in lista_documentos:
            shutil.move(f"Pasta/{arquivo}", f"Documentos/{arquivo}") 

    # Saída
    print(f"Pasta Atual", os.getcwd())
    print(f"Arquivos no diretório Pasta/", os.listdir('Pasta/'))
    print(f"Arquivos no diretório Planilhas/", os.listdir('Planilhas/'))
    print(f"Arquivos no diretório Documentos/", os.listdir('Documentos/'))
   
    
    

 
# Execução do programa

if __name__ == "__main__":
    main()