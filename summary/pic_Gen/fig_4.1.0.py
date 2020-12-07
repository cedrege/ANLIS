import matplotlib.pyplot as plt
import numpy as np

seg = 129

def f(x):
    return x*x

a = np.linspace(-2, 2, seg)

plt.grid('both')

for r in range(-2,3):
    plt.plot(a, f(a) + r)
    plt.text(0, r + 0.5,f"f(x) + ({r})", verticalalignment='center', horizontalalignment='center')

plt.savefig(fname="C:\\Users\\ced\\OneDrive - Hochschule Luzern\\Semester 1\\mathe\\Analysis\\zu\\pic\\fig_4.1.0.svg", format="svg")