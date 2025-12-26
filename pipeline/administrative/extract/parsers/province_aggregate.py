import pdfplumber


def split_cell(cell):
    if not cell:
        return []
    return [x.strip() for x in cell.split("\n") if x.strip()]


def extract_province_aggregate(pdf_path, pages):
    rows = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in pages:
            page = pdf.pages[page_num - 1]
            tables = page.extract_tables()

            if not tables:
                continue

            for table in tables:
                if not table or len(table) < 2:
                    continue

                for row in table[1:]:
                    if not row or len(row) < 3:
                        continue

                    codes = split_cell(row[1])
                    names = split_cell(row[2])

                    if not codes or not names:
                        continue

                    # remaining columns = aggregates
                    aggregates = [split_cell(c) for c in row[3:]]

                    for i, code in enumerate(codes):
                        if not code.isdigit() or len(code) != 2:
                            continue

                        try:
                            rows.append(
                                {
                                    "province_code": code,
                                    "regency_count": aggregates[0][i],
                                    "city_count": aggregates[1][i],
                                    "district_count": aggregates[2][i],
                                    "urban_village_count": aggregates[3][i],
                                    "rural_village_count": aggregates[4][i],
                                    "village_count": "",  # derived later
                                    "area_km2": aggregates[5][i],
                                    "island_count": aggregates[7][i],
                                    "source_page": page_num,
                                }
                            )
                        except IndexError:
                            # defensive: skip incomplete rows
                            continue

    return rows
