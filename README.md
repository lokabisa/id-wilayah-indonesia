# id-wilayah-indonesia 🇮🇩

Reference datasets and reproducible pipelines
for Indonesian administrative divisions and their geospatial representations.

## Scope

This repository provides:

- Official administrative division datasets (codes & hierarchy)
- Geospatial boundary datasets (GeoJSON)
- Reproducible data pipelines
- Optional read-only API outputs

## Administrative Levels

- Country
- Province
- Regency / City
- District
- Village / Kelurahan

## Data Sources

### Administrative Data

- Ministry of Home Affairs (Kemendagri) — primary authority
- Statistics Indonesia (BPS) — secondary reference and cross-checking

### Geospatial Data

- OpenStreetMap contributors (geometry)
- Extracted via Geofabrik (ODbL 1.0)

### Supplementary Data

- PT Pos Indonesia — postal code reference data

## Repository Structure

- `data/kemendagri` — administrative datasets (source of truth)
- `data/postal` — postal code reference data
- `geojson` — geospatial boundary outputs
- `pipeline` — reproducible administrative and geospatial pipelines
- `public/api` — static API outputs (e.g. GitHub Pages)
- `api` — optional runtime API (e.g. Cloudflare Workers)

## Design Principles

- Clear separation between administrative and geospatial data
- Reproducible and source-traceable pipelines
- Canonical administrative codes without separators
- Dataset-first, API as a derived layer
- Administrative data is authoritative for identity and hierarchy;
  geospatial data is authoritative for geometry only

## License

- Code & pipelines: MIT
- Geospatial data: ODbL (derived from OpenStreetMap)

> “This license applies to code, schemas, and pipeline scripts only.
> Data is subject to its respective source licenses.”
