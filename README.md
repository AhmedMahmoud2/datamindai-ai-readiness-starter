# DataMindAI — AI Readiness Starter Kit (Databricks + VS Code)

This repository is a **hands-on companion** to the blog/video series **“AI-Ready Data: Why Most AI Projects Fail Before Production.”**
It gives you runnable notebooks and sample data that demonstrate the **four pillars of AI Readiness**:

1. **Trust** — data quality + reliability (contracts, validation, monitoring)
2. **Control** — governance + security (ownership, policies, audit)
3. **Context** — semantics + metadata (glossary, lineage, “RAG-ready” curation)
4. **Feedback** — closed-loop learning (capture corrections, drift checks, continuous improvement)

## Quick Start (Local: VS Code)
1. Create and activate a virtual environment
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebooks in `notebooks/` and run top-to-bottom.

## Quick Start (Azure Databricks)
1. Create a cluster (DBR 13+ recommended).
2. Upload notebooks:
   - Workspace → **Import** → select the `.ipynb` files from `notebooks/`.
3. Install libraries:
   - Cluster → Libraries → **Install New** → **PyPI**  
     Install:
     - `great_expectations`
     - `scikit-learn`
     - `scipy`
     - `duckdb`
     - `pyarrow`
4. Upload sample data folder `data/` to DBFS or Unity Catalog volume:
   - Option A: DBFS: `dbfs:/FileStore/datamindai-ai-readiness/`
   - Option B: Volume: `/Volumes/<catalog>/<schema>/<volume>/datamindai-ai-readiness/`

Then, in each notebook, set `BASE_PATH` to your chosen location.

## Contents
- `notebooks/01_trust_data_quality.ipynb` — data contracts + Great Expectations + quality gates
- `notebooks/02_control_governance_security.ipynb` — ownership, policy checks, audit logs, row-level filtering
- `notebooks/03_context_semantics_metadata.ipynb` — glossary + metadata registry + “RAG-ready” knowledge base + retrieval demo
- `notebooks/04_feedback_closed_loop.ipynb` — capture user feedback, monitor drift, retrain a simple classifier

- `data/raw/` — intentionally imperfect sample data (duplicates, missing values, inconsistent codes)
- `data/curated/` — outputs produced by notebooks (silver/gold-style)
- `src/` — small helper modules used by notebooks
- `docs/` — short guides

## Blog + Videos
- Blog: https://datamindaiwithahmed.com (add your specific blog URL/slug here)
- YouTube Playlist: https://www.youtube.com/playlist?list=PLsL9JQ2lLNZIQmqi_5KHs01-vd8np_pDD

## License
MIT — feel free to use and adapt in your own projects.
