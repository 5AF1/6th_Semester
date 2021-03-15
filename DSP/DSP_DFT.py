#%%
import numpy as np
import math
from scipy.io.wavfile import read

#%%
def matest(a):
    if type(a) == list:
        return np.array([a]).T
    else:
        return a


def synthesis(R, I):
    R = matest(R)
    I = matest(I)
    N = (R.shape[0] - 1) * 2

    R = R / (N / 2)
    I = I / (N / 2)

    R[0, 0] = R[0, 0] / 2
    R[N // 2, 0] = R[N // 2, 0] / 2
    print(R)
    print(I)
    k = np.array([np.arange(N / 2 + 1)])
    i = np.array([np.arange(N)])

    ik = i.T @ k
    print(ik)
    ik = (2 * math.pi / N) * ik
    print(ik)
    cs = np.cos(ik)
    sn = -np.sin(ik)
    print(cs)
    print(sn)
    R = cs @ R
    I = sn @ I
    print(R)
    print(I)
    X = R + I

    return X


def analysis(X):
    X = matest(X)
    N = X.shape[0]

    k = np.array([np.arange(N / 2 + 1)])
    i = np.array([np.arange(N)])

    ki = k.T @ i
    print(ki)
    ki = (2 * math.pi / N) * ki
    print(ki)

    cs = np.cos(ki)
    sn = -np.sin(ki)
    print(cs)
    print(sn)

    R = cs @ X
    I = sn @ X

    return (R, I)


def polar(R, I):
    #
    R = matest(R)
    I = matest(I)

    M = np.sqrt(R * R + I * I)
    P = np.arctan2(I, R)

    return (M, P)


def polar_pt(R, I):
    R = matest(R)
    I = matest(I)
    Z = R + 1j * I
    return Z


#%%
R = [12, 1.293, -3, 2.707, -6]
I = [0, -0.293, -1, 1.707, 0]
X = [9, 3, 3, 9]
#%%
M, P = polar(R, I)
print(P[2] * 180 / math.pi)
#%%
R, I = analysis(X)
M, P = polar(R, I)
print(M[1])

#%%
X = np.array([[5, -1, 1, -2]]).T
R, I = analysis(X)
print(R, I)
#%%
R = np.array([[5, -4, 7]]).T
I = np.array([[0, 5, 0]]).T

X = synthesis(R, I)
print(X)

#%%
X = np.array([[11, -8, 9, 3]]).T
R, I = analysis(X)
print(I[1])
#%%
X = np.ones((256, 1))
print(X)
#%%
R = np.array([[12, 1.293, -3, 2.707, -6]]).T
I = np.array([[0, -0.293, -1, 1.707, 0]]).T
M, P = polar(R, I)
print(P[2] * 180 / math.pi)
#%%
a = read(
    "D:/Microsoft/OneDrive/OneDrive - iut-dhaka.edu/6thSem/DSP LAB/lab5/underwater.wav"
)
X = np.array([a[1][0:450]], dtype=float).T
R, I = analysis(X)
print(R)
#%%
X=[2,3,2,-5,0,-8,9,-4]
r,i=analysis(X)
print("...",r,i)
# %%
