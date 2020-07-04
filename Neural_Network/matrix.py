# 다차원 배열의 계산
import numpy as np

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# np.dot 행렬의 곱
print(np.dot(A, B))

# 신경망 구현
print("신경망")


def Neural_Network():
    X = np.array([1, 2])
    W = np.array([[1, 3, 5], [2, 4, 6]])

    Y = np.dot(X, W)
    print(Y)


Neural_Network()

print("-----------3층 신경망-------------")


def Neural_Net(X, W, B):
    # 3층 신경망
    A = np.dot(X, W) + B
    return A


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B = np.array([0.1, 0.2, 0.3])

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

step_1 = sigmoid(Neural_Net(X, W, B))
step_2 = sigmoid(Neural_Net(step_1, W2, B2))

print("2층의 z: ", step_2)

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

step_3 = Neural_Net(step_2, W3, B3)

print("입력 값: ", X)
print("가중치1: \n", W)
print("편향 뉴런1: ", B)
print("출력층: ", step_3)

# 내가짠 3층 신경망
