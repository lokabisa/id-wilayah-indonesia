# Administrative Pipeline

This pipeline is responsible for generating **Indonesia’s administrative division datasets**
based on **official government sources** (primary: Ministry of Home Affairs / Kemendagri,
secondary: BPS where applicable).

It does **not** handle geospatial data (geometry or boundaries).
Its sole responsibility is maintaining **administrative identity, official codes,
and hierarchical relationships** across all levels.

---

## Scope

The administrative pipeline covers the following hierarchy levels:

1. Province
2. Regency / City
3. District
4. Village / Kelurahan

The output of this pipeline serves as the **administrative source of truth**
and can later be joined with geospatial datasets.

---

## Data Sources

Primary source:

- **Ministry of Home Affairs (Kemendagri)**
  - Official publications (PDF / administrative code documents)

Secondary sources (optional, for cross-checking):

- Statistics Indonesia (BPS)

All sources **must be documented** in:

`metadata/sources.md`

---

## Output

This pipeline generates the following CSV files:

```text
data/kemendagri/
├── province.csv
├── regency.csv
├── district.csv
└── village.csv
```

### Output Principles

- CSV files are the **canonical outputs**
- The pipeline must be able to **fully regenerate** these files from source documents
- No manual data insertion without traceable sources
- Output files must remain stable unless source data changes

---

## Directory Structure

```text
pipeline/administrative/
├── README.md
├── extract/
│   └── extract_kemendagri_pdf.py
├── transform/
│   ├── build_province.py
│   ├── build_regency.py
│   ├── build_district.py
│   └── build_village.py
├── validate/
│   └── validate_integrity.py
└── run.py
```

---

## Pipeline Flow

```text
Kemendagri PDF
    ↓
[ extract ]
    ↓
Raw tabular data
    ↓
[ transform ]
    ↓
Normalized CSV
    ↓
[ validate ]
    ↓
data/kemendagri/*.csv
```

---

## Stage Responsibilities

### Extract

- Extract tabular data from source documents (PDF)
- Perform minimal preprocessing only
- Output remains raw and unnormalized

### Transform

- Normalize administrative codes (e.g. remove separators)
- Establish hierarchical relationships
- Produce final structured CSV files

### Validate

- Validate parent–child relationships
- Validate counts (e.g. number of villages per district)
- Detect duplicate or invalid codes
- The pipeline **MUST FAIL** if validation fails

> “Validation rules are considered part of the public contract of this dataset.”

---

## Design Principles

- Reproducible
- Source-traceable
- Deterministic
- No geospatial processing
- No database dependency

---

## Usage

Run the administrative pipeline:

```bash
python pipeline/administrative/run.py
```

> “This command executes the full administrative pipeline (extract → transform → validate) using the configured data sources.”

The pipeline may be executed:

- per province
- or nationally (once configurations are complete)

---

## Notes

- The administrative pipeline must be stable first
  before being joined with geospatial datasets.
- Geospatial processing is handled separately under:

  ```bash
  pipeline/geospatial/
  ```

- Administrative–geospatial joins are performed in a dedicated pipeline stage.

---
