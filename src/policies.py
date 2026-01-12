from __future__ import annotations
from dataclasses import dataclass
import pandas as pd

@dataclass
class UserContext:
    user: str
    role: str  # e.g., 'steward', 'analyst', 'viewer'
    allowed_departments: list[str]

def apply_row_level_policy(df: pd.DataFrame, ctx: UserContext, department_col: str = "department") -> pd.DataFrame:
    """Simple row-level filtering to demonstrate policy-based access.

    In real platforms you would use:
    - Unity Catalog row filters (Databricks)
    - Snowflake row access policies
    - Lakehouse security models
    """
    if department_col not in df.columns:
        return df
    return df[df[department_col].isin(ctx.allowed_departments)].copy()
