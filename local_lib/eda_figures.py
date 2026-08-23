#!/usr/bin/env python3
from . import config as G
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import sklearn as sk
import numpy as np
import pandas as pd
import re
plt.rcParams["figure.dpi"] = 300     # Lower DPI for rendering in-line and such
plt.rcParams["savefig.dpi"] = 1200   # Higher DPI for Saving figures to disk
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["grid.alpha"] = 0.5
sns.set_theme(style="whitegrid", palette="crest")

file_text_sane = lambda txt: re.sub(r'[^a-zA-Z0-9\.-_]+', "", txt.replace(" ", "_").replace("=", "_")) # Use Regex to remove "Special Characters"
def heatmap_figure(name:str, dframe:pd.DataFrame ,title:str = "Feature correlation") -> str:
    """Generate a heatmap and return the path it is saved under"""
    fig, ax = plt.subplots(figsize=(20, 15))
    sns.heatmap(dframe, cmap="crest", square=True, ax=ax)
    ax.set_title(title)
    fig.tight_layout()
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/{file_text_sane(name)}_heatmap.png")
    return f"{G.FIG_DIR}/{file_text_sane(name)}_heatmap.png"


def barplot(dframe: pd.Series, x_axis:str, y_axis:str, title:str) -> str:
    """Generate a bar-graph and return the path it is saved under"""
    fig, ax = plt.subplots(figsize=(15, 10))
    dframe.plot(kind="barh", ax=ax, cmap="crest")
    ax.set_ylabel(y_axis)
    ax.set_xlabel(x_axis)
    ax.set_title(title)
    fig.tight_layout()
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/{file_text_sane(title)}_bargraph.png")
    return f"{G.FIG_DIR}/{file_text_sane(title)}_bargraph.png"

def screeplot(dframe:pd.DataFrame, title:str, tdrop:list=G.DROP_COLS) -> str:
    """Generate a screeplot and return the path it is saved under
    https://en.wikipedia.org/wiki/Scree_plot
    """
    fig, ax = plt.subplots()
    color_string = "orange"
    x_axis = sk.preprocessing.StandardScaler().fit_transform(dframe.drop(tdrop, axis=1))
    pca = sk.decomposition.PCA(random_state=G.RAND)
    x_pca = pca.fit(x_axis)
    cumulative_variance = np.cumsum(x_pca.explained_variance_ratio_)
    ax.plot(range(1, len(cumulative_variance) + 1), cumulative_variance)
    feature_count = int(np.argmax(cumulative_variance >= G.HYP_CORRELATION_THRESHOLD) + 1) # How many features explain the variance
    ax.axhline(G.HYP_CORRELATION_THRESHOLD, color=color_string, label=f"{int(100 * G.HYP_CORRELATION_THRESHOLD)}%")
    ax.axvline(feature_count, color=color_string)
    ax.legend()
    ax.set_title(f"{title} for {dframe.shape[1] - len(tdrop)} components")
    ax.set_ylabel("Cumulative Variance")
    ax.set_xlabel(f"Principal Components")
    fig.text(
        0.55,
        0.25,
        f"{feature_count} components cause {int(100 * G.HYP_CORRELATION_THRESHOLD)}% of Variance",
        verticalalignment="center",
        horizontalalignment="center",
    )
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/{file_text_sane(title)}_screeplot.png")
    return f"{G.FIG_DIR}/{file_text_sane(title)}_screeplot.png"

def scatterplot(
        dframe:pd.DataFrame,
        y_axis:pd.DataFrame|pd.Series,
        title:str,
        tdrop:list=G.DROP_COLS,
        scaling:bool=False) -> str:
    """Generate a scatterplot and return the path it is saved under"""
    fig, ax = plt.subplots()
    x_axis = dframe.drop(tdrop, axis=1).values
    if scaling:
        x_axis = sk.preprocessing.StandardScaler().fit_transform(x_axis)
    pca = sk.decomposition.PCA(
        n_components=G.HYP_PCA,
        random_state=G.RAND
    )
    x_pca = pca.fit_transform(x_axis)
    sns.scatterplot(
        x=x_pca[:,0],
        y=x_pca[:,1],
        hue=y_axis,
        ax=ax
    )
    ax.set_title(title)
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/{file_text_sane(title)}_scatterplot.png")
    return f"{G.FIG_DIR}/{file_text_sane(title)}_scatterplot.png"

def lineplot(array: list, x_axis:str, y_axis:str, title:str) -> str:
    """Generate a linegraph and return the path it is saved under"""
    fig, ax = plt.subplots()
    sns.lineplot(x=[e for e in range(1, len(array)+1)], y=array, ax=ax, markers=True)
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/{file_text_sane(title)}_linegraph.png")
    return f"{G.FIG_DIR}/{file_text_sane(title)}_lineraph.png"

def dendrogramplot(model_fit:np.ndarray, title:str, linkage_name:str) -> str:
    """Generate a dendrogram and return the path it is saved under"""
    fig, ax = plt.subplots()
    linkages=linkage(model_fit, method=linkage_name)
    dendrogram(linkages, truncate_mode="lastp", p=G.FIG_DEPTH, leaf_rotation=90, ax=ax)
    ax.set_title(title)
    if not G.BLOCK_FILE_WRITE:
        fig.savefig(f"{G.OUT_DIR}/{G.FIG_DIR}/{file_text_sane(title)}_dendrogram.png")
    return f"{G.FIG_DIR}/{file_text_sane(title)}_dendogram.png"
