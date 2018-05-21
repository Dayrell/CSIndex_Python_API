from src.utils.utils import get_csv

# retorna o numero total de papers em uma determinada conferencia
def num_publicacoes_conferencia (file_type, area):
    csv_list = get_csv (file_type, area)

    numero_papers = 0

    for _ in csv_list:
        numero_papers += 1

    return [[str(numero_papers)]]

def publicacoes_determinada_area_por_ano (file_type, area, ano):
    csv_list = get_csv (file_type, area)
    publicacoes_list = []
    for row in csv_list:
        # print(type(row[0]))
        if (int(row[0]) == ano):
            publicacoes_list.append(row)

    return publicacoes_list

def publicacoes_determinada_area_por_departamento (file_type, area, departamento):
    print ("ARQUIVO:", file_type)
    csv_list = get_csv (file_type, area)
    publicacoes_list = []
    print ('publicacoes_determinada_area_por_departamento')
    for row in csv_list:
        print ("ENTROU LOOP")
        print (row)
        if (row[3] == departamento):
            publicacoes_list.append(row)

    return publicacoes_list

# retorna o numero de papers em uma determinada conferencia de uma area
def num_publicacoes_determinada_conferencia (file_type, area, conference):
    csv_list = get_csv (file_type, area)
    numero_papers = 0

    for row in csv_list:
        if (row[1] == conference):
            numero_papers += 1

    return [[str(numero_papers)]]

def publicacoes_determinada_area (file_type, area):
    csv_list = get_csv (file_type, area)
    publicacoes_list = []

    for row in csv_list:
        publicacoes_list.append(row)

    return publicacoes_list
