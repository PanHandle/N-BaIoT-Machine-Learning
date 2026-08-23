#!/usr/bin/env python3
# This is generally the minimal configuration needed for this repository,
# useful for either writing new-stages, or openning a pre-configured INTERACTIVE_SESSION
# Usage;
# STEP 1: activate and setup a python3.12 venv (See run.sh for more info)
# STEP 2: `$ python3.12 -i interactive_startup.py` (-i for interactive)
from local_lib import config as G        # Configuration and hyper-paramaters
from local_lib import tooling as f       # Utilites for loading, evaluating and printing/reporting
from local_lib import eda_figures as fig # Tools for generating figures, most useful in the eda-stage
import matplotlib.pyplot as plt
import sklearn as sk
import numpy as np

G.REPORT = "INTERACTIVE_SESSION.md" # Filename, for output
G.BLOCK_FILE_WRITE = True           # Avoids accidently changing repo content
f.reprint("# Test file title\n", True)
df_combined, data_sources = f.get_csv_data()
x_train, x_test, y_train, y_test, scaler= f.train_test_split(df_combined)

# Pre-cooked sub-samples for smaller training
x_sub_train = x_train.sample(min(G.HYP_SUBSAMPLE, x_train.shape[0]), random_state=G.RAND)
y_sub_train = y_train.iloc[x_sub_train.index.to_list()]

f.reprint(f.quantify_md(df_combined))
