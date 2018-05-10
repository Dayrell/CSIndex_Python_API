import os
from os import listdir
from os.path import isfile, join
import csv

# pega o conteudo do CSV e adiciona em uma lista de listas
def get_csv (file_type, area):
    file_name = './resources/' + area + '-out-' + file_type + '.csv'
    csv_list = []

    with open(file_name, newline='') as File:  
        csv_object = csv.reader(File)
        for row in csv_object:
            csv_list.append(row)

    return csv_list

# retorna o numero total de papers em uma determinada conferencia
def num_publicacoes_conferencia (file_type, area):
    csv_list = get_csv (file_type, area)
    
    numero_papers = 0
    
    for _ in csv_list:
        numero_papers += 1
    
    return [str(numero_papers)]

# retorna o numero de papers em uma determinada conferencia de uma area
def num_publicacoes_determinada_conferencia (file_type, area, conference):
    csv_list = get_csv (file_type, area)
    numero_papers = 0
    
    for row in csv_list:
        if (row[1] == conference):
            numero_papers += 1
    
    return [str(numero_papers)]

def publicacoes_determinada_area (file_type, area):
    csv_list = get_csv (file_type, area)
    publicacoes_list = []

    for row in csv_list:
        publicacoes_list.append(row)

    return publicacoes_list

def publicacoes_determinada_area_por_ano (file_type, area, ano):
    csv_list = get_csv (file_type, area)
    publicacoes_list = []

    for row in csv_list:
        if (row[0] == ano):
            print(ano)
            publicacoes_list.append(row)

    return publicacoes_list

def publicacoes_determinada_area_por_departamento (file_type, area, departamento):
    csv_list = get_csv (file_type, area)
    publicacoes_list = []

    for row in csv_list:
        if (row[3] == departamento):
            publicacoes_list.append(row)
    
    return publicacoes_list

def nomes_csv_professores (professor):
    lista_nomes = []

    files = [f for f in listdir('./resources/profs') if isfile(join('./resources/profs', f))]
    
    for file_name in files:
        if (file_name.find(professor) != -1):
            lista_nomes.append(file_name)

    return lista_nomes

def publicacoes_de_professor (professor):
    lista_nomes = nomes_csv_professores(professor)
    
    csv_list = []

    for nome in lista_nomes:
        file_name = './resources/profs/' + nome
        with open(file_name, newline='') as File:  
            csv_object = csv.reader(File)
            for row in csv_object:
                csv_list.append(row)
    
    return csv_list

def todos_scores (area):
    csv_list = get_csv ('scores', area)
    scores_list = []

    for row in csv_list:
        scores_list.append(row)

    return scores_list

def score_departamento (area, departamento):
    csv_list = get_csv ('scores', area)

    for row in csv_list:
        if (row[0] == departamento):
            return [row]

def num_professores_area (area):
    csv_list = get_csv ('papers', area)

    universidades = {}
    

    for row in csv_list:
        professores = row[4].split('; ')
        universidades_temp = row[3].split('; ')
        for universidade in universidades_temp:
            for professor in professores:
                if (universidade not in universidades):
                    universidades[universidade] = set()
                universidades[universidade].add(professor)
    
    universidades_csv = []

    for universidade in universidades:
        universidades_csv.append([universidade, len(universidade)])
    return universidades_csv

def num_professores_area_departamento (area, departamento):
    csv_list = get_csv ('papers', area)
    professores = set()
    for row in csv_list:
        universidades_temp = row[3].split('; ')

        for universidade in universidades_temp:
            professores_temp = row[4].split('; ')
            for professor in professores_temp:
                if (universidade == departamento):
                    professores.add(professor)
    
    return [str(len(professores))]