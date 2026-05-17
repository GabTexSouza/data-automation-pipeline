# Pipeline de Automação de Dados com Python

Este projeto simula uma rotina de automação de dados em uma área operacional.

A ideia foi consolidar arquivos mensais, tratar inconsistências, gerar uma base final e criar saídas simples para acompanhamento de indicadores.

## Objetivo

Automatizar uma rotina que normalmente seria feita manualmente em Excel, reduzindo retrabalho e risco de erro.

O pipeline realiza:

- leitura de múltiplos arquivos mensais;
- padronização de colunas;
- tratamento de valores ausentes;
- criação de indicadores;
- consolidação em uma base única;
- geração de tabelas resumo;
- criação de relatório em texto;
- criação de log de execução.

## Ferramentas usadas

- Python
- pandas
- openpyxl
- VS Code
- GitHub

## Etapas do projeto

1. Geração de arquivos mensais simulados
2. Leitura automática dos arquivos da pasta `data/raw`
3. Consolidação dos arquivos em uma base única
4. Padronização e tratamento dos dados
5. Criação de indicadores operacionais
6. Geração de tabelas resumo
7. Criação de relatório simples
8. Registro de log da execução
9. Validação da base consolidada em notebook

## Estrutura do pipeline

```text
data/raw/*.xlsx
        ↓
scripts/02_run_pipeline.py
        ↓
data/processed/consolidated_transactions.csv
        ↓
outputs/tables/
outputs/reports/
logs/