import numpy as np


def hosen(a, b):
    return [a[1]*b[2]-b[1]*a[2], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]  # 法線ベクトル計算


def hosen_norm(a):
    b = np.linalg.norm(a, ord=2)  # 2乗ノルム計算
    return [a[0]/b, a[1]/b, a[2]/b]  # 正規化


# main
print("Input a. (Ex:\"0,1,0\")")
a = list(map(float, input().split(",")))
print("Input b. (Ex:\"-1,-0.8,1\")")
b = list(map(float, input().split(",")))
print("Input c. (Ex:\"1,-0.8,1\")")
c = list(map(float, input().split(",")))
d = hosen([b[0]-a[0],b[1]-a[1],b[2]-a[2]], [c[0]-b[0],c[1]-b[1],c[2]-b[2]])

print(d)
print(hosen_norm(d))
