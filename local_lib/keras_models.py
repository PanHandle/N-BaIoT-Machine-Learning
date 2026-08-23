#!/usr/bin/env python3.12
# python3.12 is needed here for tensorflow and keras_models
import keras

def build_keras_nn_mlp(learning_rate:float, perceptrons:int,
    input_shape:tuple, output_units:int) -> keras.Sequential:
    """Build a simple keras.Sequential model"""
    model = keras.Sequential([ # Layers
        keras.layers.Input(shape=input_shape),
        keras.layers.Dense(units=int(perceptrons), activation="relu"),
        keras.layers.Dense(units=int(perceptrons /2), activation="relu"),
        keras.layers.Dense(units=int(perceptrons /4), activation="relu"),
        keras.layers.Dense(units=int(output_units), activation="softmax"),
    ])
    # https://keras.io/api/models/model_training_apis/
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss="categorical_crossentropy",
        metrics=[
            "accuracy"
        ]
    )
    return model

def build_keras_dnn(layers:int, dropout_rate:float, learning_rate:float, perceptrons:int,
    input_shape:tuple, output_units:int) -> keras.Sequential:
    """Build a keras deep-neural-network model"""
    units = perceptrons
    model = keras.Sequential([keras.layers.Input(shape=input_shape)])
    for _ in range(layers): # Using add to enable configurable layer-depth
        model.add(keras.layers.Dense(units=int(units), activation="relu"))
        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(dropout_rate))
        units = max(units/2, 16)
    model.add(keras.layers.Dense(units=int(output_units), activation="softmax"))

    # https://keras.io/api/models/model_training_apis/
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss="categorical_crossentropy",
        metrics=[
            "accuracy"
        ]
    )
    return model

