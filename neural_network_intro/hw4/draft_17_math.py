# %%
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

#%%
tf_zero= tf.zeros((3,3,3))
# %%
tf_one=tf.ones((3,3,3))
# %%
tf_range=tf.range(1,4,1)
# %%
tf_normal = tf.random.normal((100,100),0, 0.1)
print(tf.reduce_mean(tf_normal))
#print(tf_normal)
tf_normal.numpy()
#print(tf.reshape(tf_normal, [-1, ]).numpy())
counts, bins = np.histogram(tf_normal)
plt.hist(bins[:-1], bins, weights=counts)
# %%
tf_custome = tf.constant([ [[1.0, 2],
                            [3, 4]],
                            [[2, 2],
                            [3, 4]]
                            ])
print(tf.reduce_mean(tf_custome))
print(tf_custome)
print(tf.reshape(tf_custome, [-1, ]).numpy())
counts, bins = np.histogram(tf_custome)
plt.hist(bins[:-1], bins, weights=counts)
# %%

# %%

# %%
