# 미니배치 신경망 학습

import sys, os

sys.path.append(os.pardir)
import numpy as np
from Neural_Network.dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]

# batch size 10장
batch_size = 10

# np.random.choice(A, B) -> 0이상 A미만의 수 중에서 무작위로 B개를 골라낸다.
batch_mask = np.random.choice(train_size, batch_size)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print("x batch", x_batch.shape)
print("t batch", t_batch.shape)
