# Mathe Zusammenfassung

## Grundlagen
### Algebra



#### Brüche
$\frac{1}{x^2}\frac{1}{x^3}=\frac{1}{x^5}$\
$\frac{1}{cos(x)^2}tan(x)=\frac{1}{cos(x)^2}\frac{sin(x)}{cos(x)}=\frac{sin(x)}{cos(x)^3}$\
$\frac{\frac{a}{b}}{\frac{c}{d}}=\frac{a*d}{b*c}$

### Zahlen
![Zahlenmenge](./pic/zahlenmenge.png "Zahlenmenge")


## Funktionen
**Definitionsbereich/Urbildbereich**: D(f), Menge der für x einsetzbaren Zahlen \
**Wertebereich/Bildbereich**: W(f), Menge aller Funktionswerte y\
**Pol**: eine einpunktige Definitionsläcke einer Funktion, wenn die Funktionswerte in jeder Umgebung des Punktes beliebig gross werden (Nenner wird Null).\
**Asymptote**: eine Gerade, die sich dem Graphen einer Funktion beliebig genau annhähert.\
**Gerade Funktion**: f ist achsensymmetrisch bezüglich der y-Achse und es gilt:\
$f(-x) = f(x), \forall \in D(f)$ (für alle x im Definitionsbereich von f).\
**Ungerade Funktion**: f ist punktsymmetrisch bezüglich dem Ursprung und es gilt:\
$f(-x) = -f(x), \forall \in D(f)$

![Funktionen](./pic/funktionen.jpg "Funktionen")
**Beschränktheit**: Eine Funktion heisst beschränkt, wenn sie nach oben, unten oder beides beschränkt ist.\
**Monotonie**: Eine Funktion heisst streng monoton wachsend/ fallend, wenn sie immer steigt/sinkt. Eine Funktion heisst monoton wachsend, wenn sie nie sinkt.

### Intervalle
Eine eckige Klammer gibt an, dass die entsprechende Intervallsgrenze zum Intervall gehört.\
Eine runde Klammer gibt an, dass die entsprechende Intervallsgrenze nicht zum Intervall
gehört.\
Gelegentlich ist es nützlich für die Intervallgrenzen auch $-\infty$ bzw. $\infty$ zuzulassen:\
$\Reals = (-\infty,\infty), \Reals+ = (0,\infty), \Reals- = (-\infty, 0), \Reals_0+ = [0,\infty), \Reals_0- = (-\infty, 0 ]$

$I = [a, b] = {x \in \Reals  | a <= x <= b}$ : **abgeschlossenes Intervall**\
$I = (a, b) = {x \in \Reals | a < x < b}$ : **offenes Intervall**\
$I = (a, b] = {x \in \Reals | a < x <= b}$ : **halboffenes Intervall**
![Intervall_Beispiel](./pic/intervall_beispiel.PNG "Intervall")

### Lineare Funktionen
$y = mx + b$

**Proportionalität, Steigung**: Für a > 0 liegt die Gerade im I. und III. Quadranten und ist steigend. Für a < 0 liegt die Gerade im II. und IV. Quadranten und ist fallend. Für a = 0 ist die Gerade gleich der
x-Achse! Für a > 0 steigt die Gerade von links nach rechts, für a < 0 fällt sie.\
Ist die Steigung negativ, fällt die Gerade. Ist die Steigung Null, dann hat man eine
horizontale Gerade.\
Beispiel: y=3 -> horizontale Gerade

**Differenzenquotient**: Steigung, $m = \frac{y_2 - y_1}{x_2 - x_1}$\
**Steigung der Senkrechten**: $m_{senkrecht} = \frac{-1}{m}$\
**Schnittpunkt zweier Geraden**: \
Vorgehen: Funktionen gleichsetzen und nach x auflösen, anschliessend in eine der Funktionen einsetzen. 
1. Genau eine Lösung
2. Unendlich viele Lösungen
3. Keine Lösung\

**Schnittpunkt Polynom und Gerade**:\
Schneidet man ein Polynom mit einer Gerade, dann ist die Anzahl der Schnittpunkte höchstens gleich dem Grad des Polynoms.\
Vorgehen: Bei der Berechnung setzt man wieder zu Beginn die Funktionswerte gleich. Anschließend bringt man alles auf eine Seite und bestimmt die  Nullstellen  der neuen Funktion, falls nötig mit der Mitternachtsformel  oder duch Polynomdivision.
**Mitternachtsformel**: $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$

### Quadratische Funktionen
**Stammfunktion**: $y = ax^2 + bx + c$\
a: Öffnung
c: y-Achsenabschnitt

### Exponentialfunktionen
Eine Funktion der $f(x) = a · b^x$ mit $b > 0$ und $b \ne 1$ heisst Exponentialfunktion. a heisst Anfangswert und b heisst Wachstumsfaktor. Für Definitions- und Wertebereich gilt: \
$D(f) =\Reals, W(f) = \Reals+.$\
**Stammfunktion**: $y = a * e^{b*x}$\
$a^x = b  |  x=\log_a(b)$\
Exp: sehr schnelles Wachstum\
Log: sehr langsames Wachstum\
Beispiel: $y =log_{10}x \iff x=10^y$\
$y=log_ex =lnx \iff x = e^y = \exp(y)$
1. $a^xa^y = a^{x+y}$
2. $(a^x)^y=a^{xy}$
3. $a^{-1}=\frac{1}{a^x}$
4. $a^xb^x=(ab)^x$


### Logarithmusfunktion
Die Logarithmusfunktion ist die Umkehrfunktion der Exponentialfunktion, gespiegelt an der Winkelhalbierenden $y=x$\
Die Logarithmusfunktionen sind nur für $x > 0$, d.h. nur in $\Reals+$ definiert
1. $log_a (u*v)=log_a u+log_a v$
2. $log_a (\frac{u}{v})=log_a u-log_a v$
3. $log_a (b^n )=n*log_a b$

$log_a 1=0$\
$log_a a=1$\
$a^(log_a b)=b$\
$log_a (a^n )=n$\
$log_{10} = log$

### Konvex - konkav
Der Graph der Funktion f heisst konvex, falls er eine Linkskurve durchführt, wenn man von
links nach rechts geht. Andernfalls heisst der Graph konkav. Eine Gerade ist weder konvex noch
konkav.
![Konvex_konkav](./pic/konvex_konkav.PNG "Konvex/Konkav")

### Potenzfunktionen
Stammfunktion: $y= a(x-u)^n +b$\
$n>0$: gerade: Parabel, $n$ ungerade: Wendeparabel\
$n<0$: Hyperbel\
$n \in \N$: Monom\
Wachstum: langsamer als die Exponentialfunktion

### Polynome, Ganzrationale Funktionen
Stammfunktion: $a_nx^n + a_{n-1}x^{n-1}+...+a_1x+a_0$\
$a_n$: Koeffizient\
$n$: Grad des Polynoms. Die höchstens Potenz bestimmt den Grad des Polynoms.\
$x$: unabhängige Variable\
$y$: abhängige Variable\
Der Faktor k vor dem Produkt der Nullstellen bewirkt eine Streckung oder Stauchung des
Graphen in y-Richtung und bei einem Vorzeichenwechsel wird der Graph an der x-Achse gespiegelt.

### Rationale Funktionen
Rationale Funktionen sind Quotienten von Polynomen p und q.\
Stammfunktion: $y=r(x)=\frac{p(x)}{q(x)}$

### Verschieben von Funktionen
$f(x)=a*sin⁡(b*(x+c))+d$                
$a$: strecken an Y-Achse mit Faktor $a$\
$b$: stauchen an X-Achse mit Faktor $b$\
$c$: verschieben nach links um $c$\
$d$: verschieben nach oben um $d$

**Merkregel**: Will man den Graph der Funktion $y = f(x)$ vom Ursprung in den Punkt (a, b) verschieben und zusätzlich in Richtung der y-Achse um den Faktor $\alpha$ skalieren (stauchen/strecken), dann lautet die neue Funktion:\
$y - b = \alpha f(x - a) \iff y = \alpha f(x - a) + b.$

Gegeben sei die Funktion $y = f(x)$
1. Multiplikation einer Funktion $f(x)$ mit einer Konstanten $c \in \Reals$ dehnt den Graphen vertikal (falls $c > 1$) oder staucht ihn vertikal (falls $0 < c < 1$). Ein negatives Vorzeichen ($c < 0$) spiegelt den Graphen zusätzlich an der x-Achse.
2. Ersetzt man $y$ durch $y - b$ wird der Graph um $b$ nach oben verschoben (falls $b > 0$), bzw. nach unten (falls $b < 0$).
3. Ersetzt man $x$ durch $x - a$ wird der Graph um $a$ nach rechts verschoben (falls $a > 0$),
bzw. nach links (falls $a < 0$).

### Nullstellen
$x_0: y=f(x_0)=0$\
**Nullstellenform**: $y=a(x-x_1)(x-x_2)$

### Asymptote
**vertikale Asymptote**: Nenner = 0 setzen\
**horizontale Asymptote**: \
Zählergrad > Nennergrad => Asymptote bei $y=0$, Beispiel: $\frac{2*(x^0)}{x}$\
Zählgrad = Nennergrad => $\frac{4x^2}{2x^2}=\frac{4}{2}=>y=2$
**schiefe Asymptote**: Zählergrad um 1 grösser als Nennergrad -> Polynomdivision
Beispiel: 
![Polynomdivision](./pic/polynomdivision.PNG "Polynomdivision")
siehe anderes Beispiel: https://www.gut-erklaert.de/mathematik/polynomdivision.html

### Zusammengesetzte Funktion
Funktion 1: $A=f(r)=\pi r^2$\
Funktion 2: $r = g(t) = 1 + t$\
Es gilt: $A = f(g(t)) = (f \circ g)=\pi(1+t)^2$\
$f$ ist die äussere Funktion (welche zuletzt angewendet wird) und $g$ die innere Funktion (welche zuerst angewendet wird).\
Bei folgenden Beispielen gilt $u(x)$ als äussere Funktion und $v(x)$ als innere Funktion.\
**Klammer**:  $f(x) = 2*(x^2-4)^{10}$\
$u(x)= 2*x^{10}, v(x) =x^2-4$\
**Wurzel**: $f(x)=\sqrt{x-1} = (x-1)^{\frac{1}{2}}$\
$u(x)= \sqrt{x}, v(x) =x-1$\
**Exponent**: $f(x) = 7*3^{x^2-1}$\
$u(x) = 7*3^x,v(x)=x^2-1$\
Darstellung im Venndiagram der Funktion $e^{\cos(x^2-1)}$:
![Venndiagram_beispiel](./pic/venndiagram_beispiel.PNG "Venndiagram")

### Umkehrfunktionen
Beachte: $f^{-1}$ steht für die Umkehrfunktion von f, d.h. $f^{-1} \ne \frac{1}{f}$\
Umkehrfunktion existiert, falls es zu jedem $y$ genau ein $x$ gibt. Oder anders: Falls der Graph höchstens einmal von Parallelen zur x-Achse geschnitten wird. \
$f^{-1} =x \iff f(x) =y$\
**injektiv**: zu jedem y höchstens 1 x-Wert.\
**surjektiv**: zu jedem y mindestens 1 x-Wert.\
**bijektiv**: Funktion ist surjektiv und injektiv.\
Vorgehen: Gleichung nach x auflösen und x mit y vertauschen\
![injektiv_surjektiv](./pic/injektiv_surjektiv.PNG "Injektiv/Surjektiv")
Beispiele:
![Umkehrfunktionen](./pic/umkehrfunktionen.PNG "Umkehrfunktionen")

### Bogenlänge/Radiant, Trigonometrie
![Trigonometrie](./pic/trigonometrie.PNG "Trigonometrie")

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
Theorem: Es gillt: $\int f(g(x))g'(x)dx=[\int f(u)du]_{u=g(x)}$

Vorgehen:
1. Substituiere formal $g(x) = u, g'(x) dx = du$
2. Integriere unbestimmt nach $u$
3. Ersetze $u$ wieder durch $g(x)$

#### Erste Substitutionsregel bei bestimmten Integralen
Theorem: Es gillt: $\int\limits_{a}^bf(g(x))g'(x)dx = \int\limits_{g(a)}^{g(b)}f(u)du=[F(u)]_{g(a)}^{g(b)}=F(g(b))-F(g(a))$

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


-> merge von deveManu in main hat funktioniert