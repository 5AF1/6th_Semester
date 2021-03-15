#%%
import numpy as np
import math

#%%
X = [[1, 1, 1, 1, 1], [1, 1, 1, 2, 1], []]
#%%
def e(b):
    n = sum(b)
    ans = 0
    for i in b:
        ans += i * math.log(i)

    ans -= n * math.log(n)

    return ans / (-n * math.log(2))


def ent(a, b):
    n = sum(a)
    ans = 0
    for i in range(len(a)):
        ans += a[i] * e(b[i]) / n

    return ans


def tree(B):
    for i in B:
        V = [sum(j) for j in i]
        a = ent(V, i)
        print(a)


#%%
a = [5, 4, 5]
b = [[3, 2], [4], [2, 3]]

print(ent(a, b))

# %%
A = [[5, 4, 5], [4, 6, 4], [7, 7], [8, 6]]

B = [
    [[3, 2], [4], [2, 3]],
    [[2, 2], [4, 2], [3, 1]],
    [[3, 4], [6, 1]],
    [[6, 2], [3, 3]],
]
#%%
tree(B)
# %%
