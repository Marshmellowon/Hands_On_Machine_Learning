class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def hello(self):
        print("hello " + self.name + "!")

    def goodbye(self):
        print("Good bye " + self.name + "!")


m = Man("David")
m.hello()
m.goodbye()

# Numpy
print("--------------Numpy--------------")
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x * 2)
print(x + y)

q = np.array([[1, 2], [3, 4]])
print(q.shape)  # shape: 행렬의 형상
print(q.dtype)  # 원소의 자료형

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
print("1차원 * 2차원: ", A * B)
print("======")
X = np.array([[51, 55], [14, 19], [0, 4]])
for row in X:
    print(row)
print("=====")
# X를 1차원 배열로 변환
X = X.flatten()
print(X)
print(X > 15)

# 그래프 그리기
print("--------------matplotlib--------------")
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 데이터 준비
x1 = np.arange(0, 6, 0.1)
y1 = np.sin(x1)
y2 = np.cos(x1)

# 그래프 그리기
plt.plot(x1, y1, label="sin")
plt.plot(x1, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.savefig('cossin.png')
plt.show()

img = imread('img/germany.png')

plt.imshow(img)
plt.show()
