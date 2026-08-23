#!/usr/bin/env python3
from local_lib import config as G
from local_lib import tooling as f
import pandas as pd
import json
G.REPORT = "README.md"

summary_filepath = f"{G.OUT_DIR}/{G.SUMMARY}"
summary_frame = pd.DataFrame(json.load(open(summary_filepath, 'r')))
summary_float = 12
f.reprint("# Generated training and testing output", True)
f.reprint("\n".join([
	"## Table of Contents",
	"- [Exploratory Data Analysis](EDA-FIGURES.md): Pretty Graphs",
	"- [Unsupervised Learning](MODEL_REPORT-UNSUPERVISED.md): Learning, the unsupervised way",
	"- [Supervised Learning](MODEL_REPORT-SUPERVISED.md): Learning, with goals in mind",
	"- [Deep Learning](MODEL_REPORT-DEEP_LEARNING.md): Multi Layered Learning",
	"## Model Performance Summary",
	"The following table has been sorted according to the `accuracy_score` of each model.",
    summary_frame.T.sort_values(by="accuracy_score", ascending=False).to_markdown(floatfmt=f",.{summary_float}g")
]))

