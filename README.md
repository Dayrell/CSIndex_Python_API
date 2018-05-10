# CSIndex Python API

# Execução
Para utilizar essa API, tenha o Python3 e pip3 instalados. Após isso, execute os seguintes comandos no terminal.

1) `pip3 install -r requirements.txt`

2) `FLASK_APP=csindex.py flask run`

Recomenda-se o uso do [virtualenv](https://virtualenv.pypa.io/en/stable/).


# Endpoints

* [<code>GET</code> api/v1/papers/\<area>/total](#total)
* [<code>GET</code> api/v1/papers/\<area>](#papers-area)
* [<code>GET</code> api/v1/scores/\<area>](#scores-area)
* [<code>GET</code> api/v1/professores/](#professor)
* [<code>GET</code> api/v1/professores/\<area>](#professor-area)

## <a name="total"></a>Total de artigos da área
<code>GET api/v1/papers/\<area>/total</code>

Numero de publicações no conjunto de conferencias de uma área.

#### Parâmetros
- **area** _(necessário)_ — Nome área para a qual você quer o total de artigos.

#### Request

    https://120.0.0.1:5000/api/v1/papers/arc/total
    
#### Retorno (csv)
```
47
```

## <a name="papers-area"></a>Total de artigos da área
<code>GET api/v1/papers/\<area>/</code>

Retorna informações de artigos

#### Parâmetros
- **ano**  — Todos os papers de uma área em um determinado ano.
- **departamento**  — Todos os papers de um departamento em uma área.
- **conferencia**  — Número de publicações em uma determinada conferência de uma área.
- **nenhum parâmetro**  — Todos os papers de uma área (ano, título, deptos e autores).

#### Request

    https://120.0.0.1:5000/api/v1/papers/ai?ano=2017
    
#### Retorno (csv)
```
2017,AAAI,Algorithms for Deciding Counting Quantifiers over Unary Predicates.,IME/USP,Marcelo Finger; Glauber De Bona,http://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14515,top
2017,AAAI,Spatial Projection of Multiple Climate Variables Using Hierarchical Multitask Learning.,UNICAMP,André Ricardo Gonçalves; Arindam Banerjee; Fernando J. Von Zuben,http://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/15018,top
...
2017,GECCO,Optimizing one million variable NK landscapes by hybridizing deterministic recombination and local search.,FFCLRP/USP,Francisco Chicano; Darrell Whitley; Gabriela Ochoa; Renato Tinós,http://doi.acm.org/10.1145/3071178.3071285,null
2017,GECCO,Real-polarized genetic algorithm for the three-dimensional bin packing problem.,CEFET-MG,André Homem Dornas; Flávio Vinícius Cruzeiro Martins; João Fernando Machry Sarubbi; Elizabeth Fialho Wanner,http://doi.acm.org/10.1145/3071178.3071327,null
```

#### Request

    https://120.0.0.1:5000/api/v1/papers/ai?professor=2017
    
#### Retorno (csv)
```
2017,AAAI,Algorithms for Deciding Counting Quantifiers over Unary Predicates.,IME/USP,Marcelo Finger; Glauber De Bona,http://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/14515,top
2017,AAAI,Spatial Projection of Multiple Climate Variables Using Hierarchical Multitask Learning.,UNICAMP,André Ricardo Gonçalves; Arindam Banerjee; Fernando J. Von Zuben,http://aaai.org/ocs/index.php/AAAI/AAAI17/paper/view/15018,top
...
2017,GECCO,Optimizing one million variable NK landscapes by hybridizing deterministic recombination and local search.,FFCLRP/USP,Francisco Chicano; Darrell Whitley; Gabriela Ochoa; Renato Tinós,http://doi.acm.org/10.1145/3071178.3071285,null
2017,GECCO,Real-polarized genetic algorithm for the three-dimensional bin packing problem.,CEFET-MG,André Homem Dornas; Flávio Vinícius Cruzeiro Martins; João Fernando Machry Sarubbi; Elizabeth Fialho Wanner,http://doi.acm.org/10.1145/3071178.3071327,null
```
## <a name="scores-area"></a>Scores
<code>GET api/v1/scores/\<area>/</code>

Retorna dados relacionados aos scores.

#### Parâmetros
- **departamento**  — Score de um determinado departamento em uma área.
- **nenhum parâmetro**  — Scores de todos os departamentos em uma área.

#### Request

    https://120.0.0.1:5000/api/v1/scores/ai
    
#### Retorno (csv)
```
IME/USP,6.33
Poli/USP,3.66
...
UFF,0.33
UNICENTRO,0.33
```

## <a name="professor"></a>Professores
<code>GET api/v1/professores/</code>

Todos os papers de um professor (dado o seu nome)

#### Parâmetros
- **professor**  — Todos os papers de um professor (dado o seu nome)

#### Request

    https://120.0.0.1:5000/api/v1/professores/?professor=Wagner-Meira
    
#### Retorno (csv)
```
2017,CCGrid,PRIVAaaS: privacy approach for a distributed cloud-based data analytics platforms.,Tânia Basso; Regina Moraes; Nuno Antunes; Marco Vieira; Walter Santos; Wagner Meira Jr.,https://doi.org/10.1109/CCGRID.2017.136,null
2016,CCGrid,Faster: A Low Overhead Framework for Massive Data Analysis.,Matheus Santos; Wagner Meira Jr.; Dorgival O. Guedes; Virgílio A. F. Almeida,https://doi.org/10.1109/CCGrid.2016.90,null
...
2014,WSDM,Sentiment analysis on evolving social streams: how self-report imbalances can help.,Pedro Henrique Calais Guerra; Wagner Meira Jr.; Claire Cardie,http://doi.acm.org/10.1145/2556195.2556261,null
2013,JCDL,Aggregating productivity indices for ranking researchers across multiple areas.,Harlley Lima; Thiago H. P. Silva; Mirella M. Moro; Rodrygo L. T. Santos; Wagner Meira Jr.; Alberto H. F. Laender,http://doi.acm.org/10.1145/2467696.2467715,null

```
## <a name="professor-area"></a>Professores por área
<code>GET api/v1/professores/\<area>/</code>

Número de professores por área e departamento

#### Parâmetros
- **departamento**  — Número de professores de um determinado departamento que publicam em uma área
- **nenhum parâmetro** — Número de professores que publicam em uma determinada área (organizados por departamentos)

#### Request

    https://120.0.0.1:5000/api/v1/professores/ai
    
#### Retorno (csv)
```
IME/USP,7
Poli/USP,8
...
UTFPR,5
UNICENTRO,9
```

#### Request

    https://120.0.0.1:5000/api/v1/professores/ai?departamento=UFMG
    
#### Retorno (csv)
```
8
```
