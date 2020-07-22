# 편미분
# 변수가 2개이다

from Neural_Network_Learning.Derivative import numerical_diff


def function_2(x):
    return x[0] ** 2 + x[1] ** 2


def function_tmp1(x0):
    return x0 * x0 + 4.0 ** 2.0


def function_tmp2(x1):
    return 3.0 ** 2.0 + x1 * x1


print(numerical_diff(function_tmp1, 3.0))
print(numerical_diff(function_tmp2, 4.0))
