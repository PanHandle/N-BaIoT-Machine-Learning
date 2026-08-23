#!/usr/bin/env python3
from . import config as G
import io
from pandas.core.generic import pickle
import os
import pandas as pd
import numpy as np
import sklearn as sk
import warnings
import json
from datetime import datetime

# formatting for markdown and strings
def ffing_string(input_value:object, fmt_spec:str=f",.{G.FLTP}f") -> str:
    """ Formatting floats and strings into a unified thing """
    if isinstance(input_value, (int, float, complex)) and not isinstance(input_value, bool):
        return f"{input_value:{fmt_spec}}"
    return f"{input_value}"

def quantify_dict(dframe:pd.DataFrame) -> dict:
    """Quantify the dframe's features"""
    buffer = io.StringIO() # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
    dframe.info(buf=buffer) # Stow .info into a buffer
    info_dict = { # Now for some fun list-comprehension
        ae[0].strip(): ae[1].strip() for ae in [ # Split a 2d lisit into a dict
            b.split(":") for b in buffer.getvalue().split("\n")[1:-1] # First and last are not-compatible here
        ]
    }
    return {
        "Feature Count": dframe.shape[1],
        "Entries": dframe.shape[0],
        "Duplicates": dframe.duplicated().sum(),
        "Null Values": dframe.isnull().sum().sum(),
        "Data Types": info_dict["dtypes"],
        "Memory Usage": info_dict["memory usage"]
    }

def two_column_md(heading: list, table_content: dict) -> str:
    """ Create a two-colum markdown table, with a parameter for formatting
        NOTE: alternative approach ist to convert type and call DataFrame.to_markdown,
            this method ensures a fixed-width output
    """
    return " |\n".join(
        [ 
            f"| {heading[0].ljust(G.PADD[0], ' ')} | {heading[1].ljust(G.PADD[1])}",
            f"| {':'.ljust(G.PADD[0], '-')} | {':'.rjust(G.PADD[1], '-')}"
        ] + [ # Content from the dictionary version.
            f"| {k.ljust(G.PADD[0],' ')} | { f"{ffing_string(v)}".rjust(G.PADD[1]) }"
            for k,v in table_content.items()
        ] + [""] # Newline and closing '|'
    )

def quantify_md(dframe:pd.DataFrame, name:str="") -> str:
    """Create a markdown compatible table using selected features of a dataframe"""
    return two_column_md(["Dataset:", name], quantify_dict(dframe))

# Logging information
def time_log(stage:str) -> str:
    """"A simple, hacky and easy way to tag sections of proccessing to log durations"""
    if G.timing_log.get(stage, None) is not None:
        # This is an intentional type-change, datetime -> timedelta
        G.timing_log[stage] = datetime.now() - G.timing_log[stage] # type: ignore
        return f"Duration: {G.timing_log[stage]}"
    G.timing_log[stage] = datetime.now()
    return f"New Stage: {stage}"

def get_time_log() -> dict:
    return G.timing_log

def reprint(content:str, clean_file:bool = False):
    """Print and stow the output into a preconfigured `.REPORT` file."""
    report_file_path = f"{G.OUT_DIR}/{G.REPORT}"
    if clean_file:
        print(f"Using clean report_file: {G.REPORT}")
    if not G.BLOCK_FILE_WRITE:
        with open(report_file_path, 'w' if clean_file else 'a') as outfile:
            outfile.write(f"{content}\n")
    print(content)

def summary_append(content:dict, clean_file:bool = False, summary_file=f"{G.SUMMARY}"):
    """Update a key within a json file for model_summary"""
    # If the file exists and not flagged to be overwritten
    summary_filepath = f"{G.OUT_DIR}/{summary_file}"
    logic = clean_file or not os.path.isfile(summary_filepath)
    if not G.BLOCK_FILE_WRITE:
        current_dict = {} if logic else json.load(open(summary_filepath, 'r'))
        ## Merge content, with new values overwriting old (Python 3.9+)
        current_dict = current_dict | content
        with open(summary_filepath, 'w') as outfile:
            outfile.write(json.dumps(current_dict))

# Loading and tagging the datasets
def get_csv_data() -> tuple[pd.DataFrame, dict]:
    counts = {}
    frames = []
    warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
    # Collect and label each source csv file
    for csv in G.CSV_PATHS:
        csv_tag = csv.split("/")[-1].split(".")[0]
        df_temp = pd.read_csv(csv)
        df_temp.insert(0, "label", csv_tag)
        df_temp.insert(0, "is_attack", int(csv_tag != "benign_traffic"))
        # AdHoc-OneHotEncoding
        df_temp.insert(df_temp.shape[1], f"type-{csv_tag}", 1)
        counts[csv_tag] = df_temp.shape[0]
        frames.append(df_temp)
    # Downgrade some of the float64 values to float32, to reduce memory footprint

    df_merge = pd.concat(frames)
    # AdHoc-OneHotEncoding left NaN, we want to fix this, leaving any original cells missing data.
    df_merge[G.DROP_COLS] = df_merge[G.DROP_COLS].fillna(0)

    if G.DOWNGRADE_TYPES:
        ds_flt = df_merge.select_dtypes(include=["float"]).columns
        df_merge[ds_flt] = df_merge[ds_flt].apply(pd.to_numeric, downcast='float')
    warnings.simplefilter(action="default", category=pd.errors.PerformanceWarning)
    return df_merge, counts

def get_correlated(dframe:pd.DataFrame) -> tuple[pd.DataFrame, list, pd.DataFrame]:
    correlation_matrix = dframe.drop(columns=G.DROP_COLS).corr().abs()
    correlation_upper = correlation_matrix.where(
        np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)
    ) # Selecting an upper-triangle of the above correlation
    correlation_drops = [
        col for col in correlation_upper.columns if any(correlation_upper[col] > G.HYP_CORRELATION_THRESHOLD)
    ] # Drop columns below the threshold for correlation
    return correlation_matrix, correlation_drops, dframe.drop(columns=correlation_drops)

def train_test_split(dframe:pd.DataFrame, scaling:bool=False, stratify:bool=True, drop_string:bool=False) -> tuple[
    pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, sk.preprocessing.StandardScaler]:
    """Split, scale and stratify the dataset as needed. NOTE: runs reprint for a markdown flag-callout.
    """
    tdrop = G.DROP_COLS
    x_axis = dframe.drop(tdrop, axis=1)
    if drop_string: # If we want to fully drop the label, we need to drop it from the global and y_axis
        G.DROP_COLS.remove("label")
        tdrop = G.DROP_COLS
    y_axis = dframe[tdrop]
    scale = sk.preprocessing.StandardScaler()
    if stratify:
        x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(
            x_axis, y_axis, test_size=G.HYP_TRAIN, random_state=G.RAND, stratify=y_axis)
    else:
        x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(
            x_axis, y_axis, test_size=G.HYP_TRAIN, random_state=G.RAND)

    scale.fit(x_train) # Scale is always returned fit
    if scaling:
        # Return-types are important, some languages enforce them, python does not.
        # scale.transform returns an numpy.ndarray
        x_train = pd.DataFrame(scale.transform(x_train), columns=x_train.columns)
        x_test = pd.DataFrame(scale.transform(x_test), columns=x_train.columns)
    reprint("\n".join([
         "> [!INFO] Train Test Split:",
        f"> Random state: {G.RAND}",
        f"> Test Size: {G.HYP_TRAIN}",
         "> Feature Flags:",
        f"> - Stratified: {stratify}",
        f"> - Scaled: {scaling}",
        f"> - String-Label: {drop_string}",
        f"> Test columns:\n> - {"\n> - ".join(tdrop)}",
        ""
    ]))
    return x_train, x_test, y_train, y_test, scale

def pickle_this(
        cucumber:object, name_type:str,
        preserve:bool=G.PRESERVE_PICKLES) -> str:
    """ Pickle an object onto disk, optionally preserving an existing pickle."""
    cucumber_path = f"{G.OUT_DIR}/{G.PKL_DIR}/{name_type}.pkl"
    if not ((os.path.isfile(cucumber_path) and preserve) or G.BLOCK_FILE_WRITE):
        with open(cucumber_path, "wb") as handle: # Write Binary
            pickle.dump(cucumber, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return cucumber_path

def pickle_keras(
        cucumber:object, name_type:str,
        preserve:bool=G.PRESERVE_PICKLES) -> str:
    """ Pickle a keras model onto disk, optionally preserving an existing pickle."""
    cucumber_path = f"{G.OUT_DIR}/{G.PKL_DIR}/{name_type}.keras"
    if not ((os.path.isfile(cucumber_path) and preserve) or G.BLOCK_FILE_WRITE):
        # keras Models don't pickle well, the method model.save is reccomended.
        cucumber.save(cucumber_path) # type: ignore # object.save is "unknown" as keras is intentionally unimported
    return cucumber_path

def model_eval(
        algorithm_name:str,
        y_test:pd.DataFrame,
        y_pred:pd.DataFrame,
        summize:bool=G.SUMMIZE,
        flag_subsample:bool=False
) -> str:
    """Evaluate the model's performance in a consistent format"""
    df_y_pred= pd.DataFrame(y_pred, columns=y_test.columns)
    # class_confusion_matrix = sk.metrics.confusion_matrix(
    #     y_test.drop("is_attack", axis=1),
    #     df_y_pred.drop("is_attack",axis=1),
    #     labels=y_test.columns.drop("is_attack"))
    # tnfpfntp
    confusion_matrix = "\n".join([
        f"Feature:{feat}\n- TN:{m[0][0]}\n- FP:{m[0][1]}\n- FN:{m[1][0]}\n- TP:{m[1][1]}" for m, feat in [
            (sk.metrics.confusion_matrix(
            y_test[feat],
            df_y_pred[feat],
        ), feat) for feat in y_test.columns]
    ])
    class_report = pd.DataFrame(sk.metrics.classification_report(
        y_test,
        df_y_pred,
        zero_division=0,
        target_names=y_test.columns,
        output_dict=True
    ))
    accuracy_result = sk.metrics.accuracy_score(y_test, y_pred)
    if summize: # Record key features for a summary comparison
        summary_append({ algorithm_name: {
            "accuracy_score": accuracy_result,
            "f1-score": class_report["weighted avg"]["f1-score"],
            "recall": class_report["weighted avg"]["recall"],
            "precision": class_report["weighted avg"]["precision"],
            "support": class_report["weighted avg"]["support"],
            "subsample training": flag_subsample
        }})
    return "\n".join([
        f"Algorithm name: {algorithm_name}",
        f"Accuracy: {accuracy_result:.8f}",
        f"Confusion_matrix: {confusion_matrix}\n",
        f"\nClassification Report:\n{class_report.to_markdown()}"
    ] + [ "*Trained on Subsample.*" if flag_subsample else "" ])
