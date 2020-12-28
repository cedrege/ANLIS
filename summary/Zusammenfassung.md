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
Beispiele:\
![Umkehrfunktionen](./pic/umkehrfunktionen.PNG "Umkehrfunktionen")

### Bogenlänge/Radiant, Trigonometrie
![Trigonometrie](./pic/trigonometrie.PNG "Trigonometrie")

## Folgen, Reihen
Eine Folge kann wie folgt beschrieben werden:
1. Aufzählen der Glieder
2. Bildungsgesetz (explizit): $a_n$ für n-ten Wert direkt erkennbar
3. Rekursionsvorschrift (implizit): Ergibt sich auf vorherigen Gliedern

### Überprüfung auf Beschränktheit, Monotonie und Konvergenz
1. Grenzwert berechnen (oder zumindest verdächtigen)
2. Monotonie prüfen
   1. $a_{n+1}-a_n>0 \iff$ **monoton wachsend**
   2. $a_{n+1}-a_n<0 \iff$ **monoton fallend**
3. Beschränktheit prüfen (obere oder untere Grenze)

### Arithmetische Folge
Differenz d zweier beliebiger aufeinanderfolgender Glieder $a_n$ und $a_{n+1}$ sind konstant.\
Eindeutig beschrieben durch 2 Grössen: 
1. durch ein beliebiges Glied $a_n$ und die Differenz d, oder
2. durch zwei beliebige Glieder $a_n$ und $a_{n+k}$.

### Summe der Glieder einer Arithmetischen Folge
$a_1 + a_2 + ... + a_n = \sum\limits_{k=1}^na_k = na_1 + d\frac{n(n-1)}{2}=n\frac{a_1+a_n}{2}$\
$n$: Anzahl Glieder\
$a_1$: 1. Glied\
$a_n$: letztes Glied

### Geometrische Folge
Quotient q zweier beliebiger aufeinanderfolgenden Glieder $a_n$ und $a_{n+1}$ konstant sind.\
Eindeutig beschrieben durch 2 Grössen:
1. durch ein beliebiges Glied $a_n$ und den Quotienten q, oder
2. durch zwei beliebige Glieder $a_n$ und $a_{n+k}$\
$q = \frac{a_{n+1}}{a_n}$

### Rechnen mit Folgen
1. Eine Folge ($a_n$) multipliziert man mit einer (reellen) Zahl $\lambda$, indem man jedes Glied der Folge mit dieser Zahl multipliziert: $\lambda(a_n) = (\lambda a_n)$
2.  Zwei Folgen ($a_n$) und ($b_n$) addiert man, indem man entsprechende Glieder addiert: $(a_n) + (b_n) = (a_n + b_n)$
3. Ein Folge ($a_n$) hiesst konstante Folge, falls $a_n = c \in \R, \forall n \in \N$.

**Streng monoton zunehmend**: Jedes Glied ist grösser als das vorherige Glied ($a_{n+1} > a_n$)\
**beschränkt**: Glieder sind auf einen gewissen Bereich ("Teppich") eingeschränkt, wird auch mit Epsilon $\epsilon$ gekennzeichnet: $|a_n| \leqslant c$

### Grenzwert einer Folge - Rechenregeln
Falls die Folge ($a_n$) gegen a und die Folge ($b_n$) gegen b konvergiert (annähert)
1. $\lim\limits_{n\rightarrow\infty}(a_n+b_n)=\lim\limits_{n\rightarrow\infty}(a_n)+\lim\limits_{n\rightarrow\infty}(b_n)=a+b$
2. $\lim\limits_{n\rightarrow\infty}(a_n*b_n)=\lim\limits_{n\rightarrow\infty}(a_n)*\lim\limits_{n\rightarrow\infty}(b_n)=a*b$
3. $\lim\limits_{n\rightarrow\infty}(\frac{a_n}{b_n})=\frac{\lim\limits_{n\rightarrow\infty}(a_n)}{\lim\limits_{n\rightarrow\infty}(b_n)}=\frac{a}{b}$ bei $b \ne 0$ und $b_n \ne 0$

#### Trick - Erweitern
![Grenzwert_erweitern](./pic/grenzwert_erweitern.PNG "Grenzwert_erweitern")

#### Trick - Auseinandernehmen
Beispiel:\
![Grenzwert_auseinander](./pic/grenzwert_auseinander.PNG "Grenzwert_auseinander")

#### Natürliche Grenzwerte
1. $\lim\limits_{n\rightarrow\infty}(1+\frac{\alpha}{n})^n=e^{\alpha}$, $\forall \alpha \in \R$
2. $\lim\limits_{n\rightarrow\infty}(n^ke^{-n})=0$, $\forall k \in \N$
3. $\lim\limits_{n\rightarrow\infty}(\sqrt[n]{n})=1$ 
4. $\lim\limits_{n\rightarrow\infty}(\sqrt[n]{a})=1$, $(a>0)$
5. $\lim\limits_{n\rightarrow\infty}(\sqrt[n]{a_1^n+...+a_p^n})$=max{$a_1,...,a_p$}, ($a_k>0, k=1,...,p$)

### Folge der n-ten Partialsummen
Bedeutet n Glieder addieren. Mithilfe der Summe einer endlichen geometrischen Reihe.\
$a_1+a_{1q}+a_{1q^2}+...+a_{1q^{n-1}}=\sum\limits_{k=0}^{n-1}a_1q^k=a_1\frac{q^n-1}{q-1}$\
$a_1$: 1. Glied, $n$: Anzahl Glieder, $q$: Quotient\
Bei Anwendung der Formel kann $n\rightarrow \infty$ verwendet werden, so erhält man unendlich viele Glieder.\
Falls Grenzwert exisitert:\
$\sum\limits_{k=1}^{\infty}a_k=\lim\limits_{n\rightarrow\infty}s_n=\lim\limits_{n\rightarrow\infty}\sum\limits_{k=1}^{n}a_k$\
Unendliche geometrische Reihe: \
$a_1+a_{1q}+a_{1q^2}+a_{1q^3}+...=\sum\limits_{k=0}^{\infty}a_1q^k=\frac{a_1}{1-q}$ falls $|q|<1$\

### Harmonische Reihe
$\sum\limits_{k=1}^{\infty}\frac{1}{k}=\lim\limits_{n\rightarrow\infty}(1+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{n})$

### Konvergenzkriterien
Es muss unbedingt unterschieden werden zwischen der Reihe $\sum\limits_{k=1}^{\infty}a_k$ und der Folge der Glieder dieser Reihe $(a_k) =(1,\frac{1}{2},\frac{1}{3},...)$.\
  * Falls die Reihe $\sum\limits_{k=1}^{\infty}a_k$ konvergiert, dann gilt $\lim\limits_{k\rightarrow\infty}a_k=0$ (die Glieder einer
konvergenten Reihe bilden eine Nullfolge). (Die Reihe 1+2+3+4+5 konvergiert nicht, da die Glieder dieser Reihe keine Nullfolge bilden)
  * Bilden die Glieder einer Reihe keine Nullfolge divergiert die Reihe.
  * Bilden die Glieder einer Reihe eine Nullfolge, dann kann die Reihe konvergieren oder divergieren. (geom./harm. Reihe, bspw. ($\frac{1}{\sqrt{1}}+\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{3}}+\frac{1}{\sqrt{4}}+..., p=\frac{1}{2}$)
  * Die Reihe $\sum\limits_{k=1}^{\infty}\frac{1}{k^p}$ konvergiert für $p > 1$ und divergiert für $p \leqslant 1$. Bspw. ($\frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+...$) konvergiert.

**Absolute Konvergenz**: Die Reihe $\sum\limits_{k=1}^{\infty}a_k$ heisst absolut konvergent, falls die Reihe $\sum\limits_{k=1}^{\infty}|a_k|$ konvergiert. Konvergiert die 1. Reihe aber nicht die 2. Reihe, dann nennt man die Reihe **bedingt
konvergent**. Falls eine Reihe absolut konvergiert, dann konvergiert sie.

#### Quotientenkriterium
Sei $\sum\limits_{k=0}^{\infty}a_k$ eine Reihe mit Gliedern, die nicht verschwinden und $\rho = \lim\limits_{k\rightarrow\infty}(\frac{|a_{k+1}|}{|ak|})$. Dann gilt:
1. Falls $\rho < 1$ dann konvergiert die Reihe (sogar) absolut
2. Falls $\rho > 1$ dann divergiert die Reihe (sogar) absolut
3. Falls $\rho = 1$ dann kann die Reihe sowohl konvergieren wie auch divergieren (weitere Untersuchungen sind nötig).

#### Wurzelkriterium (optional)
Sei $\sum\limits_{k=0}^{\infty}a_k$ und $\rho = \lim\limits_{k\rightarrow\infty}(\sqrt[k]{|a_k|})$. Dann gilt:
1. Falls $\rho < 1$ dann konvergiert die Reihe (sogar) absolut
2. Falls $\rho > 1$ dann divergiert die Reihe (sogar) absolut
3. Falls $\rho = 1$ dann kann die Reihe sowohl konvergieren wie auch divergieren (weitere Untersuchungen sind nötig).
   
#### Majorantenkriterium (optional)
Sei $\sum\limits_{k=0}^{\infty}a_k$ eine konvergente Reihe und es gelte $|bn| \leqslant a_n$ ab einer festen Gliednummer $n_0$. Dann konvergiert auch die Reihe
$\sum\limits_{k=0}^{\infty}|b_k|$

#### Leibnizkriterium (für alternierende Reihen)
Ist ($a_k$) eine positive, monoton fallende Nullfolge, dann konvergiert die alternierende Reihe $\sum\limits_{k=0}^{\infty}(-1)^ka_k$ . Fehler beim Abbruch nach $n$ Gliedern:
$|\sum\limits_{k=0}^{\infty}(-1)^ka_k-\sum\limits_{k=0}^{n-1}(-1)^ka_k|\leqslant a_n$

### Konvergenz Rechenregeln
1. Notwendige Bedingung, damit die Reihe $\sum\limits_{n=1}^{\infty}a_n$ konvergiert ist, dass ihre Glieder eine Nullfolge bilden, d.h. $\lim\limits_{n\rightarrow\infty}a_n = 0$
2. Eine konvergente Reihe bleibt konvergent, wenn man endlich viele Glieder verändert,
weglässt oder dazunimmt.
3. Eine konvergente Reihe darf gliedweise mit einer Konstanten $c \in \R$ multipliziert werden, wobei gilt\ 
$c*\sum\limits_{n=1}^{\infty}a_n=\sum\limits_{n=1}^{\infty}c*a_n$
4. Die Summe (Differenz) zweier konvergenter Reihen ist konvergent wobei gilt\
$\sum\limits_{n=1}^{\infty}a_n \pm \sum\limits_{n=1}^{\infty}b_n= \sum\limits_{n=1}^{\infty}(a_n \pm b_n)$   

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
### Tangentenproblem (Annäherung)
Sekante (Linie durch 2 Punkte) betrachten, und einer der Punkte entlang des Graphen immer näher an den anderen Punkt setzen. So erhält man die Tangente

### Flächenproblem (Annäherung)
Fläche in Rechtecke einteilen und Breite der Rechtecke gegen 0 gehen lassen.

### Grenzwerte
Unterscheiden zwischen links- und rechtsseitiger Grenzwert, oft bei bspw. $|x|$. Wenn bei beiden das Gleiche rauskommt ist es der Grenzwert, **zweiseitiger** oder auch **einfacher** Grenzwert genannt.\
$\lim\limits_{x\rightarrow a^-}f(x)=\lim\limits_{x\rightarrow a^+}f(x)$

#### Linksseitiger Grenzwert
Grenzwert, wenn man von links annähert.\
$\lim\limits_{x\rightarrow a^-}f(x)$

#### Rechtsseitiger Grenzwert
Grenzwert, wenn man von rechts annähert.\
$\lim\limits_{x\rightarrow a^+}f(x)$

#### Uneigentlicher Grenzwert
Grenzwerte, die unendlich sind. D.h, $f(x)$ wächst über alle Grenzen wenn man x gegen a gehen lässt. Kann auch bei links- und rechtsseitigen Grenzwerten vorkommen.\
$\lim\limits_{x\rightarrow a}f(x)=\infty$ \
Kann auch bei links- und rechtsseitigen Grenzwerten vorkommen.\
$\lim\limits_{x\rightarrow a^+}f(x)=-\infty$ oder $\lim\limits_{x\rightarrow a^-}f(x)=+\infty$

#### Grundlegene Grenzwerte

1. $\lim\limits_{x\rightarrow a}k=k$ \
Der Grenzwert einer Konstante ist die Konstante selber.
2. $\lim\limits_{x\rightarrow a}x=a$\
Der Grenzwert von x wenn sich x einer Konstante nähert ist die Konstante selber.
3. $\lim\limits_{x\rightarrow 0^-}\frac{1}{x}=-\infty$
4. $\lim\limits_{x\rightarrow 0^+}\frac{1}{x}=\infty$

#### Rechenregeln Grenzwerte
Diese Regeln gelten nur, falls die einzelnen Grenzwerte existieren!
1. $\lim\limits_{x\rightarrow a}(\mu f(x) \pm \nu g(x))=\mu \lim\limits_{x\rightarrow\ a}f(x)+\nu \lim\limits_{x\rightarrow a}g(x)=\mu L_1 \pm \nu L_2$
2. $\lim\limits_{x\rightarrow a}(f(x)g(x))=\lim\limits_{x\rightarrow\ a}f(x)\lim\limits_{x\rightarrow a}g(x)=L_1L_2$
3. ist $L_2 \ne 0$ und g in einer Umgebung von a verschieden von 0, dann ist der Grenzwert des Quotienten gleich dem Quotient des Grentwertes\
$\lim\limits_{x\rightarrow a}(\frac{f(x)}{g(x)})=\frac{\lim\limits_{x\rightarrow\ a}f(x)}{\lim\limits_{x\rightarrow a}g(x)}=\frac{L_1}{L_2}$

#### Weitere Rechenregeln für Grenzwerte
  * $\lim\limits_{x\rightarrow a}x^n=(\lim\limits_{x\rightarrow a}x)^n=a^n$
  * $\lim\limits_{x\rightarrow a}(f(x))^n=(\lim\limits_{x\rightarrow a}f(x))^n$
  * Für ein Polynom $p(x) = c_0 + c_1x + ··· + c_nx^n = \sum\limits_{k=0}^nc_kx^k$ gilt: \
  $\lim\limits_{x\rightarrow a}p(x)=p(x) = c_0 + c_1a + ··· + c_na^n=p(a)$
  * Für eine rationale Funktion $r(x) = \frac{p(x)}{q(x)}$ (dabei sind $p(x)$ und $q(x)$ Polynome) und eine $a \in \R$ gilt:\
      1.  Falls $q(a) \ne 0$, dann ist $\lim\limits_{x \rightarrow a}r(x)=r(a)$
      2.  Falls $q(a) = 0$ und $p(a) \ne 0$, dann existiert $\lim\limits_{x \rightarrow a}r(x)=r(a)$ nicht
      3.  Falls $q(a) = 0$ und $p(a) = 0$, dann kann der Grenzwert existieren, muss aber nicht
  * Sei $a \in \R \cup$ {$-\infty, \infty$}. Gilt dann $\lim\limits_{x\rightarrow c}g(x)=L$ und ist f im Punkt L stetig, dann gilt:
    * $\lim\limits_{x\rightarrow a}f(g(x)) = f(\lim\limits_{x\rightarrow a}g(x))$
    * insbesondere: $\lim\limits_{x\rightarrow a}|g(x)| = |\lim\limits_{x\rightarrow c}g(x)|$, falls $\lim\limits_{x\rightarrow a}g(x)$ existiert

#### Stückweise definierte Funktion
Eine Funktion, die unterschiedlich definiert ist. Ist mit einem Deifnitionsbereich versehen.
Beispiel:\
![stückweise_funktion](./pic/stückweise_funktion.PNG "stückweise_funktion")
Aufzeichnen, falls man es sich nicht vorstellen kann.\
Falls nötig, Grenzwert ausrechnen. Schauen, in welchen Definitionsbereich der Wert für x fällt.

#### Squeezing-Theorem
Liegt eine Funktion $f(x)$ zwischen zwei Funktionen $g(x)$ und $h(x)$, und ist der Grenzwert der beiden Funktionen gleich $L$, so ist auch der Grenzwert der Funktion $f(x)$ $L$.\
$g(x) \leqslant f(x) \leqslant h(x)$ und $\lim\limits_{x\rightarrow c}g(x) = \lim\limits_{x\rightarrow c}h(x)=L$\
$\lim\limits_{x\rightarrow c}f(x)=L$
![squeezing_theorem](./pic/squeezing_theorem.PNG "squeezing_theorem")

### Stetigkeit
Salopp: eine Funktion f heisst stetig, wenn man deren Graphen zeichnen kann, **ohne den
Stift absetzen zu müssen**. Eine Funktion heisst stetig, falls sie überall, d.h. $\forall x \in D(f)$ stetig ist. \
f ist stetig in a, falls\
$\lim\limits_{x\rightarrow a}f(x)=f(a)$

#### Stetigkeit von Funktionen
  * Summe u. Differenz stetiger Funktionen sind stetig.
  * Der Quotient zweier stetiger Funktionen ist dort stetig, wo der Nenner nicht
verschwindet.
  * Polynome $P(x) = \sum\limits_{k=0}^n a_kx^k$ sind stetig
  * Rationale Funktionen $r(x) = \frac{P(x)}{Q(x)}$ sind dort stetig, wo das Nennerpolynom $Q(x)$ nicht verschwindet.
  * Sinus- $(sin x)$ und Kosinusfunktion $(cos x)$ sind stetig.
  * Der Tangens ($tan x = \frac{sin x}{cos x}$) ist stetig, falls {cosx \ne 0$, d.h. falls $x \ne \frac{\pi}{2} + k\pi, k \in \Z$.
  * Exponential- und Logarithmusfunktion sind in ihren Definitionsbereichen stetig
  * Zusammensetzung stetiger Funktionen ist stetig.
  * Eine zusammengesetzte Funktionen kann dort unstetig sein, wo eine der verwendeten
Funktionen nicht stetig ist.

### Regula Falsi
Regula Falsi wird verwendet, um sich einer Nullstellen anzunähern. Eine Funktion in einem Intervall [a, b] hat eine Nullstelle, wenn sie stetig ist und wenn die beiden Werte eingesetzt in die Funktion f 1x positiv und 1x negativ sind ($f(a)f(b)<0$)
1. 2 Werte bestimmen, wo die Nullstelle dazwischen ist, bspw. $x_0$ und $x_1$. Darauf achten, dass die Vorzeichen der eingesetzten Werte in f, also $f(x_0)$ und $f(x_1)$ ,unterschiedlich sein müssen.
2. Werte in die Formel einsetzen
$x_{neu}=\frac{x_0f(x_1)-x_1f(x_0)}{f(x_1)-f(x_0)}$
3. 2 neue Werte wählen, bspw. $x_{neu} = x_2$ und $x_1$, Schritt wiederholen

Geht auch in Python!

## Differentialrechnung

**Sekante**: Linie durch 2 Punkte auf einem Graphen.
**Tangente**: Falls der der Grenzwert des Differenzenquotienten($\frac{\Delta y}{\Delta x}$) für $\Delta x \rightarrow 0$ existiert, ist die Steigung der Tangente in einem Punkt definiert.
**Differenzenquotient**: Steigung der Sekante, $\frac{\Delta y}{\Delta x}$
**Differentialquotient**: Steigung der Tangente, $\lim\limits_{\Delta x \rightarrow 0}\frac{\Delta y}{\Delta x}= \lim\limits_{\Delta x \rightarrow 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$ Falls dieser Grenzwert existiert, ist die Funktion differenzierbar.

### Tangentengleichung
Liniearisierung von f in $x_0$: $y=f(x_0) + f'(x_0)(x-x_0)$

### Newton-Raphson Verfahren
Verfahren, um Nullstellen (auch Wurzel genannt) rauszufinden, wo andere Methoden nicht helfen, bspw. $f(x)=-x^3-4x+10=0$
1. Tabelle anlegen, um 2 x Werte $x_0$ und $x_1$ zu finden. Achten, dass der f(x) Werte unterschiedliche Vorzeichen hat, d.h da wo der Übergang des y-Wertes vom Positiven ins Negative oder umgekehrt ist! 
2. Einen der Werte, am einfachsten den f(x) Werte, der am nächsten von 0 ist, in die Formel einsetzen: $x_{neu}=x_0-\frac{f(x_0)}{f'(x_0)}$
3. Verfahren wiederholen mit $x_{neu}$

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