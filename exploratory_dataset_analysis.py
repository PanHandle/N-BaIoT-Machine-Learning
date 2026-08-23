#!/usr/bin/env python3
from local_lib import config as G
from local_lib import tooling as f
from local_lib import eda_figures as fig
import matplotlib.pyplot as plt
import numpy as np
import warnings

G.REPORT = "EDA-FIGURES.md"

f.time_log("setup")
df_combined, data_sources = f.get_csv_data()

f.time_log("setup")

f.reprint("# Exploratory Data Analysis\n", True)
f.reprint(f.two_column_md(["label", "count"], data_sources))
f.reprint(f.quantify_md(df_combined, "Raw Data:"))
f.reprint("## Feature Skewing")

skewership = df_combined.drop(G.DROP_COLS, axis=1).skew().sort_values(ascending=False)
f.reprint(f"![Features by Skew]({
    fig.barplot(skewership.head(G.FIG_BARS), "skew", "Feature Names", f"{G.FIG_BARS} most positively skewed features")
})")

f.time_log("correlation figures")
f.reprint("## Correlation\n")

correlation_matrix, _, df_decorr = f.get_correlated(df_combined)
f.reprint(f"![raw_correlation heatmap]({fig.heatmap_figure("raw_correlation", correlation_matrix)})")
f.reprint(f"New Shape: {df_decorr.shape}")

f.reprint(f"![correlation_filtered]({
    fig.heatmap_figure("correlation_filtered", df_decorr.drop(columns=G.DROP_COLS).corr().abs())
})")
f.time_log("correlation figures")
f.time_log("Screeplot")
f.reprint(f"![Feature Reduction by Screeplot]({
    fig.screeplot(df_combined, "Feature Reduction")
})")
f.time_log("Screeplot")

f.reprint("\n## Data-Shape")
f.time_log(stage="raw scatterplot")
f.reprint(f"![pca Data shape]({fig.scatterplot(df_combined, df_combined["label"], "PCA Data Shape", scaling=True)})\n")
f.time_log(stage="raw scatterplot")


warnings.simplefilter(action="ignore", category=UserWarning) # Supress known warning for overwriting subplot

f.time_log(stage="histograms")
f.reprint("\n## Histogram by window-size")
for label in [ "_L5", "_L3", "_L1", "_L0.1", "_L0.01" ]:
    fig, ax =  plt.subplots(figsize=(20,15))
    df_combined[list(df_combined.filter(regex=label))].hist(figsize=(20,15), ax=ax)
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/histogram{label}.png")
    f.reprint(f"![Histogram for ({label}) window]({G.FIG_DIR}/histogram{label}.png)")
f.time_log(stage="histograms")
warnings.simplefilter(action="default", category=UserWarning)


f.time_log("total")
f.reprint(f.two_column_md(["Section", "Duration"], f.get_time_log()))
