# Machine Learning for N-BaIoT

## List of Models

| Module        | Model                        | Variation upon                        | Stage/Type           |
| ------------- | ---------------------------- | ------------------------------------- | -------------------- |
| Sci-Kit Learn | Random Forest MLP-Classifier | Weight                                | `train-supervised`   |
| Sci-Kit Learn | Decision Tree Classifier     | Depth, Criteria                       | `train-supervised`   |
| Sci-Kit Learn | K-Means                      | Init, Inertia                         | `train-unsupervised` |
| Sci-Kit Learn | DBSCAN                       | Euclidian Distance, Minimum Sample    | `train-unsupervised` |
| Sci-Kit Learn | OPTICS                       | Euclidian Distance, Minimum Sample    | `train-unsupervised` |
| Sci-Kit Learn | Agglomerative Clustering     | Linkage                               | `train-unsupervised` |
| Sci-Kit Learn | MLP-Classifier               | Activation                            | `train-deeplearning` |
| Keras         | 4 Layer MLP                  | Learning Rate, Units                  | `train-deeplearning` |
| Keras         | Deep Nerual Network          | Layers, Dropout, Learning Rate, Units | `train-deeplearning` |

## Dataset overview

The dataset used in this example is a portion of the
[N-BaIoT: Data for network based detection of IoT botnet attaciks][1],
specifically the IOT Camera dataset under `737E`.

This set contains three categories of traffic in distinct files, this are
combined as part of the setup with a `data_source` label to preserve the
origin where needed, such as within supervised learning. No missing values were
identified, 4 label-features have been added.

> [!Warning]
> The dataset is _NOT_ included within this repository, see `local_lib/config.py`
> for how to configure this.

## References

[1]: (https://archive.ics.uci.edu/dataset/442/detection+of+iot+botnet+attacks+n+baiot)
