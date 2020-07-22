# 기울기
import numpy as np


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)  # x와 형상이 같은 배열 생성

    for idx in range(x.size):
        tmp_val = x[idx]

# TODO:  여까지 함
