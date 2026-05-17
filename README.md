# Pipeline de Automação de Dados com Python

Este projeto simula uma rotina de automação de dados em uma área operacional.

A ideia é consolidar arquivos mensais, tratar inconsistências, gerar uma base final e criar saídas simples para acompanhamento de indicadores.

## Objetivo

Automatizar uma rotina que normalmente seria feita manualmente em Excel, reduzindo retrabalho e risco de erro.

O pipeline realiza:

- leitura de múltiplos arquivos mensais;
- padronização de colunas;
- tratamento de valores ausentes;
- criação de indicadores;
- consolidação em uma base única;
- geração de tabelas resumo;
- criação de log de execução.

## Ferramentas

- Python
- pandas
- openpyxl
- VS Code
- GitHub

## Estrutura

```text
data-automation-pipeline/
├── data/
├── logs/
├── outputs/
├── scripts/
├── notebooks/
├── reports/
├── requirements.txt
└── README.md