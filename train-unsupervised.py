#!/usr/bin/env python3
from local_lib import config as G
from local_lib import tooling as f
from local_lib import eda_figures as fig
import pandas as pd
import sklearn as sk
import numpy as np
import warnings

G.REPORT = "MODEL_REPORT-UNSUPERVISED.md"
f.reprint("# Training - Unsupervised", True)
f.time_log("setup")
df_combined, data_sources = f.get_csv_data()
f.time_log("train test split")
x_train, x_test, y_train, y_test, scaler= f.train_test_split(df_combined, scaling=True, stratify=True)
f.time_log("sub-sample")
x_sub_train = x_train.sample(min(G.HYP_SUBSAMPLE, x_train.shape[0]), random_state=G.RAND)
y_sub_train = y_train.iloc[x_sub_train.index.to_list()]
f.time_log("sub-sample")
f.time_log("train test split")
f.time_log("setup")
# ---------------------------------------------------------------------------------------------------------------------

f.time_log("k-means")
f.reprint("\n".join([
    "## KMeans",
    "Arguably the most simple clustering method, given a new point poll the",
    "nearest K points, majority wins. To refine the best K, we iterate over",
    "the possible values and plot the output."
]))
for kinit in ["k-means++", "random"]:
    km_cycle = []
    for k in range(1, G.HYP_ELBOW):
        f.time_log(stage=f"k:{k+1} I:{kinit}") # KMeans for 1 cluster would just be silly (And mess with Silhouette Scoring)
        model_km = sk.cluster.KMeans(n_clusters=k+1, init=kinit, random_state=G.RAND)
        fitting = model_km.fit_predict(x_train)
        km_cycle.append({
            "Inertia": model_km.inertia_,
            "Noise": ( fitting == -1 ).mean() * 100,
            # Using x_sub_train's indexes to reduce proccessing time required for score-generation
            "Silhouette": sk.metrics.silhouette_score(
                x_sub_train, fitting[x_sub_train.index.to_list()]),
            "Adjusted Random Index": sk.metrics.adjusted_rand_score(
                y_sub_train["label"], fitting[x_sub_train.index.to_list()]),
            "Normalised Mutual Information": sk.metrics.normalized_mutual_info_score(
                y_sub_train["label"], fitting[x_sub_train.index.to_list()])
        })
        if G.PICKLE_EVERYTHING:
            f.pickle_this(model_km, f"KMeans-I{kinit}-K{k}-model".replace("+",""))
        f.time_log(stage=f"k:{k+1} I:{kinit}")

    f.reprint(f"![KMeans Elbow {kinit}]({
        fig.lineplot(
            [cyc["Inertia"] for cyc in km_cycle],
            "Number of clusters (k)",
            "WCSS (Inertia)",
            f"Elbow Method for KMeans ({kinit})"
        )
    })")
    f.reprint(f"![KMeans Silhouette {kinit}]({
        fig.lineplot(
            [cyc["Silhouette"] for cyc in km_cycle],
            "Number of clusters (k)",
            "Silhouette score",
            f"KMeans Silhouette ({kinit})"
        )
    })")
    f.reprint(f"![KMeans Adjusted Random Index {kinit}]({
        fig.lineplot(
            [cyc["Adjusted Random Index"] for cyc in km_cycle],
            "Number of clusters (k)",
            "Adjusted Random Index (ARI)",
            f"KMeans ARI ({kinit})"
        )
    })")
    f.reprint(f"![KMeans Normalised Mutual Information {kinit}]({
        fig.lineplot(
            [cyc["Normalised Mutual Information"] for cyc in km_cycle],
            "Number of clusters (k)",
            "Normalised Mutual Information (NMI)",
            f"KMeans NMI ({kinit})"
        )
    })")
    best_kmeans = np.argmax([cyc["Silhouette"] for cyc in km_cycle]) + 2 # 1 for indexing by 0, 1 for the +1 above
    f.reprint(f"Best kmeans for `{kinit}` is {best_kmeans}")
    fitting = sk.cluster.KMeans(
        n_clusters=best_kmeans,
        init=kinit,
        random_state=G.RAND).fit_predict(x_train)
    f.reprint(f"![Kmeans {kinit} Data shape]({fig.scatterplot(
        x_train,
        fitting,
        f"Kmeans Data ({kinit})",
        tdrop=[], scaling=True
    )})")
f.time_log("k-means")

# ---------------------------------------------------------------------------------------------------------------------
f.reprint("\n".join([
	"## OPTICS and DBSCAN",
	"Both of these models are functionally interesting with some issues for training",
	"situations. Sci-kit's `OPTICS` is less actively memory intensive, but is prone",
	"to hanging quietly as it shuffles the memory consumption behind the scenes.",
	"`OPTICS` also works similarly to `DBSCAN`, a model that does not share the same",
	"approach to  memory-safety. `DBSCAN` will consume the available ram and cause",
	"system-crashes. To reduce the impact of these issues, both models are trained",
	f"on {x_sub_train.shape[0]} random sub-samples",
]))

warnings.filterwarnings("ignore", category=RuntimeWarning) # OPTICS has an ignorable issue on some platforms
for model_object, name, nym , heading in [(
        sk.cluster.DBSCAN,
        "DBSCAN",
        "DBS",
        "DBSCAN - Distance Based Scanning"
    ),(
        sk.cluster.OPTICS,
        "OPTICS",
        "OPT",
        "OPTICS - Ordering Points To Identify the Clustering Structure\nOPTICS is functionally similar to DBSCAN."
    )]: # ---- 2 Models, 3 Loops ----
    f.time_log(name)
    f.reprint(f"### {heading}")
    cycle = []
    for euclid in np.arange(*G.HYP_DBS_BOUNDS[0]):
        for sample in np.arange(*G.HYP_DBS_BOUNDS[1]):
            f.time_log(stage=f"{nym}-E:{euclid}/MS:{sample}")
            model_hefty = model_object(
                eps=euclid,
                min_samples=sample,
            )
            fitting = model_hefty.fit_predict(x_sub_train)
            clusters = len(set(fitting)) - (1 if  -1 in fitting else 0)
            cycle.append({
                "Euclidean Distance": euclid,
                "Minimum Samples": sample,
                "Clusters identified": clusters,
                "Noise": ( fitting == -1).mean() * 100,
                "Silhouette": sk.metrics.silhouette_score(
                    x_sub_train, fitting),
                "Adjusted Random Index": sk.metrics.adjusted_rand_score(
                    y_sub_train["label"], fitting),
                "Normalised Mutual Information": sk.metrics.normalized_mutual_info_score(   
                    y_sub_train["label"], fitting)
            })
            if G.PICKLE_EVERYTHING:
                f.pickle_this(model_hefty, f"{nym}-E{euclid}-MS{sample}-model")
            f.time_log(stage=f"{nym}-E:{euclid}/MS:{sample}")
    f.reprint(pd.DataFrame(cycle).to_markdown())
    f.time_log(name)
warnings.filterwarnings("default", category=RuntimeWarning)
# ---------------------------------------------------------------------------------------------------------------------

f.time_log("AgglomerativeClustering")
f.reprint("\n".join([
    "## AgglomerativeClustering",
    "Recursively merge clusters by linkage distance."
]))
cycle = {}
for linkage in ["ward", "complete", "average"]:
    for n in range(2, G.HYP_ELBOW):
        f.time_log(stage=f"n:{n}/{linkage}")
        model_af = sk.cluster.AgglomerativeClustering(n_clusters=n, linkage=linkage)
        fitting = model_af.fit_predict(x_sub_train)
        if G.PICKLE_EVERYTHING:
            f.pickle_this(model_af, f"AGC-L_{linkage}-N{n}-model")
        clusters = len(set(fitting)) - (1 if  -1 in fitting else 0)
        cycle[linkage] = {
            "Clusters identified": clusters,
            "Noise": ( fitting == -1).mean() * 100,
            # Using x_sub_train's indexes to reduce proccessing time required for score-generation
            "Silhouette": sk.metrics.silhouette_score(
                x_sub_train, fitting),
            "Adjusted Random Index": sk.metrics.adjusted_rand_score(
                y_sub_train["label"], fitting),
            "Normalised Mutual Information": sk.metrics.normalized_mutual_info_score(
                y_sub_train["label"], fitting)
            }
        f.time_log(stage=f"n:{n}/{linkage}")

    best_n = np.argmax(cycle[linkage]["Silhouette"]) + 2 # 1 for indexing by 0, 1 for the +1 above
    best_model = sk.cluster.AgglomerativeClustering(n_clusters=best_n, linkage=linkage)
    best_model.fit_predict(x_sub_train)
    dendronym=f"AgglomerativeClustering-{linkage} (N{best_n})"
    f.reprint(f"![{dendronym}]({fig.dendrogramplot(best_model.children_, dendronym, linkage)})")

f.reprint(pd.DataFrame(cycle).T.to_markdown())
f.time_log("AgglomerativeClustering")

# ---------------------------------------------------------------------------------------------------------------------
f.time_log("total")
f.reprint("## Timings for Training")
f.reprint(f.two_column_md(["Section", "Duration"], f.get_time_log()))
