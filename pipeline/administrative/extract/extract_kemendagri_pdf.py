import pandas as pd
from pathlib import Path
from .parsers.province_aggregate import extract_province_aggregate

PDF = Path("data/kemendagri/raw/kepmendagri-300.2.2-2138-2025.pdf")
OUT = Path("data/kemendagri/raw/extracted/province_aggregate_raw.csv")

rows = extract_province_aggregate(PDF, pages=[16, 17])

df = pd.DataFrame(rows)
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

print(f"Extracted {len(df)} province aggregate rows → {OUT}")
