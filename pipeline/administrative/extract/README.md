# Administrative Data Extraction

This directory contains scripts and notes for extracting
administrative data from official Kemendagri PDF documents.

## Source Document

- Minister of Home Affairs Decree No. 300.2.2-2138 of 2025
- File: `kepmendagri-300.2.2-2138-2025.pdf`
- Source URL documented in `metadata/sources.md`

## Extraction Strategy

Administrative tables in Kemendagri PDFs are not fully machine-friendly.
They often contain:

- multi-row headers
- page-split tables
- legal footnotes
- inconsistent formatting across sections

For this reason, extraction is performed using a **semi-automated approach**:

- page ranges are explicitly defined
- extraction is done per administrative level
- normalization and validation are handled in later stages

## Output

Extraction produces **raw tabular outputs** only.
These outputs are not canonical and are not validated.

Normalization and validation occur in the transform and validate stages.
