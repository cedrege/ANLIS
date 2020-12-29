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
TODO:

### Integrationstabelle
Eine weitaus umfangreichere Liste kann auf https://en.wikipedia.org/wiki/Lists_of_integrals gefunden werden.\
![Integrationstabelle](./pic/fig_4.4.0.png "fig 4.4.0")

### Integral als Summe
TODO: in aufgabe sw8 abschreiebn

TODO: python Integral.as_sum()

### Unbestimmtes Integral
Funktion = Stammfunktion = $F(x)$\
Abgeleitete Funktion = $F'(x) = f(x)$\
Parabelschar = Verallgemeinerung der möglichen Stammfunktionen: $y=x^2+C\ \ \ \ (C\in\R)$\
Da beim integrieren nicht gesagt werden kann welche oder überhaupt konstante Zahlen bei der `Stammfunktion` $F(x)$ dabei war gibt es mehrere Möglichkeiten, wie die Funktion ausgesehen haben könnte.

Bsp: $f(x)_0=x^2+2$ ist eine `Stammfunktion` von $2x$\
Weitere Funktionen im Bild fig_4.1.0.svg dargtestellt:\
![Stammfunktionen_beispiel](./pic/fig_4.1.0.svg "fig 4.1.0")

Man sieht also, dass die Umkehrung einer `Differenzierung` mehrere Lösung haben kann. Darum ist das `Unbestimmte Integral` von $F(x)$ die Menge ALLER Stammfunktionen (`Parabelschar`) von $f(x)$.

### Bestimmtes Integral
$A=\int\limits_{a}^b x^2dx= F(b) - F(a)$\
Beispiel an $f(x)=x^2$
Um die Fläche unter dem Graphen von $f(1)$ bis $f(2)$ zu errechnen muss zuerste eine der möglichen `Stammfunktionen` ausgewählt werden. In dem Fall von $x^2$ wäre es $F(x) =\frac{1}{3}x^3$, da $3*\frac{1}{3}x^{3-1} = x^2$.\
Wenn diese Funktion herausgefunden ist und auch existiert, kann die Berrechnung durchgeführt werden: $A=\int\limits_{1}^2x^2dx=F(2)-F(1)=\frac{1}{3}2^3-\frac{1}{3}1^3=\frac{8}{3}-\frac{1}{3}=\frac{7}{3}$\
Bei der Funktion $e^{-2x}$ geht dies zum Beispiel nicht, da diese keine `Stammfunktion` hat.

####  Rechenregel für bestimmtes Integral
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

#### Erste Substitutionsregel bei unbestimmten Integralen
Theorem: Es gilt: $\int f(g(x))g'(x)dx=[\int f(u)du]_{u=g(x)}$

Die erste Substitutionsregel kommt immer dann zum Einsatz, wenn klar ersichtlich ist, dass ein Teil des Ausdrucks die Ableitung des anderen Teiles ist. Die Idee ist, dass $\frac{dx}{du} = u'$ dann so gewählt werden kann, dass der zweite Teil des Audrucks damit gestrichen werden kann.

Vorgehen:
1. Substituiere formal $g(x) = u, g'(x) dx = du$
2. Integriere unbestimmt nach $u$
3. Ersetze $u$ wieder durch $g(x)$

Beispiel:

$\int \frac{2x+6}{x^2+6x-12}dx \rightarrow \int \frac{2x+6}{u}\frac{dx}{du} \rightarrow \int\frac{2x+6}{u}\frac{du}{2x+6} \rightarrow \int\frac{1}{u}du$

Dies wurde mit der Substitution von $u=x^2+6x-12$ bewerkstelligt.\
$u = x^2+6x-12$\
$u' = 2x+6$\
$\frac{du}{dx} = 2x+6 \rightarrow \frac{du}{2x+6} = dx$

#### Erste Substitutionsregel bei bestimmten Integralen
Theorem: Es gilt: $\int\limits_{a}^bf(g(x))g'(x)dx = \int\limits_{g(a)}^{g(b)}f(u)du=[F(u)]_{g(a)}^{g(b)}=F(g(b))-F(g(a))$

Vorgehen:
1. Substituiere formal $g(x) = u, g0(x) dx = du$
2. Ersetze die x-Grenzen $a, b$ durch die u-Grenzen $g(a), g(b)$
3. Integriere

<img src="./pic/fig_4.3.0.png" alt="fig 4.3.0" width="600"/>

#### Zweite Substitutionsregel bei unbestimmten Integralen
#### Zweite Substitutionsregel bei bestimmten Integralen
Wichtige infos in diesen VIds:

https://www.youtube.com/watch?v=vtyaO162fa4

https://www.youtube.com/watch?v=AWN01OjmgWI

#### Mittelwert eines Integrals
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

# calculate the quadratic average of a given integral within a fixed range
# TODO: Not yet fully working. need more examples to test it
def mw_q(func, range):
    multip = 1 / (range[2] - range[1])
    test = sp.Integral(sp.Abs(func) ** 2, range)
    display(test)
    aaa = sp.sqrt(multip * test.doit())
    display(sp.N(aaa))

# calculate the linear average of a given integral within a fixed range
def mw_lin(func, range):
    multip = 1 / (range[2] - range[1])
    test = sp.Integral(func, range)
    display(test)
    aaa = multip * test.doit()
    display(aaa)
    display(sp.N(aaa))

# RUN IT
#mw_lin(sp.ln(x), (x, 1, 5))
#mw_q(sp.sin(x), (x, 0, 2*sp.pi))
```

#### Bogenlänge eines Integrals
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
    test = sp.Integral(sp.sqrt(1 + sp.diff(function) ** 2), range)
    print("Integral")
    display(test)
    print("Integral simplified")
    display(test.simplify())
    print("Integral result")
    display(test.simplify().doit())
    print("Integral result as number")
    display(sp.N(test.simplify().doit()))


# RUN IT
#int_arc_length(5*sp.cosh(x/5), (x, -7.15, 7.15))
#int_arc_length(4.2*sp.ln(x**3), (x, 1, sp.E))
#int_arc_length(sp.sin(x), (x, 0, sp.pi))
```

## Taylorreihen

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