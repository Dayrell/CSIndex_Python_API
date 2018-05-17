from flask import Flask
from flask import make_response, request
from flask import render_template
import io
import csv

from src.papers import *
from src.scores import *
from src.professores import *


app = Flask(__name__)

def cria_csv (csv_list):
    si = io.StringIO()

    cw = csv.writer(si)
    cw.writerows(csv_list)

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=total_papers.csv"
    output.headers["Content-type"] = "text/csv"

    return output

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/api/v1/papers/<area>/total')
# Numero de publicacoes no conjunto de conferencias de uma area
def total_papers(area):
    csv_list = num_publicacoes_conferencia('papers', area)
    # print ("csv_list: ", csv_list)

    output = cria_csv(csv_list)

    return output

@app.route('/api/v1/papers/<area>')
def list_papers_from_area (area):
    ano = request.args.get('ano')
    departamento = request.args.get('departamento')
    conferencia = request.args.get('conferencia')
    print(ano)

    if (ano != None):
        # Todos os papers de uma área em um determinado ano
        csv_list = publicacoes_determinada_area_por_ano('papers', area, int(ano))
    elif (departamento != None):
        # Todos os papers de um departamento em uma área
        csv_list = publicacoes_determinada_area_por_departamento('papers', area, departamento)
    elif (conferencia != None):
        # Número de publicações em uma determinada conferência de uma área
        csv_list = num_publicacoes_determinada_conferencia('papers', area, conferencia)
    else:
        # Todos os papers de uma área (ano, título, deptos e autores)
        csv_list = publicacoes_determinada_area('papers', area)

    output = cria_csv(csv_list)

    return output

@app.route('/api/v1/scores/<area>')
def scores(area):
    departamento = request.args.get('departamento')

    if (departamento != None):
        # Score de um determinado departamento em uma área.
        csv_list = score_departamento(area, departamento)
    else:
        # Scores de todos os departamentos em uma área
        csv_list = todos_scores(area)

    output = cria_csv(csv_list)

    return output

@app.route('/api/v1/professores/')
def professores ():
    professor = request.args.get('professor')

    # Todos os papers de um professor (dado o seu nome)
    csv_list = publicacoes_de_professor(professor)

    output = cria_csv(csv_list)

    return output

@app.route('/api/v1/professores/<area>')
def professores_area (area):
    departamento = request.args.get('departamento')

    if (departamento != None):
        # Número de professores de um determinado departamento que publicam em uma área
        csv_list = num_professores_area_departamento(area, departamento)
    else:
        # Número de professores que publicam em uma determinada área (organizados por departamentos)
        csv_list = num_professores_area(area)

    output = cria_csv(csv_list)

    return output
