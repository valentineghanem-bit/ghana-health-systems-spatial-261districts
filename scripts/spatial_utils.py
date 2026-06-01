"""Reusable spatial utility functions for Ghana Health Systems analysis."""
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


def composite_index(df: pd.DataFrame, cols: list[str], weights: list[float] | None = None) -> pd.Series:
    """Compute equal-weight or custom-weight composite performance index (0-100)."""
    if weights is None:
        weights = [1.0 / len(cols)] * len(cols)
    normed = pd.DataFrame({c: (df[c] - df[c].min()) / (df[c].max() - df[c].min() + 1e-9) for c in cols})
    score = sum(normed[c] * w for c, w in zip(cols, weights))
    return (score * 100).round(2)


def two_step_fca(facilities: gpd.GeoDataFrame, pop_points: gpd.GeoDataFrame,
                 catchment_km: float = 10.0) -> pd.Series:
    """Simplified 2-step floating catchment area accessibility index."""
    facilities = facilities.to_crs(epsg=32630)
    pop_points = pop_points.to_crs(epsg=32630)
    threshold = catchment_km * 1000
    accessibility = []
    for _, pop_row in pop_points.iterrows():
        nearby = facilities[facilities.geometry.distance(pop_row.geometry) <= threshold]
        if nearby.empty:
            accessibility.append(0.0)
        else:
            accessibility.append(nearby['capacity'].sum() / pop_row.get('population', 1))
    return pd.Series(accessibility, index=pop_points.index)
