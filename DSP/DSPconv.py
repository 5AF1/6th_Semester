# %%
from scipy import signal
import sympy as sp
import numpy as np

# %%
X = [1, -2, 3, 4]
H = [1, 2, 3]

Y = signal.convolve(X, H)
print("conv", Y)
X = [11, 8, 3, 7, 5, 100, 13, 74, 19]
H = [8, 3, 7]
Y = signal.correlate(X, H)
print("cor", Y)
Xx, rem = signal.deconvolve(Y, H)
print("deconv", Xx)
#%%
def matest(a):
    if type(a) == list:
        return np.array([a])
    else:
        return a


def my_conv(X, H):
    X = matest(X)
    H = matest(H)

    N = X.shape[1]
    M = H.shape[1]

    X = np.flip(X)
    X = X.T
    H = np.append(np.zeros((1, N - 1)), H)
    H = np.append(H, np.zeros((1, N - 1)))

    Stack = np.zeros((M + N - 1, N))

    for i in range(M + N - 1):
        Stack[i, :] = H[i : i + N]

    return (Stack @ X).T


def my_deconv(Y, H):
    Y = matest(Y)
    H = matest(H)

    O = Y.shape[1]
    M = H.shape[1]
    N = O - M + 1

    Y = Y.T
    H = np.append(np.zeros((1, N - 1)), H)
    H = np.append(H, np.zeros((1, N - 1)))
    Stack = np.zeros((N, N))

    for i in range(N):
        Stack[i, :] = H[i : i + N]

    Stack = np.append(Stack, Y[0:N], axis=1)

    M = sp.Matrix(Stack)
    M, _ = M.rref()
    M = np.array(M[:, -1])
    M = np.flip(M).T
    return M

def spec_inv(X):
    X = matest(X)
    X = -X
    N = X.shape[1]
    X[:,(N-1)//2] = X[:,(N-1)//2]+1
    return X

def spec_rev(X):
    X = matest(X)
    N = X.shape[1]
    X[:,1:N:2] = -X[:,1:N:2]
    return X
    

#%%
H = [1, 2, 4, 8]
Y = [1, 0, 4, 12, 6, 45, 26, -12, 8]
Y = np.array([Y])
H = np.array([H])
# Y =
my_deconv(Y, H)

# %%
X = [1, -2, 3, 4]
H = [1, 2, 3]

X = np.array([X])
H = np.array([H])

H = [1, 2, 4, 8]
Y = [1, 0, 4, 12, 6, 45, 26, -12, 8]
Y = np.array([Y])
H = np.array([H])
print(Y)
# Y =
my_deconv(Y, H)

# %%
X = [1, 2, 2, 3, 4, -2]
H = [-1, 0, -1]

Y = signal.convolve(X, H)
print("conv", Y)
# X = [11,8,3,7,5,100,13,74,19]
# H = [8,3,7]
# Y = signal.correlate(X,H)
# print('cor', Y)
# Xx, rem = signal.deconvolve(Y, H)
# print('deconv', Xx)
# %%
X1 = [1, 2, 3, 2, 1]
X2 = spec_rev(X1)
X3 = my_conv(X1,X2)
X4 = spec_inv(X3)

X = [1, 3, 4, -5, 2, -6 ]
print(spec_inv(X))
print(spec_rev(X))
#y = my_conv(X1, X2)
print(X2,X3,X4)
# %%
X = [1, -2, 3, 4]
H = [1, 2, 3]
Y = my_conv(X, H)
print(Y)

# %%
x=my_deconv(Y, H)
print(x)
# %%
