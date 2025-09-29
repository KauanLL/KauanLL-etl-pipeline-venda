# 🛠️ ETL Pipeline de Vendas (Projeto de Estudo)

Este é um projeto de **estudo** em Engenharia de Dados, com o objetivo de aprender e praticar a construção de **pipelines ETL** utilizando Python, Pandas, SQLite e Prefect.  

A ideia é simular um cenário simples de uma empresa que recebe dados de vendas em **arquivos CSV** e precisa:  
1. Extrair os dados       (E – Extract)  
2. Transformar os dados   (T – Transform)  
   - Padronizar colunas  
   - Converter tipos de dados  
   - Validar qualidade (data quality checks)  
3. Carregar em um banco de dados relacional (L – Load)  

Mesmo sendo um projeto simples, ele já traz conceitos muito usados em cenários reais, como **logs, observabilidade e testes automatizados**.

---

## 🎯 Objetivos do Projeto
- Praticar a construção de pipelines ETL.  
- Aprender boas práticas de organização de projetos em Python.  
- Exercitar **Data Quality** (validação de dados antes de carregar).  
- Usar o **Prefect** para orquestração e logs.  
- Aplicar **testes unitários** para validar as transformações.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Pandas** → manipulação de dados  
- **SQLite** → banco de dados leve para armazenar os dados transformados  
- **Prefect** → orquestração e monitoramento do pipeline  
- **Pytest** → testes automatizados

---

## 📂 Estrutura do Projeto
	etl-pipeline-venda/
	│──data/ # Arquivos CSV de entrada (ex: vendas.csv)
	│── src/
	│ ├── extract.py # Extração dos dados
	│ ├── transform.py # Transformação + validações de qualidade
	│ ├── load.py # Carregamento no SQLite
	│ └── pipeline.py # Orquestração com Prefect
	│── tests/ # Testes unitários
	│── requirements.txt # Dependências
	│── README.md # Documentação
