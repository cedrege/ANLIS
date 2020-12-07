import matplotlib.pyplot as plt
import numpy as np

seg = 128

a=1
c=3
b=5

t = np.linspace(-1, b,seg)

# 4 x³ - 21 x² + 18 x + 12 
def f(x: float) -> float:
    return 4*x**3 - 21*x**2 + 18*x + 12

def f_s(x: float) -> float:
    return round(12*x**2 - 42*x + 18, 2)

def f_ss(x: float) -> float:
    return 24*x - 42

#plt.axis("equal")
plt.title("Zerlegung des Integrationsintervalls")
plt.grid("both")
plt.plot(t, f(t))
plt.plot(a, f(a), "ro")
plt.text(a, f(a)+ 5, f"a({a}, {f(a):.02f})",horizontalalignment="left", verticalalignment="center")
plt.plot(b, f(b), "ro")
plt.text(b - 0.2, f(b), f"b({b}, {f(b):.02f})",horizontalalignment="right", verticalalignment="center")
plt.plot(c, f(c), "ro")
plt.text(c, f(c) -5, f"c({c}, {f(c):.02f})",horizontalalignment="left", verticalalignment="center")

# Generate filling ranges:
alli = [(i, f(i)) for i in t]
a_f = [(a, f(a))]+[(k,v) for k,v in alli if k >=a and (v>=0 and k<c)]
c_f = [(k,v) for k,v in alli if k >=a and (v<=0 and k<b)]
b_f = [(k,v) for k,v in alli if k >=c and v>=0]

plt.fill_between([i[0] for i in a_f], [i[1] for i in a_f], 0, color="red", alpha=0.2)
plt.fill_between([i[0] for i in c_f], [i[1] for i in c_f], 0, color="blue", alpha=0.2)
plt.fill_between([i[0] for i in b_f], [i[1] for i in b_f], 0, color="green", alpha=0.2)

plt.savefig(fname="C:\\Users\\ced\\OneDrive - Hochschule Luzern\\Semester 1\\mathe\\Analysis\\zu\\pic\\fig_4.2.0.svg", format="svg")
#plt.show()