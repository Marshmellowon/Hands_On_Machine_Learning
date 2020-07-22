# batch CEE

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


# y = 신경망
# t = 정답 레이블

# one-hot-encoding 일때
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size


# one-hot-encoding이 아닐때 레이블 표현 일때(숫자일 때 -> 0,1아님)
def cross_entropy_error_not_onehot(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
