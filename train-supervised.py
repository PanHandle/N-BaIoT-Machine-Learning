#!/usr/bin/env python3
from local_lib import config as G
from local_lib import tooling as f
import sklearn as sk

G.REPORT = "MODEL_REPORT-SUPERVISED.md"
f.reprint("# Training - Supervised", True)

f.time_log("setup")
df_combined, data_sources = f.get_csv_data()
f.time_log("train test split")
x_train, x_test, y_train, y_test, scaler= f.train_test_split(df_combined, drop_string=True)
f.time_log("train test split")
f.time_log("setup")

# ---------------------------------------------------------------------------------------------------------------------
f.time_log("DecisionTreeClassifier")
f.reprint("\n".join([
    "## DecisionTreeClassifier",
    "Decision-Trees are an example non-parametric classification methods ideal for",
    "multi-classification problems, such as the traffic-type",
    "(Benign or of N-Botnets",
]))
for dep in range(1, G.HYP_DEPTH):
    for criteria in ["entropy", "gini", "log_loss"]: # https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
        f.reprint(f"### DT - Depth {dep}, Critera {criteria}")
        f.time_log(stage=f"D{dep}-{criteria}")
        model_tag=f"DTC-D{dep}-{criteria}"
        f.time_log(model_tag)
        model_dt = sk.tree.DecisionTreeClassifier(
            max_depth=dep,
            criterion=criteria,
            random_state=G.RAND
        )
        model_dt.fit(x_train, y_train)
        model_dt_pred = model_dt.predict(x_test)
        f.reprint(f.model_eval( f"DecisionTreeClassifier Depth {dep} - {criteria}", y_test, model_dt_pred ))
        f.pickle_this(model_dt, f"{model_tag}-model")
        f.time_log(model_tag)
        f.time_log(stage=f"D{dep}-{criteria}")

f.time_log("DecisionTreeClassifier")
# ---------------------------------------------------------------------------------------------------------------------
f.time_log("RandomForestClassifier")
f.reprint("\n".join([
    "## RandomForestClassifier",
	"A Random-Forest acts as a collection of Decision Trees, to provide a",
	"meta-estimator across subsamples of the fit or predict input data.",
	"This combination of 'trees' provide the inspiration for the name",
]))
for weight in ["balanced", "balanced_subsample"]:
    model_tag=f"RFC-W{weight}"
    f.time_log(weight)
    f.reprint(f"### Class Weight - {weight}")
    model_rfc = sk.ensemble.RandomForestClassifier(
        n_estimators=100,
        class_weight=weight,
        n_jobs=-1,
        random_state=G.RAND
    )
    model_rfc.fit(x_train, y_train)
    model_rfc_pred = model_rfc.predict(x_test)
    # model_rfc.predict_proba(x_test)[:, 1]
    f.reprint(f.model_eval(
        f"RandomForestClassifier - {weight}",
        y_test, model_rfc_pred
    ))
    f.pickle_this(model_rfc, f"{model_tag}-model")
    f.time_log(weight)
f.time_log("RandomForestClassifier")


# ---------------------------------------------------------------------------------------------------------------------
f.time_log("total")
f.reprint("## Timings for Training")
f.reprint(f.two_column_md(["Section", "Duration"], f.get_time_log()))
