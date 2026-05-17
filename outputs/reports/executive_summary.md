# Resumo executivo

Este projeto simulou uma rotina de automação de dados para consolidar arquivos mensais e gerar saídas tratadas para análise.

## Principais resultados

O pipeline foi capaz de:

- localizar arquivos mensais na pasta `data/raw`;
- consolidar todos os arquivos em uma única base;
- padronizar colunas;
- tratar valores ausentes;
- criar indicadores operacionais;
- gerar tabelas resumo por mês, departamento e região;
- criar um relatório simples em texto;
- registrar log da execução.

## Valor para o negócio

Esse tipo de automação reduz o tempo gasto em consolidações manuais, diminui risco de erro operacional e cria uma base mais confiável para análise.

A estrutura também facilita a atualização recorrente dos dados, pois novos arquivos podem ser adicionados à pasta de entrada e processados pelo mesmo script.

## Possíveis próximos passos

- Agendar a execução automática do pipeline.
- Adicionar validações de qualidade de dados.
- Enviar relatório por e-mail.
- Integrar os dados consolidados com Power BI.
- Criar alertas para arquivos ausentes ou inconsistentes.