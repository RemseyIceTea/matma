# -*- coding: utf-8 -*-
"""
Zestaw 2 & 3: Zadania ze zdjęć podręcznika
- Temat 4.1: Dowody w algebrze (1) (str. 178–180)
- Temat 4.2: Dowody w algebrze (2) (str. 182–184)
"""

TASKS_PODRECZNIK = [
    # ==========================================
    # TEMAT 4.1: Dowody w algebrze (1)
    # ==========================================
    {
        "id": "p41-cw-1",
        "number": "Ćwiczenie 1 / 4.1",
        "title": "Nieparzystość sumy kwadratów trzech liczb",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że jeśli suma trzech liczb naturalnych jest nieparzysta, to suma ich kwadratów jest nieparzysta.",
        "hint": "Zastanów się, w jakich sytuacjach suma trzech liczb naturalnych $a+b+c$ jest nieparzysta. Zbadaj parzystość kwadratu liczby.",
        "solution": """
<p><strong>Założenie:</strong> $a, b, c \\in \\mathbb{N}$ oraz $a + b + c$ jest liczbą nieparzystą.</p>
<p><strong>Krok 1:</strong> Analiza parzystości składników sumy $a + b + c$:</p>
<p>Suma trzech liczb naturalnych jest nieparzysta tylko w dwóch przypadkach:</p>
<ol class="list-decimal pl-5 space-y-1">
  <li>Wszystkie trzy liczby są nieparzyste.</li>
  <li>Dokładnie jedna liczba jest nieparzysta, a dwie pozostałe są parzyste.</li>
</ol>
<p><strong>Krok 2:</strong> Parzystość kwadratów liczb:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Kwadrat liczby parzystej jest parzysty: $(2k)^2 = 4k^2 = 2(2k^2)$.</li>
  <li>Kwadrat liczby nieparzystej jest nieparzysty: $(2m+1)^2 = 4m^2 + 4m + 1 = 2(2m^2+2m) + 1$.</li>
</ul>
<p><strong>Krok 3:</strong> Sprawdzenie sumy kwadratów $a^2 + b^2 + c^2$:</p>
<ul class="list-disc pl-5 space-y-1">
  <li><strong>W przypadku 1:</strong> Wszystkie trzy kwadraty są nieparzyste. Suma trzech liczb nieparzystych jest nieparzysta: $(2p_1+1) + (2p_2+1) + (2p_3+1) = 2(p_1+p_2+p_3+1) + 1$.</li>
  <li><strong>W przypadku 2:</strong> Dwa kwadraty są parzyste, jeden jest nieparzysty: $2p_1 + 2p_2 + (2p_3+1) = 2(p_1+p_2+p_3) + 1$, co również jest liczbą nieparzystą.</li>
</ul>
<p><strong>Wniosek:</strong> W każdym możliwym przypadku suma kwadratów $a^2 + b^2 + c^2$ jest liczbą nieparzystą. $c.n.d.$</p>
""",
        "answer": "Suma kwadratów w obu przypadkach redukuje się do postaci $2K + 1$ ($K \\in \\mathbb{N}$)."
    },
    {
        "id": "p41-cw-2",
        "number": "Ćwiczenie 2 / 4.1",
        "title": "Podzielność $n(n^4 - 1)$ przez 6 oraz $n^6 - 2n^4 + n^2$ przez 36",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla każdej liczby całkowitej $n$ liczba:<br>
<strong>a)</strong> $n(n^4 - 1)$ jest podzielna przez 6,<br>
<strong>b)</strong> $n^6 - 2n^4 + n^2$ jest podzielna przez 36.""",
        "hint": "Rozłóż wyrażenia na czynniki, szukając iloczynu kolejnych liczb całkowitych $(n-1)n(n+1)$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$n(n^4 - 1) = n(n^2 - 1)(n^2 + 1) = (n - 1)n(n + 1)(n^2 + 1)$$
<p>Czynnik $(n - 1)n(n + 1)$ to iloczyn 3 kolejnych liczb całkowitych, a taki iloczyn jest zawsze podzielny przez $3! = 6$. Zatem cała liczba jest podzielna przez 6. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$n^6 - 2n^4 + n^2 = n^2(n^4 - 2n^2 + 1) = n^2(n^2 - 1)^2 = [n(n^2 - 1)]^2 = [(n - 1)n(n + 1)]^2$$
<p>Skoro $(n - 1)n(n + 1)$ jest iloczynem trzech kolejnych liczb całkowitych, to dzieli się przez 6, czyli $(n - 1)n(n + 1) = 6k$ dla pewnego $k \\in \\mathbb{C}$.</p>
<p>Podnosząc do kwadratu:</p>
$$[(n - 1)n(n + 1)]^2 = (6k)^2 = 36k^2$$
<p>Wartość ta jest podzielna przez 36. $c.n.d.$</p>
""",
        "answer": "a) $6 \\mid (n-1)n(n+1) \\implies 6 \\mid n(n^4-1)$; b) $W = [(n-1)n(n+1)]^2 = (6k)^2 = 36k^2$."
    },
    {
        "id": "p41-cw-3",
        "number": "Ćwiczenie 3 / 4.1",
        "title": "Iloczyn 5 kolejnych liczb oraz suma sześcianów 3 kolejnych liczb",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Udowodnij, że iloczyn pięciu kolejnych liczb naturalnych jest podzielny przez 120.<br>
<strong>b)</strong> Udowodnij, że suma sześcianów trzech kolejnych liczb naturalnych jest podzielna przez 3.""",
        "hint": "W punkcie b) oznacz trzy kolejne liczby symetrycznie jako $n-1, n, n+1$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<p>Iloczyn pięciu kolejnych liczb naturalnych ma postać $P = n(n+1)(n+2)(n+3)(n+4)$.</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Wśród 5 kolejnych liczb co najmniej jedna dzieli się przez 5.</li>
  <li>Wśród 5 kolejnych liczb co najmniej dwie są parzyste, a jedna z nich dzieli się przez 4, więc iloczyn dzieli się przez $2 \\cdot 4 = 8$.</li>
  <li>Wśród 5 kolejnych liczb co najmniej jedna dzieli się przez 3.</li>
</ul>
<p>Ponieważ liczby 5, 8, 3 są parami względnie pierwsze, iloczyn dzieli się przez $5 \\cdot 8 \\cdot 3 = 120 = 5!$. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Niech trzema kolejnymi liczbami naturalnymi będą $n - 1, n, n + 1$ dla $n \\ge 1$:</p>
$$S = (n - 1)^3 + n^3 + (n + 1)^3$$
$$S = (n^3 - 3n^2 + 3n - 1) + n^3 + (n^3 + 3n^2 + 3n + 1) = 3n^3 + 6n = 3(n^3 + 2n)$$
<p>Ponieważ $n \\in \\mathbb{N}$, to $n^3 + 2n \\in \\mathbb{N}$. Zatem suma jest podzielna przez 3. $c.n.d.$</p>
""",
        "answer": "a) $5! = 120 \\mid P$; b) $S = 3(n^3 + 2n) \\implies 3 \\mid S$."
    },
    {
        "id": "p41-cw-4",
        "number": "Ćwiczenie 4 / 4.1",
        "title": "Podzielność potęg: $7^{77} - 6 \\cdot 7^{76} + 12 \\cdot 7^{75}$ oraz $32^{32} - 5^{64}$",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Wykaż, że liczba $7^{77} - 6 \\cdot 7^{76} + 12 \\cdot 7^{75}$ jest podzielna przez 19.<br>
<strong>b)</strong> Wykaż, że liczba $32^{32} - 5^{64}$ jest podzielna przez 7.""",
        "hint": "W punkcie a) wyłącz $7^{75}$. W punkcie b) zauważ, że $5^{64} = (5^2)^{32} = 25^{32}$ i użyj wzoru $a^n - b^n$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$L = 7^{75} \\cdot (7^2 - 6 \\cdot 7 + 12) = 7^{75} \\cdot (49 - 42 + 12) = 7^{75} \\cdot 19 = 19 \\cdot 7^{75}$$
<p>Liczba $7^{75}$ jest całkowita, co dowodzi podzielności przez 19. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Przekształcamy drugi składnik:</p>
$$5^{64} = (5^2)^{32} = 25^{32}$$
<p>Badana liczba to:</p>
$$32^{32} - 25^{32}$$
<p>Ze wzoru na różnicę potęg $a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + \\dots + b^{n-1})$ dla $a = 32$ i $b = 25$:</p>
$$32^{32} - 25^{32} = (32 - 25)(32^{31} + 32^{30} \\cdot 25 + \\dots + 25^{31}) = 7 \\cdot (\\dots)$$
<p>Czynnik w nawiasie jest liczbą całkowitą, co dowodzi podzielności przez 7. $c.n.d.$</p>
""",
        "answer": "a) $L = 19 \\cdot 7^{75}$; b) $32^{32} - 25^{32} = (32 - 25)(\\dots) = 7 \\cdot k$."
    },
    {
        "id": "p41-cw-5",
        "number": "Ćwiczenie 5 / 4.1",
        "title": "Reszty z dzielenia przez 6 i kwadraty liczb",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Reszta z dzielenia liczby naturalnej $n$ przez 6 jest równa 5. Wykaż, że reszta z dzielenia liczby $n^2$ przez 6 jest równa 1.<br>
<strong>b)</strong> Reszta z dzielenia każdej z liczb naturalnych $n_1, n_2$ i $n_3$ przez 6 jest równa 4. Wykaż, że suma kwadratów tych liczb jest podzielna przez 12.""",
        "hint": "Zapisz liczby w postaci $n = 6k + r$ i podnieś do kwadratu.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<p>Skoro reszta z dzielenia $n$ przez 6 wynosi 5, to $n = 6k + 5$ dla $k \\in \\mathbb{N}$.</p>
$$n^2 = (6k + 5)^2 = 36k^2 + 60k + 25 = 36k^2 + 60k + 24 + 1 = 6(6k^2 + 10k + 4) + 1$$
<p>Ponieważ $6k^2 + 10k + 4 \\in \\mathbb{N}$, to reszta z dzielenia $n^2$ przez 6 wynosi 1. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Niech $n_i = 6k_i + 4$ dla $i \\in \\{1, 2, 3\\}$ ($k_i \\in \\mathbb{N}$). Kwadrat każdej z liczb to:</p>
$$n_i^2 = (6k_i + 4)^2 = 36k_i^2 + 48k_i + 16$$
<p>Dodajemy kwadraty trzech takich liczb:</p>
$$S = (36k_1^2 + 48k_1 + 16) + (36k_2^2 + 48k_2 + 16) + (36k_3^2 + 48k_3 + 16)$$
$$S = 36(k_1^2 + k_2^2 + k_3^2) + 48(k_1 + k_2 + k_3) + 48$$
<p>Wyłączamy 12 przed nawias:</p>
$$S = 12 \\cdot \\left[ 3(k_1^2 + k_2^2 + k_3^2) + 4(k_1 + k_2 + k_3) + 4 \\right]$$
<p>Wyrażenie w nawiasie jest całkowite, zatem suma kwadratów dzieli się przez 12. $c.n.d.$</p>
""",
        "answer": "a) $n^2 = 6m + 1 \\implies$ reszta 1; b) $S = 12 \\cdot [\\dots] \\implies 12 \\mid S$."
    },
    {
        "id": "p41-zad-1",
        "number": "Zadanie 1 / 4.1",
        "title": "Dwie liczby podzielne przez 3: różnica kwadratów i suma sześcianów",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """Dane są dwie liczby naturalne, obie podzielne przez 3.<br>
<strong>a)</strong> Udowodnij, że różnica kwadratów tych liczb jest podzielna przez 9.<br>
<strong>b)</strong> Udowodnij, że suma sześcianów tych liczb jest podzielna przez 27.""",
        "hint": "Niech $a = 3k$ oraz $b = 3m$, gdzie $k, m \\in \\mathbb{N}$.",
        "solution": """
<p><strong>Założenie:</strong> $a = 3k$, $b = 3m$ ($k, m \\in \\mathbb{N}$).</p>
<p><strong>Podpunkt a):</strong></p>
$$a^2 - b^2 = (3k)^2 - (3m)^2 = 9k^2 - 9m^2 = 9(k^2 - m^2)$$
<p>Ponieważ $k^2 - m^2 \\in \\mathbb{C}$, różnica ta dzieli się przez 9. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$a^3 + b^3 = (3k)^3 + (3m)^3 = 27k^3 + 27m^3 = 27(k^3 + m^3)$$
<p>Ponieważ $k^3 + m^3 \\in \\mathbb{N}$, suma sześcianów dzieli się przez 27. $c.n.d.$</p>
""",
        "answer": "a) $a^2 - b^2 = 9(k^2 - m^2)$; b) $a^3 + b^3 = 27(k^3 + m^3)$."
    },
    {
        "id": "p41-zad-2",
        "number": "Zadanie 2 / 4.1",
        "title": "Iloczyn 3 kolejnych liczb o pierwszej parzystej",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": "Wykaż, że iloczyn trzech kolejnych liczb naturalnych, z których pierwsza jest parzysta, jest podzielny przez 24.",
        "hint": "Zapisz liczby jako $2k, 2k+1, 2k+2 = 2(k+1)$. Zbadaj podzielność przez 8 oraz przez 3.",
        "solution": """
<p><strong>Założenie:</strong> Pierwsza liczba jest parzysta, więc trzy kolejne liczby to $2k, 2k + 1, 2k + 2$ dla $k \\in \\mathbb{N}$.</p>
<p><strong>Krok 1:</strong> Zapisujemy iloczyn:</p>
$$I = 2k(2k + 1)(2k + 2) = 2k(2k + 1) \\cdot 2(k + 1) = 4k(k + 1)(2k + 1)$$
<p><strong>Krok 2:</strong> Podzielność przez 8:</p>
<p>Liczby $k$ i $k + 1$ to dwie kolejne liczby całkowite, więc co najmniej jedna z nich jest parzysta: $k(k + 1) = 2m$. Wtedy:</p>
$$4k(k + 1) = 4 \\cdot 2m = 8m$$
<p><strong>Krok 3:</strong> Podzielność przez 3:</p>
<p>Wśród trzech kolejnych liczb naturalnych $2k, 2k + 1, 2k + 2$ dokładnie jedna jest podzielna przez 3.</p>
<p><strong>Wniosek:</strong> Iloczyn dzieli się przez 8 oraz przez 3, a ponieważ $\\operatorname{NWD}(8, 3) = 1$, iloczyn dzieli się przez $8 \\cdot 3 = 24$. $c.n.d.$</p>
""",
        "answer": "$8 \\mid I$ oraz $3 \\mid I \\implies 24 \\mid I$."
    },
    {
        "id": "p41-zad-3",
        "number": "Zadanie 3 / 4.1",
        "title": "Sumy liczb o stałych resztach z dzielenia",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Dane są trzy liczby naturalne takie, że reszta z dzielenia każdej z nich przez 3 jest równa 2. Udowodnij, że suma tych liczb jest podzielna przez 3.<br>
<strong>b)</strong> Dane są trzy liczby naturalne takie, że reszta z dzielenia każdej z nich przez 6 jest równa 4. Udowodnij, że suma tych liczb jest podzielna przez 6.""",
        "hint": "Zapisz $a = 3k_1 + 2, b = 3k_2 + 2, c = 3k_3 + 2$ i zsumuj.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<p>Niech liczbami będą $3k_1 + 2, 3k_2 + 2, 3k_3 + 2$ ($k_i \\in \\mathbb{N}$). Ich suma:</p>
$$S = 3k_1 + 2 + 3k_2 + 2 + 3k_3 + 2 = 3(k_1 + k_2 + k_3) + 6 = 3(k_1 + k_2 + k_3 + 2)$$
<p>Wyrażenie w nawiasie jest całkowite, zatem $S$ dzieli się przez 3. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Niech liczbami będą $6k_1 + 4, 6k_2 + 4, 6k_3 + 4$ ($k_i \\in \\mathbb{N}$). Ich suma:</p>
$$S = 6k_1 + 4 + 6k_2 + 4 + 6k_3 + 4 = 6(k_1 + k_2 + k_3) + 12 = 6(k_1 + k_2 + k_3 + 2)$$
<p>Liczba ta dzieli się przez 6. $c.n.d.$</p>
""",
        "answer": "a) $S = 3(k_1+k_2+k_3+2)$; b) $S = 6(k_1+k_2+k_3+2)$."
    },
    {
        "id": "p41-zad-4",
        "number": "Zadanie 4 / 4.1",
        "title": "Podzielność sum potęg dla $n > 0$",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """Udowodnij, że dla każdej liczby naturalnej $n > 0$:<br>
<strong>a)</strong> liczba $3^{n+1} + 3^n + 3^{n-1}$ jest podzielna przez 13,<br>
<strong>b)</strong> liczba $8^{2n-1} + 4^{3n-1}$ jest podzielna przez 24.""",
        "hint": "W a) wyłącz $3^{n-1}$. W b) sprowadź obie potęgi do wspólnej podstawy 2.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$L = 3^{n+1} + 3^n + 3^{n-1} = 3^{n-1}(3^2 + 3^1 + 1) = 3^{n-1}(9 + 3 + 1) = 13 \\cdot 3^{n-1}$$
<p>Dla $n \\ge 1$ liczba $3^{n-1}$ jest całkowita, zatem $L$ dzieli się przez 13. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Sprowadzamy do potęg liczby 2:</p>
$$8^{2n-1} = (2^3)^{2n-1} = 2^{6n-3}$$
$$4^{3n-1} = (2^2)^{3n-1} = 2^{6n-2}$$
<p>Sumujemy:</p>
$$L = 2^{6n-3} + 2^{6n-2} = 2^{6n-3}(1 + 2) = 3 \\cdot 2^{6n-3}$$
<p>Ponieważ $n \\ge 1$, to wykładnik $6n - 3 \\ge 3$, więc możemy wyłączyć $2^3 = 8$:</p>
$$L = 3 \\cdot 2^3 \\cdot 2^{6n-6} = 24 \\cdot 2^{6n-6}$$
<p>Dla $n \\ge 1$ liczba $6n - 6 \\ge 0$, więc $2^{6n-6} \\in \\mathbb{N}$. Zatem $L$ dzieli się przez 24. $c.n.d.$</p>
""",
        "answer": "a) $L = 13 \\cdot 3^{n-1}$; b) $L = 24 \\cdot 2^{6n-6}$."
    },
    {
        "id": "p41-zad-5",
        "number": "Zadanie 5 / 4.1",
        "title": "Ułamki algebraiczne jako liczby naturalne",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Wykaż, że dla każdej liczby naturalnej $n$ liczba $\\frac{n^4}{4} + \\frac{n^3}{2} + \\frac{n^2}{4}$ jest naturalna.<br>
<strong>b)</strong> Wykaż, że dla każdej nieparzystej liczby naturalnej $n$ liczba $\\frac{n^3}{8} - \\frac{n}{8}$ jest naturalna.""",
        "hint": "Sprowadź do wspólnego mianownika i zwiń licznik ze wzorów skróconego mnożenia.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$W = \\frac{n^4 + 2n^3 + n^2}{4} = \\frac{n^2(n^2 + 2n + 1)}{4} = \\frac{n^2(n+1)^2}{4} = \\left( \\frac{n(n+1)}{2} \\right)^2$$
<p>Liczba $n(n+1)$ to iloczyn dwóch kolejnych liczb całkowitych, więc jest parzysta. Stąd $\\frac{n(n+1)}{2} = k \\in \\mathbb{N}$.</p>
$$W = k^2 \\in \\mathbb{N}$$
<p>co kończy dowód. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$W = \\frac{n^3 - n}{8} = \\frac{n(n^2 - 1)}{8} = \\frac{(n - 1)n(n + 1)}{8}$$
<p>Skoro $n$ jest liczbą nieparzystą, to $n = 2k + 1$ ($k \\in \\mathbb{N}$). Wtedy $n - 1 = 2k$ oraz $n + 1 = 2(k + 1)$:</p>
$$(n - 1)n(n + 1) = 2k \\cdot (2k + 1) \\cdot 2(k + 1) = 4k(k + 1)(2k + 1)$$
<p>Ponieważ $k(k + 1)$ jest iloczynem dwóch kolejnych liczb, jest parzysty: $k(k + 1) = 2m$. Licznik wynosi $4 \\cdot 2m \\cdot (2k + 1) = 8m(2k + 1)$. Dzieląc przez 8:</p>
$$W = \\frac{8m(2k + 1)}{8} = m(2k + 1) \\in \\mathbb{N}$$
""",
        "answer": "a) $W = [n(n+1)/2]^2 \\in \\mathbb{N}$; b) $W = m(2k+1) \\in \\mathbb{N}$."
    },
    {
        "id": "p41-zad-6",
        "number": "Zadanie 6 / 4.1",
        "title": "Podzielność przez 5 i reszty",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Udowodnij, że jeśli reszta z dzielenia liczby naturalnej $n$ przez 5 jest równa 4, to liczba $n^2 - 1$ jest podzielna przez 5.<br>
<strong>b)</strong> Udowodnij, że jeśli liczba naturalna $n$ nie jest podzielna przez 5, to jedna z liczb $n^2 - 1$ lub $n^2 + 1$ jest podzielna przez 5.""",
        "hint": "W punkcie b) sprawdź możliwe reszty z dzielenia przez 5: $r \\in \\{1, 2, 3, 4\\}$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<p>Skoro $n = 5k + 4$ ($k \\in \\mathbb{N}$), to:</p>
$$n^2 - 1 = (n - 1)(n + 1) = (5k + 3)(5k + 5) = 5(5k + 3)(k + 1)$$
<p>Liczba ta jest podzielna przez 5. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Liczba $n$ nie dzieli się przez 5, więc daje resztę $r \\in \\{1, 2, 3, 4\\}$:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Dla $r = 1$: $n^2 \\equiv 1^2 = 1 \\pmod 5 \\implies n^2 - 1 \\equiv 0 \\pmod 5$ (dzieli się $n^2 - 1$).</li>
  <li>Dla $r = 2$: $n^2 \\equiv 2^2 = 4 \\pmod 5 \\implies n^2 + 1 \\equiv 4 + 1 = 5 \\equiv 0 \\pmod 5$ (dzieli się $n^2 + 1$).</li>
  <li>Dla $r = 3$: $n^2 \\equiv 3^2 = 9 \\equiv 4 \\pmod 5 \\implies n^2 + 1 \\equiv 5 \\equiv 0 \\pmod 5$ (dzieli się $n^2 + 1$).</li>
  <li>Dla $r = 4$: $n^2 \\equiv 4^2 = 16 \\equiv 1 \\pmod 5 \\implies n^2 - 1 \\equiv 0 \\pmod 5$ (dzieli się $n^2 - 1$).</li>
</ul>
<p>Zatem w każdym przypadku co najmniej jedna z liczb $n^2 - 1$ lub $n^2 + 1$ dzieli się przez 5. $c.n.d.$</p>
""",
        "answer": "Dla reszt 1 i 4 dzieli się $n^2 - 1$, dla reszt 2 i 3 dzieli się $n^2 + 1$."
    },
    {
        "id": "p41-zad-7",
        "number": "Zadanie 7 / 4.1",
        "title": "Kwadraty liczb niepodzielnych przez 3",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Wykaż, że jeśli liczba naturalna $n$ nie jest podzielna przez 3, to reszta z dzielenia liczby $n^2$ przez 3 jest równa 1.<br>
<strong>b)</strong> Wykaż, że suma kwadratów trzech liczb naturalnych niepodzielnych przez 3 jest podzielna przez 3.""",
        "hint": "Rozpatrz $n = 3k+1$ oraz $n = 3k+2$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<ul class="list-disc pl-5 space-y-1">
  <li>Dla $n = 3k + 1$: $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$, reszta 1.</li>
  <li>Dla $n = 3k + 2$: $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$, reszta 1.</li>
</ul>
<p>W obu przypadkach reszta z dzielenia $n^2$ przez 3 jest równa 1. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Niech $a, b, c$ będą liczbami naturalnymi niepodzielnymi przez 3. Z podpunktu a) ich kwadraty dają resztę 1:</p>
$$a^2 = 3k_1 + 1, \\quad b^2 = 3k_2 + 1, \\quad c^2 = 3k_3 + 1$$
$$a^2 + b^2 + c^2 = (3k_1 + 1) + (3k_2 + 1) + (3k_3 + 1) = 3(k_1 + k_2 + k_3) + 3 = 3(k_1 + k_2 + k_3 + 1)$$
<p>Liczba ta dzieli się przez 3. $c.n.d.$</p>
""",
        "answer": "a) $n^2 = 3m + 1$; b) $a^2 + b^2 + c^2 = 3(k_1+k_2+k_3+1)$."
    },
    {
        "id": "p41-zad-8",
        "number": "Zadanie 8 / 4.1",
        "title": "Brak podzielności przez 4 oraz przez 3",
        "category": "podrecznik-41",
        "category_label": "Podręcznik 4.1 (Podzielność)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla żadnej liczby naturalnej $n$ liczba:<br>
<strong>a)</strong> $n^2 + 6n + 2$ nie jest podzielna przez 4,<br>
<strong>b)</strong> $n^2 + n + 2$ nie jest podzielna przez 3.""",
        "hint": "Zbadaj reszty z dzielenia kwadratu liczby naturalnej.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<ul class="list-disc pl-5 space-y-1">
  <li>Dla $n$ parzystego ($n = 2k$):
    $$n^2 + 6n + 2 = 4k^2 + 12k + 2 = 4(k^2 + 3k) + 2$$
    Reszta z dzielenia przez 4 wynosi 2 (brak podzielności).</li>
  <li>Dla $n$ nieparzystego ($n = 2k + 1$):
    $$n^2 + 6n + 2 = (4k^2 + 4k + 1) + 6(2k + 1) + 2 = 4k^2 + 16k + 9 = 4(k^2 + 4k + 2) + 1$$
    Reszta z dzielenia przez 4 wynosi 1 (brak podzielności).</li>
</ul>
<p>W żadnym przypadku liczba nie dzieli się przez 4. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Zauważmy, że $n^2 + n + 2 = n(n + 1) + 2$. Iloczyn dwóch kolejnych liczb $n(n + 1)$ może dawać resztę 0 lub 2 z dzielenia przez 3:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Dla $n = 3k$: $n(n+1) + 2 = 3k(3k+1) + 2 \\equiv 2 \\pmod 3$.</li>
  <li>Dla $n = 3k + 1$: $(3k+1)(3k+2) + 2 = 9k^2 + 9k + 4 = 3(3k^2 + 3k + 1) + 1 \\equiv 1 \\pmod 3$.</li>
  <li>Dla $n = 3k + 2$: $(3k+2)(3k+3) + 2 = 3(3k+2)(k+1) + 2 \\equiv 2 \\pmod 3$.</li>
</ul>
<p>W żadnym wypadku reszta nie jest równa 0, co oznacza brak podzielności przez 3. $c.n.d.$</p>
""",
        "answer": "a) reszty to 2 lub 1; b) reszty to 1 lub 2 $\\implies$ brak podzielności."
    },

    # ==========================================
    # TEMAT 4.2: Dowody w algebrze (2)
    # ==========================================
    {
        "id": "p42-cw-1",
        "number": "Ćwiczenie 1 / 4.2",
        "title": "Nierówności sumy odwrotności $a/b + b/a$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Wykaż, że dla dowolnych liczb rzeczywistych $a, b$ takich, że $ab > 0$, prawdziwa jest nierówność $\\frac{a}{b} + \\frac{b}{a} \\ge 2$.<br>
<strong>b)</strong> Wykaż, że dla dowolnych liczb rzeczywistych $a, b$ takich, że $ab < 0$, prawdziwa jest nierówność $\\frac{a}{b} + \\frac{b}{a} \\le -2$.""",
        "hint": "Sprowadź do wspólnego mianownika i zwiń licznik do kwadratu różnicy $(a-b)^2$ lub sumy $(a+b)^2$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$\\frac{a}{b} + \\frac{b}{a} - 2 = \\frac{a^2 + b^2 - 2ab}{ab} = \\frac{(a - b)^2}{ab}$$
<p>Ponieważ $(a - b)^2 \\ge 0$ dla $a, b \\in \\mathbb{R}$, a z założenia $ab > 0$, to iloraz $\\frac{(a - b)^2}{ab} \\ge 0$, skąd $\\frac{a}{b} + \\frac{b}{a} \\ge 2$. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$\\frac{a}{b} + \\frac{b}{a} + 2 = \\frac{a^2 + b^2 + 2ab}{ab} = \\frac{(a + b)^2}{ab}$$
<p>Licznik $(a + b)^2 \\ge 0$, a mianownik z założenia $ab < 0$. Iloraz liczby nieujemnej i ujemnej jest niedodatni ($\\le 0$):</p>
$$\\frac{(a + b)^2}{ab} \\le 0 \\iff \\frac{a}{b} + \\frac{b}{a} \\le -2$$
<p>co kończy dowód. $c.n.d.$</p>
""",
        "answer": "a) $\\frac{(a-b)^2}{ab} \\ge 0$; b) $\\frac{(a+b)^2}{ab} \\le 0$."
    },
    {
        "id": "p42-cw-2",
        "number": "Ćwiczenie 2 / 4.2",
        "title": "Nierówności $a^2 \\ge 4b(a-b)$ oraz $a(6b-7a) \\le 2(b-a)(b+a)$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla dowolnych liczb rzeczywistych $a, b$ prawdziwa jest nierówność:<br>
<strong>a)</strong> $a^2 \\ge 4b(a - b)$,<br>
<strong>b)</strong> $a(6b - 7a) \\le 2(b - a)(b + a)$.""",
        "hint": "Przenieś wszystko na jedną stronę i zwiń w sumę kwadratów: w b) $5a^2 - 6ab + 2b^2 = (2a-b)^2 + (a-b)^2$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$a^2 - 4b(a - b) = a^2 - 4ab + 4b^2 = (a - 2b)^2 \\ge 0$$
<p>Kwadrat dowolnej liczby rzeczywistej jest nieujemny, więc nierówność jest prawdziwa. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$a(6b - 7a) \\le 2(b^2 - a^2)$$
$$6ab - 7a^2 \\le 2b^2 - 2a^2$$
<p>Przenosimy wszystko na prawą stronę:</p>
$$0 \\le 2b^2 - 2a^2 - 6ab + 7a^2$$
$$0 \\le 5a^2 - 6ab + 2b^2$$
<p>Rozpisujemy jako sumę dwóch kwadratów:</p>
$$5a^2 - 6ab + 2b^2 = (4a^2 - 4ab + b^2) + (a^2 - 2ab + b^2) = (2a - b)^2 + (a - b)^2$$
<p>Ponieważ $(2a - b)^2 \\ge 0$ oraz $(a - b)^2 \\ge 0$, ich suma jest zawsze $\\ge 0$. To kończy dowód. $c.n.d.$</p>
""",
        "answer": "a) $(a - 2b)^2 \\ge 0$; b) $(2a - b)^2 + (a - b)^2 \\ge 0$."
    },
    {
        "id": "p42-cw-3",
        "number": "Ćwiczenie 3 / 4.2",
        "title": "Nierówności stopnia 4 dla dowolnego $x \\in \\mathbb{R}$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Udowodnij, że podana nierówność jest prawdziwa dla dowolnej liczby rzeczywistej $x$:<br>
<strong>a)</strong> $x^4 - 2x + 2 > x^2 + 4x - 8$,<br>
<strong>b)</strong> $x^4 - 4x^2 + 5 > 4x - 12$.""",
        "hint": "Przenieś na jedną stronę i rozbij na sumę kwadratów.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$x^4 - x^2 - 6x + 10 > 0$$
<p>Dopełniamy do pełnych kwadratów:</p>
$$x^4 - x^2 - 6x + 10 = (x^4 - 2x^2 + 1) + (x^2 - 6x + 9) = (x^2 - 1)^2 + (x - 3)^2$$
<p>Kwadraty $(x^2 - 1)^2 \\ge 0$ i $(x - 3)^2 \\ge 0$. Mogłyby sumować się do zera tylko wtedy, gdyby jednocześnie $x^2 - 1 = 0$ ($x = \\pm 1$) oraz $x - 3 = 0$ ($x = 3$). Ponieważ warunki te są sprzeczne, suma ta jest zawsze ostro dodatnia ($> 0$). $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$x^4 - 4x^2 - 4x + 17 > 0$$
<p>Zauważmy tożsamość:</p>
$$4(x^4 - 4x^2 - 4x + 17) = 4x^4 - 16x^2 - 16x + 68 = (2x^2 - 5)^2 + 4(x - 2)^2 + 27$$
<p>Sprawdzenie: $(4x^4 - 20x^2 + 25) + (4x^2 - 16x + 16) + 27 = 4x^4 - 16x^2 - 16x + 68$.</p>
<p>Suma dwóch kwadratów powiększona o dodatnią liczbę 27 jest zawsze ostro dodatnia: $(2x^2 - 5)^2 + 4(x - 2)^2 + 27 \\ge 27 > 0$. Dzieląc przez 4, otrzymujemy $x^4 - 4x^2 - 4x + 17 > 0$. $c.n.d.$</p>
""",
        "answer": "a) $(x^2 - 1)^2 + (x - 3)^2 > 0$; b) $(2x^2 - 5)^2 + 4(x - 2)^2 + 27 > 0$."
    },
    {
        "id": "p42-cw-4",
        "number": "Ćwiczenie 4 / 4.2",
        "title": "Nierówności dwóch zmiennych z pełnymi kwadratami",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla dowolnych liczb rzeczywistych $x, y$ prawdziwa jest nierówność:<br>
<strong>a)</strong> $x^2 + 10y^2 + 9 \\ge 6y(x + 1)$,<br>
<strong>b)</strong> $3x^2 + y^2 - 2xy \\ge 2x - \\frac{1}{2}$.""",
        "hint": "Przenieś na lewą stronę i pogrupuj w pełne kwadraty.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$x^2 + 10y^2 + 9 - 6xy - 6y \\ge 0$$
$$(x^2 - 6xy + 9y^2) + (y^2 - 6y + 9) \\ge 0$$
$$(x - 3y)^2 + (y - 3)^2 \\ge 0$$
<p>Suma kwadratów liczb rzeczywistych jest zawsze nieujemna. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$3x^2 + y^2 - 2xy - 2x + \\frac{1}{2} \\ge 0$$
<p>Rozbijamy $3x^2 = x^2 + 2x^2$:</p>
$$(x^2 - 2xy + y^2) + \\left(2x^2 - 2x + \\frac{1}{2}\\right) = (x - y)^2 + 2\\left(x^2 - x + \\frac{1}{4}\\right) = (x - y)^2 + 2\\left(x - \\frac{1}{2}\\right)^2$$
<p>Oba składniki są nieujemne, więc ich suma jest $\\ge 0$. $c.n.d.$</p>
""",
        "answer": "a) $(x - 3y)^2 + (y - 3)^2 \\ge 0$; b) $(x - y)^2 + 2(x - 1/2)^2 \\ge 0$."
    },
    {
        "id": "p42-zad-1",
        "number": "Zadanie 1 / 4.2",
        "title": "Nierówności dla dowolnej liczby $x > 0$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla dowolnej liczby $x > 0$ prawdziwa jest nierówność:<br>
<strong>a)</strong> $x + \\frac{4}{x} \\ge 4$,<br>
<strong>b)</strong> $4 + \\frac{1}{x} \\ge \\frac{4}{\\sqrt{x}}$,<br>
<strong>c)</strong> \\frac{1}{x} + \\frac{9}{x^3} \\ge \\frac{6}{x^2}.""",
        "hint": "W każdym podpunkcie sprowadź do wspólnego mianownika lub pomnóż przez mianownik (skoro $x > 0$).",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$x + \\frac{4}{x} - 4 = \\frac{x^2 - 4x + 4}{x} = \\frac{(x - 2)^2}{x}$$
<p>Dla $x > 0$ licznik $(x - 2)^2 \\ge 0$, a mianownik $x > 0$, więc ułamek jest $\\ge 0$. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$4 - \\frac{4}{\\sqrt{x}} + \\frac{1}{x} = \\left( 2 - \\frac{1}{\\sqrt{x}} \\right)^2 \\ge 0$$
<p>Kwadrat dowolnego wyrażenia rzeczywistego jest nieujemny. $c.n.d.$</p>
<p><strong>Podpunkt c):</strong></p>
<p>Mnożymy obie strony przez $x^3 > 0$:</p>
$$x^2 + 9 \\ge 6x \\iff x^2 - 6x + 9 \\ge 0 \\iff (x - 3)^2 \\ge 0$$
<p>Nierówność jest zawsze prawdziwa dla $x > 0$. $c.n.d.$</p>
""",
        "answer": "a) $\\frac{(x-2)^2}{x} \\ge 0$; b) $(2 - 1/\\sqrt{x})^2 \\ge 0$; c) $(x - 3)^2 \\ge 0$."
    },
    {
        "id": "p42-zad-2",
        "number": "Zadanie 2 / 4.2",
        "title": "Nierówności dla dowolnych liczb dodatnich $a, b$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla dowolnych dodatnich liczb $a$ i $b$ prawdziwa jest nierówność:<br>
<strong>a)</strong> $\\frac{(a+b)^2}{ab} \\ge 4$,<br>
<strong>b)</strong> $\\frac{a^2}{b} + \\frac{b^2}{a} \\ge a + b$,<br>
<strong>c)</strong> $\\frac{4}{a+b} \\le \\frac{1}{a} + \\frac{1}{b}$.""",
        "hint": "Wykorzystaj fakt, że $(a - b)^2 \\ge 0$ dla dowolnych liczb rzeczywistych.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$\\frac{(a+b)^2}{ab} - 4 = \\frac{a^2 + 2ab + b^2 - 4ab}{ab} = \\frac{(a - b)^2}{ab}$$
<p>Dla $a, b > 0$ iloczyn $ab > 0$, zatem ułamek jest $\\ge 0$. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$\\frac{a^3 + b^3}{ab} \\ge a + b \\iff a^3 + b^3 \\ge ab(a + b)$$
$$(a + b)(a^2 - ab + b^2) - ab(a + b) \\ge 0 \\iff (a + b)(a^2 - 2ab + b^2) \\ge 0 \\iff (a + b)(a - b)^2 \\ge 0$$
<p>Dla $a, b > 0$ mamy $a + b > 0$ oraz $(a - b)^2 \\ge 0$, więc nierówność zachodzi. $c.n.d.$</p>
<p><strong>Podpunkt c):</strong></p>
$$\\frac{1}{a} + \\frac{1}{b} = \\frac{a + b}{ab}$$
$$\\frac{a + b}{ab} \\ge \\frac{4}{a + b} \\iff (a + b)^2 \\ge 4ab \\iff (a - b)^2 \\ge 0$$
<p>co jest zawsze prawdziwe. $c.n.d.$</p>
""",
        "answer": "Wszystkie podpunkty sprowadzają się do $(a - b)^2 \\ge 0$ dla $a, b > 0$."
    },
    {
        "id": "p42-zad-3",
        "number": "Zadanie 3 / 4.2",
        "title": "Nierówności dwóch zmiennych stopnia drugiego",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Udowodnij, że dla dowolnych liczb rzeczywistych $x, y$ prawdziwa jest nierówność:<br>
<strong>a)</strong> $(x - y)^2 + 2x^2 + 8 \\ge 4x(2 - y)$,<br>
<strong>b)</strong> $(x + 2)(x + 3) + 1 > (1 - y)(x + y + 1)$.""",
        "hint": "Wymnóż nawiasy i pogrupuj w pełne kwadraty.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$x^2 - 2xy + y^2 + 2x^2 + 8 - 8x + 4xy \\ge 0$$
$$3x^2 + 2xy + y^2 - 8x + 8 \\ge 0$$
<p>Grupujemy:</p>
$$(x^2 + 2xy + y^2) + (2x^2 - 8x + 8) = (x + y)^2 + 2(x - 2)^2 \\ge 0$$
<p>Oba składniki są nieujemne, więc nierówność jest prawdziwa. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
<p>Wymnażamy obie strony:</p>
$$L = x^2 + 5x + 6 + 1 = x^2 + 5x + 7$$
$$P = x + y + 1 - xy - y^2 - y = x + 1 - xy - y^2$$
$$L - P = x^2 + 4x + 6 + xy + y^2 = x^2 + (y + 4)x + (y^2 + 6)$$
<p>Traktujemy jako trójmian kwadratowy zmiennej $x$. Wyróżnik $\\Delta_x$ wynosi:</p>
$$\\Delta_x = (y + 4)^2 - 4(y^2 + 6) = y^2 + 8y + 16 - 4y^2 - 24 = -3y^2 + 8y - 8$$
<p>Badamy wyróżnik tego trójmianu względem $y$:</p>
$$\\Delta_y = 64 - 4(-3)(-8) = 64 - 96 = -32 < 0$$
<p>Ponieważ współczynnik przy $y^2$ wynosi $-3 < 0$, a $\\Delta_y < 0$, to $\\Delta_x < 0$ dla każdego $y \\in \\mathbb{R}$.</p>
<p>Wobec tego trójmian zmiennej $x$ ma dodatni współczynnik wiodący ($1 > 0$) i ujemny wyróżnik, co oznacza, że przyjmuje wyłącznie wartości ściśle dodatnie ($> 0$). $c.n.d.$</p>
""",
        "answer": "a) $(x + y)^2 + 2(x - 2)^2 \\ge 0$; b) $\\Delta_x = -3y^2 + 8y - 8 < 0 \\implies L - P > 0$."
    },
    {
        "id": "p42-zad-4",
        "number": "Zadanie 4 / 4.2",
        "title": "Klasyczne tożsamości sumy kwadratów",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Udowodnij, że dla dowolnych liczb rzeczywistych $x, y$ prawdziwa jest nierówność:<br>
<strong>a)</strong> $x^2 + y^2 - x(y + 1) \\ge y - 1$,<br>
<strong>b)</strong> $2x^2 y^2 + x^2 + y^2 \\ge 6xy - 2$.""",
        "hint": "W punkcie a) pomnóż przez 2 i zwiń w 3 kwadraty: $(x-y)^2 + (x-1)^2 + (y-1)^2$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$x^2 + y^2 - xy - x - y + 1 \\ge 0$$
<p>Mnożymy obie strony przez 2:</p>
$$2x^2 + 2y^2 - 2xy - 2x - 2y + 2 \\ge 0$$
$$(x^2 - 2xy + y^2) + (x^2 - 2x + 1) + (y^2 - 2y + 1) \\ge 0$$
$$(x - y)^2 + (x - 1)^2 + (y - 1)^2 \\ge 0$$
<p>Suma trzech kwadratów liczb rzeczywistych jest zawsze nieujemna. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$2x^2 y^2 - 4xy + 2 + x^2 - 2xy + y^2 \\ge 0$$
$$2(x^2 y^2 - 2xy + 1) + (x^2 - 2xy + y^2) \\ge 0$$
$$2(xy - 1)^2 + (x - y)^2 \\ge 0$$
<p>Oba składniki są kwadratami, zatem ich suma jest nieujemna. $c.n.d.$</p>
""",
        "answer": "a) $(x - y)^2 + (x - 1)^2 + (y - 1)^2 \\ge 0$; b) $2(xy - 1)^2 + (x - y)^2 \\ge 0$."
    },
    {
        "id": "p42-zad-5",
        "number": "Zadanie 5 / 4.2",
        "title": "Nierówności warunkowe z $a + b = 1/2$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Udowodnij, że dla dowolnych liczb dodatnich $a$ i $b$ takich, że $a + b = \\frac{1}{2}$, prawdziwa jest podana nierówność:<br>
<strong>a)</strong> $ab \\le \\frac{1}{16}$,<br>
<strong>b)</strong> $\\frac{1}{a} + \\frac{1}{b} \\ge 8$,<br>
<strong>c)</strong> $\\frac{1}{2ab} - 4a \\ge 6 + 4b$.""",
        "hint": "Skorzystaj ze średniej arytmetycznej i geometrycznej: $\\sqrt{ab} \\le \\frac{a+b}{2}$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<p>Ze związku między średnią arytmetyczną i geometryczną:</p>
$$\\sqrt{ab} \\le \\frac{a + b}{2} = \\frac{1/2}{2} = \\frac{1}{4}$$
<p>Podnosząc obustronnie do kwadratu (dla liczb dodatnich):</p>
$$ab \\le \\frac{1}{16}$$
<p>co kończy dowód podpunktu a. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$\\frac{1}{a} + \\frac{1}{b} = \\frac{a + b}{ab} = \\frac{1/2}{ab}$$
<p>Skoro z podpunktu a) $ab \\le \\frac{1}{16}$, to $\\frac{1}{ab} \\ge 16$. Zatem:</p>
$$\\frac{1/2}{ab} \\ge \\frac{1}{2} \\cdot 16 = 8$$
<p>co dowodzi podpunktu b. $c.n.d.$</p>
<p><strong>Podpunkt c):</strong></p>
$$\\frac{1}{2ab} \\ge 4a + 4b + 6 = 4(a + b) + 6$$
<p>Podstawiamy $a + b = \\frac{1}{2}$:</p>
$$4 \\cdot \\frac{1}{2} + 6 = 2 + 6 = 8$$
$$\\frac{1}{2ab} \\ge 8 \\iff \\frac{1}{ab} \\ge 16 \\iff ab \\le \\frac{1}{16}$$
<p>A to jest prawdziwe na mocy podpunktu a. $c.n.d.$</p>
""",
        "answer": "Wszystkie nierówności wynikają z oszacowania $ab \\le 1/16$."
    },
    {
        "id": "p42-zad-6",
        "number": "Zadanie 6 / 4.2",
        "title": "Nierówności z warunkami $ab = 4$ oraz $a + b = 1$",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Udowodnij, że dla dowolnych liczb dodatnich $a, b$ takich, że $ab = 4$, prawdziwa jest nierówność $a + b \\ge 4$.<br>
<strong>b)</strong> Udowodnij, że dla dowolnych liczb rzeczywistych $a, b$ takich, że $a + b = 1$, prawdziwa jest nierówność $a^3 + b^3 \\ge ab$.""",
        "hint": "W b) użyj wzoru na sumę sześcianów: $a^3 + b^3 = (a+b)(a^2 - ab + b^2) = (a+b)^2 - 3ab$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
<p>Dla $a, b > 0$ zachodzi nierówność między średnimi: $\\frac{a + b}{2} \\ge \\sqrt{ab}$.</p>
$$a + b \\ge 2\\sqrt{ab} = 2\\sqrt{4} = 2 \\cdot 2 = 4$$
<p>co kończy dowód. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$a^3 + b^3 = (a + b)(a^2 - ab + b^2) = 1 \\cdot ((a + b)^2 - 3ab) = 1 - 3ab$$
<p>Chcemy wykazać, że $1 - 3ab \\ge ab$:</p>
$$1 - 3ab \\ge ab \\iff 1 \\ge 4ab \\iff ab \\le \\frac{1}{4}$$
<p>Z nierówności $(a - b)^2 \\ge 0$ mamy:</p>
$$4ab \\le (a + b)^2 = 1^2 = 1 \\implies ab \\le \\frac{1}{4}$$
<p>Zatem nierówność $a^3 + b^3 \\ge ab$ jest zawsze spełniona. $c.n.d.$</p>
""",
        "answer": "a) $a + b \\ge 2\\sqrt{4} = 4$; b) $a^3 + b^3 = 1 - 3ab \\ge ab \\iff 4ab \\le 1$."
    },
    {
        "id": "p42-zad-7",
        "number": "Zadanie 7 / 4.2",
        "title": "Iloczyny $(1+a)(1+b)$ z warunkiem na iloczyn",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """Wykaż, że dla dowolnych liczb dodatnich $a, b$ takich, że:<br>
<strong>a)</strong> $ab = 16$, prawdziwa jest nierówność $(1 + a)(1 + b) \\ge 25$,<br>
<strong>b)</strong> $ab = \\frac{1}{4}$, prawdziwa jest nierówność $4(1 + a)(1 + b) \\ge 9$.""",
        "hint": "Wymnóż nawiasy $(1+a)(1+b) = 1 + a + b + ab$ i oszacuj sumę $a + b \\ge 2\\sqrt{ab}$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$(1 + a)(1 + b) = 1 + a + b + ab = 1 + 16 + a + b = 17 + (a + b)$$
<p>Dla liczb dodatnich $a + b \\ge 2\\sqrt{ab} = 2\\sqrt{16} = 8$. Zatem:</p>
$$(1 + a)(1 + b) \\ge 17 + 8 = 25$$
<p>co kończy dowód. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$4(1 + a)(1 + b) = 4(1 + a + b + ab) = 4\\left( 1 + \\frac{1}{4} + a + b \\right) = 4 \\cdot \\frac{5}{4} + 4(a + b) = 5 + 4(a + b)$$
<p>Dla $a, b > 0$: $a + b \\ge 2\\sqrt{ab} = 2\\sqrt{\\frac{1}{4}} = 2 \\cdot \\frac{1}{2} = 1$. Zatem:</p>
$$5 + 4(a + b) \\ge 5 + 4(1) = 9$$
<p>co kończy dowód. $c.n.d.$</p>
""",
        "answer": "a) $17 + a + b \\ge 17 + 8 = 25$; b) $5 + 4(a+b) \\ge 5 + 4 = 9$."
    },
    {
        "id": "p42-zad-8",
        "number": "Zadanie 8 / 4.2",
        "title": "Nierówności warunkowe: ilorazy i suma kwadratów równa 1",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": """<strong>a)</strong> Udowodnij, że dla dowolnych liczb rzeczywistych $a, b$ takich, że $a \\ge b > 0$, prawdziwa jest nierówność $b^2(a + 1) \\le a^2(b + 1)$.<br>
<strong>b)</strong> Udowodnij, że dla dowolnych liczb rzeczywistych $a \\neq 0$ i $b \\neq 0$ takich, że $a^2 + b^2 = 1$, prawdziwa jest nierówność $\\left(1 + \\frac{1}{a^2}\\right)\\left(1 + \\frac{1}{b^2}\\right) \\ge 9$.""",
        "hint": "W b) wymnóż nawiasy, zauważ $\\frac{1}{a^2} + \\frac{1}{b^2} = \\frac{a^2+b^2}{a^2 b^2} = \\frac{1}{a^2 b^2}$ oraz $a^2 b^2 \\le 1/4$.",
        "solution": """
<p><strong>Podpunkt a):</strong></p>
$$a^2(b + 1) - b^2(a + 1) = a^2b + a^2 - ab^2 - b^2 = (a^2 - b^2) + ab(a - b) = (a - b)(a + b) + ab(a - b) = (a - b)(a + b + ab)$$
<p>Z założeń $a \\ge b > 0$ wynika, że $a - b \\ge 0$ oraz $a + b + ab > 0$. Iloczyn liczb nieujemnej i dodatniej jest nieujemny ($\\ge 0$), stąd $a^2(b + 1) \\ge b^2(a + 1)$. $c.n.d.$</p>
<p><strong>Podpunkt b):</strong></p>
$$\\left(1 + \\frac{1}{a^2}\\right)\\left(1 + \\frac{1}{b^2}\\right) = 1 + \\frac{1}{a^2} + \\frac{1}{b^2} + \\frac{1}{a^2 b^2} = 1 + \\frac{a^2 + b^2}{a^2 b^2} + \\frac{1}{a^2 b^2}$$
<p>Ponieważ $a^2 + b^2 = 1$:</p>
$$= 1 + \\frac{1}{a^2 b^2} + \\frac{1}{a^2 b^2} = 1 + \\frac{2}{a^2 b^2}$$
<p>Z nierówności $(a^2 - b^2)^2 \\ge 0$ mamy:</p>
$$4a^2 b^2 \\le (a^2 + b^2)^2 = 1^2 = 1 \\implies a^2 b^2 \\le \\frac{1}{4} \\implies \\frac{1}{a^2 b^2} \\ge 4$$
<p>Wobec tego:</p>
$$1 + \\frac{2}{a^2 b^2} \\ge 1 + 2 \\cdot 4 = 9$$
<p>co kończy dowód. $c.n.d.$</p>
""",
        "answer": "a) $(a - b)(a + b + ab) \\ge 0$; b) $1 + 2/(a^2 b^2) \\ge 1 + 2 \\cdot 4 = 9$."
    },
    {
        "id": "p42-zad-9",
        "number": "Zadanie *9 / 4.2",
        "title": "Nierówność dla prostopadłościanu: suma krawędzi a przekątna",
        "category": "podrecznik-42",
        "category_label": "Podręcznik 4.2 (Nierówności)",
        "level": "rozszerzenie",
        "statement": "Dany jest prostopadłościan o krawędziach $a, b, c$ i przekątnej $d$. Wykaż, że $a + b + c \\le \\sqrt{3}d$.",
        "hint": "Przekątna prostopadłościanu wynosi $d^2 = a^2 + b^2 + c^2$. Zbadaj kwadrat sumy $(a + b + c)^2$ i skorzystaj z $(a-b)^2 + (b-c)^2 + (c-a)^2 \\ge 0$.",
        "solution": """
<p><strong>Założenie:</strong> $a, b, c > 0$ to długości krawędzi prostopadłościanu, a $d = \\sqrt{a^2 + b^2 + c^2} \\implies d^2 = a^2 + b^2 + c^2$.</p>
<p><strong>Krok 1:</strong> Rozwijamy kwadrat sumy krawędzi:</p>
$$(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)$$
<p><strong>Krok 2:</strong> Z tożsamości sumy kwadratów różnic:</p>
$$(a - b)^2 + (b - c)^2 + (c - a)^2 \\ge 0$$
$$(a^2 - 2ab + b^2) + (b^2 - 2bc + c^2) + (c^2 - 2ca + a^2) \\ge 0$$
$$2(a^2 + b^2 + c^2) - 2(ab + bc + ca) \\ge 0$$
$$2(ab + bc + ca) \\le 2(a^2 + b^2 + c^2)$$
<p><strong>Krok 3:</strong> Szacujemy kwadrat sumy:</p>
$$(a + b + c)^2 = (a^2 + b^2 + c^2) + 2(ab + bc + ca) \\le (a^2 + b^2 + c^2) + 2(a^2 + b^2 + c^2) = 3(a^2 + b^2 + c^2) = 3d^2$$
<p><strong>Krok 4:</strong> Ponieważ $a + b + c > 0$ oraz $d > 0$, możemy wyciągnąć pierwiastek kwadratowy z obu stron:</p>
$$a + b + c \\le \\sqrt{3}d$$
<p>co kończy dowód. $c.n.d.$</p>
""",
        "answer": "$(a + b + c)^2 \\le 3(a^2 + b^2 + c^2) = 3d^2 \\implies a + b + c \\le \\sqrt{3}d$."
    }
]
