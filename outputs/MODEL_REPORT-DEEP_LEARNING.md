# Training - Deeplearning

> [!INFO] Train Test Split:
> Random state: 19980616
> Test Size: 0.2
> Feature Flags:
>
> - Stratified: True
> - Scaled: False
> - String-Label: True
>   Test columns:
> - is_attack
> - type-benign_traffic
> - type-gafgyt_attacks_udp
> - type-mirai_attacks_udp

## MLPClassifier

The following 4 instances of Sklearn's MLPClassifier are split based upon their activation function;

- Identity: A no-op activation (Do Nothing) `f(x) = x`
- Logistic: A sigmoid function `f(x) = 1 / (1 + exp(-x))`
- Tanh: Hyberbolic tan function, `f(x) = tanh(x)`
- Relu: Max value between 0 and x `f(x) = max(0, x)`

### Activation - identity

Algorithm name: MLPC - identity
Accuracy: 0.00003102
Confusion_matrix: Feature:is_attack

- TN:3984
- FP:8447
- FN:18019
- TP:34033
  Feature:type-benign_traffic
- TN:51077
- FP:975
- FN:4176
- TP:8255
  Feature:type-gafgyt_attacks_udp
- TN:35801
- FP:7880
- FN:20802
- TP:0
  Feature:type-mirai_attacks_udp
- TN:22203
- FP:11030
- FN:13258
- TP:17992

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.801153 |            0.894366 |                       0 |               0.619943 |  0.680269 |  0.578866 |     0.619494 |    0.833217 |
| recall    |  0.653827 |            0.664066 |                       0 |               0.575744 |  0.517269 |  0.473409 |     0.517269 |    0.531419 |
| f1-score  |  0.720031 |            0.762199 |                       0 |               0.597027 |  0.587676 |  0.519814 |     0.563016 |    0.588613 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### Activation - logistic

Algorithm name: MLPC - logistic
Accuracy: 0.75483461
Confusion_matrix: Feature:is_attack

- TN:10793
- FP:1638
- FN:903
- TP:51149
  Feature:type-benign_traffic
- TN:51149
- FP:903
- FN:1638
- TP:10793
  Feature:type-gafgyt_attacks_udp
- TN:30402
- FP:13279
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:31606
- FP:1627
- FN:14144
- TP:17106

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |   0.96897 |            0.922794 |                 0.61006 |               0.913148 |  0.851224 |  0.853743 |     0.885008 |    0.857714 |
| recall    |  0.982652 |            0.868233 |                0.998702 |               0.547392 |  0.856592 |  0.849245 |     0.856592 |    0.857714 |
| f1-score  |  0.975763 |            0.894682 |                0.757438 |               0.684473 |    0.8539 |  0.828089 |      0.85003 |    0.857714 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### Activation - tanh

Algorithm name: MLPC - tanh
Accuracy: 0.97557496
Confusion_matrix: Feature:is_attack

- TN:10884
- FP:1547
- FN:7
- TP:52045
  Feature:type-benign_traffic
- TN:52045
- FP:7
- FN:1547
- TP:10884
  Feature:type-gafgyt_attacks_udp
- TN:43663
- FP:18
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:31683
- FP:1550
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.971134 |            0.999357 |                0.999134 |               0.952742 |  0.973559 |  0.980592 |     0.974211 |    0.975738 |
| recall    |  0.999866 |            0.875553 |                0.998702 |               0.999968 |  0.986425 |  0.968522 |     0.986425 |    0.975738 |
| f1-score  |   0.98529 |            0.933368 |                0.998918 |               0.975784 |   0.97995 |   0.97334 |     0.979635 |    0.975738 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### Activation - relu

Algorithm name: MLPC - relu
Accuracy: 0.65387777
Confusion_matrix: Feature:is_attack

- TN:10914
- FP:1517
- FN:0
- TP:52052
  Feature:type-benign_traffic
- TN:52052
- FP:0
- FN:1517
- TP:10914
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:20802
- TP:0
  Feature:type-mirai_attacks_udp
- TN:10914
- FP:22319
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.971681 |                   1 |                       0 |                0.58336 |  0.798089 |   0.63876 |     0.697121 |    0.815176 |
| recall    |         1 |            0.877966 |                       0 |                      1 |  0.808478 |  0.719492 |     0.808478 |    0.815176 |
| f1-score  |  0.985637 |            0.935018 |                       0 |               0.736863 |   0.80325 |   0.66438 |     0.737586 |    0.815176 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

## Keras Models

The following models are built using [Keras](https://keras.io), to go beyond
the basic Deep-learning structures within Sklearn.

### Manual Multi-Layer Perception using Keras-Sequential

Algorithm name: Manual Multi-Layer Perception (U:32/LR:0.5)
Accuracy: 0.00001551
Confusion_matrix: Feature:is_attack

- TN:1
- FP:12430
- FN:0
- TP:52052
  Feature:type-benign_traffic
- TN:0
- FP:52052
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:1
- FP:43680
- FN:0
- TP:20802
  Feature:type-mirai_attacks_udp
- TN:1
- FP:33232
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.807233 |            0.192779 |                0.322602 |               0.484631 |   0.45181 |  0.451811 |     0.568671 |    0.451817 |
| recall    |         1 |                   1 |                       1 |                      1 |         1 |         1 |            1 |           1 |
| f1-score  |  0.893336 |            0.323244 |                0.487829 |               0.652864 |   0.62241 |  0.589318 |     0.695654 |    0.615268 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### Deep Neural Network

Algorithm name: Deep Neural Network (U:128/LR:0.005/Dr:0.4/L6)
Accuracy: 0.00276042
Confusion_matrix: Feature:is_attack

- TN:178
- FP:12253
- FN:67
- TP:51985
  Feature:type-benign_traffic
- TN:51985
- FP:67
- FN:12252
- TP:179
  Feature:type-gafgyt_attacks_udp
- TN:233
- FP:43448
- FN:12
- TP:20790
  Feature:type-mirai_attacks_udp
- TN:190
- FP:33043
- FN:55
- TP:31195

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.809256 |            0.727642 |                 0.32364 |               0.485616 |  0.539744 |  0.586539 |     0.627078 |    0.540219 |
| recall    |  0.998713 |           0.0143995 |                0.999423 |                0.99824 |  0.893714 |  0.752694 |     0.893714 |    0.808957 |
| f1-score  |  0.894058 |           0.0282401 |                0.488946 |               0.653381 |  0.673025 |  0.516156 |     0.664845 |    0.647712 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

## Timings for Training

| Section                       |                   Duration |
| :---------------------------- | -------------------------: |
| total                         |             0:04:48.369237 |
| setup                         |             0:00:04.697897 |
| train test split              |             0:00:01.512338 |
| MLPClassifier                 |             0:00:58.685174 |
| MLPC - identity               |             0:00:07.941773 |
| MLPC - logistic               |             0:00:20.589577 |
| MLPC - tanh                   |             0:00:16.467095 |
| MLPC - relu                   |             0:00:13.686542 |
| Manual Multi-Layer Perception | 2026-09-04 16:30:07.897854 |
| MMLP U:256/LR:0.0025          |             0:00:16.849135 |
| MMLP U:128/LR:0.005           |             0:00:13.633428 |
| MMLP U:96/LR:0.025            |             0:00:12.767596 |
| MMLP U:64/LR:0.05             |             0:00:11.757342 |
| MMLP U:48/LR:0.25             |             0:00:11.391959 |
| MMLP U:32/LR:0.5              |             0:00:10.827816 |
| MMLP Final                    |             0:00:01.739488 |
| MMLP pickle                   |             0:00:00.000008 |
| Manual Multi-Layer perception | 2026-09-04 16:31:26.864701 |
| Deep Neural Network           |             0:02:22.282081 |
| DNN U:256/LR:0.0025/Dr:0.4/L6 |             0:00:36.233828 |
| DNN U:128/LR:0.005/Dr:0.4/L6  |             0:00:28.871971 |
| DNN U:96/LR:0.025/Dr:0.2/L4   |             0:00:22.986631 |
| DNN U:64/LR:0.05/Dr:0.2/L4    |             0:00:20.194480 |
| DNN U:48/LR:0.25/Dr:0.1/L3    |             0:00:17.645537 |
| DNN U:32/LR:0.5/Dr:0.1/L2     |             0:00:14.162732 |
| DNN Final                     |             0:00:02.186813 |
| DNN pickle                    |             0:00:00.000009 |
