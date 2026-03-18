---
title: scRNA Orchestrator
description: End-to-end single-cell RNA-seq analysis pipeline
---

# scRNA Orchestrator

End-to-end single-cell RNA-seq pipeline built on Scanpy. QC filtering, normalisation, dimensionality reduction, clustering, marker gene identification, and doublet removal.

## Quick Demo

```bash
python skills/scrna-orchestrator/scrna_orchestrator.py --demo --output /tmp/scrna_demo
```

## CLI Reference

```bash
python skills/scrna-orchestrator/scrna_orchestrator.py \
  --input <data.h5ad> \
  --output <report_dir>

# With doublet detection
python skills/scrna-orchestrator/scrna_orchestrator.py \
  --demo --doublet-method scrublet --output /tmp/scrna_doublet_demo
```

| Argument | Required | Description |
|----------|----------|-------------|
| `--input` | Yes* | Path to AnnData (.h5ad) file |
| `--output` | Yes | Output directory |
| `--demo` | No | Use built-in PBMC3k demo data |
| `--doublet-method` | No | Doublet detection method (scrublet) |

## Pipeline Steps

1. **QC Filtering** — mitochondrial %, gene counts, cell counts
2. **Normalisation** — library size normalisation + log1p
3. **HVG Selection** — highly variable genes
4. **PCA** — dimensionality reduction
5. **Neighbourhood Graph** — k-NN graph construction
6. **Clustering** — Leiden community detection
7. **UMAP** — 2D embedding visualisation
8. **Marker Genes** — rank_genes_groups per cluster
9. **Doublet Detection** — optional Scrublet integration

## Output

- `report.md` — Analysis report with QC stats and cluster annotations
- `figures/` — UMAP plots, QC violin plots, marker gene dotplots
- `processed.h5ad` — Processed AnnData object
- Reproducibility bundle
