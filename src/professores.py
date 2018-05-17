from os import listdir
from os.path import isfile, join
import csv
from src.utils.utils import get_csv


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