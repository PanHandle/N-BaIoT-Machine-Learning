#!/usr/bin/env python3.12
# python3.12 is needed here for tensorflow and keras_models
import os
from local_lib import config as G
from local_lib import tooling as f
from local_lib import keras_models as k
import pandas as pd
import keras
import sklearn as sk

G.REPORT = "MODEL_REPORT-DEEP_LEARNING.md"
f.reprint("# Training - Deeplearning", True)

# Binary classification for the prediction, using an appraopriately named lambda
bodge = lambda nput: pd.DataFrame([[int(classify > 0) for classify in prediction] for prediction in nput ], columns=y_test.columns)

f.time_log("setup")
df_combined, data_sources = f.get_csv_data()
f.time_log("train test split")
x_train, x_test, y_train, y_test, scaler = f.train_test_split(df_combined, drop_string=True)
f.time_log("train test split")
f.time_log("setup")

# ---------------------------------------------------------------------------------------------------------------------
f.time_log("MLPClassifier")
f.reprint("\n".join([
    "## MLPClassifier",
    "The following 4 instances of Sklearn's MLPClassifier are split based upon their activation function;",
    "- Identity: A no-op activation (Do Nothing) `f(x) = x`",
    "- Logistic: A sigmoid function `f(x) = 1 / (1 + exp(-x))`",
    "- Tanh: Hyberbolic tan function, `f(x) = tanh(x)`",
    "- Relu: Max value between 0 and x `f(x) = max(0, x)`"
]))
for activation in ["identity", "logistic", "tanh", "relu"]:
    f.reprint(f"### Activation - {activation}")
    f.time_log(f"MLPC - {activation}")
    model_mlpc = sk.neural_network.MLPClassifier(
        activation=activation,
        hidden_layer_sizes=G.HYP_SK_MLP_LAYERS,
        learning_rate_init=G.HYP_SK_MLP_LEARNING_RATE,
        max_iter=350,
        random_state=G.RAND
    )
    model_mlpc.fit(x_train, y_train)
    model_mlpc_pred = model_mlpc.predict(x_test)
    f.reprint(f.model_eval( f"MLPC - {activation}", y_test, model_mlpc_pred ))
    f.pickle_this(model_mlpc, f"SK-MLPC-{activation}-model")
    f.time_log(f"MLPC - {activation}")
f.time_log("MLPClassifier")

# ---------------------------------------------------------------------------------------------------------------------
f.reprint("\n".join([ # A bit of context for the shift in process
	"## Keras Models",
	"The following models are built using [Keras](https://keras.io), to go beyond",
	"the basic Deep-learning structures within Sklearn.",
    "### Manual Multi-Layer Perception using Keras-Sequential"
]))
input_features = x_train.shape[1]
output_categories = len(G.DROP_COLS)

f.time_log("Manual Multi-Layer Perception")
sequence_compare = {}

for _, _, learning_rate, units in G.HYP_NN_LAYERS_TUPLE:
    f.time_log(f"MMLP U:{units}/LR:{learning_rate}")
    model = k.build_keras_nn_mlp(learning_rate, units, (input_features, ), output_categories)
    fitting = model.fit(
        x_train,y_train,
        epochs=G.HYP_EPOCHS,
        batch_size=G.HYP_BATCH
    )
    sequence_compare[max(fitting.history['accuracy'])] = { # In the unlikely case of two values the same, the later value is preserved.
        "learning_rate": learning_rate,
        "units": units
    }
    if G.PICKLE_EVERYTHING:
        f.pickle_keras(model, f"MMLP-U{units}-LR{learning_rate}-model")
    f.time_log(f"MMLP U:{units}/LR:{learning_rate}")
f.time_log(f"MMLP Final")

b_key = max(sequence_compare.keys())
b_units = sequence_compare[b_key]["units"]
b_learning_rate = sequence_compare[b_key]["learning_rate"]

cucumber_path = f"{G.OUT_DIR}/{G.PKL_DIR}/MMLP-U{b_units}-LR{b_learning_rate}-model.keras"
if ( os.path.isfile(cucumber_path) and G.PICKLE_EVERYTHING):
    model_mmlp = keras.models.load_model(cucumber_path)
else:
    model_mmlp = k.build_keras_nn_mlp(b_learning_rate, b_units, (input_features, ), output_categories)
    fitting = model_mmlp.fit(x_train, y_train, epochs=G.HYP_EPOCHS, batch_size=G.HYP_BATCH )
model_mmlp_pred = bodge(model_mmlp.predict(x_test)) # type: ignore # This will fail in the event the model is not loaded by keras


f.reprint(f.model_eval(
    f"Manual Multi-Layer Perception (U:{b_units}/LR:{b_learning_rate})",
    y_test, model_mmlp_pred, False
))
f.time_log(f"MMLP Final")
f.time_log(f"MMLP pickle")
f.pickle_keras(model_mmlp, "best-MMLP-model")
f.time_log(f"MMLP pickle")
f.time_log("Manual Multi-Layer perception")

# ---------------------------------------------------------------------------------------------------------------------
f.reprint("### Deep Neural Network")
f.time_log("Deep Neural Network")
sequence_compare = {}
for layers, dropout, learning_rate, units in G.HYP_NN_LAYERS_TUPLE:
    f.time_log(f"DNN U:{units}/LR:{learning_rate}/Dr:{dropout}/L{layers}")
    model = k.build_keras_dnn(layers, dropout, learning_rate, units, (input_features,), output_categories)
    fitting = model.fit(
        x_train,y_train,
        epochs=G.HYP_EPOCHS,
        batch_size=G.HYP_BATCH
    )
    if G.PICKLE_EVERYTHING:
        f.pickle_keras(model, f"DNN-U{units}-LR{learning_rate}-DR{dropout}-L{layers}-model")

    sequence_compare[max(fitting.history['accuracy'])] = {
        "learning_rate": learning_rate,
        "units": units,
        "dropout": dropout,
        "layers": layers
    }
    f.time_log(f"DNN U:{units}/LR:{learning_rate}/Dr:{dropout}/L{layers}")

f.time_log("DNN Final")
b_key = max(sequence_compare.keys())
b_units = sequence_compare[b_key]["units"]
b_dropout = sequence_compare[b_key]["dropout"]
b_learning_rate = sequence_compare[b_key]["learning_rate"]
b_layers = sequence_compare[b_key]["layers"]
cucumber_path = f"{G.OUT_DIR}/{G.PKL_DIR}/DNN-U{b_units}-LR{b_learning_rate}-DR{b_dropout}-L{b_layers}-model.keras"
if (os.path.isfile(cucumber_path) and G.PICKLE_EVERYTHING):
    model_dnn = keras.models.load_model(cucumber_path)
else:
    model_dnn = k.build_keras_dnn(
        b_layers,
        b_dropout,
        b_learning_rate,
        b_units,
        (input_features, ),
        output_categories
    )
    fitting = model_dnn.fit(x_train, y_train, epochs=G.HYP_EPOCHS, batch_size=G.HYP_BATCH )

model_dnn_pred = bodge(model_dnn.predict(x_test)) # type: ignore # This will fail in the event the model is not loaded by keras

f.reprint(f.model_eval(
    f"Deep Neural Network (U:{b_units}/LR:{b_learning_rate}/Dr:{b_dropout}/L{b_layers})",
    y_test, model_dnn_pred, False
))

f.time_log("DNN Final")
f.time_log(f"DNN pickle")
f.pickle_keras(model_dnn, "best-DNN-model")
f.time_log(f"DNN pickle")

f.time_log("Deep Neural Network")
# ---------------------------------------------------------------------------------------------------------------------
f.time_log("total")
f.reprint("## Timings for Training")
f.reprint(f.two_column_md(["Section", "Duration"], f.get_time_log()))


