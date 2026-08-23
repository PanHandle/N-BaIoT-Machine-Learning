# Training - Supervised

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

## DecisionTreeClassifier

Decision-Trees are an example non-parametric classification methods ideal for
multi-classification problems, such as the traffic-type
(Benign or of N-Botnets

### DT - Depth 1, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 1 - entropy
Accuracy: 0.80720500
Confusion_matrix: Feature:is_attack

- TN:0
- FP:12431
- FN:0
- TP:52052
  Feature:type-benign_traffic
- TN:52052
- FP:0
- FN:12431
- TP:0
  Feature:type-gafgyt_attacks_udp
- TN:31249
- FP:12432
- FN:0
- TP:20802
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.807221 |                   0 |                0.625925 |                      1 |  0.807213 |  0.608286 |     0.740447 |    0.807213 |
| recall    |         1 |                   0 |                       1 |               0.999968 |   0.89332 |  0.749992 |      0.89332 |    0.807213 |
| f1-score  |  0.893328 |                   0 |                0.769931 |               0.999984 |  0.848086 |  0.665811 |     0.804609 |    0.807213 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 1, Critera gini

Algorithm name: DecisionTreeClassifier Depth 1 - gini
Accuracy: 0.80720500
Confusion_matrix: Feature:is_attack

- TN:0
- FP:12431
- FN:0
- TP:52052
  Feature:type-benign_traffic
- TN:52052
- FP:0
- FN:12431
- TP:0
  Feature:type-gafgyt_attacks_udp
- TN:31250
- FP:12431
- FN:0
- TP:20802
  Feature:type-mirai_attacks_udp
- TN:33232
- FP:1
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.807221 |                   0 |                0.625944 |               0.999968 |  0.807213 |  0.608283 |     0.740441 |    0.807213 |
| recall    |         1 |                   0 |                       1 |               0.999968 |   0.89332 |  0.749992 |      0.89332 |    0.807213 |
| f1-score  |  0.893328 |                   0 |                0.769945 |               0.999968 |  0.848086 |   0.66581 |     0.804607 |    0.807213 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 1, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 1 - log_loss
Accuracy: 0.80720500
Confusion_matrix: Feature:is_attack

- TN:0
- FP:12431
- FN:0
- TP:52052
  Feature:type-benign_traffic
- TN:52052
- FP:0
- FN:12431
- TP:0
  Feature:type-gafgyt_attacks_udp
- TN:31249
- FP:12432
- FN:0
- TP:20802
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.807221 |                   0 |                0.625925 |                      1 |  0.807213 |  0.608286 |     0.740447 |    0.807213 |
| recall    |         1 |                   0 |                       1 |               0.999968 |   0.89332 |  0.749992 |      0.89332 |    0.807213 |
| f1-score  |  0.893328 |                   0 |                0.769931 |               0.999984 |  0.848086 |  0.665811 |     0.804609 |    0.807213 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 2, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 2 - entropy
Accuracy: 0.99956578
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:27
- TP:52025
  Feature:type-benign_traffic
- TN:52025
- FP:27
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.997833 |                0.999952 |                      1 |   0.99976 |  0.999446 |      0.99976 |    0.999574 |
| recall    |  0.999481 |                   1 |                0.998702 |               0.999968 |  0.999528 |  0.999538 |     0.999528 |    0.999574 |
| f1-score  |  0.999741 |            0.998915 |                0.999327 |               0.999984 |  0.999644 |  0.999492 |     0.999644 |    0.999574 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 2, Critera gini

Algorithm name: DecisionTreeClassifier Depth 2 - gini
Accuracy: 0.99956578
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:27
- TP:52025
  Feature:type-benign_traffic
- TN:52025
- FP:27
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.997833 |                0.999952 |                      1 |   0.99976 |  0.999446 |      0.99976 |    0.999574 |
| recall    |  0.999481 |                   1 |                0.998702 |               0.999968 |  0.999528 |  0.999538 |     0.999528 |    0.999574 |
| f1-score  |  0.999741 |            0.998915 |                0.999327 |               0.999984 |  0.999644 |  0.999492 |     0.999644 |    0.999574 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 2, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 2 - log_loss
Accuracy: 0.99956578
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:27
- TP:52025
  Feature:type-benign_traffic
- TN:52025
- FP:27
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.997833 |                0.999952 |                      1 |   0.99976 |  0.999446 |      0.99976 |    0.999574 |
| recall    |  0.999481 |                   1 |                0.998702 |               0.999968 |  0.999528 |  0.999538 |     0.999528 |    0.999574 |
| f1-score  |  0.999741 |            0.998915 |                0.999327 |               0.999984 |  0.999644 |  0.999492 |     0.999644 |    0.999574 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 3, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 3 - entropy
Accuracy: 0.99958128
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:27
- TP:52025
  Feature:type-benign_traffic
- TN:52025
- FP:27
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.997833 |                       1 |                      1 |  0.999768 |  0.999458 |     0.999769 |    0.999581 |
| recall    |  0.999481 |                   1 |                0.998702 |                      1 |  0.999537 |  0.999546 |     0.999537 |    0.999581 |
| f1-score  |  0.999741 |            0.998915 |                0.999351 |                      1 |  0.999652 |  0.999502 |     0.999652 |    0.999581 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 3, Critera gini

Algorithm name: DecisionTreeClassifier Depth 3 - gini
Accuracy: 0.99968984
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:20
- TP:52032
  Feature:type-benign_traffic
- TN:52032
- FP:20
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:20
- TP:20782
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998394 |                       1 |                      1 |  0.999828 |  0.999598 |     0.999829 |     0.99969 |
| recall    |  0.999616 |                   1 |                0.999039 |                      1 |  0.999657 |  0.999664 |     0.999657 |     0.99969 |
| f1-score  |  0.999808 |            0.999196 |                0.999519 |                      1 |  0.999743 |  0.999631 |     0.999743 |     0.99969 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 3, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 3 - log_loss
Accuracy: 0.99958128
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:27
- TP:52025
  Feature:type-benign_traffic
- TN:52025
- FP:27
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:27
- TP:20775
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.997833 |                       1 |                      1 |  0.999768 |  0.999458 |     0.999769 |    0.999581 |
| recall    |  0.999481 |                   1 |                0.998702 |                      1 |  0.999537 |  0.999546 |     0.999537 |    0.999581 |
| f1-score  |  0.999741 |            0.998915 |                0.999351 |                      1 |  0.999652 |  0.999502 |     0.999652 |    0.999581 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 4, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 4 - entropy
Accuracy: 0.99967433
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:21
- TP:52031
  Feature:type-benign_traffic
- TN:52031
- FP:21
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:21
- TP:20781
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998314 |                       1 |                      1 |   0.99982 |  0.999578 |      0.99982 |    0.999674 |
| recall    |  0.999597 |                   1 |                 0.99899 |                      1 |   0.99964 |  0.999647 |      0.99964 |    0.999674 |
| f1-score  |  0.999798 |            0.999156 |                0.999495 |                      1 |   0.99973 |  0.999612 |      0.99973 |    0.999674 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 4, Critera gini

Algorithm name: DecisionTreeClassifier Depth 4 - gini
Accuracy: 0.99973636
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:17
- TP:52035
  Feature:type-benign_traffic
- TN:52035
- FP:17
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:17
- TP:20785
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998634 |                       1 |                      1 |  0.999854 |  0.999659 |     0.999854 |    0.999736 |
| recall    |  0.999673 |                   1 |                0.999183 |                      1 |  0.999708 |  0.999714 |     0.999708 |    0.999736 |
| f1-score  |  0.999837 |            0.999317 |                0.999591 |                      1 |  0.999781 |  0.999686 |     0.999781 |    0.999736 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 4, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 4 - log_loss
Accuracy: 0.99967433
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:21
- TP:52031
  Feature:type-benign_traffic
- TN:52031
- FP:21
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:21
- TP:20781
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998314 |                       1 |                      1 |   0.99982 |  0.999578 |      0.99982 |    0.999674 |
| recall    |  0.999597 |                   1 |                 0.99899 |                      1 |   0.99964 |  0.999647 |      0.99964 |    0.999674 |
| f1-score  |  0.999798 |            0.999156 |                0.999495 |                      1 |   0.99973 |  0.999612 |      0.99973 |    0.999674 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 5, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 5 - entropy
Accuracy: 0.99967433
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:21
- TP:52031
  Feature:type-benign_traffic
- TN:52031
- FP:21
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:21
- TP:20781
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998314 |                       1 |                      1 |   0.99982 |  0.999578 |      0.99982 |    0.999674 |
| recall    |  0.999597 |                   1 |                 0.99899 |                      1 |   0.99964 |  0.999647 |      0.99964 |    0.999674 |
| f1-score  |  0.999798 |            0.999156 |                0.999495 |                      1 |   0.99973 |  0.999612 |      0.99973 |    0.999674 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 5, Critera gini

Algorithm name: DecisionTreeClassifier Depth 5 - gini
Accuracy: 0.99973636
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:17
- TP:52035
  Feature:type-benign_traffic
- TN:52035
- FP:17
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:17
- TP:20785
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998634 |                       1 |                      1 |  0.999854 |  0.999659 |     0.999854 |    0.999736 |
| recall    |  0.999673 |                   1 |                0.999183 |                      1 |  0.999708 |  0.999714 |     0.999708 |    0.999736 |
| f1-score  |  0.999837 |            0.999317 |                0.999591 |                      1 |  0.999781 |  0.999686 |     0.999781 |    0.999736 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 5, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 5 - log_loss
Accuracy: 0.99967433
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:21
- TP:52031
  Feature:type-benign_traffic
- TN:52031
- FP:21
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:21
- TP:20781
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998314 |                       1 |                      1 |   0.99982 |  0.999578 |      0.99982 |    0.999674 |
| recall    |  0.999597 |                   1 |                 0.99899 |                      1 |   0.99964 |  0.999647 |      0.99964 |    0.999674 |
| f1-score  |  0.999798 |            0.999156 |                0.999495 |                      1 |   0.99973 |  0.999612 |      0.99973 |    0.999674 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 6, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 6 - entropy
Accuracy: 0.99995348
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:2
- TP:52050
  Feature:type-benign_traffic
- TN:52050
- FP:2
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:2
- TP:20800
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999839 |                0.999952 |                      1 |  0.999966 |  0.999943 |     0.999966 |    0.999953 |
| recall    |  0.999962 |             0.99992 |                0.999904 |                      1 |  0.999957 |  0.999946 |     0.999957 |    0.999953 |
| f1-score  |  0.999971 |            0.999879 |                0.999928 |                      1 |  0.999961 |  0.999945 |     0.999961 |    0.999953 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 6, Critera gini

Algorithm name: DecisionTreeClassifier Depth 6 - gini
Accuracy: 0.99973636
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:17
- TP:52035
  Feature:type-benign_traffic
- TN:52035
- FP:17
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:17
- TP:20785
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.998634 |                       1 |                      1 |  0.999854 |  0.999659 |     0.999854 |    0.999736 |
| recall    |  0.999673 |                   1 |                0.999183 |                      1 |  0.999708 |  0.999714 |     0.999708 |    0.999736 |
| f1-score  |  0.999837 |            0.999317 |                0.999591 |                      1 |  0.999781 |  0.999686 |     0.999781 |    0.999736 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 6, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 6 - log_loss
Accuracy: 0.99995348
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:2
- TP:52050
  Feature:type-benign_traffic
- TN:52050
- FP:2
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:2
- TP:20800
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999839 |                0.999952 |                      1 |  0.999966 |  0.999943 |     0.999966 |    0.999953 |
| recall    |  0.999962 |             0.99992 |                0.999904 |                      1 |  0.999957 |  0.999946 |     0.999957 |    0.999953 |
| f1-score  |  0.999971 |            0.999879 |                0.999928 |                      1 |  0.999961 |  0.999945 |     0.999961 |    0.999953 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 7, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 7 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 7, Critera gini

Algorithm name: DecisionTreeClassifier Depth 7 - gini
Accuracy: 0.99992246
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:4
- TP:52048
  Feature:type-benign_traffic
- TN:52048
- FP:4
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:4
- TP:20798
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999678 |                0.999952 |                      1 |  0.999949 |  0.999903 |     0.999949 |    0.999922 |
| recall    |  0.999923 |             0.99992 |                0.999808 |                      1 |  0.999923 |  0.999913 |     0.999923 |    0.999922 |
| f1-score  |  0.999952 |            0.999799 |                 0.99988 |                      1 |  0.999936 |  0.999908 |     0.999936 |    0.999922 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 7, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 7 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 8, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 8 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 8, Critera gini

Algorithm name: DecisionTreeClassifier Depth 8 - gini
Accuracy: 0.99993797
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:3
- TP:52049
  Feature:type-benign_traffic
- TN:52049
- FP:3
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:3
- TP:20799
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999759 |                0.999952 |                      1 |  0.999957 |  0.999923 |     0.999957 |    0.999938 |
| recall    |  0.999942 |             0.99992 |                0.999856 |                      1 |   0.99994 |  0.999929 |      0.99994 |    0.999938 |
| f1-score  |  0.999962 |            0.999839 |                0.999904 |                      1 |  0.999949 |  0.999926 |     0.999949 |    0.999938 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 8, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 8 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 9, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 9 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 9, Critera gini

Algorithm name: DecisionTreeClassifier Depth 9 - gini
Accuracy: 0.99993797
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:3
- TP:52049
  Feature:type-benign_traffic
- TN:52049
- FP:3
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:3
- TP:20799
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999759 |                0.999952 |                      1 |  0.999957 |  0.999923 |     0.999957 |    0.999938 |
| recall    |  0.999942 |             0.99992 |                0.999856 |                      1 |   0.99994 |  0.999929 |      0.99994 |    0.999938 |
| f1-score  |  0.999962 |            0.999839 |                0.999904 |                      1 |  0.999949 |  0.999926 |     0.999949 |    0.999938 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 9, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 9 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 10, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 10 - entropy
Accuracy: 0.99996898
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:2
- TP:52050
  Feature:type-benign_traffic
- TN:52050
- FP:2
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:2
- TP:20800
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.999839 |                       1 |                      1 |  0.999983 |   0.99996 |     0.999983 |    0.999969 |
| recall    |  0.999962 |                   1 |                0.999904 |                      1 |  0.999966 |  0.999966 |     0.999966 |    0.999969 |
| f1-score  |  0.999981 |             0.99992 |                0.999952 |                      1 |  0.999974 |  0.999963 |     0.999974 |    0.999969 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 10, Critera gini

Algorithm name: DecisionTreeClassifier Depth 10 - gini
Accuracy: 0.99993797
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:3
- TP:52049
  Feature:type-benign_traffic
- TN:52049
- FP:3
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:3
- TP:20799
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999759 |                0.999952 |                      1 |  0.999957 |  0.999923 |     0.999957 |    0.999938 |
| recall    |  0.999942 |             0.99992 |                0.999856 |                      1 |   0.99994 |  0.999929 |      0.99994 |    0.999938 |
| f1-score  |  0.999962 |            0.999839 |                0.999904 |                      1 |  0.999949 |  0.999926 |     0.999949 |    0.999938 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 10, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 10 - log_loss
Accuracy: 0.99996898
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:2
- TP:52050
  Feature:type-benign_traffic
- TN:52050
- FP:2
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:2
- TP:20800
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.999839 |                       1 |                      1 |  0.999983 |   0.99996 |     0.999983 |    0.999969 |
| recall    |  0.999962 |                   1 |                0.999904 |                      1 |  0.999966 |  0.999966 |     0.999966 |    0.999969 |
| f1-score  |  0.999981 |             0.99992 |                0.999952 |                      1 |  0.999974 |  0.999963 |     0.999974 |    0.999969 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 11, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 11 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 11, Critera gini

Algorithm name: DecisionTreeClassifier Depth 11 - gini
Accuracy: 0.99993797
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:3
- TP:52049
  Feature:type-benign_traffic
- TN:52049
- FP:3
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:3
- TP:20799
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999759 |                0.999952 |                      1 |  0.999957 |  0.999923 |     0.999957 |    0.999938 |
| recall    |  0.999942 |             0.99992 |                0.999856 |                      1 |   0.99994 |  0.999929 |      0.99994 |    0.999938 |
| f1-score  |  0.999962 |            0.999839 |                0.999904 |                      1 |  0.999949 |  0.999926 |     0.999949 |    0.999938 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 11, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 11 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 12, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 12 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 12, Critera gini

Algorithm name: DecisionTreeClassifier Depth 12 - gini
Accuracy: 0.99996898
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |             0.99992 |                0.999952 |                      1 |  0.999974 |  0.999963 |     0.999974 |    0.999969 |
| recall    |  0.999981 |             0.99992 |                0.999952 |                      1 |  0.999974 |  0.999963 |     0.999974 |    0.999969 |
| f1-score  |  0.999981 |             0.99992 |                0.999952 |                      1 |  0.999974 |  0.999963 |     0.999974 |    0.999969 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 12, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 12 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 13, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 13 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 13, Critera gini

Algorithm name: DecisionTreeClassifier Depth 13 - gini
Accuracy: 0.99993797
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:3
- TP:52049
  Feature:type-benign_traffic
- TN:52049
- FP:3
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:3
- TP:20799
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999759 |                0.999952 |                      1 |  0.999957 |  0.999923 |     0.999957 |    0.999938 |
| recall    |  0.999942 |             0.99992 |                0.999856 |                      1 |   0.99994 |  0.999929 |      0.99994 |    0.999938 |
| f1-score  |  0.999962 |            0.999839 |                0.999904 |                      1 |  0.999949 |  0.999926 |     0.999949 |    0.999938 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 13, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 13 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 14, Critera entropy

Algorithm name: DecisionTreeClassifier Depth 14 - entropy
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 14, Critera gini

Algorithm name: DecisionTreeClassifier Depth 14 - gini
Accuracy: 0.99993797
Confusion_matrix: Feature:is_attack

- TN:12430
- FP:1
- FN:3
- TP:52049
  Feature:type-benign_traffic
- TN:52049
- FP:3
- FN:1
- TP:12430
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:3
- TP:20799
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |  0.999981 |            0.999759 |                0.999952 |                      1 |  0.999957 |  0.999923 |     0.999957 |    0.999938 |
| recall    |  0.999942 |             0.99992 |                0.999856 |                      1 |   0.99994 |  0.999929 |      0.99994 |    0.999938 |
| f1-score  |  0.999962 |            0.999839 |                0.999904 |                      1 |  0.999949 |  0.999926 |     0.999949 |    0.999938 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### DT - Depth 14, Critera log_loss

Algorithm name: DecisionTreeClassifier Depth 14 - log_loss
Accuracy: 0.99998449
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43681
- FP:0
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:0
- TP:31250

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                       1 |                      1 |  0.999991 |   0.99998 |     0.999991 |    0.999984 |
| recall    |  0.999981 |                   1 |                0.999952 |                      1 |  0.999983 |  0.999983 |     0.999983 |    0.999984 |
| f1-score  |   0.99999 |             0.99996 |                0.999976 |                      1 |  0.999987 |  0.999982 |     0.999987 |    0.999984 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

## RandomForestClassifier

A Random-Forest acts as a collection of Decision Trees, to provide a
meta-estimator across subsamples of the fit or predict input data.
This combination of 'trees' provide the inspiration for the name

### Class Weight - balanced

Algorithm name: RandomForestClassifier - balanced
Accuracy: 0.99995348
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:2
- TP:52050
  Feature:type-benign_traffic
- TN:52050
- FP:2
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:2
- TP:20800
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |            0.999839 |                0.999952 |                      1 |  0.999974 |  0.999948 |     0.999974 |    0.999961 |
| recall    |  0.999962 |                   1 |                0.999904 |               0.999968 |  0.999957 |  0.999958 |     0.999957 |    0.999961 |
| f1-score  |  0.999981 |             0.99992 |                0.999928 |               0.999984 |  0.999966 |  0.999953 |     0.999966 |    0.999961 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

### Class Weight - balanced_subsample

Algorithm name: RandomForestClassifier - balanced_subsample
Accuracy: 0.99996898
Confusion_matrix: Feature:is_attack

- TN:12431
- FP:0
- FN:1
- TP:52051
  Feature:type-benign_traffic
- TN:52051
- FP:1
- FN:0
- TP:12431
  Feature:type-gafgyt_attacks_udp
- TN:43680
- FP:1
- FN:1
- TP:20801
  Feature:type-mirai_attacks_udp
- TN:33233
- FP:0
- FN:1
- TP:31249

Classification Report:

|           | is_attack | type-benign_traffic | type-gafgyt_attacks_udp | type-mirai_attacks_udp | micro avg | macro avg | weighted avg | samples avg |
| :-------- | --------: | ------------------: | ----------------------: | ---------------------: | --------: | --------: | -----------: | ----------: |
| precision |         1 |             0.99992 |                0.999952 |                      1 |  0.999983 |  0.999968 |     0.999983 |    0.999977 |
| recall    |  0.999981 |                   1 |                0.999952 |               0.999968 |  0.999974 |  0.999975 |     0.999974 |    0.999977 |
| f1-score  |   0.99999 |             0.99996 |                0.999952 |               0.999984 |  0.999979 |  0.999972 |     0.999979 |    0.999977 |
| support   |     52052 |               12431 |                   20802 |                  31250 |    116535 |    116535 |       116535 |      116535 |

## Timings for Training

| Section                |       Duration |
| :--------------------- | -------------: |
| total                  | 0:02:41.459891 |
| setup                  | 0:00:04.636116 |
| train test split       | 0:00:01.460920 |
| DecisionTreeClassifier | 0:02:19.573774 |
| D1-entropy             | 0:00:02.000068 |
| DTC-D1-entropy         | 0:00:02.000057 |
| D1-gini                | 0:00:01.343065 |
| DTC-D1-gini            | 0:00:01.343056 |
| D1-log_loss            | 0:00:01.972594 |
| DTC-D1-log_loss        | 0:00:01.972585 |
| D2-entropy             | 0:00:02.575445 |
| DTC-D2-entropy         | 0:00:02.575407 |
| D2-gini                | 0:00:02.517552 |
| DTC-D2-gini            | 0:00:02.517541 |
| D2-log_loss            | 0:00:02.636866 |
| DTC-D2-log_loss        | 0:00:02.636857 |
| D3-entropy             | 0:00:03.223473 |
| DTC-D3-entropy         | 0:00:03.223464 |
| D3-gini                | 0:00:02.985882 |
| DTC-D3-gini            | 0:00:02.985872 |
| D3-log_loss            | 0:00:03.166476 |
| DTC-D3-log_loss        | 0:00:03.166467 |
| D4-entropy             | 0:00:03.351243 |
| DTC-D4-entropy         | 0:00:03.351221 |
| D4-gini                | 0:00:03.505255 |
| DTC-D4-gini            | 0:00:03.505245 |
| D4-log_loss            | 0:00:03.228547 |
| DTC-D4-log_loss        | 0:00:03.228534 |
| D5-entropy             | 0:00:03.151377 |
| DTC-D5-entropy         | 0:00:03.151367 |
| D5-gini                | 0:00:03.525385 |
| DTC-D5-gini            | 0:00:03.525376 |
| D5-log_loss            | 0:00:03.135260 |
| DTC-D5-log_loss        | 0:00:03.135252 |
| D6-entropy             | 0:00:03.134750 |
| DTC-D6-entropy         | 0:00:03.134741 |
| D6-gini                | 0:00:03.919916 |
| DTC-D6-gini            | 0:00:03.919907 |
| D6-log_loss            | 0:00:03.215431 |
| DTC-D6-log_loss        | 0:00:03.215419 |
| D7-entropy             | 0:00:03.176274 |
| DTC-D7-entropy         | 0:00:03.176264 |
| D7-gini                | 0:00:03.962281 |
| DTC-D7-gini            | 0:00:03.962268 |
| D7-log_loss            | 0:00:03.501445 |
| DTC-D7-log_loss        | 0:00:03.501435 |
| D8-entropy             | 0:00:03.336995 |
| DTC-D8-entropy         | 0:00:03.336984 |
| D8-gini                | 0:00:04.143739 |
| DTC-D8-gini            | 0:00:04.143728 |
| D8-log_loss            | 0:00:03.140306 |
| DTC-D8-log_loss        | 0:00:03.140295 |
| D9-entropy             | 0:00:03.301163 |
| DTC-D9-entropy         | 0:00:03.301153 |
| D9-gini                | 0:00:03.962262 |
| DTC-D9-gini            | 0:00:03.962250 |
| D9-log_loss            | 0:00:03.318648 |
| DTC-D9-log_loss        | 0:00:03.318637 |
| D10-entropy            | 0:00:03.307497 |
| DTC-D10-entropy        | 0:00:03.307485 |
| D10-gini               | 0:00:04.540852 |
| DTC-D10-gini           | 0:00:04.540842 |
| D10-log_loss           | 0:00:03.302687 |
| DTC-D10-log_loss       | 0:00:03.302677 |
| D11-entropy            | 0:00:03.380527 |
| DTC-D11-entropy        | 0:00:03.380518 |
| D11-gini               | 0:00:04.261264 |
| DTC-D11-gini           | 0:00:04.261255 |
| D11-log_loss           | 0:00:03.511986 |
| DTC-D11-log_loss       | 0:00:03.511975 |
| D12-entropy            | 0:00:03.527253 |
| DTC-D12-entropy        | 0:00:03.527243 |
| D12-gini               | 0:00:04.358732 |
| DTC-D12-gini           | 0:00:04.358721 |
| D12-log_loss           | 0:00:03.505235 |
| DTC-D12-log_loss       | 0:00:03.505224 |
| D13-entropy            | 0:00:03.300152 |
| DTC-D13-entropy        | 0:00:03.300140 |
| D13-gini               | 0:00:04.064346 |
| DTC-D13-gini           | 0:00:04.064335 |
| D13-log_loss           | 0:00:03.243317 |
| DTC-D13-log_loss       | 0:00:03.243304 |
| D14-entropy            | 0:00:03.360522 |
| DTC-D14-entropy        | 0:00:03.360512 |
| D14-gini               | 0:00:04.190743 |
| DTC-D14-gini           | 0:00:04.190732 |
| D14-log_loss           | 0:00:03.284516 |
| DTC-D14-log_loss       | 0:00:03.284504 |
| RandomForestClassifier | 0:00:16.109899 |
| balanced               | 0:00:07.305838 |
| balanced_subsample     | 0:00:08.803985 |
