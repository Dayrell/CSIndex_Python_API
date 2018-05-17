from src.utils.utils import get_csv

def score_departamento (area, departamento):
    csv_list = get_csv ('scores', area)

    for row in csv_list:
        if (row[0] == departamento):
            return [row]

def todos_scores (area):
    csv_list = get_csv ('scores', area)
    scores_list = []

    for row in csv_list:
        scores_list.append(row)

    return scores_list