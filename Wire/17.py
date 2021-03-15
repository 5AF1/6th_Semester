#%%
import numpy as np

#%%
e = [0.7, 0.9, 0.9, 0.9, 0.8]
h = [0.2, 0.2, 0.2, 0.2, 0.1]
t = len(e) * [0.1]

p = [[1, 2], [3, 4], [5]]

#%%
e = np.array(e)
h = np.array(h)
t = np.array(t)

off = np.maximum((e + h) - 1, np.zeros(e.shape))
on = np.maximum((e + h - t) - 1, np.zeros(e.shape))

print(np.array([e, h, t, off, on]))

# %%
for l in p:
    c = 0
    for i in range(len(e)):
        if i + 1 in l:
            c += t[i]
            c += on[i]
        else:
            c += off[i]
    print(c)

# %%
