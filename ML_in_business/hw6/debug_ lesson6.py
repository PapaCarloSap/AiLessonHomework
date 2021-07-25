# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

# %% [markdown]
# ## Работа с данными
# %% [markdown]
# ## Описание переменных
# 
# ### данные банковского клиента
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | age | numeric | возраст |
# | job | categorical | текущая работа |
# | marital | categorical | семейное положение |
# | education | categorical | образование |
# | default | categorical | имеет ли кредит по умолчанию? |
# | housing | categorical | есть ли жилищный кредит? |
# | loan | categorical | есть ли личный кредит? |
# 
# ### связано с последним контактом текущей кампании 
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | contact | categorical | тип контактной связи |
# | month | categorical | последний месяц контакта в году |
# | day_of_week | categorical | последний контактный день недели |
# | duration | numeric | продолжительность последнего контакта, в секундах (числовое значение). Важное примечание: этот атрибут сильно влияет на целевой результат вывода (например, если длительность=0, то y="нет"). Тем не менее, продолжительность не известна до выполнения вызова. Кроме того, после окончания вызова y, очевидно, известен. Таким образом, эти входные данные следует включать только для целей сравнения и их следует отбросить, если предполагается создать реалистичную прогностическую модель. |
# 
# ### другие атрибуты
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | campaign | numeric | количество контактов, выполненных в ходе этой кампании и для данного клиента |
# | pdays | numeric | количество дней, прошедших после того, как с клиентом в последний раз связывались в рамках предыдущей кампании (числовое значение; 999 означает, что с клиентом ранее не связывались) |
# | previous | numeric | количество контактов, выполненных до этой кампании и для данного клиента |
# | poutcome | categorical | результат предыдущей маркетинговой кампании |
# 
# ### атрибуты социального и экономического контекста
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | emp.var.rate | numeric | коэффициент вариации занятости - квартальный показатель |
# | cons.price.idx | numeric | индекс потребительских цен - месячный показатель |
# | cons.conf.idx | numeric | индекс доверия потребителей - месячный показатель |
# | euribor3m | numeric | ставка euribor за 3 месяца - ежедневный показатель |
# | nr.employed | numeric | численность работников - квартальный показатель |
# 
# ### Выходная переменная (желаемая цель)
# | Название | Тип данных | Описание |
# | ----------- | ----------- | ----------- |
# | y | binary | зарегистрировал ли клиент срочный депозит? |

# %%
df = pd.read_csv("bank-additional-full.csv", delimiter=';')
df.info()


# %%
df.head(10)


# %%
df['y'].value_counts()


# %%
from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_recall_curve
import seaborn as sns

#%%
N = 500
known_labels_ratio = 0.2
X, y = make_blobs(n_samples=N, centers=2, 
                  n_features=2, shuffle=True, 
                  cluster_std=5, random_state=42)
rp = np.random.permutation(int(N/2))
data_P = X[y==1][rp[:int(len(rp)*known_labels_ratio)]]
data_U = np.concatenate((X[y==1][rp[int(len(rp)*known_labels_ratio):]], X[y==0]), axis=0)
print("labeled samples: %d" % (data_P.shape[0]))
# plt.figure(figsize=(10, 6.5))
plt.scatter(data_U[:, 0], data_U[:, 1], c='k', marker='.', linewidth=3, s=1, alpha=0.5, label='Unlabeled')
plt.scatter(data_P[:, 0], data_P[:, 1], c='b', marker='o', linewidth=1, s=20, alpha=0.5, label='Positive')
plt.grid()
plt.legend()

# %%
sns.displot(data_P);

# %%
sns.displot(data_U);


#%%
from tqdm import tqdm

NP = data_P.shape[0]
NU = data_U.shape[0]

T = 1000
K = NP
train_label = np.zeros(shape=(NP+K,))
train_label[:NP] = 1.0
n_oob = np.zeros(shape=(NU,))
f_oob = np.zeros(shape=(NU, 2))
for _ in tqdm(range(T)):
    # Bootstrap resample
    bootstrap_sample = np.random.choice(np.arange(NU), replace=True, size=K)
    # Positive set + bootstrapped unlabeled set
    data_bootstrap = np.concatenate((data_P, data_U[bootstrap_sample, :]), axis=0)
    # Train model
    model = DecisionTreeClassifier(max_depth=None, max_features=None, 
                                   criterion='gini', class_weight='balanced')
    model.fit(data_bootstrap, train_label)
    # Index for the out of the bag (oob) samples
    idx_oob = sorted(set(range(NU)) - set(np.unique(bootstrap_sample)))
    # Transductive learning of oob samples 
    f_oob[idx_oob] += model.predict_proba(data_U[idx_oob])
    n_oob[idx_oob] += 1
predict_proba = f_oob[:, 1]/n_oob

#%%
# Plot the class probabilities for the unlabeled samples
fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(1, 2, 1)
sp= ax1.scatter(data_U[:, 0], data_U[:, 1], c=predict_proba, 
                linewidth=0, s=5, alpha=0.5, cmap=plt.cm.plasma, label='unlabeled')
plt.grid()
plt.colorbar(sp, label='Class probability on Unlabeled set')

true_labels = np.zeros(shape=(data_U.shape[0]))
true_labels[:int(len(rp)*(1.0-known_labels_ratio))] = 1.0
precision, recall, th = precision_recall_curve(true_labels, predict_proba)
ax2 = fig.add_subplot(1, 2, 2)
f1s = precision[:-1]*recall[:-1]
ax2.plot(th, f1s, linewidth=2, alpha=0.5)
best_th = np.argmax(f1s)
ax2.plot(th[best_th], f1s[best_th], c='r', marker='o')
ax2.plot([th[best_th], th[best_th]], [0.0,f1s[best_th] ], 'r--')
ax2.plot([0.0, th[best_th]], [f1s[best_th], f1s[best_th] ], 'r--')
ax2.annotate('Pre: %0.3f, Rec: %0.3f' %(precision[best_th], recall[best_th]), 
             xy=(th[best_th]+ 0.01, f1s[best_th]-0.05))
ax2.set_ylabel('F1 score')
ax2.set_xlabel('Probability threshold')
plt.grid()


# %%
