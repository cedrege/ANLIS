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
![Integralrechnung](./pic/fig_4.5.0.png_TODO "fig 4.5.0")

### Integrationstabelle
Eine weitaus umfangreichere Liste kann auf https://en.wikipedia.org/wiki/Lists_of_integrals gefunden werden.\
Zudem ist folgender Integralrechner empfehlenswert: https://www.integral-calculator.com \
![Integrationstabelle](./pic/fig_4.4.0.png_TODO "fig 4.4.0")

### Integral als Summe (Reimannsche Summe)
Die Fläche eines Integrals kann mittels der Reimannschen Summe gebildet werden. Dafür wird die Fläche in $n$ Intervalle aufgeteilt und zwischen der Untergrenze $a$ und der Obergrenze $b$ zusammengezählt.\
**Untersumme**\
Die Untersumme ist die Summer aller Rechtecke, welche den zu integrierenden Bogen nicht überschreiten (Die linke, obere Seite berührt den Bogen).\
![Untersumme](./pic/fig_4.6.0.png_TODO "fig 4.6.0")

**Obersumme**\
Die Obersumme ist die Summer aller Rechtecke, welche den zu integrierenden Bogen überschreiten (Die rechte, obere Seite berührt den Bogen).\
![Obersumme](./pic/fig_4.7.0.png_TODO "fig 4.7.0")

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
# Numerical calculations based on the Reimann-Integral 
import numpy as np

#Define function -> here x^2
def f(x):
    return x*x
# Reimannsche untersumme
# func = funcpointer
# a = lower border
# b = upper border
# n = amount of intevalls
def reimann_us(func, a, b, n):
    sum = 0
    dx = (b-a) / n
    for i in range(1, n+1):
        xk = a + (i-1)  * dx
        sum += func(xk) * dx
    return sum
    
# Reimannsche untersumme
# func = funcpointer
# a = lower border
# b = upper border
# n = amount of intevalls
def reimann_os(func, a, b, n):
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
# print(f"N-Value: {n} Reimann-Untersumme: {reimann_us(f,a,b,n):0.5f} Reimann-Obersumme: {reimann_os(f,a,b,n):0.5f}")

## Multiple Steps based on 2^(1 to 10)
# m = 10
# for k in range(1, m+1):
#    n = np.power(2, k)
#    print(f"N-Value: {n} Reimann-Untersumme: {reimann_us(f,a,b,n):0.5f} Reimann-Obersumme: {reimann_os(f,a,b,n):0.5f}")
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
Weitere Funktionen im Bild fig_4.1.0.svg_TODO dargtestellt:\
![Stammfunktionen_beispiel](./pic/fig_4.1.0.svg_TODO "fig 4.1.0")

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

<img src="./pic/fig_4.3.0.png_TODO" alt="fig 4.3.0" width="600"/>

#### Zweite Substitutionsregel bei bestimmten Integralen
Theorem: Es gilt: $\int\limits_{a}^bf(x)dx=\int\limits_{\phi^{-1}(a)}^{\phi^{-1}(b)}f(\phi(u))\phi'(u)du$

Vorgehen:
1. Wähle eine geeignete invertierbare Substitutionsfunktion $\phi$
2. Substituiere formal $x = \phi(u), dx = \phi'(u) du$
3. Ersetze die $x$-Grenzen $a, b$ durch die $u$-Grenzen $\phi^{-1}(a), \phi^{-1}(b)$
4. Integriere

Das Integrieren funktioniert gleich wie bei der zweiten Substitutionsregel für `unbestmmte Integrale`. Einzig müssen am Schluss die Integrationsgrenzen angepasst werden. Das Anpassen der Grenzen ist gleich wie bei der ersten Substitutionsregel für `bestimmte Integrale`.

### Bemerkungen zur Integralsubstitution

<img src="./pic/fig_4.8.1.png_TODO" alt="fig 4.8.1" width="600"/>
<img src="./pic/fig_4.8.2.png_TODO" alt="fig 4.8.2" width="600"/>

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
![Stammfunktionen_beispiel](./pic/fig_4.2.0.svg_TODO "fig 4.2.0")

### Partielle Integration
TODO: stimmt diese aussage -> wenn nicht splitten und entsprechen am richtigen ort einfügen; Partielle Integration kann bei bestimmten wie auch bei unbestimmten Integralen gleich angewandt werden.
TODO

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
## Taylorreihen

## Simpsonreihen

## Mehrdimensionale Differentialrechnung



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
$V=\frac{4}{3}\pi*r^3$
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