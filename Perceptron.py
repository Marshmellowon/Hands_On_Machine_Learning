def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print("AND logic")
print(AND(0, 0))
print(AND(1, 0))
print(AND(0, 1))
print(AND(1, 1))

# 가중치 편향 도입
print("가중치 편향 도입")
import numpy as np


def ANDbias(x1, x2):
    x = np.array([x1, x2])  # 입력
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.7  # 편향

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print(ANDbias(1, 0))

# NAND
print("NAND logic")


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print(NAND(1, 0))

print("OR logic")


def OR(x1, x2):
    x = np.array([x1, x2])  # 입력
    w = np.array([0.5, 0.5])  # 가중치
    b = -0.2  # 편향

    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print(OR(1, 0))
