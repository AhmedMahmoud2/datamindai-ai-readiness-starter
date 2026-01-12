# Azure Databricks Setup (Quick Guide)

## Option A — Using DBFS (simple)
1. Upload `data/` folder to:
   `dbfs:/FileStore/datamindai-ai-readiness/`
2. In notebooks set:
   `BASE_PATH = "/dbfs/FileStore/datamindai-ai-readiness"`

## Option B — Using Unity Catalog Volume (recommended)
1. Create a volume (or use an existing one).
2. Upload `data/` to:
   `/Volumes/<catalog>/<schema>/<volume>/datamindai-ai-readiness/`
3. In notebooks set:
   `BASE_PATH = "/Volumes/<catalog>/<schema>/<volume>/datamindai-ai-readiness"`

## Libraries
Install on the cluster:
- great_expectations
- scikit-learn
- scipy
- duckdb
- pyarrow
