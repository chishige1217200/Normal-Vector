import numpy as np


def normal_vector(a, b):
    return [a[1]*b[2]-b[1]*a[2], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]  # 法線ベクトル計算


def vector_square_norm(a):
    b = np.linalg.norm(a, ord=2)  # 2乗ノルム計算
    return [a[0]/b, a[1]/b, a[2]/b]  # 正規化


def vector(a, b):
    return [b[0]-a[0], b[1]-a[1], b[2]-a[2]]  # 2点からベクトルを計算


# main
print("Input a. (Ex:\"0,1,0\")")  # 3点の3次元座標を入力
a = list(map(float, input().split(",")))  # ,で分割
print("Input b. (Ex:\"-1,-0.8,1\")")
b = list(map(float, input().split(",")))
print("Input c. (Ex:\"1,-0.8,1\")")
c = list(map(float, input().split(",")))
d = normal_vector(vector(a, b), vector(b, c))

print(d)
print(vector_square_norm(d))
