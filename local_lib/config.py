#!/usr/bin/env python3
from datetime import datetime
import os
# Global constant Definition
## File definition and system behaviour
USERPATH = os.path.expanduser("~")
CSV_DIR = f"{USERPATH}/Datasets/IOT Dataset-Provision_PT_737E_Security_Camera"
OUT_DIR = "outputs" #os.path.abspath("./outputs")
REPORT = "DEFAULT-REPORT.md" # Not treated as a true-constant ;)
SUMMARY = "SUMMARY.json"
FIG_DIR = "figures"  # Relative to OUT_DIR
PKL_DIR = "pickles"  # Relative to OUT_DIR

SUMMIZE = True            # Collect evaluated model info
PRESERVE_PICKLES = True   # Avoid overwriting pickle-files
PICKLE_EVERYTHING = True  # Pickle instances in loops
DOWNGRADE_TYPES = True    # Save memory by shrinking dataset-types
BLOCK_FILE_WRITE = False  # Useful for testing, blocks writing to disk.

## Repeatable output
PADD = [25, 45]  # Column 1, Column 2
FLTP = 3        # Float precision in display
RAND = 19980616
FIG_BARS = 25
FIG_DEPTH = 42

## Generic Hyper Paramaters
HYP_ELBOW = 15
HYP_TRAIN = 0.2
HYP_VALIDATE = 0.15
HYP_DEPTH = 15
HYP_EPOCHS = 16
HYP_BATCH = 256
HYP_PCA = 0.95
HYP_TOP_FT = 20
HYP_CORRELATION_THRESHOLD = 0.95
HYP_SUBSAMPLE = 5150 # Roughly a 50th of sample-set

### Neural Network Paramaters
HYP_NN_LAYERS_TUPLE = [ # Layers, Dropout, Learning rate, Perceptual units
    (6, 0.4, 0.0025, 256),  # Large and slow changing
    (6, 0.4, 0.005, 128),   # Above this point there are more units than intial features
    (4, 0.2, 0.025, 96),
    (4, 0.2, 0.05, 64),
    (3, 0.1, 0.25, 48),
    (2, 0.1, 0.5, 32),      # Small and fast changes
]

### OPTICS & DBSCAN Config
HYP_DBS_BOUNDS = [  # Lower, Upper, Step
    (0.5, 4, 0.5),  # Euclidian Distance
    (5, 21, 5)      # Samples
]
### Sci-Kit Learns Multi Layer Perception Classifier
HYP_SK_MLP_LEARNING_RATE = 0.02
HYP_SK_MLP_LAYERS = (50,50)

## Data sources and formatting
CSV_PATHS = [
    f"{CSV_DIR}/benign_traffic.csv",
    f"{CSV_DIR}/gafgyt_attacks_udp.csv",
    f"{CSV_DIR}/mirai_attacks_udp.csv"
]
DROP_COLS = [
    "label",
    "is_attack" # Binary 0|1 for if the result is an attack
	# "type-benign_traffic",      # Effectively the same as above
	# "type-gafgyt_attacks_udp",  # If the attack matches patterns for gafgyt_attacks
	# "type-mirai_attacks_udp"    # If the attack matches patterns for mirai_attacks
] + [ # Dynamically add each attack-category using path information.
    f"type-{csv_tag.split("/")[-1].split(".")[0]}" for csv_tag in CSV_PATHS
] 
## Timing log for tracking how long things have taken 
timing_log = { "total": datetime.now() } # keep a running log of each stage's duration

## Keras - Tensorflow configuration
os.environ["KERAS_BACKEND"] = "tensorflow"
