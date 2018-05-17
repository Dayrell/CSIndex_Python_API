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