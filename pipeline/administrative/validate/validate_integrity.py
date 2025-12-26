import csv
import sys


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fail(message):
    raise ValueError(message)


def validate_provinces(provinces):
    """
    Validate province.csv
    """
    required_columns = {"code", "name"}
    seen_codes = set()

    for idx, row in enumerate(provinces, start=1):
        # --- required columns ---
        missing = required_columns - row.keys()
        if missing:
            fail(f"[province.csv] Row {idx}: missing columns {missing}")

        code = row.get("code", "").strip()
        name = row.get("name", "").strip()

        # --- code rules ---
        if not code:
            fail(f"[province.csv] Row {idx}: code is empty")

        if not code.isdigit():
            fail(f"[province.csv] Row {idx}: code must be numeric (got '{code}')")

        if len(code) != 2:
            fail(f"[province.csv] Row {idx}: code must be 2 digits (got '{code}')")

        if code in seen_codes:
            fail(f"[province.csv] Row {idx}: duplicate code '{code}'")

        seen_codes.add(code)

        # --- name rules ---
        if not name:
            fail(f"[province.csv] Row {idx}: name is empty")

        # --- area_km2 rules ---
        area = row.get("area_km2", "").strip()
        if area:
            try:
                area_val = float(area)
            except ValueError:
                fail(f"[province.csv] Row {idx}: area_km2 must be numeric (got '{area}')")

            if area_val <= 0:
                fail(f"[province.csv] Row {idx}: area_km2 must be > 0 (got '{area}')")

        # --- island_count rules ---
        island_count = row.get("island_count", "").strip()
        if island_count:
            if not island_count.isdigit():
                fail(
                    f"[province.csv] Row {idx}: island_count must be integer "
                    f"(got '{island_count}')"
                )

            if int(island_count) < 0:
                fail(
                    f"[province.csv] Row {idx}: island_count must be >= 0 "
                    f"(got '{island_count}')"
                )


def main():
    try:
        provinces = load_csv("data/kemendagri/province.csv")
        validate_provinces(provinces)
    except Exception as e:
        print(f"VALIDATION FAILED: {e}", file=sys.stderr)
        sys.exit(1)

    print("Province validation passed ✔")


if __name__ == "__main__":
    main()
