import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from scipy import interp
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold
#from sklearn.model_selection import GridSearchCV


def show_roc_auc(
    X_train:np.array, 
    y_train:np.array,
    pipe_lr:Pipeline
):
    X_train2 = X_train#[:, [4, 14]]

    cv = list(StratifiedKFold(n_splits=3,
                                random_state=1).split(X_train, y_train))

    fig = plt.figure(figsize=(7, 5))

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)
    all_tpr = []

    for i, (train, test) in enumerate(cv):
        probas = pipe_lr.fit(X_train2.iloc[train],
                            y_train.iloc[train]).predict_proba(X_train2.iloc[test])

        fpr, tpr, thresholds = roc_curve(y_train.iloc[test],
                                        probas[:, 1],
                                        pos_label=1)
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr,
                tpr,
                lw=1,
                label='Блок ROC %d (площадь = %0.2f)'
                    % (i + 1, roc_auc))

    plt.plot([0, 1],
            [0, 1],
            linestyle='--',
            color=(0.6, 0.6, 0.6),
            label='случайное гадание')

    mean_tpr /= len(cv)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    plt.plot(mean_fpr, mean_tpr, 'k--',
            label='средняя ROC (площадь = %0.2f)' % mean_auc, lw=2)


    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('доля ложноположительных')
    plt.ylabel('доля истинноположительных')
    plt.title('График ROC-кривой')
    plt.legend(loc="lower right")

    # plt.tight_layout()
    # plt.savefig('./figures/roc.png', dpi=300)
    plt.show()
