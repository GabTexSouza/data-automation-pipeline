import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

raw_path = Path("data/raw")
raw_path.mkdir(parents=True, exist_ok=True)

months = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06"]

departments = ["Operations", "Sales", "Support", "Finance", "Logistics"]
regions = ["Southeast", "South", "Northeast", "Midwest", "North"]
status_options = ["Completed", "Pending", "Canceled"]

for month in months:
    rows = np.random.randint(450, 700)

    df = pd.DataFrame({
        "transaction_id": [f"{month}-{i+1:04d}" for i in range(rows)],
        "transaction_date": pd.date_range(
            start=f"{month}-01",
            periods=rows,
            freq="h"
        ),
        "department": np.random.choice(departments, rows, p=[0.32, 0.24, 0.18, 0.14, 0.12]),
        "region": np.random.choice(regions, rows, p=[0.46, 0.18, 0.16, 0.11, 0.09]),
        "status": np.random.choice(status_options, rows, p=[0.82, 0.12, 0.06]),
        "quantity": np.random.randint(1, 8, rows),
        "unit_value": np.random.normal(180, 45, rows).round(2),
        "responsible_team": np.random.choice(["Team A", "Team B", "Team C"], rows)
    })

    df["unit_value"] = df["unit_value"].clip(lower=30)
    df["total_value"] = (df["quantity"] * df["unit_value"]).round(2)

    missing_index = df.sample(frac=0.02, random_state=42).index
    df.loc[missing_index, "responsible_team"] = np.nan

    file_name = f"transactions_{month}.xlsx"
    df.to_excel(raw_path / file_name, index=False)

print("Arquivos mensais gerados com sucesso.")