# CSIndex Python API

# Endpoints

[<code>GET</code> api/v1/papers/\<professor>](#professor)
[<code>GET</code> api/v1/papers/\<area>/total](#total)
[<code>GET</code> api/v1/papers/\<area>](#papers-area)
[<code>GET</code> api/v1/scores/\<area>](#scores-area)
[<code>GET</code> api/v1/professores/\<area>](#professor-area)


## <a name="professor"></a>Professor
Retorna todos os papers de um professor (dado o seu nome).

#### Parâmetros
- **professor** _(necessário)_ — Nome do professor para o qual você quer os artigos.

#### Request

    https://120.0.0.1:5000/api/v1/papers/Wagner-Meira
    
#### Retorno (csv)
```
2017,CCGrid,PRIVAaaS: privacy approach for a distributed cloud-based data analytics platforms.,Tânia Basso; Regina Moraes; Nuno Antunes; Marco Vieira; Walter Santos; Wagner Meira Jr.,https://doi.org/10.1109/CCGRID.2017.136,null
2016,CCGrid,Faster: A Low Overhead Framework for Massive Data Analysis.,Matheus Santos; Wagner Meira Jr.; Dorgival O. Guedes; Virgílio A. F. Almeida,https://doi.org/10.1109/CCGrid.2016.90,null
...
2014,WSDM,Sentiment analysis on evolving social streams: how self-report imbalances can help.,Pedro Henrique Calais Guerra; Wagner Meira Jr.; Claire Cardie,http://doi.acm.org/10.1145/2556195.2556261,null
2013,JCDL,Aggregating productivity indices for ranking researchers across multiple areas.,Harlley Lima; Thiago H. P. Silva; Mirella M. Moro; Rodrygo L. T. Santos; Wagner Meira Jr.; Alberto H. F. Laender,http://doi.acm.org/10.1145/2467696.2467715,null
```

## <a name="total"></a>Total de artigos da área
Numero de publicações no conjunto de conferencias de uma área.

#### Parâmetros
- **area** _(necessário)_ — Nome área para a qual você quer o total de artigos.

#### Request

    https://120.0.0.1:5000/api/v1/papers/arch/total
    
#### Retorno (csv)
```
47
```

## <a name="papers-area"></a>Total de artigos da área
Retorna informações de artigos

#### Parâmetros
- **ano**  — Todos os papers de uma área em um determinado ano.
- **departamento**  — Todos os papers de um departamento em uma área.
- **conferencia**  — Número de publicações em uma determinada conferência de uma área.
- **nenhum parâmetro**  — Todos os papers de uma área (ano, título, deptos e autores).

#### Request

    https://120.0.0.1:5000/api/v1/papers/arch/total
    
#### Retorno (csv)
```
47
```
