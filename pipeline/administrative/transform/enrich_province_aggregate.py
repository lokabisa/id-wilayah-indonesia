from pathlib import Path
import pandas as pd


PROVINCE_PATH = Path("data/kemendagri/province.csv")
AGG_PATH = Path("data/kemendagri/raw/extracted/province_aggregate_raw.csv")
OUT_PATH = Path("data/kemendagri/province.csv")


def parse_number(val):
    if pd.isna(val) or val == "":
        return None
    val = str(val).replace(".", "").replace(",", ".")
    try:
        if "." in val:
            return float(val)
        return int(val)
    except ValueError:
        return None


def enrich_province():
    # Load data
    prov = pd.read_csv(PROVINCE_PATH, dtype=str)
    agg = pd.read_csv(AGG_PATH, dtype=str)

    # Normalize numeric fields
    for col in [
        "area_km2",
        "island_count",
        "regency_count",
        "city_count",
        "district_count",
        "urban_village_count",
        "rural_village_count",
    ]:
        agg[col] = agg[col].apply(parse_number)

    # Derived field
    agg["village_count"] = (
        agg["urban_village_count"].fillna(0)
        + agg["rural_village_count"].fillna(0)
    )

    # Merge
    merged = prov.merge(
        agg[
            [
                "province_code",
                "area_km2",
                "island_count",
                "regency_count",
                "city_count",
                "district_count",
                "village_count",
                "urban_village_count",
                "rural_village_count",
            ]
        ],
        left_on="code",
        right_on="province_code",
        how="left",
    )

    # Drop join helper
    merged = merged.drop(columns=["province_code"], errors="ignore")

    # Clean _x / _y columns deterministically
    aggregate_cols = [
        "area_km2",
        "island_count",
        "regency_count",
        "city_count",
        "district_count",
        "village_count",
        "urban_village_count",
        "rural_village_count",
    ]

    for col in aggregate_cols:
        col_x = f"{col}_x"
        col_y = f"{col}_y"

        if col_y in merged.columns:
            merged[col] = merged[col_y]
        elif col_x in merged.columns:
            merged[col] = merged[col_x]

        merged = merged.drop(
            columns=[c for c in [col_x, col_y] if c in merged.columns]
        )

    # Final column order (schema contract)
    merged = merged[
        [
            "code",
            "name",
            "area_km2",
            "island_count",
            "regency_count",
            "city_count",
            "district_count",
            "village_count",
            "urban_village_count",
            "rural_village_count",
        ]
    ]

    merged = merged.sort_values(by="code")
    merged.to_csv(OUT_PATH, index=False)

    print("Enriched province.csv successfully")


if __name__ == "__main__":
    enrich_province()
