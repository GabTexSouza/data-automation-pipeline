import logging
from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
OUTPUT_TABLES_PATH = Path("outputs/tables")
OUTPUT_REPORTS_PATH = Path("outputs/reports")
LOG_PATH = Path("logs")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
OUTPUT_TABLES_PATH.mkdir(parents=True, exist_ok=True)
OUTPUT_REPORTS_PATH.mkdir(parents=True, exist_ok=True)
LOG_PATH.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH / "pipeline_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_files():
    files = sorted(RAW_PATH.glob("transactions_*.xlsx"))

    if not files:
        raise FileNotFoundError("Nenhum arquivo mensal encontrado em data/raw.")

    dataframes = []

    for file in files:
        df = pd.read_excel(file)
        df["source_file"] = file.name
        dataframes.append(df)
        logging.info(f"Arquivo carregado: {file.name} | Linhas: {len(df)}")

    return pd.concat(dataframes, ignore_index=True)


def transform_data(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    df["responsible_team"] = df["responsible_team"].fillna("Not assigned")

    df["month"] = df["transaction_date"].dt.to_period("M").astype(str)

    df["is_completed"] = df["status"].eq("Completed")

    df["total_value"] = df["quantity"] * df["unit_value"]
    df["total_value"] = df["total_value"].round(2)

    return df


def create_summary_tables(df):
    monthly_summary = (
        df
        .groupby("month")
        .agg(
            transactions=("transaction_id", "count"),
            completed_transactions=("is_completed", "sum"),
            total_value=("total_value", "sum"),
            avg_ticket=("total_value", "mean")
        )
        .reset_index()
    )

    monthly_summary["completion_rate"] = (
        monthly_summary["completed_transactions"] / monthly_summary["transactions"] * 100
    )

    monthly_summary = monthly_summary.round(2)

    department_summary = (
        df
        .groupby("department")
        .agg(
            transactions=("transaction_id", "count"),
            completed_transactions=("is_completed", "sum"),
            total_value=("total_value", "sum"),
            avg_ticket=("total_value", "mean")
        )
        .reset_index()
    )

    department_summary["completion_rate"] = (
        department_summary["completed_transactions"] / department_summary["transactions"] * 100
    )

    department_summary = department_summary.round(2)

    region_summary = (
        df
        .groupby("region")
        .agg(
            transactions=("transaction_id", "count"),
            completed_transactions=("is_completed", "sum"),
            total_value=("total_value", "sum"),
            avg_ticket=("total_value", "mean")
        )
        .reset_index()
    )

    region_summary["completion_rate"] = (
        region_summary["completed_transactions"] / region_summary["transactions"] * 100
    )

    region_summary = region_summary.round(2)

    return monthly_summary, department_summary, region_summary


def save_outputs(df, monthly_summary, department_summary, region_summary):
    df.to_csv(PROCESSED_PATH / "consolidated_transactions.csv", index=False)

    monthly_summary.to_csv(OUTPUT_TABLES_PATH / "monthly_summary.csv", index=False)
    department_summary.to_csv(OUTPUT_TABLES_PATH / "department_summary.csv", index=False)
    region_summary.to_csv(OUTPUT_TABLES_PATH / "region_summary.csv", index=False)

    report_text = f"""
Pipeline de Automação de Dados

Arquivos processados: {df["source_file"].nunique()}
Total de transações: {len(df)}
Valor total consolidado: {df["total_value"].sum():,.2f}
Taxa geral de conclusão: {df["is_completed"].mean() * 100:.2f}%
Ticket médio: {df["total_value"].mean():,.2f}

Arquivos gerados:
- data/processed/consolidated_transactions.csv
- outputs/tables/monthly_summary.csv
- outputs/tables/department_summary.csv
- outputs/tables/region_summary.csv
- logs/pipeline_execution.log
"""

    with open(OUTPUT_REPORTS_PATH / "pipeline_summary.txt", "w", encoding="utf-8") as file:
        file.write(report_text.strip())


def main():
    logging.info("Início da execução do pipeline")

    df = load_files()
    df = transform_data(df)

    monthly_summary, department_summary, region_summary = create_summary_tables(df)

    save_outputs(df, monthly_summary, department_summary, region_summary)

    logging.info("Pipeline executado com sucesso")

    print("Pipeline executado com sucesso.")


if __name__ == "__main__":
    main()