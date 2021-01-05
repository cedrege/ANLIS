# Mathe Zusammenfassung

## Grundlagen
### Algebra
TODO:

### Sympy Solve()
```python
import sympy as sp
x = sp.symbols("x")
expr = -1/3 * x ** 2 + 13/3 * x + 16
sp.solve(expr)
```

#### Brüche
$\frac{1}{x^2}\frac{1}{x^3}=\frac{1}{x^5}$\
$\frac{1}{cos(x)^2}tan(x)=\frac{1}{cos(x)^2}\frac{sin(x)}{cos(x)}=\frac{sin(x)}{cos(x)^3}$


## Funktionen
### Lineare Funktionen
Die Formel für eine Lineare Funktion ist folgende:\
$y = mx + b$

### Polynome
TODO:

## Folgen, Reihen
TODO:


### Summenformeln
Alle drei Beispiele anhand von $n$, $n^2$, $n^3$ 1-100:
#### Normal
Summe von 1 bis 100:\
$S=\sum\limits_{k=1}^n\frac{n}{2}(n+1)$

#### Quadratisch
Summe von $1^2$ bis $100^2$:\
$S=\sum\limits_{k=1}^n\frac{n}{6}(n+1)(2n+1)$

#### Kubisch
Summe von $1^3$ bis $100^3$:\
$S=\sum\limits_{k=1}^n\frac{n^2(n+1)^2}{4}$


## Grenzwerte, Stetigkeit
TODO:

## Differentialrechnung

### Tangentengleichung
TODO: wo gehört dies hin?\
$y-y_0=m(x-x_0)$

### Ableitungen
#### Produktregel
$u' * v + v' * u$\
Beispiel: $[x^2 * x^{10}]'=2*x^{10}+x^2*10x^9$
#### Differenzregel
TODO:

#### Kettenregel
TODO:

####  Logarithmische Differentiation
TODO: https://www.youtube.com/watch?v=_AlvbhIrnWQ

#### Ableitung Exponentialfunktion
|f(x)|f'(x)|  \|  |f(x)|f'(x)|
|--|-:|--|--|-:|
|$e^x$|$e^x$|  \|  |$e^{x^2}$|$2x*e^{x^2}$|
|$2e^x$|$2e^x$|  \|  |$20*e^{x^3}$|$60x^2*e^{x^3}$|
|$10+3e^x$|$3e^x$|  \|  |$2x+e^{-4x^3}$|$2+(-12x^2)*e^{-4x^3}$|
|$e^{2x}$|$2e^{2x}$|  \|  |$2x*e^{-3x^3}$|$2*e^{-3x^3}+2x*-9x^2*e^{-3x^3}$|

### Implizite Ableitung
TODO:

### Kurvendiskussion
Folgende Punkte sollen bei der Kurvendiskusion untersucht werden:
* **Definitions- und Wertebereich, Definitionslücken, Unstetigkeitsstellen**
* **Symmetrien:** ist $f$ gerade $(f(x) = f(-x))$, ungerade $(f(x) = -f(-x))$ oder $T$-periodisch $(f(x + T) = f(x))$.
* **Nullstellen** $(f(x) = 0)$; **Schnittpunkt mit y-Achse** $(f(0) = y)$.
* **Pole** (Nenner verschwindet!), **senkrechte Asymptoten** (Polgeraden).
* **Ableitungen** (in der Regel bis zur 3. Ordnung)
* **Relative Extremwerte** (Maxima und Minima): Notwendige Bedingung $fx'(x) = 0$! Überprüfen mit der 2. Ableitung.
* **Monotonieeigenschaften, Wendepunkte, Krümmung, etc.**
* **Asymptotisches Verhalten** für $x \rightarrow \pm \infty$.
* **Krümmungskreismittelpunkt** (optional: **Evolute** und **Evolvente**, etc.)
* Graph $G(f)$ der Funktion $f$ skizzieren

TODO: von jedem genannten Punkt min ein Bsp in der Zusammenfassung haben...

#### Nullstellen
TODO: https://www.youtube.com/watch?v=gaa9qiREPaE

## Integralrechnung
Im allgemeinen ist die Integralrechnung die Umkehrung der Differentialrechnung.\
Mittels Integralen kann zum einen eine Fläche eines beliebigen Objektes berechnet werden und zum anderen die Bogenlänge. (ähnlich zum Umfang des Objektes)\
![Integralrechnung](./pic/fig_4.5.0.png "fig 4.5.0")

### Integrationstabelle
Eine weitaus umfangreichere Liste kann auf https://en.wikipedia.org/wiki/Lists_of_integrals gefunden werden.\
Zudem ist folgender Integralrechner empfehlenswert: https://www.integral-calculator.com \
![Integrationstabelle](./pic/fig_4.4.0.png "fig 4.4.0")

### Integral als Summe (Riemannsche Summe)
Die Fläche eines Integrals kann mittels der Riemannschen Summe gebildet werden. Dafür wird die Fläche in $n$ Intervalle aufgeteilt und zwischen der Untergrenze $a$ und der Obergrenze $b$ zusammengezählt.\
**Untersumme**\
Die Untersumme ist die Summer aller Rechtecke, welche den zu integrierenden Bogen nicht überschreiten (Die linke, obere Seite berührt den Bogen).\
![Untersumme](./pic/fig_4.6.0.png "fig 4.6.0")

**Obersumme**\
Die Obersumme ist die Summer aller Rechtecke, welche den zu integrierenden Bogen überschreiten (Die rechte, obere Seite berührt den Bogen).\
![Obersumme](./pic/fig_4.7.0.png "fig 4.7.0")

Beispiel:\
In diesem Beispiel wird aufgezeigt, wie das Integral $\int\limits_{0}^{1}x^2$ als Summe dargestellt werden kann.\
Unterteilung des Intevalls $[a,b] = [0,1]$ (Unter, Obergrenze) in $n$ gleich grosse Teilintervalle.
$$\Delta x=\frac{b-a}{n}=\frac{1-0}{n}=\frac{1}{n}$$
Dies führt zur folgenden $x$-Koordinate für den $k$. Zwischenpunkt. (Wobei $x_0 = a = 0$ und $x_n = b = 1$)
$$x_k=a+k\Delta x = 0+k\frac{1}{n}=\frac{k}{n}$$
Der Funktionswert von $f$ an der Stelle $x_k^\star = x_k$ (rechter Rand) ist
$$f(x_k^\star)=f(x_k)=x_k^2=(\frac{k}{n})^2$$
Somit erhalten wir für die Summer der Rechteckflächen
$$\sum\limits_{k=1}^nf(x_k^\star)\Delta x=\sum\limits_{k=1}^n(\frac{k}{n})^2\frac{1}{n}=\frac{1}{n^3}\sum\limits_{k=1}^nk^2$$
Schliesslich erhalten wir durch das bilden des Grenzwertes für $n$ gegen unendlich die gesuchte Fläche
$$
\begin{aligned}
A=\displaystyle{\lim_{n \to \infty}} \sum\limits_{k=1}^n f(x_k^\star)\Delta x = \displaystyle{\lim_{n \to \infty}} \frac{1}{6}(1+\frac{1}{n})(2+\frac{1}{n}) \\
=\frac{1}{6} \displaystyle{\lim_{n \to \infty}}(1+\frac{1}{n}) \displaystyle{\lim_{n \to \infty}}(2+\frac{1}{n}) \\
=\frac{1}{6} * 1 * 2 = \frac{1}{3}
\end{aligned}
$$

**Python**
```python
# Numerical calculations based on the Riemann-Integral 
import numpy as np

#Define function -> here x^2
def f(x):
    return x*x
# Riemannsche untersumme
# func = funcpointer
# a = lower border
# b = upper border
# n = amount of intevalls
def Riemann_us(func, a, b, n):
    sum = 0
    dx = (b-a) / n
    for i in range(1, n+1):
        xk = a + (i-1)  * dx
        sum += func(xk) * dx
    return sum
    
# Riemannsche untersumme
# func = funcpointer
# a = lower border
# b = upper border
# n = amount of intevalls
def Riemann_os(func, a, b, n):
    sum = 0
    dx = (b-a) / n
    for i in range(1, n+1):
        xk = a + i * dx
        sum += func(xk) * dx
    return sum

## RUN IT:
## One Step:
# a = 1
# b = 2
# n = 5
# print(f"N-Value: {n} Riemann-Untersumme: {Riemann_us(f,a,b,n):0.5f} Riemann-Obersumme: {Riemann_os(f,a,b,n):0.5f}")

## Multiple Steps based on 2^(1 to 10)
# m = 10
# for k in range(1, m+1):
#    n = np.power(2, k)
#    print(f"N-Value: {n} Riemann-Untersumme: {Riemann_us(f,a,b,n):0.5f} Riemann-Obersumme: {Riemann_os(f,a,b,n):0.5f}")
```

```python
# Sympy has a built in function, which renders an Integral as Sum
import numpy as np
import sympy as sp
sp.init_printing(use_latex='mathjax')
x = sp.symbols("x")
display(sp.Integral(x**2, (x, 0, 1)).as_sum(100, method='midpoint').n(4))
display(sp.Integral(x**2, (x, 0, 1)).as_sum(method='midpoint', evaluate=False))
#https://docs.sympy.org/latest/modules/integrals/integrals.html#sympy.integrals.integrals.Integral.as_sum
```

### Unbestimmtes Integral
Ein unbestimmtes Integral ist ein Integral, welches keine Grenzen hat.

Funktion = Stammfunktion = $F(x)$\
Abgeleitete Funktion = $F'(x) = f(x)$\
Parabelschar = Verallgemeinerung der möglichen Stammfunktionen: $y=x^2+C\ \ \ \ (C\in\R)$\
Da beim integrieren nicht gesagt werden kann welche oder überhaupt konstante Zahlen bei der `Stammfunktion` $F(x)$ dabei war gibt es mehrere Möglichkeiten, wie die Funktion ausgesehen haben könnte.

Bsp: $f(x)_0=x^2+2$ ist eine `Stammfunktion` von $2x$\
Weitere Funktionen im Bild fig_4.1.0.svg dargtestellt:\
![Stammfunktionen_beispiel](./pic/fig_4.1.0.svg "fig 4.1.0")

Man sieht also, dass die Umkehrung einer `Differenzierung` mehrere Lösung haben kann. Darum ist das `Unbestimmte Integral` von $F(x)$ die Menge ALLER Stammfunktionen (`Parabelschar`) von $f(x)$.

#### Erste Substitutionsregel bei unbestimmten Integralen
Theorem: Es gilt: $\int f(g(x))g'(x)dx=[\int f(u)du]_{u=g(x)}$

Vorgehen:
1. Substituiere formal $g(x) = u, g'(x) dx = du$
2. Integriere unbestimmt nach $u$
3. Ersetze $u$ wieder durch $g(x)$

Die erste Substitutionsregel kommt immer dann zum Einsatz, wenn klar ersichtlich ist, dass ein Teil des Ausdrucks die Ableitung des anderen Teiles ist. Man sieht diesem Integranden an, dass er durch die Kettenregel entstanden ist. Die Idee ist, dass $\frac{dx}{du} = u'$ dann so gewählt werden kann, dass der zweite Teil des Audrucks damit gestrichen werden kann.

Beispiel:

$\int \frac{2x+6}{x^2+6x-12}dx \rArr \int \frac{2x+6}{u}\frac{du}{dx} \rArr \int\frac{2x+6}{u}\frac{du}{2x+6} \rArr \int\frac{1}{u}du$

Dies wurde mit der Substitution von $u=x^2+6x-12$ bewerkstelligt.\
> Substitutions-Box\
> $u = x^2+6x-12$\
> $u' = 2x+6$\
> $\frac{du}{dx} = 2x+6 \rArr \frac{du}{2x+6} = dx$

#### Zweite Substitutionsregel bei unbestimmten Integralen
Theorem: Es gilt: $\int f(x)dx = \begin{bmatrix} \int f(\phi (u)) \phi'(u) du\end{bmatrix}$

Vorgehen:
1. Wähle eine geeignete invertierbare Substitutionsfunktion $\phi$
2. Substituiere formal $x = \phi(u), dx = \phi'(u) du$
3. Integriere unbestimmt nach $u$
4. Drücke $u$ wieder durch $x$ aus

Die zweite Substitutionsregel ist flexibler und auf alle Integrale anwendbar. Die Idee ist, ein Teil des Integrals zu substituieren, damit die aus der Substitution resultierende Ableitung den Integranden einfacher zu intergrieren macht. Andere, noch im Integral vorhandene Variabeln, müssen entsprechend umgerechnet werden. Dies ist im Normalfall nicht immer sofort ersichtlich. Heisst, die Try and Error Taktik kommt zum Einsatz. Die Substitution *muss* im $u$-Intervall umkehrbar sein und somit durch $u=\phi^{-1}(x)$ ausdruckbar sein.\
Für die Prüfung ist folgender Integralrechner zu empfehlen: https://www.integral-calculator.com. 

Beispiel:

$\int x^2\sqrt{x-1}dx \rArr \int(u^2+2u+1)\sqrt(t)du =$\
$\int(u^2+2u+1)t^{1/2}du = \int(u^{5/2}+2u^{3/2}+t^{1/2})du$

> Substitutions-Box\
> $u = x - 1$\
> $u' = 1$\
> $\frac{du}{dx}=1\rArr dx = du$\
> $x = u + 1$\
> $x^2\rArr(u+1)^2= u^2+1u+1u+1= u^2+2u+1$

### Bestimmtes Integral
Ein bestimmtes Integral ist ein Integral, welches Grenzen hat.

$A=\int\limits_{a}^b x^2dx= F(b) - F(a)$\
Beispiel an $f(x)=x^2$
Um die Fläche unter dem Graphen von $f(1)$ bis $f(2)$ zu errechnen muss zuerste eine der möglichen `Stammfunktionen` ausgewählt werden. In dem Fall von $x^2$ wäre es $F(x) =\frac{1}{3}x^3$, da $3*\frac{1}{3}x^{3-1} = x^2$.\
Wenn diese Funktion herausgefunden ist und auch existiert, kann die Berrechnung durchgeführt werden: $A=\int\limits_{1}^2x^2dx=F(2)-F(1)=\frac{1}{3}2^3-\frac{1}{3}1^3=\frac{8}{3}-\frac{1}{3}=\frac{7}{3}$\
Bei der Funktion $e^{-2x}$ geht dies zum Beispiel nicht, da diese keine `Stammfunktion` hat.

#### Erste Substitutionsregel bei bestimmten Integralen
Theorem: Es gilt: $\int\limits_{a}^bf(g(x))g'(x)dx = \int\limits_{g(a)}^{g(b)}f(u)du=[F(u)]_{g(a)}^{g(b)}=F(g(b))-F(g(a))$

Vorgehen:
1. Substituiere formal $g(x) = u, g0(x) dx = du$
2. Ersetze die $x$-Grenzen $a, b$ durch die u-Grenzen $g(a), g(b)$
3. Integriere

Das Integrieren bei `bestimmten Integralen` funktioniert identisch wie bei den `unbestimmten Integralen`. Einzig müssen die Grenzen von $x$ (Integralgrenzen) gemäss der Substitution angepasst werden. Dies geschieht indem die Grenzen durch den substituierten Teil (als Funktion angesehen) geschickt werden.

Beispiel:

Angenommen von einem Integral mit den Grenzen $1,2$ wurde $x^2$ substituiert,\
$\int\limits_{1}^2f(x) \rightarrow \int\limits_{1}^4f(u)$\
so müssen die Grenzen $1,2$ jeweils $1^2$ respektive $2^2$ gerechnet werden. Somit erhällt das Integral neu die Grenzen $1,4$.

<img src="./pic/fig_4.3.0.png" alt="fig 4.3.0" width="600"/>

#### Zweite Substitutionsregel bei bestimmten Integralen
Theorem: Es gilt: $\int\limits_{a}^bf(x)dx=\int\limits_{\phi^{-1}(a)}^{\phi^{-1}(b)}f(\phi(u))\phi'(u)du$

Vorgehen:
1. Wähle eine geeignete invertierbare Substitutionsfunktion $\phi$
2. Substituiere formal $x = \phi(u), dx = \phi'(u) du$
3. Ersetze die $x$-Grenzen $a, b$ durch die $u$-Grenzen $\phi^{-1}(a), \phi^{-1}(b)$
4. Integriere

Das Integrieren funktioniert gleich wie bei der zweiten Substitutionsregel für `unbestmmte Integrale`. Einzig müssen am Schluss die Integrationsgrenzen angepasst werden. Das Anpassen der Grenzen ist gleich wie bei der ersten Substitutionsregel für `bestimmte Integrale`.

### Bemerkungen zur Integralsubstitution

<img src="./pic/fig_4.8.1.png" alt="fig 4.8.1" width="600"/>
<img src="./pic/fig_4.8.2.png" alt="fig 4.8.2" width="600"/>

### Rechenregel für Integrale
**Umkehrung**\
Wenn von einer grösseren Zahl zu einer kleineren integriert werden muss, können die Integrationswerte vertauscht werden. Es muss jedoch auch das Vorzeichen des Integrals gewechselt werden.\
Beispiel:\
$\int\limits_{a}^bF(x)dx$ kann auch so ausgerechnet werden: $-\int\limits_{b}^aF(x)dx,\ \ (a=5, b=0)$

**Faktor- und Summenregel**\
Sind $f$ und $g$ über $[a, b]$ integrierbar und $c \in \Reals$ eine Konstante, dann sind auch $cf$ und $f + g$ über $[a, b]$ integrierbar und es gilt:
* Konstante Faktoren können vor das Integral genommen werden.\
$\int\limits_{a}^bcf(x)dx=c\int\limits_{a}^bf(x)dx$
* Linearkombinationen können einzeln berechnet und dann summiert werden.\
$\int\limits_{a}^b(f(x)\plusmn g(x))dx=\int\limits_{a}^bf(x)dx \plusmn \int\limits_{a}^bg(x)dx$

**Zerlegung des Integrationsintervalls**\
Ist $f$ über einem geschlossenen Intervall, welches die Punkte $a, b, c$ enthält integrierbar, dann gilt:\
$\int\limits_{a}^bf(x)dx=\int\limits_{a}^cf(x)dx+\int\limits_{c}^bf(x)dx$\
![Stammfunktionen_beispiel](./pic/fig_4.2.0.svg "fig 4.2.0")

### Partielle Integration
_Partielle Integration_ kann bei `bestimmten` wie auch bei `unbestimmten Integralen` gleich angewandt werden. **Einzig muss bei `bestimmten Integralen` an die Grenzen gedacht werden**. Diese müssen jedoch nicht umgeschrieben werden während dem partiellen Integrieren. Ziel ist es, dass das Integral auf der rechten (RHS) Seite eingacher wird.

Theorem: Es gilt: $\int {\underset{\uparrow}{u'(x)}} * {\underset{\downarrow}{v(x)}} dx=u(x) * (v)- \int u(x) * v'(x) dx$

**Bemerkung**: Der nach oben gerichtete Pfeil ($\uparrow$) unter einer Funktion deutet an, dass diese Funktion auf der RHS überall in integrierter Form vorkommt. Der nach unten gerichteten Pfeil ($\downarrow$) deuetet an, dass diese
Funktion auf der RHS nur unter dem Integral in abgeleiteter Form vorkommt.

Vorgehen:
1. Zerlege den Integranden in eine Produkt von zwei Faktoren
2. Ein Faktor ist $u'(x)$, der andere ist $v(x)$
3. Der erste Faktor $u'(x)$ kommt auf der RHS überall in integrierter Form, d.h. als $u(x)$ vor
4. Der zweite Faktor $v(x)$ kommt auf der RHS nur unter dem Integral in abgeleiteter Form, d.h. als $v'(x)$ vor

Es ist egal welcher der beiden Terme abgeleitet wird. Einzig bei $ln$ sollte drauf geachtet werden, dass der mit Prio abgeleitet wird.

Beispiel:

$\int \color{lightblue}{\underset{\downarrow}{x}} * \color{orange}{\underset{\uparrow}{cos(x)}} \color{normal}dx = \color{lightblue}x *  \color{orange}sin(x)  \color{normal}- \int \color{lightblue}1 *  \color{orange}sin(x)  \color{normal}dx \rArr x * sin(x) + cos(x) + C$\
In diesem Beispiel ist es $+ cos(x)$, da $sin(x)$ aufgeleitet $-cos(x)$ ergeben und somit $- (-cos(x))$ gerechnet wird.

### Mittelwert eines Integrals
**Linearer Mittelwert**\
Der lineare Mittelwert $\overline{y}_{linear}$ der Funktion $y = f(x)$ über dem Intervall $[a, b]$ gibt an, welchen Wert diese Funktion im Mittel hat.\
$\overline{y}_{linear} = \frac{1}{b-a}\int\limits_{a}^bf(x)dx$, wobei $a$ die untere und $b$ die obere Genze des Integrals sind.

**Quadratischer Mittelwert**\
Der quadratische Mittelwert von $y = f(x)$ über dem Intervall $[a, b]$ ist definiert durch:
$\overline{y}_{quadratisch} = \sqrt{\frac{1}{b-a}\int\limits_{a}^b[f(x)]^2dx}$

```python
import numpy as np
import sympy as sp
sp.init_printing(use_latex='mathjax')
x = sp.symbols("x")

# calculate the quadratic average of a given integral within a fixed border
# TODO: Not yet fully working. need more examples to test it
def mw_q(func, border):
    normalization = 1 / (border[2] - border[1])
    integral = sp.Integral(sp.Abs(func) ** 2, border)
    print("Integral")
    display(integral)
    integral_calculated = sp.sqrt(normalization * integral.doit())
    print("Result of integrated integral")
    display(integral_calculated)
    print("Numerical evaluation of Integral")
    display(sp.N(integral_calculated))

# calculate the linear average of a given integral within a fixed border
def mw_lin(func, border):
    normalization = 1 / (border[2] - border[1])
    integral = sp.Integral(func, border)
    print("Integral")
    display(integral)
    integral_calculated = normalization * integral.doit()
    print("Result of integrated integral")
    display(integral_calculated)
    print("Numerical evaluation of Integral")
    display(sp.N(integral_calculated))

# RUN IT
#mw_lin(sp.ln(x), (x, 1, 5))
#mw_q(sp.sin(x), (x, 0, 2*sp.pi))
```
### Trapez-Reihen
TODO:

### Simpson-Reihen
TODO:

### Bogenlänge eines Integrals
Für die normale Bogenlänge kann folgende Formel genutzt werden:\
$L=\int\limits_{a}^{b}\sqrt{1+[f'(x)]^2}dx = \int\limits_{a}^{b}\sqrt{1+(\frac{dy}{dx})^2}dx$

Für Bogenlege im Poolarkoordinatensystem muss diese Formel genutzt werden:\
$L=\int\limits_{\alpha}^{\beta}\sqrt{(r(\phi))^2+(r'(\phi))^2}d\phi$

```python
import numpy as np
import sympy as sp
sp.init_printing(use_latex='mathjax')
x = sp.symbols("x")

def int_arc_length(function, range):
    integral = sp.Integral(sp.sqrt(1 + sp.diff(function) ** 2), range)
    print("Integral")
    display(integral)
    print("Trying to simplify integral (warning, could get messy)")
    display(integral.simplify())
    print("Solve the integral (output is sometimes numerical)")
    display(integral.simplify().doit())
    print("Numerical evaluation of Integral")
    display(sp.N(integral.simplify().doit()))

# RUN IT
#int_arc_length(5*sp.cosh(x/5), (x, -7.15, 7.15))
#int_arc_length(4.2*sp.ln(x**3), (x, 1, sp.E))
#int_arc_length(sp.sin(x), (x, 0, sp.pi))
```

TODO: PYTHON -> Bogenlänge Poolarkoordinaten

## Summen Indextransformation
Bei der Indextransformation ist es da Ziel, dass Potenzen nur noch als $x^m$ dastehen. Sieht man in der Summe also eine Potenz, wie z.B. $x^{(m-2)}$, so soll der Summenindex in diesem Fall um 2 reduziert werden. Dafür muss bei jedem vorkommendem $m$, $m+2$ geschrieben werden.

**Beispiele**

$\sum\limits_{n=1}^\infty \frac{(-1)^{n+1}}{3n}x^{n+2} \rArr \sum\limits_{n=3}^\infty \frac{(-1)^{n-1}}{3(n-2)}x^{n}$

$\sum\limits_{p=2}^\infty p(p-1)x^{p-2} \rArr \sum\limits_{p=0}^\infty (p+2)(p+1)x^{p}$

## Potenzreihe
Eine Potenzreihe in Potenzen von $(x - x_0)$ ist eine Reihe der Form
$$\sum\limits_{h=0}^\infty a_k(x - x_0)^k=a_0+a_1(x - x_0)+a_2(x - x_0)^2+a_3(x - x_0)^3+...$$

Hier sind $a_k$ ($k=0,1,2,...$) die **Koeffizienten**, $x_0$ der **Entwicklungspunkt** und $x$ die **Variable der Potenzreihe**.

### Konvergenz einer Potenzreihe (Konvergenzradius)
Für jede Potenzreihe gibt es ein $R \geqslant 0$, genannt **Konvergenzradius**, sodass die Potenzreihe konvergiert, falls $|x-x_0| < R$ oder divergiert, falls $|x-x_0| > R$. Wenn $|x-x_0| = R$ kann die Reihe entweder konvergieren wie auch divergieren.

Für das Ausrechnen von $R$ gibt es zwei Möglichkeiten. (Jedoch muss dafür ein Grenzwert existieren!). Übrigens, $a_k$ ist im Normalfall alles unter der Summe auser das, was von $x$ abhängig ist.\
Quotientenkriterium: $R=\displaystyle{\lim_{k \to \infty}}  \Bigl|\frac{a_k}{a_{k+1}}\Bigr|$

Wurzelkriterium: $R=\bigg( \displaystyle{\lim_{k \to \infty}} \sqrt[k]{|{a_k}|} \bigg)^{-1}$

TODO: PYTHON -> vllt machbar indem man iwie ak und ak+1 bekommt und dann ausrechnet

## Binomialreihen
Mit der Binomialreihe kann, gleich wie mit der Taylor-Reihe, eine Potenzreihe aufgestellt werden. Mit dieser kann dann eine Approximation einer Funktion abgebildet werden. 

>Wichtig: Die Binomialreihe funktioniern nur bei Funktionen, welche aus äusserte Funktion eine Potzen haben. ($\sqrt{}$, $\frac{1}{x}$, $x^m$)

Der Binomische Lehrsatz sieht folgende Formel für den Aufbau der Reihe vor:
$$(1+x)^\alpha=\sum\limits_{k=0}^\alpha\bigg(\substack{\alpha \\ \\ k} \bigg)x^k$$

wobei $\bigg(\substack{\alpha \\ \\ k} \bigg) = \frac{\alpha!}{k!(\alpha-k)!}$ die **Binomialkoeffizienten** sind.\
Der Reihenaufbau sieht dann wie folgt aus:

$(1+x)^\alpha=\sum\limits_{k=0}^\alpha\bigg(\substack{\alpha \\ \\ k} \bigg)x^k$ mit $\bigg(\substack{\alpha \\ \\ k} \bigg) = \frac{\alpha*(\alpha-1)*...*(\alpha-k+1)}{k * (k-1)*...*3*2*1}$

**Beispiel**

$f(x)=\sqrt{1+x} = (1+x)^{1/2}=\sum\limits_{k=0}^\infty\bigg(\substack{1/2 \\ \\ k} \bigg)x^k=\bigg(\substack{1/2 \\ \\ 0} \bigg)x^0+\bigg(\substack{1/2 \\ \\ 1} \bigg)x^1+\bigg(\substack{1/2 \\ \\ 2} \bigg)x^2+\bigg(\substack{1/2 \\ \\ 3} \bigg)x^3+...$

## Taylor
### Taylor-Polynom
Das Taylor-Ploynom $T_n(x)$ stellt eine Funktion $f(x)$ an einer beliebigen stelle $x_0$ möglichst genau dar. Die Idee ist, dass man eine Summe über n Teilintevalle bildet, welche $f(x)$ immer genauer approximiert. Dies wird mit folgender Summe gemacht:
$$T_n(x) = \sum\limits_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$$
Den Wert der $f'ten$ Ableitung an Stelle von $x_0$ durch die Anzahl der Summenelemente ($k$) mal $(x - x_0)^k$.

$T_n(x_0) = f(x_0) \rArr$ die 0.te Ableitung von $f$ und $T^n$ an der Stelle $x_0$ ist gleich\
$T_n'(x_0) = f(x_0) \rArr$ die 1.te Ableitung von $f$ und $T^n$ an der Stelle $x_0$ ist gleich\
$T_n''(x_0) = f(x_0) \rArr$ die 2.te Ableitung von $f$ und $T^n$ an der Stelle $x_0$ ist gleich\
$T_n'''(x_0) = f(x_0) \rArr$ die 3.te Ableitung von $f$ und $T^n$ an der Stelle $x_0$ ist gleich\
$T_n^{(4)}(x_0) = f(x_0) \rArr$ die 4.te Ableitung von $f$ und $T^n$ an der Stelle $x_0$ ist gleich\
...\
$T_n^{(n)}(x_0) = f(x_0) \rArr$ die n.te Ableitung von $f$ und $T^n$ an der Stelle $x_0$ ist gleich

Sobald diese Reihe steht, kann das Taylor Polynom als Summe abgelesen werden.

Beispiel an $sin(x)$, an Stelle $x_0 = 0$:

Ausrechnen von den Ableitungen von $sin(x)$:\
$f(0) = sin(0) = 0$\
$f'(x) = cos(x) \rArr f'(0) = cos(0) = 1$\
$f''(x) = -sin(x) \rArr f''(0) = -sin(0) = 0$\
$f'''(x) = -cos(x) \rArr f'''(0) = -cos(0) = -1$\
$f^{(4)}(x) = sin(x) \rArr f^{(4)}(0) = sin(0) = 0$

Somit ist $T_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \frac{f^{(4)}(0)}{4!}x^4 + \frac{f^{(5)}(0)}{5!}x^5 + ...$

Ausgewertet: $x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!} \approx sin(x)$

Da $sin(0)$ und $-sin(0) = 0$ sind die Ableitung nicht in der Taylor Reihe enthalten. Aus der ausgewerteten Folge kann nun folgende Summe errechnet werden:
$$\sum\limits_{k=0}^n(-1)^k\frac{x^{{2k+1}}}{(2k+1)!}$$

Der Error beim Abbruch an einem bestimmten Glied kann folgendermassen errechnet werden: $\frac{f(x) - T_n(x)}{f(x)}$, wobei $T_n$ die ausgerechnete Folge bis zum Glied $n$ ist.

### Taylor-Reihen
Das Taylor-Ploynom wird zur Taylor-Reihe, sobald wir das $n$ des Taylor-Ploynomes gegen $\infty$ streben lassen.

Beispiel anhand von $f(x) = sin(x)$ 

Wir nehmen hier den weiter oben beschriebene Methode für das Berechnen des `Konvergenzradius` zur Hilfe.

$T(x)=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\frac{x^9}{9!} = \sum\limits_{k=0}^\infty(-1)^k\frac{x^{{2k+1}}}{(2k+1)!} \rArr$ Potenz mit dem $k$. Glied ist also $(-1)^k\frac{x^{{2k+1}}}{(2k+1)!}$ und somit ist $a_k = \frac{(-1)^k}{(2k+1)!}$

Nun den `Konvergenzradius` berechnen:

$R=\displaystyle{\lim_{k \to \infty}} \Bigl|\frac{a_k}{a_{k+1}}\Bigr| = \displaystyle{\lim_{k \to \infty}} \Bigl|\frac{\frac{(-1)^k}{(2k+1)!}}{\frac{(-1)^{k+1}}{(2k+3)!}}\Bigr| = \displaystyle{\lim_{k \to \infty}} \Bigl|\frac{(-1)^k(2k+3)!}{(2k+1)!(-1)^{k+1}}\Bigr| = \displaystyle{\lim_{k \to \infty}} \frac{(2k+3)!}{(2k+1)!} = \displaystyle{\lim_{k \to \infty}} \frac{(2k+3)(2k+2)(2k+1)}{(2k+1)!} = \displaystyle{\lim_{k \to \infty}} (2k+3)(2k+2)=\infty$

>Sidenote: $\frac{(-1)^k}{(-1)^{k+1}} = -1^1$, und davon wurde oben der Betrag genommen. Somit ist es weggefallen.

## Restgleid nach Lagrange
Das Restglied nach Lagrange ist gleich dem Fehler den wir machen, wenn wir die Funktion $f$ durch das $n$. Taylor-Polynom ersetzen.

Falls die Funktion mindestens $n+1$ mal differenzierbar ist, gilt:
$$f(x) = \sum\limits_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k + R_n(x)$$
Die Funktion muss eben einmal mehr differenzierbar sein, sonst gäbe es ja keinen Rest und $f(x) = R_n(x)$

Das Restglied ergibt sich druch:
$$|R_n(x)| = \bigg| \frac{f^{(n+1)}(c)}{(n+1)!}x^{n+1}\bigg|$$ 
$f^{(n+1)}(c)$ ist die $n+1$ Ableitung der Funktion. Davon soll der Max-Wert genommen werden, da ja der Fehler maximal so gross sein kann, wie auch dieser Wert ist. 

> Zudem, wenn es eine alternierende Reihe ist, ist der Fehler maximal der des $n+1$-ten Gliedes nach dem Abbruch.

**Beispiel**

Anhand von $sin(x)$ an Stelle $x_0 = 0$ entwickelt. Da diese Funktion auch abgeleitet nie grösser als 1 werden kann, wird 1 als Max-Wert eingesetzt.

$|R_n(x)| = \bigg| \frac{f^{(n+1)}(c)}{(n+1)!}x^{n+1}\bigg| \leq \frac{1}{(n+1)!}|x|^{n+1}$\
Man sieht also, dass für ein bestimmtes $x$ nur ein genügend grossen $n$ eingesetzt werden muss.

### Konvergenz Taylor-Reihe zusammen mit dem Restgleid
Die Taylor-Reihe von $f$ an der Stelle $x_0$ konvergiert in ihrem Konvergenzbereich genau dann gegen $f(x)$ wenn das $n$. Restglied nach Lagrange $R_n(x)=f(x)-\sum\limits_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$ für $n \rightarrow \infty$ gegen $0$ konvergiert.

## Rechnen mit Potenzreihen
### Differenzieren
Genauso wie Funktionen können auch Potenzriehen abgeleitet werden. Dafür muss Gliedweise differenziert werden. Gleiches gilt auch für die definierende Summe der Reihe. Jedoch Kann die Summe auch einfach erneut abgelesen werden, nachdem man die Potenzreihe abgeleitet hat.

**Beispiel**

Beispiel anhand von $sin(x)$ zu $cos(x)$ ableiten:\
![Potenzreihe_Ableiten](./pic/fig_5.0.0.png "fig 5.0.0")

### Integrieren
Genauso wie Funktionen können auch Potenzriehen integriert werden. Dafür muss Gliedweise integriert werden. Gleiches gilt auch für die definierende Summe der Reihe. Jedoch Kann die Summe auch einfach erneut abgelesen werden, nachdem man die Potenzreihe integriert hat.

**Beispiele**

Beispiel anhand von $sin(x)$ zu $cos(x)$ integriern:\
![Potenzreihe_Integrieren](./pic/fig_5.1.0.png "fig 5.1.0")

![Potenzreihe_Integrieren](./pic/fig_5.2.0.png "fig 5.2.0")

### Substitution
Kompliziertere Ausdrücke können mittels Substitution ersetzt werden.

Ausgehen von der Binomialreihe $\frac{1}{1-z}=1+z+z^2+z^3+z^4 = (1-z)^{-1}\sum\limits_{k=0}^\infty\bigg(\substack{-1 \\ \\ k} \bigg)(-z^k)$

Wir wollen erreichen, dass $\frac{1}{1-z}$ genutzt werden kann, um folgendes Beispiel auszurechnen: $\frac{1}{1+2x^2}$\
Dafür müssen wir $-2x^2$ (da - + - = +) mit $z$ ersetzen. Nun kann die Funktion gemäss der obenstehenden Summe ausgerechnet werden. (also eigentlich gemäss $\bigg(\substack{-1 \\ \\ k} \bigg) = \frac{(-1)(-2)(-3)...(-1-(k-1))}{1*2*3*...*k}$ )\
$\frac{1}{1+2x^2}=1-2x^2+4x^4-8x^6+16x^8-.+...$

## Mehrdimensionale Differentialrechnung
### Konturlinien
TODO: Wolfram alpha nutzen ;)

### Partielle Ableitung
Die `partielle Ableitung` wird eingesetzt, wenn es in einer Funktion mehrere unterschiedliche Variablen gibt. die Schriebweise der partiellen Ableitung wird anstatt mit dem $\frac{dx}{dy}$ mit dem Partial Zeichen $\partial$ bewerkstelltigt. Die Funktion muss so oft abgleitet werden, wie sie unterschiedliche Variabeln hat. Bei jeder dieser Ableitungen wird nach einer Variabel abgeleitet. Die anderen werden als Konstanten betrachtet.

Für eine Funktion $f(x,y)$ würde folgendes geschrieben werden.:\
Dies ist die Parielle Ableitung von $f(x,y)$ nach $\partial x$
$$f_x(x,y_0)=\frac{\partial f(x,y)}{\partial x}\biggl|_{x,y=y_0}$$
Dies ist die Parielle Ableitung von $f(x,y)$ nach $\partial y$
$$
f_x(x_0,y)=\frac{\partial f(x,y)}{\partial y}\biggl|_{x=x_0,y}
$$

Die `partiellen Ableitungen` von $f$ nach $x$ und $y$ an der Stelle $(x_0, y_0)$ sind nach dem oben Gesagten wie folgt definiert:

![Partielle_Ableitung](./pic/fig_6.0.0.png "fig 6.0.0")

Fasst man $x_0$ und $y_0$ wieder als Variablen auf, erhält man partiellen Ableitungsfunktionen $f_x(x, y)$ und $f_y(x, y)$. Oft verwendet man mit $z = f(x, y)$ alternative Bezeichnungen

$$
f_x(x,y)=\frac{\partial z}{\partial x}\ \ \ \ \ \ and \ \ \ \ \ \ f_y(x,y)=\frac{\partial z}{\partial y} \\
f_x(x,y)=\frac{\partial z}{\partial x}\biggl|_{x_0,y_0}\ \ \ \ \ \ and \ \ \ \ \ \ f_y(x,y)=\frac{\partial z}{\partial y}\biggl|_{x_0,y_0}
$$

> Beachte: Wir verwenden anstatt $f$ oft $z$ weil $z=f(x,y)$

**Beispiel**

Wenn nach einem Gewissen Punkt gesucht wird:\
Sei $f(x,y) = $\frac{x^2}{y+1}$. Gesucht ist $\frac{\partial z}{\partial x}$ (oder andere Schreibweise) $f_x(x,y)$ am Punkt (3,2).\
Da, wenn nach $x$ abgeleitet, alle anderen Variabeln als Konstanten betrachtet werden, würde die Ableitung wie folgt aussehen:\
1. Konstante(n) einsetzen $z = f(x, 2) = \frac{x^2}{y+1} \frac{x^2}{2+1} \frac{x^2}{3}$
2. Nach $x$ ableiten $\frac{d}{dx} \bigg(\frac{x^2}{3}\bigg) = \frac{2x}{3}$
3. Nun kann für $x$ noch 3 eingesetzt werden $\frac{2*3}{3} = 2$

> Beachte: Die partielle Ableitung einer Funktion nach einer Variablen bestimmen heisst nichts anderes als gewöhnlich nach dieser Variablen ableiten und dabei alle anderen Variablen als Konstanten betrachten.

Es ist aber so, dass Beispiele an einem Punkt nur sehr selten vorkommen!

Nun zu Beispielen, die nicht an einem bestimmten Punkt abgeleitet werden. (Man beachte auch die entsprechenden Schriebweisen wenn $f(x,y)$ oder $z=$ steht)

1. $f(x,y) = y^2e^{3x}$
   1. $\frac{\partial f}{\partial x}= f_x = y^2\cdot e^{3x} \cdot3$
   2. $\frac{\partial f}{\partial y}= f_y = 2y\cdot e^{3x}$
2. $z=(3xy+2x)^5$
   1. $\frac{\partial z}{\partial x}= z_x = 5(3xy+2x)^4 \cdot (3y + 2)$
   2. $\frac{\partial z}{\partial y}= z_y = 5(3xy+2x)^4 \cdot (3x) = 15x(3xy+2x)^4$
3. $g(x,y)=e^{x+3y}sin(xy)$
   1. $\frac{\partial g}{\partial x}= g_x = e^{x+3y} \cdot 1 \cdot sin(xy) + e^{x+3y} \cdot cos(xy) \cdot y$
   2. $\frac{\partial g}{\partial y}= g_y = e^{x+3y} \cdot 3 \cdot sin(xy) + e^{x+3y} \cdot cos(xy) \cdot x$

Bei dem Beispiel 3 wurde die Kettenregel für einzelne Elemente der Ableitung nach $x$ oder $y$ angewant. Diese hat aber nicht mit der Partiellen Kettenregel zu tun, welche später noch behandelt wird.

Nochmals Kurz als repetition
+ Mit + oder - unterteilte Ausdrücke fallen weg, wenn sich in ihnen die abzuleitende Variabel nicht befindet.
+ In * oder / Ausdrücken, in den nur ein Teil des Ausdrucks von der Variabel abhängt, muss die Produkt / Quotiontenregel **NICHT** angewandt werden. Dort wird nur die entsprechende Variabel abgeleitet und der andere Teil ganz normal daran multipliziert.
+ In * oder / Ausdrücken, in den beide Teile des Ausdrucks von der Variabel abhängt, muss die Produkt / Quotiontenregel

### Gradient
Der Gradient ist eigentlich nichts anderes als ein Vector, der die einzelnen partiellen Ableitungen für entsprechende Variabeln ($[x,y,z,...]^T$) beinhaltet. Der Gradient wird mittels einem auf den Kopf gestellten Delta Zeichen $\nabla$ vor der Funktion Dargestellt.
$$\nabla f(x,y)=\begin{bmatrix} f_x(x,y) \\ f_y(x,y) \end{bmatrix}$$

>In Richtung des Gradienten nimmt die **Funktion maximal zu**, in entgegengesetzter Richtung nimmt die **Funktion maximal ab**: darauf basiert das Gradientenabstiegsverfahren

Weiter Eigenschaften eines Gradienten:\
Ist $f$ eine anständige Funktion, d.h. insbesondere im Punkt $(x_0, y_0)$ differenzierbar mit dem Gradienten $\nabla f(x_0, y_0) \neq 0$, dann ist
+ die Richtung des Gradienten $\nabla f(x_0, y_0) \neq 0$
  + **Senkrecht (orthogonal)** zu den Konturlinien von $f$ durch $(x_0, y_0)$, d.h. den Kurven mit $f(x_0, y_0) = f(x, y)$.
  + in **Richtung der maximalen Zunahme** von $f$.
+ der Betrage des Gradienten $\vert \nabla f(x_0, y_0) \vert$
  + ist gleich der **maximalen Änderungsrate** von $f$ in diesem Punkt.
  + ist gross, wenn die Konturlinien nahe beieinander sind und klein, wenn sie weit auseinander liegen.

Da die Partielle Ableitung eine Überschrift darüber behandelt wurde verweise ich darauf und werde für den Gradienten nur ein Beispiel machen. _Es handelt sich schliesslich nur ums Einsetzen der Partiellen Ableitung in einen Vector_.

**Beispiel**

Gesucht ist der Gradient von $f(x, y) = x + e^y$\
$\nabla f(x,y) = \begin{bmatrix} f_x(x,y) \\ f_y(x,y) \end{bmatrix} = \begin{bmatrix} 1 \\ e^y \end{bmatrix}$

#### Gradient an einem Punkt
Der Gradient kann auch an einem bestimmten Punkt errechnet werden. Dann muss dieser Punkt gegeben sein und auch in die entsprechende Dimension des Gradienten passen.

**Beispiel von oben** (Funktion: $f(x, y) = x + e^y$, Punkt $\color{orange}(5, 1)$)

$\nabla f(x,y) = \begin{bmatrix} f_x(x,y) \\ f_y(x,y) \end{bmatrix} = \begin{bmatrix} 1 \\ e^y \end{bmatrix} = \color{orange}\begin{bmatrix} 1\cdot5 \\ e^1 \end{bmatrix} = \begin{bmatrix} 5 \\ e \end{bmatrix}$

Wenn eine Ableitung nach z.B. $x$ am Ende noch andere Variabeln beinhaltet, so müssen die entsprechenden Werte dieser halt ebenfalls eingefüllt werden.

### Richtungsableitung
Wenn in der Aufgabe stehen würde, dass man den Gradienten nicht dafür nutzen darf steht alles auf den Slides SW13 ab Slide 27! Es macht jedoch keinen Sinn alles aufzuführen, da es mit dem Gradienten 100 mal einfacher ist! Nun zu Thema:

Für eine anständige (sprich differenzierbare) Funktion kann die Richtungsableitung von $f$ im Punkt $x_0$ in Richtung des Einheitsvektors $e$ mit Hilfe des Gradienten bestimmt werden:

Als Info: Um aus $\vec{a}$ einen Einheitsvector zu machen muss er selbst duch seine Länge geteilt werden. $\frac{\vec{a}}{|\vec{a}|}$ Die länge (mit den beiden || dargestellt), kann berechnet werden, indem alle Werte im Quadrat **ADDIERT** werden und dann von diesem Resultat die Wurzel gezogen wird. (pythagoras)

Die Richtungsableitung kann folgendermassen berechnet werden:
$$D_ef(x_0)=\nabla f(x_0) \bullet e$$
Diese Gleichung sagt aus, dass man dien Gradienten einer Funktion nehmen soll und diesen mit dem nomierten Richtungsvektor Scalar multiplizieren soll.\
Das Resultat sagt dann aus, wie ein Unit Step in die Richtung des nomierten Richtungsvektor den Wert der Funktion ändern wird.

Übrigens, die Partielle Ableitung nach $x$ ist auch gleich der Richtungsableitung in Richtung $x$. Gleiches gilt auch für $y$ oder sonstige Variabeln. Mit der Richtungsableitung selbst aber, ist es einem möglich, in eine beliebige Richtung zu gehen.

**Beispiel**

Sei $f(x,y,z) = 2x^2 + 3y^3 + z^2$, $x_0 =[2,1,3]^T$, $a = [1,0,-2]^T$ (Beachten, dies ist kein Einheitsvector)

Zuerst erstellt man den Gradienten:\
$\nabla f(x,y,z) = \begin{bmatrix} 4x \\ 9y \\ 2z\end{bmatrix}$

Dieser wird dann an den Punkt $x_0$ gesetzt:\
$\begin{bmatrix} 4x \\ 9y \\ 2z\end{bmatrix}$ an dem Punkt $x_0 \rArr \begin{bmatrix} 8 \\ 9 \\ 6\end{bmatrix}$

Dann muss aus $a$ einen Einheitsvektor gemacht werden.
$\frac{a}{\vert a \vert} = \frac{a}{\sqrt{5}} = \frac{1}{\sqrt{5}} \cdot a = [\frac{1}{\sqrt{5}}, 0, -\frac{2}{\sqrt{5}}]^T$

Am Schluss kann das Skalarprodukt $\nabla f(x,y,z)\bullet a$ gebildet werden:\
$\nabla f(x,y,z)\bullet a = \begin{bmatrix} 8 \\ 9 \\ 6 \end{bmatrix} \bullet \begin{bmatrix} \frac{1}{\sqrt{5}} \\ 0 \\ -\frac{2}{\sqrt{5}} \end{bmatrix} =\frac{8}{\sqrt{5}} + (-\frac{12}{\sqrt{5}}) = -\frac{4}{\sqrt{5}}$

## Totales Differential
Das Totale Differential ist die Ableitung einer Funktion nach $x,y$ an einem Punkt(a,b).\
$df=d_x(a,b)dx+f_y(a,b)dy$ oder in Kurzform $df=d_xdx+f_ydy$

Es ist wichtig, dass hier $dx, dy$ auch mitgeschrieben werden, da diese Variabeln den Fehler darstellen

TODO Example??

## Kettenregel multidimensionaler Differenzialrechnung

## Linearisierung von Funktionen mehrerer Variabeln

## Kritische Punkte multidimensionaler Differenzialrechnung
Wenn der Gradient 0 ist, hat man einen kritischen Punkt. Es dürfen aber nicht die einzelnen Werte des Gradienten mitenander verrechnet werden, um schlussendlich 0 zu erhalten. Es geht wirklich nur darum, dass alle Variabeln an einem gewissen Punkt 0 sind.

Wenn es einen undefinierten Punkt gibt, ist dieser auch ein kritischer Punkt, jedoch sind bei diese weitere Untersuchungen notwendig. z.B. $\frac{1}{\sqrt{x^2 + y^2}}$ ist bei $x$ und $y$ = 0 undefiniert.

> Theorem: Falls eine anständige Funktion f in $x_0$ ein (lokales) Maximum oder Minimum hat, dann verschwindet dort der Gradient, d.h. $\nabla f(x_0) = 0$, d.h. $x_0$ ist ein kritische Punkt. achtung: die Umkehrung gilt nicht!

Um was es sich bei diesem Punkt handelt wird im Kapitel **Klassifikation der kritischen Punkte** besprochen.

**Beispiel 1**\
Based on: $f(x,y) ) \frac{1}{4}(x^4-2x^2+y^4-2y^2)$

Der Gradient von $f$ ist $\nabla f(x,y) = \begin{bmatrix} \partial f / \partial x \\ \partial f /\partial y \end{bmatrix} = \begin{bmatrix} x^3 - x \\ y^3 -y \end{bmatrix}$. Kritische Punkte sind Lösungen des folgenden Systems nichtlinearer Gleichungen:

$\nabla f(x,y) = 0 \lrArr x^3 -x = 0$ und $y^3 -y = 0$\
Daraus ergibt sich, dass $x$ und $y$ eines der folgenden Kombinationen sein kann: $(0,0), (\plusmn1,\plusmn1), (\plusmn1, 0), (0, \plusmn1)$.

$\rArr$ Somit sind die folgenden Punkte kritische Punkte: $(0,0), (\plusmn1,\plusmn1), (\plusmn1, 0), (0, \plusmn1)$

**Beispiel 2**\
Based on: $f(x,y) = x^2-y^2$

Somit ist der Gradient $\nabla f(x,y) = \begin{bmatrix} 2x \\ -2y \end{bmatrix}$. Wir fragen uns nun, an welchem Punkt der Gradient null ist und stellen fest, dass dieser nur am Punkt $(0,0) = 0$ sein kann. 

$\rArr$ Somit ist der folgenden Punkt ein kritischer Punkt: $(0,0)$

## Partielle Ableitung höherer Ordnung
Die partiellen Ableitungen einer Funktion sind meist wieder Funktionen und können deshalb wieder abgeleitet werden. Dadurch entstehen die zweiten partiellen Ableitungen oder die partiellen Ableitungen 2. Ordnung. Diesen Prozess kann man natürlich wiederholen.

Es wird also eigentlich zuerst $f$ nach zum Besipiel $x$ abgeleitet und diese Ableitung dann wieder nach $x$ sowie nach $y$. Danach wird die eigentliche Funktion nach $y$ abgeleitet und diese Ableitung dann auch nach $x$ und $y$. So ergeben sich von der initialen Funktion (1), 2, 4, 8, 16, 32,... Ableitungen.

Geschrieben wird es so:

$$
\frac{\partial}{\partial x}\bigg(\frac{\partial f}{\partial x}\bigg) = \frac{\partial^2z}{\partial x \partial x} = f_{xx} = (f_x)_x
\ \ \ \ \ \ \ \ \ \ 
\frac{\partial}{\partial x}\bigg(\frac{\partial f}{\partial y}\bigg) = \frac{\partial^2z}{\partial x \partial y} = f_{yx} = (f_y)_x
\\
\frac{\partial}{\partial y}\bigg(\frac{\partial f}{\partial x}\bigg) = \frac{\partial^2z}{\partial y \partial x} = f_{xy} = (f_x)_y
\ \ \ \ \ \ \ \ \ \ 
\frac{\partial}{\partial y}\bigg(\frac{\partial f}{\partial y}\bigg) = \frac{\partial^2z}{\partial y \partial y} = f_{yy} = (f_y)_y
$$

Die **`partiellen Ableitungen` zweiter Ordnung** haben etwas mit der **Krümmung** der Funktion zu tun (wie im Fall einer Variablen).

## Klassifikation der kritischen Punkte
Die Funktion $f : (x, y) \rightarrow f(x, y)$ habe stetige partielle Ableitungen bis und mit 2. Ordnung und
$(x_0, y_0)$ sei ein kritischer Punkt von f. Wir definieren

$D=f_{xx}(x_0,y_0)f_{yy}(x_0,y_0) - [f_{xy}(x_0,y_0)]^2$.

Dies ist eigentlich nichts anderes als die Determinate einer 2x2 Matrix zu berechnen. (Natürlich müssen zuerst die Werte des entsprechenden Punkts eingesetzt werden.)\
Man kann sich diese so vorstellen: $\begin{bmatrix} f_{xx} && f_{xy} \\ f_{xy} && f_{yy} \end{bmatrix}$

Es gilt dann:
1. Falls $D > 0$ und $f_{xx}(x_0, y_0) > 0$, dann ist $f$ minimal in $(x_0, y_0)$
2. Falls $D > 0$ und $f_{xx}(x_0, y_0) < 0$, dann ist $f$ maximal in $(x_0, y_0)$
3. Falls $D < 0$, dann ist $(x_0, y_0)$ ein Sattelpunkt
4. Falls $D = 0$, dann kann ohne weitere Untersuchungen nichts gesagt werden

## Optimierung



## Parameterdarstellung
TODO: 
## Allgemeine Formeln der Geometrie
### Kreis Formeln
#### 1. Circumference
$C=U=2\pi*r$
#### 2. Area
$A=\pi*r^2$
### Kugel Formeln
#### 1. Surface
$A=4\pi*r^2$
#### 2. Volume
$V=\frac{4}{3}\pi*r^3=\frac{1}{6}\pi d^3$
### Kegel Formeln
#### 1. Mantelline
$s=\sqrt{h^2+r^2}$
#### 2. Grundfläche
$A_G=r^2*\pi$
#### 3. Mantelfläche
$A_M = r*s*\pi$
#### 4. Gesamtfläche
$A=A_G + A_M=r*\pi*(r+s)$
#### 5. Volume
$V=\frac{1}{3}*\pi*r^2*h=\frac{1}{3}*A_G*h$


## Allgemeine Formeln
### Pq Formel
$x_{1,2}=-\frac{P}{2}\pm\sqrt{(\frac{P}{2})^2-q}$\
Folgende Funktion eingesetzt: $0=x^2-6x+5$\
$x_{1,2}=\frac{6}{2}\pm\sqrt{(\frac{6}{2})^2-5}$\



## Allgemeine Winkelfunktionen
$sin(x)^2cos(x)^2=1$\
$\frac{sin(x)}{cos(x)}=tan(x)$

### arctanh
$arctanh = \frac{1}{\sqrt{1-x^2}}$\
Wird genutzt, wenn $x<1$.

### arcoth
$arctanh = \frac{1}{\sqrt{1-x^2}}$\
Wird genutzt, wenn $x>1$.


-> auflisten der einzelnen Winkelfunktionsbeziehungen. Dies kann zb. in dem einten Integral Vid von dem mathe peter gefunden werden...