#%%
from prettytable import PrettyTable
import numpy as np

np.set_printoptions(suppress=True)
#%%
n = 6
fix = [0, 0, 10000, 800, 2200, 600]
var = [18, 6.25, 0, 0.2, 0, 0.8]
actual = [35000, 11110, 10130, 1080, 2200, 2240]

# %%
def bud(q, fix, var):
    f = np.array([fix]).T
    v = np.array([var]).T
    fv = np.hstack((f, v))
    Q = np.array([[1, q]]).T
    l = list((fv @ Q).T[0])
    tab = PrettyTable()
    tab.field_names = ["q", q]
    tab.align["q"] = "l"
    tab.add_row([f"Revenue (${var[0]}q)", f"${l[0]}"])
    tab.add_row(["", "-----"])
    tab.add_row(["Expenses", ""])
    t = 0
    for i in range(1, len(fix)):
        t += l[i]
        tab.add_row([f"     (${fix[i]} + ${var[i]}q)", l[i]])

    tab.add_row(["", "-----"])
    tab.add_row(["Total Expenses", t])
    tab.add_row(["", "-----"])
    tab.add_row(["Net operating income", f"${l[0]-t}"])
    tab.add_row(["", "====="])

    return tab, l


#%%
t, _ = bud(1900, fix, var)
print(t)
# %%
def report(pq, fq, fix, var, acc):
    _, plan = bud(pq, fix, var)
    _, flex = bud(fq, fix, var)
    tab = PrettyTable()
    tab.field_names = ["", "Plan", "ActVar", "Flex", "Rev&SpendVar", "Actual"]
    tab.align[""] = "l"

    tab.add_row(["q", pq, "", fq, "", fq])

    av = flex[0] - plan[0]
    if av < 0:
        av = str(-av) + " U"
    elif av > 0:
        av = str(av) + " F"

    rsv = acc[0] - flex[0]
    if rsv < 0:
        rsv = str(-rsv) + " U"
    elif rsv > 0:
        rsv = str(rsv) + " F"
    tab.add_row([f"Revenue (${var[0]}q)", f"${plan[0]}", av, flex[0], rsv, acc[0]])
    tab.add_row(["", "-----", "-----", "-----", "-----", "-----"])
    tab.add_row(["Expenses", "", "", "", "", ""])
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    for i in range(1, len(fix)):
        c1 += plan[i]
        c3 += flex[i]
        c5 += acc[i]

        c2 += plan[i] - flex[i]
        c4 += flex[i] - acc[i]

        av = plan[i] - flex[i]
        if av < 0:
            av = str(-1 * av) + " U"
        elif av > 0:
            av = str(av) + " F"

        rsv = flex[i] - acc[i]
        if rsv < 0:
            rsv = str(-1 * rsv) + " U"
        elif rsv > 0:
            rsv = str(rsv) + " F"

        tab.add_row(
            [f"     (${fix[i]} + ${var[i]}q)", plan[i], av, flex[i], rsv, acc[i]]
        )

    tab.add_row(["", "-----", "-----", "-----", "-----", "-----"])
    av = c2
    if av < 0:
        av = str(-1 * av) + " U"
    elif av > 0:
        av = str(av) + " F"

    rsv = c4
    if rsv < 0:
        rsv = str(-1 * rsv) + " U"
    elif rsv > 0:
        rsv = str(rsv) + " F"
    tab.add_row(["Total Expenses", c1, av, c3, rsv, c5])
    tab.add_row(["", "-----", "-----", "-----", "-----", "-----"])
    av = flex[0] - plan[0] + c2
    if av < 0:
        av = str(-1 * av) + " U"
    elif av > 0:
        av = str(av) + " F"

    rsv = acc[0] - flex[0] + c4
    if rsv < 0:
        rsv = str(-1 * rsv) + " U"
    elif rsv > 0:
        rsv = str(rsv) + " F"

    tab.add_row(
        ["Net operating income", f"${plan[0]-c1}", av, flex[0] - c3, rsv, acc[0] - c5]
    )
    tab.add_row(["", "=====", "=====", "=====", "=====", "====="])

    print(tab)


# %%
report(2000, 1900, fix, var, actual)
# %%
