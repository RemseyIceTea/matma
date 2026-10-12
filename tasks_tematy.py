# -*- coding: utf-8 -*-
"""
Zestaw 4: Zadania ze sprawdzianów z Tematów 1 i 2 (z repozytorium matma)
- Temat 1: Liczby rzeczywiste (dowody podzielności i pierwiastki)
- Temat 2: Zbiory i wzory skróconego mnożenia (nierówności algebraiczne i moduły)
"""

TASKS_TEMATY = [
    {
        "id": "t1-zad-18",
        "number": "Zadanie 18 / T1",
        "title": "Podzielność $3^{18} - 2^{18}$ przez 19",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $3^{18} - 2^{18}$ jest podzielna przez 19.",
        "hint": "Zapisz $3^{18} - 2^{18} = (3^3)^6 - (2^3)^6$ lub jako różnicę sześcianów $((3^3)^3 - (2^3)^3)$ albo różnicę kwadratów $(3^9 - 2^9)(3^9 + 2^9)$. Zauważ, że $3^3 - 2^3 = 27 - 8 = 19$.",
        "solution": """
<p><strong>Krok 1:</strong> Zauważmy, że $3^3 = 27$ oraz $2^3 = 8$. Zatem:</p>
$$3^3 - 2^3 = 27 - 8 = 19$$
<p><strong>Krok 2:</strong> Zapisujemy wyrażenie w postaci potęg o wykładniku 3:</p>
$$3^{18} - 2^{18} = (3^3)^6 - (2^3)^6 = 27^6 - 8^6$$
<p><strong>Krok 3:</strong> Stosujemy wzór na różnicę potęg $a^n - b^n = (a - b)(a^{n-1} + \\dots + b^{n-1})$ dla $a = 27, b = 8$:</p>
$$27^6 - 8^6 = (27 - 8)(27^5 + 27^4 \\cdot 8 + \\dots + 8^5) = 19 \\cdot (27^5 + \\dots + 8^5)$$
<p><strong>Wniosek:</strong> Liczba w nawiasie jest całkowita, co dowodzi, że $3^{18} - 2^{18}$ jest podzielna przez 19. $c.n.d.$</p>
""",
        "answer": "$3^{18} - 2^{18} = 19 \\cdot k$ ($k \\in \\mathbb{C}$) $\\implies 19 \\mid (3^{18} - 2^{18})$."
    },
    {
        "id": "t1-zad-19",
        "number": "Zadanie 19 / T1",
        "title": "Podzielność $k^3 - k$ przez 6 dla dowolnej liczby całkowitej $k$",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że dla każdej liczby całkowitej $k$ liczba $k^3 - k$ jest podzielna przez 6.",
        "hint": "Wyłącz $k$ przed nawias i zastosuj wzór na różnicę kwadratów: $k^3 - k = (k-1)k(k+1)$.",
        "solution": """
<p><strong>Krok 1:</strong> Rozkładamy wyrażenie na czynniki:</p>
$$k^3 - k = k(k^2 - 1) = (k - 1)k(k + 1)$$
<p><strong>Krok 2:</strong> Wyrażenie to jest iloczynem <strong>trzech kolejnych liczb całkowitych</strong>.</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Wśród trzech kolejnych liczb całkowitych co najmniej jedna jest parzysta (podzielna przez 2).</li>
  <li>Wśród trzech kolejnych liczb całkowitych dokładnie jedna jest podzielna przez 3.</li>
  <li>Ponieważ $\\operatorname{NWD}(2, 3) = 1$, iloczyn ten dzieli się przez $2 \\cdot 3 = 6$.</li>
</ul>
<p><strong>Wniosek:</strong> Dla każdego $k \\in \\mathbb{C}$ liczba $k^3 - k$ dzieli się przez 6. $c.n.d.$</p>
""",
        "answer": "$k^3 - k = (k-1)k(k+1)$ to iloczyn 3 kolejnych liczb całkowitych $\\implies 6 \\mid (k^3 - k)$."
    },
    {
        "id": "t1-zad-20",
        "number": "Zadanie 20 / T1",
        "title": "Uzasadnienie naturalności liczby z podwójnymi pierwiastkami",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Uzasadnij, że liczba $x = \\sqrt{7 - 4\\sqrt{3}} + \\sqrt{7 + 4\\sqrt{3}}$ jest liczbą naturalną.",
        "hint": "Zwiń wyrażenia pod pierwiastkami do pełnych kwadratów $(a \\pm b)^2$ lub podnieś liczbę $x$ do kwadratu.",
        "solution": """
<p><strong>Sposób 1 (zwijanie pod pierwiastkami):</strong></p>
<p>Zauważmy, że $7 \\pm 4\\sqrt{3} = 4 \\pm 4\\sqrt{3} + 3 = 2^2 \\pm 2 \\cdot 2 \\cdot \\sqrt{3} + (\\sqrt{3})^2 = (2 \\pm \\sqrt{3})^2$.</p>
<p>Wtedy:</p>
$$x = \\sqrt{(2 - \\sqrt{3})^2} + \\sqrt{(2 + \\sqrt{3})^2} = |2 - \\sqrt{3}| + |2 + \\sqrt{3}|$$
<p>Ponieważ $2 > \\sqrt{3} \\approx 1{,}73$, to $2 - \\sqrt{3} > 0$ oraz $2 + \\sqrt{3} > 0$. Stąd:</p>
$$x = (2 - \\sqrt{3}) + (2 + \\sqrt{3}) = 4 \\in \\mathbb{N}$$
<p><strong>Wniosek:</strong> Liczba $x = 4$ jest liczbą naturalną. $c.n.d.$</p>
""",
        "answer": "$x = (2 - \\sqrt{3}) + (2 + \\sqrt{3}) = 4 \\in \\mathbb{N}$."
    },
    {
        "id": "t2-zad-13",
        "number": "Zadanie 13 / T2",
        "title": "Nierówność $x^4 + y^4 \\ge x^3 y + x y^3$",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że dla dowolnych liczb rzeczywistych $x, y$ zachodzi nierówność $x^4 + y^4 \\ge x^3 y + x y^3$.",
        "hint": "Przenieś na lewą stronę i pogrupuj: $(x^4 - x^3 y) - (x y^3 - y^4) = x^3(x - y) - y^3(x - y)$.",
        "solution": """
<p><strong>Krok 1:</strong> Przenosimy wszystkie wyrazy na lewą stronę:</p>
$$x^4 + y^4 - x^3 y - x y^3 \\ge 0$$
<p><strong>Krok 2:</strong> Grupujemy wyrazy:</p>
$$x^3(x - y) - y^3(x - y) \\ge 0$$
$$(x - y)(x^3 - y^3) \\ge 0$$
<p><strong>Krok 3:</strong> Ze wzoru na różnicę sześcianów $x^3 - y^3 = (x - y)(x^2 + xy + y^2)$:</p>
$$(x - y)(x - y)(x^2 + xy + y^2) = (x - y)^2(x^2 + xy + y^2) \\ge 0$$
<p><strong>Krok 4:</strong> Analiza znaków:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>$(x - y)^2 \\ge 0$ dla dowolnych $x, y \\in \\mathbb{R}$.</li>
  <li>$x^2 + xy + y^2 = \\left(x + \\frac{y}{2}\\right)^2 + \\frac{3y^2}{4} \\ge 0$.</li>
</ul>
<p>Iloczyn dwóch liczb nieujemnych jest nieujemny, co kończy dowód. $c.n.d.$</p>
""",
        "answer": "$(x - y)^2 \\left[ (x + y/2)^2 + 3y^2/4 \\right] \\ge 0$."
    },
    {
        "id": "t2-zad-14",
        "number": "Zadanie 14 / T2",
        "title": "Suma sześcianów przy $a + b + c = 0$",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że jeśli $a + b + c = 0$, to $a^3 + b^3 + c^3 = 3abc$.",
        "hint": "Z założenia $c = -(a + b)$. Wstaw to do lewej strony i rozwiń $-(a + b)^3$.",
        "solution": """
<p><strong>Założenie:</strong> $a + b + c = 0 \\implies c = -(a + b)$.</p>
<p><strong>Krok 1:</strong> Podstawiamy do sumy sześcianów:</p>
$$a^3 + b^3 + c^3 = a^3 + b^3 + [-(a + b)]^3 = a^3 + b^3 - (a + b)^3$$
<p><strong>Krok 2:</strong> Rozpisujemy sześcian sumy $(a + b)^3 = a^3 + 3a^2 b + 3ab^2 + b^3$:</p>
$$a^3 + b^3 - (a^3 + 3a^2 b + 3ab^2 + b^3) = -3a^2 b - 3ab^2 = -3ab(a + b)$$
<p><strong>Krok 3:</strong> Zauważamy, że $a + b = -c$:</p>
$$-3ab(-c) = 3abc$$
<p>Otrzymaliśmy $a^3 + b^3 + c^3 = 3abc$, co kończy dowód. $c.n.d.$</p>
""",
        "answer": "$a^3 + b^3 + [-(a+b)]^3 = -3ab(a+b) = -3ab(-c) = 3abc$."
    },
    {
        "id": "t2-zad-15",
        "number": "Zadanie 15 / T2",
        "title": "Nierówność $(a+b)(b+c)(c+a) \\ge 8abc$ dla $a,b,c > 0$",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Udowodnij, że dla dowolnych liczb dodatnich $a, b, c$ zachodzi nierówność $(a+b)(b+c)(c+a) \\ge 8abc$.",
        "hint": "Zastosuj nierówność między średnią arytmetyczną a geometryczną dla każdej pary: $a+b \\ge 2\\sqrt{ab}$.",
        "solution": """
<p><strong>Krok 1:</strong> Dla dowolnych liczb dodatnich zachodzą nierówności między średnią arytmetyczną i geometryczną:</p>
$$\\frac{a + b}{2} \\ge \\sqrt{ab} \\implies a + b \\ge 2\\sqrt{ab}$$
$$\\frac{b + c}{2} \\ge \\sqrt{bc} \\implies b + c \\ge 2\\sqrt{bc}$$
$$\\frac{c + a}{2} \\ge \\sqrt{ca} \\implies c + a \\ge 2\\sqrt{ca}$$
<p><strong>Krok 2:</strong> Ponieważ wszystkie strony są dodatnie, mnożymy te trzy nierówności stronami:</p>
$$(a + b)(b + c)(c + a) \\ge 2\\sqrt{ab} \\cdot 2\\sqrt{bc} \\cdot 2\\sqrt{ca} = 8\\sqrt{a^2 b^2 c^2} = 8abc$$
<p>co kończy dowód. $c.n.d.$</p>
""",
        "answer": "$(a+b)(b+c)(c+a) \\ge 2\\sqrt{ab} \\cdot 2\\sqrt{bc} \\cdot 2\\sqrt{ca} = 8abc$."
    },
    {
        "id": "t2-zad-16",
        "number": "Zadanie 16 / T2",
        "title": "Nierówność z dwiema wartościami bezwzględnymi $|2x-4| + |x+1| \\le 5$",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Rozwiąż nierówność z wartością bezwzględną: $|2x - 4| + |x + 1| \\le 5$.",
        "hint": "Miejsca zerowe wnętrz modułów to $x = 2$ oraz $x = -1$. Rozpatrz trzy przedziały: $(-\\infty, -1)$, $\\langle -1, 2)$ oraz $\\langle 2, \\infty)$.",
        "solution": """
<p><strong>Krok 1:</strong> Punkty podziału osi liczbowej: $x = -1$ oraz $x = 2$.</p>
<ul class="list-disc pl-5 space-y-2">
  <li><strong>Przypadek 1: $x \\in (-\\infty, -1)$</strong>
    <br>Oba wyrażenia pod modułem są ujemne:
    $$-(2x - 4) - (x + 1) \\le 5 \\iff -2x + 4 - x - 1 \\le 5 \\iff -3x + 3 \\le 5 \\iff -3x \\le 2 \\iff x \\ge -\\frac{2}{3}$$
    Część wspólna: $x \\in (-\\infty, -1) \\cap \\langle -\\frac{2}{3}, \\infty) = \\emptyset$.
  </li>
  <li><strong>Przypadek 2: $x \\in \\langle -1, 2)$</strong>
    <br>$2x - 4 < 0$ oraz $x + 1 \\ge 0$:
    $$-(2x - 4) + (x + 1) \\le 5 \\iff -2x + 4 + x + 1 \\le 5 \\iff -x + 5 \\le 5 \\iff -x \\le 0 \\iff x \\ge 0$$
    Część wspólna: $x \\in \\langle -1, 2) \\cap \\langle 0, \\infty) = \\langle 0, 2)$.
  </li>
  <li><strong>Przypadek 3: $x \\in \\langle 2, \\infty)$</strong>
    <br>Oba wyrażenia są nieujemne:
    $$(2x - 4) + (x + 1) \\le 5 \\iff 3x - 3 \\le 5 \\iff 3x \\le 8 \\iff x \\le \\frac{8}{3}$$
    Część wspólna: $x \\in \\langle 2, \\infty) \\cap \\left( -\\infty, \\frac{8}{3} \\right\\rangle = \\left\\langle 2, \\frac{8}{3} \\right\\rangle$.
  </li>
</ul>
<p><strong>Krok 2:</strong> Suma rozwiązań ze wszystkich trzech przypadków:</p>
$$x \\in \\emptyset \\cup \\langle 0, 2) \\cup \\left\\langle 2, \\frac{8}{3} \\right\\rangle = \\left\\langle 0, \\frac{8}{3} \\right\\rangle$$
""",
        "answer": "$x \\in \\left\\langle 0, \\frac{8}{3} \\right\\rangle$ (czyli $x \\in \\left\\langle 0, 2\\frac{2}{3} \\right\\rangle$)."
    },
    {
        "id": "t2-zad-17",
        "number": "Zadanie 17 / T2",
        "title": "Nierówność $a^2 + b^2 + 1 \\ge ab + a + b$",
        "category": "temat-1-2",
        "category_label": "Baza Zadań (Działy 1 i 2)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że dla dowolnych liczb rzeczywistych $a, b$ zachodzi nierówność $a^2 + b^2 + 1 \\ge ab + a + b$.",
        "hint": "Pomnóż nierówność obustronnie przez 2 i pogrupuj w trzy kwadraty różnicy.",
        "solution": """
<p><strong>Krok 1:</strong> Przenosimy wszystkie wyrazy na lewą stronę i mnożymy przez 2:</p>
$$2(a^2 + b^2 + 1 - ab - a - b) \\ge 0$$
$$2a^2 + 2b^2 + 2 - 2ab - 2a - 2b \\ge 0$$
<p><strong>Krok 2:</strong> Rozbijamy wyrazy i grupujemy w pełne kwadraty:</p>
$$(a^2 - 2ab + b^2) + (a^2 - 2a + 1) + (b^2 - 2b + 1) \\ge 0$$
$$(a - b)^2 + (a - 1)^2 + (b - 1)^2 \\ge 0$$
<p><strong>Wniosek:</strong> Jako suma trzech kwadratów liczb rzeczywistych, wyrażenie to jest zawsze nieujemne ($\\ge 0$), z równością zachodzącą wyłącznie dla $a = b = 1$. $c.n.d.$</p>
""",
        "answer": "$(a - b)^2 + (a - 1)^2 + (b - 1)^2 \\ge 0$ dla dowolnych $a, b \\in \\mathbb{R}$."
    }
]
