# -*- coding: utf-8 -*-
"""
Zestaw 1: Zadania ze zbioru maturalnego (DOWÓD 35 – DOWÓD 68)
"""

TASKS_ZBIOR = [
    {
        "id": "dowod-35",
        "number": "DOWÓD 35",
        "title": "Suma pięciu kolejnych liczb nieparzystych",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że suma pięciu kolejnych liczb nieparzystych jest podzielna przez 5.",
        "hint": "Dowolną liczbę nieparzystą możemy zapisać w postaci $2n+1$ dla $n \\in \\mathbb{C}$. Kolejne liczby nieparzyste różnią się o 2.",
        "solution": """
<p><strong>Założenie:</strong> Niech $n \\in \\mathbb{C}$. Pięć kolejnych liczb nieparzystych możemy zapisać jako:</p>
$$2n + 1, \\quad 2n + 3, \\quad 2n + 5, \\quad 2n + 7, \\quad 2n + 9$$
<p><strong>Krok 1:</strong> Zapisujemy sumę tych liczb:</p>
$$S = (2n + 1) + (2n + 3) + (2n + 5) + (2n + 7) + (2n + 9)$$
<p><strong>Krok 2:</strong> Redukujemy wyrazy podobne:</p>
$$S = 10n + 25$$
<p><strong>Krok 3:</strong> Wyłączamy wspólny czynnik $5$ przed nawias:</p>
$$S = 5(2n + 5)$$
<p><strong>Wniosek:</strong> Ponieważ $n \\in \\mathbb{C}$, to wyrażenie $(2n + 5)$ jest liczbą całkowitą. Zatem suma $S$ jest iloczynem liczby 5 i liczby całkowitej, co oznacza, że jest podzielna przez 5. $c.n.d.$</p>
""",
        "answer": "$S = 5(2n + 5)$, gdzie $2n + 5 \\in \\mathbb{C}$, zatem $5 \\mid S$."
    },
    {
        "id": "dowod-36",
        "number": "DOWÓD 36",
        "title": "Suma czterech kolejnych liczb podzielnych przez 3",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że suma czterech kolejnych liczb podzielnych przez 3 jest podzielna przez 6.",
        "hint": "Kolejne liczby podzielne przez 3 różnią się o 3. Można je zapisać jako $3n, 3n+3, 3n+6, 3n+9$.",
        "solution": """
<p><strong>Założenie:</strong> Niech $n \\in \\mathbb{C}$. Cztery kolejne liczby podzielne przez 3 mają postać:</p>
$$3n, \\quad 3(n + 1), \\quad 3(n + 2), \\quad 3(n + 3)$$
<p><strong>Krok 1:</strong> Obliczamy sumę tych liczb:</p>
$$S = 3n + (3n + 3) + (3n + 6) + (3n + 9) = 12n + 18$$
<p><strong>Krok 2:</strong> Wyłączamy czynnik $6$ przed nawias:</p>
$$S = 6(2n + 3)$$
<p><strong>Wniosek:</strong> Dla $n \\in \\mathbb{C}$ wyrażenie $2n + 3$ jest liczbą całkowitą. Otrzymana postać $6k$ ($k \\in \\mathbb{C}$) dowodzi, że suma jest podzielna przez 6. $c.n.d.$</p>
""",
        "answer": "$S = 6(2n + 3)$, gdzie $2n + 3 \\in \\mathbb{C}$, zatem $6 \\mid S$."
    },
    {
        "id": "dowod-37",
        "number": "DOWÓD 37",
        "title": "Suma kwadratów trzech kolejnych liczb nieparzystych",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że suma kwadratów trzech kolejnych liczb nieparzystych powiększona o 1 jest podzielna przez 12.",
        "hint": "Trzy kolejne liczby nieparzyste najwygodniej zapisać symetrycznie: $2n - 1, 2n + 1, 2n + 3$ (dla $n \\in \\mathbb{C}$).",
        "solution": """
<p><strong>Założenie:</strong> Niech kolejnymi liczbami nieparzystymi będą $2n - 1, 2n + 1, 2n + 3$, gdzie $n \\in \\mathbb{C}$.</p>
<p><strong>Krok 1:</strong> Zapisujemy wyrażenie będące sumą ich kwadratów powiększoną o 1:</p>
$$W = (2n - 1)^2 + (2n + 1)^2 + (2n + 3)^2 + 1$$
<p><strong>Krok 2:</strong> Rozpisujemy kwadraty sumy i różnicy:</p>
$$W = (4n^2 - 4n + 1) + (4n^2 + 4n + 1) + (4n^2 + 12n + 9) + 1$$
<p><strong>Krok 3:</strong> Redukujemy wyrazy podobne:</p>
$$W = 12n^2 + 12n + 12 = 12(n^2 + n + 1)$$
<p><strong>Wniosek:</strong> Ponieważ $n \\in \\mathbb{C}$, to $n^2 + n + 1 \\in \\mathbb{C}$. Liczba $W$ jest wielokrotnością 12, więc dzieli się przez 12. $c.n.d.$</p>
""",
        "answer": "$W = 12(n^2 + n + 1)$, $n^2 + n + 1 \\in \\mathbb{C} \\implies 12 \\mid W$."
    },
    {
        "id": "dowod-38",
        "number": "DOWÓD 38",
        "title": "Suma kwadratów liczb różniących się o 7",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że suma kwadratów dwóch liczb całkowitych różniących się o siedem powiększona o 1 jest liczbą parzystą.",
        "hint": "Niech tymi liczbami będą $n$ oraz $n + 7$. Liczba parzysta to taka, którą można zapisać jako $2k$ dla $k \\in \\mathbb{C}$.",
        "solution": """
<p><strong>Założenie:</strong> Niech $n, n + 7 \\in \\mathbb{C}$.</p>
<p><strong>Krok 1:</strong> Wyznaczamy sumę kwadratów powiększoną o 1:</p>
$$W = n^2 + (n + 7)^2 + 1 = n^2 + n^2 + 14n + 49 + 1 = 2n^2 + 14n + 50$$
<p><strong>Krok 2:</strong> Wyłączamy 2 przed nawias:</p>
$$W = 2(n^2 + 7n + 25)$$
<p><strong>Wniosek:</strong> Dla dowolnego $n \\in \\mathbb{C}$, liczba $n^2 + 7n + 25$ jest liczbą całkowitą. Zatem $W$ jest liczbą parzystą. $c.n.d.$</p>
""",
        "answer": "$W = 2(n^2 + 7n + 25) \\implies W$ jest parzysta."
    },
    {
        "id": "dowod-39",
        "number": "DOWÓD 39",
        "title": "Podzielność wyrażenia $(4n+1)^2 - (4m-1)^2$ przez 8",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Udowodnij, że wyrażenie $(4n+1)^2 - (4m-1)^2$ jest podzielne przez 8, jeśli $m, n$ należą do liczb naturalnych.",
        "hint": "Rozwiń kwadraty lub skorzystaj ze wzoru na różnicę kwadratów $a^2 - b^2 = (a-b)(a+b)$.",
        "solution": """
<p><strong>Krok 1:</strong> Rozwijamy oba składniki ze wzorów skróconego mnożenia:</p>
$$(4n + 1)^2 - (4m - 1)^2 = (16n^2 + 8n + 1) - (16m^2 - 8m + 1)$$
<p><strong>Krok 2:</strong> Odejmujemy wyrażenia (jedynki się redukują):</p>
$$= 16n^2 - 16m^2 + 8n + 8m$$
<p><strong>Krok 3:</strong> Wyłączamy 8 przed nawias:</p>
$$= 8(2n^2 - 2m^2 + n + m)$$
<p><strong>Wniosek:</strong> Ponieważ $m, n \\in \\mathbb{N}$, to $2n^2 - 2m^2 + n + m \\in \\mathbb{C}$. Otrzymaliśmy wielokrotność liczby 8, co dowodzi podzielności przez 8. $c.n.d.$</p>
""",
        "answer": "$W = 8(2n^2 - 2m^2 + n + m) \\implies 8 \\mid W$."
    },
    {
        "id": "dowod-40",
        "number": "DOWÓD 40",
        "title": "Podzielność potęg ósemki przez 27",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że liczba $8^{1000} - 5 \\cdot 8^{999} + 3 \\cdot 8^{998}$ jest podzielna przez 27.",
        "hint": "Wyłącz przed nawias potęgę ósemki o najniższym wykładniku, czyli $8^{998}$.",
        "solution": """
<p><strong>Krok 1:</strong> Wyłączamy wspólny czynnik $8^{998}$ przed nawias:</p>
$$L = 8^{998} \\cdot (8^2 - 5 \\cdot 8^1 + 3)$$
<p><strong>Krok 2:</strong> Obliczamy wartość wyrażenia w nawiasie:</p>
$$8^2 - 5 \\cdot 8 + 3 = 64 - 40 + 3 = 27$$
<p><strong>Krok 3:</strong> Zapisujemy w postaci iloczynowej:</p>
$$L = 27 \\cdot 8^{998}$$
<p><strong>Wniosek:</strong> Ponieważ $8^{998} \\in \\mathbb{C}$, liczba $L$ dzieli się przez 27. $c.n.d.$</p>
""",
        "answer": "$L = 27 \\cdot 8^{998} \\implies 27 \\mid L$."
    },
    {
        "id": "dowod-41",
        "number": "DOWÓD 41",
        "title": "Suma potęg 999 podzielna przez 1000",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że suma $999 + 999^2 + 999^3 + 999^4 + 999^5 + 999^6 + 999^7 + 999^8$ jest podzielna przez 1000.",
        "hint": "Połącz wyrazy w pary sąsiednich potęg: $(999 + 999^2) + (999^3 + 999^4) + \\dots$",
        "solution": """
<p><strong>Krok 1:</strong> Grupujemy składniki sumy w 4 pary:</p>
$$S = (999 + 999^2) + (999^3 + 999^4) + (999^5 + 999^6) + (999^7 + 999^8)$$
<p><strong>Krok 2:</strong> Z każdej pary wyłączamy potęgę o niższym wykładniku:</p>
$$S = 999(1 + 999) + 999^3(1 + 999) + 999^5(1 + 999) + 999^7(1 + 999)$$
<p><strong>Krok 3:</strong> Zauważmy, że $1 + 999 = 1000$:</p>
$$S = 1000 \\cdot (999 + 999^3 + 999^5 + 999^7)$$
<p><strong>Wniosek:</strong> Czynnik w nawiasie jest liczbą całkowitą, zatem suma $S$ jest wielokrotnością 1000. $c.n.d.$</p>
""",
        "answer": "$S = 1000 \\cdot (999 + 999^3 + 999^5 + 999^7) \\implies 1000 \\mid S$."
    },
    {
        "id": "dowod-42",
        "number": "DOWÓD 42",
        "title": "Suma potęg 103 podzielna przez 10 712",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że wyrażenie $103 + 103^2 + 103^3 + \\dots + 103^{18}$ jest podzielne przez 10 712.",
        "hint": "Oblicz wartość sumy pierwszych dwóch składników: $103 + 103^2 = 103(1 + 103) = 103 \\cdot 104$.",
        "solution": """
<p><strong>Krok 1:</strong> Sprawdzamy wartość pierwszych dwóch składników:</p>
$$103 + 103^2 = 103(1 + 103) = 103 \\cdot 104 = 10\\,712$$
<p><strong>Krok 2:</strong> Łączymy 18 składników w 9 kolejnych par:</p>
$$S = (103 + 103^2) + 103^2(103 + 103^2) + 103^4(103 + 103^2) + \\dots + 103^{16}(103 + 103^2)$$
<p><strong>Krok 3:</strong> Wyłączamy wspólny czynnik $10\\,712$:</p>
$$S = 10\\,712 \\cdot (1 + 103^2 + 103^4 + \\dots + 103^{16})$$
<p><strong>Wniosek:</strong> Ponieważ suma w nawiasie jest całkowita, całe wyrażenie dzieli się przez $10\\,712$. $c.n.d.$</p>
""",
        "answer": "$S = 10\\,712 \\cdot (1 + 103^2 + \\dots + 103^{16}) \\implies 10\\,712 \\mid S$."
    },
    {
        "id": "dowod-43",
        "number": "DOWÓD 43",
        "title": "Suma potęg 9 podzielna przez 13",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że wyrażenie $9 + 9^2 + 9^3 + \\dots + 9^{99}$ jest podzielne przez 13.",
        "hint": "Pogrupuj składniki po 3: $9 + 9^2 + 9^3 = 9(1 + 9 + 81) = 9 \\cdot 91$, a $91 = 7 \\cdot 13$.",
        "solution": """
<p><strong>Krok 1:</strong> Wyrażenie ma 99 składników ($99 = 33 \\cdot 3$, czyli 33 trójki).</p>
<p><strong>Krok 2:</strong> Zbadajmy sumę w pierwszej trójce:</p>
$$9 + 9^2 + 9^3 = 9(1 + 9 + 81) = 9 \\cdot 91 = 9 \\cdot 7 \\cdot 13 = 13 \\cdot 63$$
<p><strong>Krok 3:</strong> Grupujemy wszystkie 99 wyrazów w trójki:</p>
$$S = (9 + 9^2 + 9^3) + 9^3(9 + 9^2 + 9^3) + \\dots + 9^{96}(9 + 9^2 + 9^3)$$
$$S = 13 \\cdot 63 \\cdot (1 + 9^3 + 9^6 + \\dots + 9^{96})$$
<p><strong>Wniosek:</strong> Czynnik w nawiasie jest całkowity, stąd suma $S$ jest podzielna przez 13. $c.n.d.$</p>
""",
        "answer": "$S = 13 \\cdot [63(1 + 9^3 + \\dots + 9^{96})] \\implies 13 \\mid S$."
    },
    {
        "id": "dowod-44",
        "number": "DOWÓD 44",
        "title": "Podzielność sumy potęg piątki przez 36",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że liczba $5^{10} + 2 \\cdot 5^9 + 5^8$ jest podzielna przez 36.",
        "hint": "Wyłącz przed nawias $5^8$. W nawiasie otrzymasz kwadrat sumy $(5 + 1)^2$.",
        "solution": """
<p><strong>Krok 1:</strong> Wyłączamy $5^8$ przed nawias:</p>
$$L = 5^8(5^2 + 2 \\cdot 5 + 1)$$
<p><strong>Krok 2:</strong> Zwijamy nawias ze wzoru skróconego mnożenia lub bezpośrednio sumujemy:</p>
$$5^2 + 2 \\cdot 5 + 1 = 25 + 10 + 1 = 36$$
<p><strong>Krok 3:</strong> Zapisujemy wynik:</p>
$$L = 36 \\cdot 5^8$$
<p><strong>Wniosek:</strong> Liczba $L$ jest iloczynem 36 i liczby całkowitej $5^8$, a więc jest podzielna przez 36. $c.n.d.$</p>
""",
        "answer": "$L = 36 \\cdot 5^8 \\implies 36 \\mid L$."
    },
    {
        "id": "dowod-45",
        "number": "DOWÓD 45",
        "title": "Podzielność wyrażenia z potęgami piątki przez 195",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że wyrażenie $5^n + 5^{n+1} + 5^{n+2} + 5^{n+3}$ jest podzielne przez 195, jeśli $n \\in \\mathbb{N}_+$.",
        "hint": "Wyłącz $5^n$ przed nawias. Następnie wykorzystaj fakt, że dla $n \\ge 1$ zachodzi $5^n = 5 \\cdot 5^{n-1}$.",
        "solution": """
<p><strong>Krok 1:</strong> Wyłączamy $5^n$ przed nawias:</p>
$$5^n(1 + 5 + 25 + 125) = 5^n \\cdot 156$$
<p><strong>Krok 2:</strong> Dla $n \\in \\mathbb{N}_+$ ($n \\ge 1$) rozpisujemy $5^n = 5 \\cdot 5^{n-1}$:</p>
$$5^n \\cdot 156 = 5^{n-1} \\cdot (5 \\cdot 156) = 5^{n-1} \\cdot 780$$
<p><strong>Krok 3:</strong> Zauważamy, że $780 = 4 \\cdot 195$:</p>
$$= 195 \\cdot (4 \\cdot 5^{n-1})$$
<p><strong>Wniosek:</strong> Skoro $n \\ge 1$, to $n - 1 \\ge 0$, więc $4 \\cdot 5^{n-1} \\in \\mathbb{C}$. Oznacza to podzielność przez 195. $c.n.d.$</p>
""",
        "answer": "$W = 195 \\cdot (4 \\cdot 5^{n-1}) \\implies 195 \\mid W$."
    },
    {
        "id": "dowod-46",
        "number": "DOWÓD 46",
        "title": "Wielokrotność liczby 20",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Uzasadnij, że dla każdej liczby dodatniej całkowitej $n$ liczba $4^{n+2} + 4 \\cdot 5^{n+1} + 4^{n+1}$ jest wielokrotnością liczby 20.",
        "hint": "Połącz $4^{n+2} + 4^{n+1} = 4^{n+1}(4 + 1) = 5 \\cdot 4 \\cdot 4^n = 20 \\cdot 4^n$.",
        "solution": """
<p><strong>Krok 1:</strong> Grupujemy wyrazy z potęgami czwórki:</p>
$$4^{n+2} + 4^{n+1} = 4^{n+1}(4 + 1) = 5 \\cdot 4^{n+1} = 5 \\cdot 4 \\cdot 4^n = 20 \\cdot 4^n$$
<p><strong>Krok 2:</strong> Przekształcamy środkowy wyraz:</p>
$$4 \\cdot 5^{n+1} = 4 \\cdot 5 \\cdot 5^n = 20 \\cdot 5^n$$
<p><strong>Krok 3:</strong> Dodajemy przekształcone składniki:</p>
$$L = 20 \\cdot 4^n + 20 \\cdot 5^n = 20(4^n + 5^n)$$
<p><strong>Wniosek:</strong> Dla $n \\in \\mathbb{N}_+$ liczba $4^n + 5^n$ jest całkowita, co dowodzi, że $L$ jest wielokrotnością 20. $c.n.d.$</p>
""",
        "answer": "$L = 20(4^n + 5^n) \\implies 20 \\mid L$."
    },
    {
        "id": "dowod-47",
        "number": "DOWÓD 47",
        "title": "Podzielność $5^{16} - 2^{16}$ przez 29",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $5^{16} - 2^{16}$ jest podzielna przez 29.",
        "hint": "Stosuj wielokrotnie wzór na różnicę kwadratów, aż pojawi się czynnik $5^2 + 2^2 = 29$.",
        "solution": """
<p><strong>Krok 1:</strong> Stosujemy wzór na różnicę kwadratów $a^2 - b^2 = (a-b)(a+b)$:</p>
$$5^{16} - 2^{16} = (5^8 + 2^8)(5^8 - 2^8)$$
$$= (5^8 + 2^8)(5^4 + 2^4)(5^4 - 2^4)$$
$$= (5^8 + 2^8)(5^4 + 2^4)(5^2 + 2^2)(5^2 - 2^2)$$
<p><strong>Krok 2:</strong> Obliczamy wartość czynnika $(5^2 + 2^2)$:</p>
$$5^2 + 2^2 = 25 + 4 = 29$$
<p><strong>Krok 3:</strong> Zapisujemy liczbę jako:</p>
$$5^{16} - 2^{16} = 29 \\cdot \\left[ (5^8 + 2^8)(5^4 + 2^4)(5^2 - 2^2) \\right]$$
<p><strong>Wniosek:</strong> Czynnik w nawiasie jest liczbą całkowitą, co dowodzi podzielności przez 29. $c.n.d.$</p>
""",
        "answer": "$5^{16} - 2^{16} = 29 \\cdot k$, gdzie $k \\in \\mathbb{C} \\implies 29 \\mid (5^{16} - 2^{16})$."
    },
    {
        "id": "dowod-48",
        "number": "DOWÓD 48",
        "title": "Suma sześcianów $1007^3 + 993^3$ podzielna przez 1000",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $1007^3 + 993^3$ jest podzielna przez 1000.",
        "hint": "Skorzystaj ze wzoru na sumę sześcianów: $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$. Zauważ, że $1007 + 993 = 2000$.",
        "solution": """
<p><strong>Krok 1:</strong> Stosujemy wzór $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ dla $a = 1007$ i $b = 993$:</p>
$$1007 + 993 = 2000$$
$$1007^3 + 993^3 = 2000 \\cdot (1007^2 - 1007 \\cdot 993 + 993^2)$$
<p><strong>Krok 2:</strong> Wyodrębniamy czynnik 1000:</p>
$$= 1000 \\cdot \\left[ 2(1007^2 - 1007 \\cdot 993 + 993^2) \\right]$$
<p><strong>Wniosek:</strong> Wartość w nawiasie jest całkowita, więc liczba dzieli się przez 1000 (a nawet przez 2000). $c.n.d.$</p>
""",
        "answer": "$1007^3 + 993^3 = 1000 \\cdot [2(\\dots)] \\implies 1000 \\mid (1007^3 + 993^3)$."
    },
    {
        "id": "dowod-49",
        "number": "DOWÓD 49",
        "title": "Różnica sześcianów $6^9 - 5^9$ podzielna przez 91",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że wyrażenie $6^9 - 5^9$ jest podzielne przez 91.",
        "hint": "Zapisz $6^9 - 5^9 = (6^3)^3 - (5^3)^3$ i użyj wzoru $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$. Oblicz $6^3 - 5^3$.",
        "solution": """
<p><strong>Krok 1:</strong> Zapisujemy wyrażenie jako różnicę sześcianów:</p>
$$6^9 - 5^9 = (6^3)^3 - (5^3)^3$$
<p><strong>Krok 2:</strong> Stosujemy wzór skróconego mnożenia dla $a = 6^3 = 216$ i $b = 5^3 = 125$:</p>
$$a - b = 216 - 125 = 91$$
$$6^9 - 5^9 = (216 - 125) \\cdot (216^2 + 216 \\cdot 125 + 125^2) = 91 \\cdot (216^2 + 216 \\cdot 125 + 125^2)$$
<p><strong>Wniosek:</strong> Drugi czynnik jest całkowity, zatem wyrażenie jest podzielne przez 91. $c.n.d.$</p>
""",
        "answer": "$6^9 - 5^9 = 91 \\cdot (216^2 + 216 \\cdot 125 + 125^2) \\implies 91 \\mid (6^9 - 5^9)$."
    },
    {
        "id": "dowod-50",
        "number": "DOWÓD 50",
        "title": "Iloczyn czterech kolejnych liczb podzielny przez 24",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że wyrażenie $(n^2+n)(n^2-3n+2)$ jest podzielne przez 24 dla każdej liczby całkowitej $n$.",
        "hint": "Rozłóż oba wielomiany na czynniki liniowe: $n^2+n = n(n+1)$, $n^2-3n+2 = (n-1)(n-2)$.",
        "solution": """
<p><strong>Krok 1:</strong> Rozkładamy wielomiany na czynniki:</p>
$$n^2 + n = n(n + 1)$$
$$n^2 - 3n + 2 = (n - 1)(n - 2)$$
<p><strong>Krok 2:</strong> Łączymy czynniki w kolejności rosnącej:</p>
$$W = (n - 2)(n - 1)n(n + 1)$$
<p>Jest to iloczyn <strong>czterech kolejnych liczb całkowitych</strong>.</p>
<p><strong>Krok 3:</strong> Analiza podzielności:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Wśród 4 kolejnych liczb są dwie liczby parzyste, w tym co najmniej jedna podzielna przez 4, więc iloczyn dzieli się przez $2 \\cdot 4 = 8$.</li>
  <li>Wśród 4 kolejnych liczb co najmniej jedna dzieli się przez 3.</li>
  <li>Ponieważ $\\operatorname{NWD}(8, 3) = 1$, iloczyn dzieli się przez $8 \\cdot 3 = 24$.</li>
</ul>
<p><strong>Wniosek:</strong> Wyrażenie dzieli się przez 24 dla każdego $n \\in \\mathbb{C}$. $c.n.d.$</p>
""",
        "answer": "$W = (n-2)(n-1)n(n+1)$ to iloczyn 4 kolejnych liczb całkowitych $\\implies 24 \\mid W$."
    },
    {
        "id": "dowod-51",
        "number": "DOWÓD 51",
        "title": "Iloczyn trzech kolejnych liczb parzystych",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że iloczyn trzech kolejnych liczb parzystych jest podzielny przez 48.",
        "hint": "Trzy kolejne liczby parzyste to $2k, 2k+2, 2k+4$. Wyłącz dwójki z każdego czynnika.",
        "solution": """
<p><strong>Założenie:</strong> Niech kolejnymi liczbami parzystymi będą $2k, 2k+2, 2k+4$, gdzie $k \\in \\mathbb{C}$.</p>
<p><strong>Krok 1:</strong> Tworzymy ich iloczyn:</p>
$$P = 2k \\cdot (2k + 2) \\cdot (2k + 4) = 2k \\cdot 2(k + 1) \\cdot 2(k + 2) = 8k(k + 1)(k + 2)$$
<p><strong>Krok 2:</strong> Wyrażenie $k(k + 1)(k + 2)$ to iloczyn 3 kolejnych liczb całkowitych, więc dzieli się przez $3! = 6$:</p>
$$k(k + 1)(k + 2) = 6m, \\quad m \\in \\mathbb{C}$$
<p><strong>Krok 3:</strong> Podstawiamy:</p>
$$P = 8 \\cdot 6m = 48m$$
<p><strong>Wniosek:</strong> Liczba $P$ jest podzielna przez 48. $c.n.d.$</p>
""",
        "answer": "$P = 48m$ ($m \\in \\mathbb{C}$) $\\implies 48 \\mid P$."
    },
    {
        "id": "dowod-52",
        "number": "DOWÓD 52",
        "title": "Podzielność wyrażenia $n^2k^2 - nk^2 + kn^2 - kn$ przez 4",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że wyrażenie $n^2k^2 - nk^2 + kn^2 - kn$ jest podzielne przez 4, jeśli $n \\in \\mathbb{C}$ i $k \\in \\mathbb{C}$.",
        "hint": "Pogrupuj wyrazy: $(n^2k^2 - nk^2) + (kn^2 - kn) = k^2(n^2 - n) + k(n^2 - n)$.",
        "solution": """
<p><strong>Krok 1:</strong> Grupujemy wyrazy i wyłączamy wspólne czynniki:</p>
$$W = k^2(n^2 - n) + k(n^2 - n) = (n^2 - n)(k^2 + k)$$
<p><strong>Krok 2:</strong> Rozkładamy oba nawiasy:</p>
$$W = n(n - 1) \\cdot k(k + 1)$$
<p><strong>Krok 3:</strong> Analiza parzystości:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>$n(n - 1)$ to iloczyn dwóch kolejnych liczb całkowitych, więc jest parzyste ($2a$, $a \\in \\mathbb{C}$).</li>
  <li>$k(k + 1)$ to iloczyn dwóch kolejnych liczb całkowitych, więc jest parzyste ($2b$, $b \\in \\mathbb{C}$).</li>
</ul>
$$W = 2a \\cdot 2b = 4ab$$
<p><strong>Wniosek:</strong> Iloczyn $W$ jest wielokrotnością 4, więc dzieli się przez 4. $c.n.d.$</p>
""",
        "answer": "$W = 4ab$ ($a, b \\in \\mathbb{C}$) $\\implies 4 \\mid W$."
    },
    {
        "id": "dowod-53",
        "number": "DOWÓD 53",
        "title": "Kwadrat iloczynu liczb podzielnych przez 5",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że kwadrat iloczynu dwóch kolejnych liczb całkowitych podzielnych przez 5 jest podzielny przez 2500.",
        "hint": "Dwie kolejne liczby podzielne przez 5 to $5k$ oraz $5(k+1)$. Zauważ, że $k(k+1)$ jest liczbą parzystą.",
        "solution": """
<p><strong>Założenie:</strong> Niech $5k$ oraz $5(k+1)$ będą dwiema kolejnymi liczbami całkowitymi podzielnymi przez 5 ($k \\in \\mathbb{C}$).</p>
<p><strong>Krok 1:</strong> Obliczamy ich iloczyn:</p>
$$I = 5k \\cdot 5(k + 1) = 25k(k + 1)$$
<p><strong>Krok 2:</strong> Podnosimy iloczyn do kwadratu:</p>
$$I^2 = [25k(k + 1)]^2 = 625 \\cdot [k(k + 1)]^2$$
<p><strong>Krok 3:</strong> Ponieważ $k$ i $k + 1$ to kolejne liczby całkowite, jedna z nich jest parzysta: $k(k + 1) = 2m$ ($m \\in \\mathbb{C}$):</p>
$$[k(k + 1)]^2 = (2m)^2 = 4m^2$$
$$I^2 = 625 \\cdot 4m^2 = 2500m^2$$
<p><strong>Wniosek:</strong> Liczba $I^2$ jest podzielna przez 2500. $c.n.d.$</p>
""",
        "answer": "$I^2 = 2500m^2$ ($m \\in \\mathbb{C}$) $\\implies 2500 \\mid I^2$."
    },
    {
        "id": "dowod-54",
        "number": "DOWÓD 54",
        "title": "Wielomian stopnia 5 i wielokrotność 5!",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że dla $n \\in \\mathbb{N}$ wyrażenie $n^5 - 5n^4 + 5n^3 + 5n^2 - 6n$ jest wielokrotnością $5!$.",
        "hint": "Wyłącz $n$ przed nawias i znajdź pierwiastki całkowite wielomianu w nawiasie (np. 1, 2, 3, -1).",
        "solution": """
<p><strong>Krok 1:</strong> Wyłączamy $n$ przed nawias:</p>
$$W(n) = n(n^4 - 5n^3 + 5n^2 + 5n - 6)$$
<p><strong>Krok 2:</strong> Rozkładamy wielomian w nawiasie:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Dla $n = 1$: $1 - 5 + 5 + 5 - 6 = 0 \\implies$ czynnik $(n - 1)$.</li>
  <li>Dzieląc przez $(n - 1)$ otrzymujemy $n^3 - 4n^2 + n + 6$.</li>
  <li>Dla $n = 2$: $8 - 16 + 2 + 6 = 0 \\implies$ czynnik $(n - 2)$.</li>
  <li>Dzieląc przez $(n - 2)$ otrzymujemy $n^2 - 2n - 3 = (n - 3)(n + 1)$.</li>
</ul>
<p><strong>Krok 3:</strong> Łączymy czynniki w kolejności rosnącej:</p>
$$W(n) = (n - 3)(n - 2)(n - 1)n(n + 1)$$
<p>Jest to iloczyn <strong>pięciu kolejnych liczb całkowitych</strong>.</p>
<p><strong>Wniosek:</strong> Iloczyn dowolnych 5 kolejnych liczb całkowitych dzieli się przez $5! = 120$. Zatem wyrażenie jest wielokrotnością $5!$. $c.n.d.$</p>
""",
        "answer": "$W(n) = (n-3)(n-2)(n-1)n(n+1)$ to iloczyn 5 kolejnych liczb $\\implies 5! \\mid W(n)$."
    },
    {
        "id": "dowod-55",
        "number": "DOWÓD 55",
        "title": "Wartość wielomianu dla liczby parzystej podzielna przez 96",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Liczby 2, 4, 6 są pierwiastkami wielomianu stopnia trzeciego, w którym współczynnik przy najwyższej potędze zmiennej jest równy 2. Uzasadnij, że dla każdej liczby całkowitej parzystej wartość tego wielomianu jest liczbą podzielną przez 96.",
        "hint": "Zapisz postać iloczynową $W(x) = 2(x-2)(x-4)(x-6)$, a następnie podstaw $x = 2k$ dla $k \\in \\mathbb{C}$.",
        "solution": """
<p><strong>Krok 1:</strong> Postać iloczynowa wielomianu stopnia trzeciego o danych pierwiastkach i współczynniku $a = 2$:</p>
$$W(x) = 2(x - 2)(x - 4)(x - 6)$$
<p><strong>Krok 2:</strong> Podstawiamy liczbę parzystą $x = 2k$ ($k \\in \\mathbb{C}$):</p>
$$W(2k) = 2(2k - 2)(2k - 4)(2k - 6) = 2 \\cdot 2(k - 1) \\cdot 2(k - 2) \\cdot 2(k - 3) = 16(k - 1)(k - 2)(k - 3)$$
<p><strong>Krok 3:</strong> Wyrażenie $(k - 1)(k - 2)(k - 3)$ to iloczyn trzech kolejnych liczb całkowitych, więc dzieli się przez $3! = 6$:</p>
$$(k - 1)(k - 2)(k - 3) = 6m, \\quad m \\in \\mathbb{C}$$
$$W(2k) = 16 \\cdot 6m = 96m$$
<p><strong>Wniosek:</strong> Wartość wielomianu jest podzielna przez 96. $c.n.d.$</p>
""",
        "answer": "$W(2k) = 96m$ ($m \\in \\mathbb{C}$) $\\implies 96 \\mid W(2k)$."
    },
    {
        "id": "dowod-56",
        "number": "DOWÓD 56",
        "title": "Podzielność wyrażenia z potęgami siódemki przez 56",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $7^{30} - 8 \\cdot 7^{20} + 15 \\cdot 7^{10}$ jest podzielna przez 56.",
        "hint": "Wyłącz $7^{10}$ przed nawias i rozłóż trójmian $t^2 - 8t + 15$ dla $t = 7^{10}$. Zbadaj podzielność przez 7 i przez 8.",
        "solution": """
<p><strong>Krok 1:</strong> Wyłączamy $7^{10}$ przed nawias:</p>
$$L = 7^{10}\\left[ (7^{10})^2 - 8 \\cdot 7^{10} + 15 \\right]$$
<p><strong>Krok 2:</strong> Rozkładamy trójmian $t^2 - 8t + 15 = (t - 3)(t - 5)$ dla $t = 7^{10}$:</p>
$$L = 7^{10}(7^{10} - 3)(7^{10} - 5)$$
<p><strong>Krok 3:</strong> Badamy podzielność przez $56 = 7 \\cdot 8$ (gdzie $\\operatorname{NWD}(7, 8) = 1$):</p>
<ul class="list-disc pl-5 space-y-1">
  <li><strong>Przez 7:</strong> Czynnik $7^{10}$ gwarantuje podzielność przez 7.</li>
  <li><strong>Przez 8:</strong> Ponieważ $7 \\equiv -1 \\pmod 8$, to $7^{10} \\equiv (-1)^{10} \\equiv 1 \\pmod 8$.
    <br>Stąd $7^{10} - 3 \\equiv 1 - 3 = -2 \\equiv 6 \\pmod 8$ (jest parzysta, czyli $2a$).
    <br>Oraz $7^{10} - 5 \\equiv 1 - 5 = -4 \\equiv 4 \\pmod 8$ (jest podzielna przez 4, czyli $4b$).
    <br>Iloczyn $(7^{10} - 3)(7^{10} - 5) = 2a \\cdot 4b = 8ab$ jest podzielny przez 8.
  </li>
</ul>
<p><strong>Wniosek:</strong> Liczba $L$ dzieli się przez 7 i 8, więc dzieli się przez 56. $c.n.d.$</p>
""",
        "answer": "$7 \\mid L$ oraz $8 \\mid L \\implies 56 \\mid L$."
    },
    {
        "id": "dowod-57",
        "number": "DOWÓD 57",
        "title": "Wielokrotność liczby 16 dla $81^n - 1$",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że dla $n \\in \\mathbb{N}$ liczba $81^n - 1$ jest wielokrotnością liczby 16.",
        "hint": "Użyj wzoru na różnicę potęg: $a^n - b^n = (a - b)(a^{n-1} + \\dots + 1)$. Zauważ, że $81 - 1 = 80 = 5 \\cdot 16$.",
        "solution": """
<p><strong>Krok 1:</strong> Dla $n = 0$: $81^0 - 1 = 0 = 16 \\cdot 0$ (spełnione).</p>
<p><strong>Krok 2:</strong> Dla $n \\ge 1$ stosujemy wzór na różnicę $n$-tych potęg:</p>
$$81^n - 1 = (81 - 1)(81^{n-1} + 81^{n-2} + \\dots + 1)$$
$$= 80 \\cdot (81^{n-1} + 81^{n-2} + \\dots + 1)$$
<p><strong>Krok 3:</strong> Rozkładamy $80 = 16 \\cdot 5$:</p>
$$81^n - 1 = 16 \\cdot \\left[ 5(81^{n-1} + 81^{n-2} + \\dots + 1) \\right]$$
<p><strong>Wniosek:</strong> Wartość w nawiasie jest liczbą całkowitą, co dowodzi, że $81^n - 1$ jest wielokrotnością 16. $c.n.d.$</p>
""",
        "answer": "$81^n - 1 = 16 \\cdot k$ ($k \\in \\mathbb{C}$) $\\implies 16 \\mid (81^n - 1)$."
    },
    {
        "id": "dowod-58",
        "number": "DOWÓD 58",
        "title": "Wielokrotność liczby 15 dla $16^n - 1$",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że dla $n \\in \\mathbb{N}$ liczba $16^n - 1$ jest wielokrotnością liczby 15.",
        "hint": "Wykorzystaj tożsamość $16^n - 1 = (16 - 1)(16^{n-1} + \\dots + 1)$.",
        "solution": """
<p><strong>Krok 1:</strong> Dla $n = 0$: $16^0 - 1 = 0 = 15 \\cdot 0$ (prawda).</p>
<p><strong>Krok 2:</strong> Dla $n \\ge 1$ ze wzoru na różnicę $n$-tych potęg:</p>
$$16^n - 1 = (16 - 1)(16^{n-1} + 16^{n-2} + \\dots + 1) = 15 \\cdot (16^{n-1} + 16^{n-2} + \\dots + 1)$$
<p><strong>Wniosek:</strong> Suma w nawiasie jest całkowita, zatem liczba $16^n - 1$ jest wielokrotnością 15. *(Dla szczególnego wykładnika $n = 7$ dowód zachodzi analogicznie)*. $c.n.d.$</p>
""",
        "answer": "$16^n - 1 = 15 \\cdot k$ ($k \\in \\mathbb{C}$) $\\implies 15 \\mid (16^n - 1)$."
    },
    {
        "id": "dowod-59",
        "number": "DOWÓD 59",
        "title": "Podzielność wyrażenia dwukwadratowego przez 25",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że wyrażenie $113^4 - 3 \\cdot 113^2 - 4$ jest podzielne przez 25.",
        "hint": "Rozłóż trójmian dwukwadratowy $x^4 - 3x^2 - 4 = (x^2 - 4)(x^2 + 1) = (x - 2)(x + 2)(x^2 + 1)$ i podstaw $x = 113$.",
        "solution": """
<p><strong>Krok 1:</strong> Rozkładamy wielomian $x^4 - 3x^2 - 4$ na czynniki:</p>
$$x^4 - 3x^2 - 4 = (x^2 - 4)(x^2 + 1) = (x - 2)(x + 2)(x^2 + 1)$$
<p><strong>Krok 2:</strong> Podstawiamy $x = 113$:</p>
$$(113 - 2)(113 + 2)(113^2 + 1) = 111 \\cdot 115 \\cdot (113^2 + 1)$$
<p><strong>Krok 3:</strong> Analiza podzielności przez 5:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Czynnik $115 = 5 \\cdot 23$ dzieli się przez 5.</li>
  <li>Liczba $113$ ma ostatnią cyfrę 3, więc $113^2$ ma ostatnią cyfrę 9 ($3^2 = 9$). Zatem $113^2 + 1$ ma cyfrę jedności $9 + 1 = 0$, czyli dzieli się przez 5 ($113^2 + 1 = 12770 = 5 \\cdot 2554$).</li>
</ul>
<p><strong>Krok 4:</strong> Iloczyn zawiera dwa czynniki równe 5:</p>
$$111 \\cdot (5 \\cdot 23) \\cdot (5 \\cdot 2554) = 25 \\cdot (111 \\cdot 23 \\cdot 2554)$$
<p><strong>Wniosek:</strong> Wyrażenie jest podzielne przez 25. $c.n.d.$</p>
""",
        "answer": "$W = 25 \\cdot (111 \\cdot 23 \\cdot 2554) \\implies 25 \\mid W$."
    },
    {
        "id": "dowod-60",
        "number": "DOWÓD 60",
        "title": "Podzielność przez 100 wyrażenia z potęgami szóstki",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $6^{400} - 17 \\cdot 6^{200} + 16$ jest podzielna przez 100.",
        "hint": "Podstaw $t = 6^{200}$ i rozłóż na czynniki $(t - 1)(t - 16)$. Wykaż podzielność przez 25 oraz przez 4.",
        "solution": """
<p><strong>Krok 1:</strong> Niech $t = 6^{200}$. Otrzymujemy:</p>
$$t^2 - 17t + 16 = (t - 1)(t - 16) = (6^{200} - 1)(6^{200} - 16)$$
<p><strong>Krok 2:</strong> Podzielność przez $100 = 25 \\cdot 4$ (gdzie $\\operatorname{NWD}(25, 4) = 1$):</p>
<ul class="list-disc pl-5 space-y-1">
  <li><strong>Przez 25:</strong> $6^1 \\equiv 6, 6^2 \\equiv 11, 6^3 \\equiv 16, 6^4 \\equiv 21, 6^5 \\equiv 1 \\pmod{25}$.
    <br>Zatem $6^{200} = (6^5)^{40} \\equiv 1^{40} \\equiv 1 \\pmod{25} \\implies 25 \\mid (6^{200} - 1)$.</li>
  <li><strong>Przez 4:</strong> $6^{200} - 16 = 2^{200} \\cdot 3^{200} - 16 = 4 \\cdot (2^{198} \\cdot 3^{200} - 4) \\implies 4 \\mid (6^{200} - 16)$.</li>
</ul>
<p><strong>Wniosek:</strong> Iloczyn dzieli się przez 25 i przez 4, a więc dzieli się przez 100. $c.n.d.$</p>
""",
        "answer": "$25 \\mid (6^{200}-1)$ oraz $4 \\mid (6^{200}-16) \\implies 100 \\mid L$."
    },
    {
        "id": "dowod-61",
        "number": "DOWÓD 61",
        "title": "Podzielność kwadratu $(10^n - 7)^2$ przez 9",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Uzasadnij, że liczba $(10^n - 7)^2$ jest podzielna przez 9 dla $n \\in \\mathbb{N}_+$.",
        "hint": "Wykaż najpierw, że wyrażenie $10^n - 7$ dzieli się przez 3. Kwadrat liczby podzielnej przez 3 dzieli się przez 9.",
        "solution": """
<p><strong>Krok 1:</strong> Zapisujemy wyrażenie w nawiasie jako:</p>
$$10^n - 7 = (10^n - 1) - 6$$
<p><strong>Krok 2:</strong> Liczba $10^n - 1$ składa się z samych dziewiątek:</p>
$$10^n - 1 = \\underbrace{999\\dots9}_{n} = 9 \\cdot \\underbrace{111\\dots1}_{n}$$
$$10^n - 7 = 9 \\cdot \\underbrace{111\\dots1}_{n} - 6 = 3 \\cdot \\left( 3 \\cdot \\underbrace{111\\dots1}_{n} - 2 \\right)$$
<p><strong>Krok 3:</strong> Podnosimy do kwadratu:</p>
$$(10^n - 7)^2 = \\left[ 3 \\cdot \\left( 3 \\cdot \\underbrace{111\\dots1}_{n} - 2 \\right) \\right]^2 = 9 \\cdot \\left( 3 \\cdot \\underbrace{111\\dots1}_{n} - 2 \\right)^2$$
<p><strong>Wniosek:</strong> Czynnik w nawiasie jest całkowity, stąd liczba dzieli się przez 9. $c.n.d.$</p>
""",
        "answer": "$(10^n - 7)^2 = 9 \\cdot k^2$ ($k \\in \\mathbb{C}$) $\\implies 9 \\mid (10^n - 7)^2$."
    },
    {
        "id": "dowod-62",
        "number": "DOWÓD 62",
        "title": "Podzielność $100^n + 5$ przez 15",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $100^n + 5$ dzieli się przez 15 dla $n \\in \\mathbb{N}_+$.",
        "hint": "Wykaż podzielność przez 5 (ostatnia cyfra) oraz przez 3 (suma cyfr lub kongruencja $100 \\equiv 1 \\pmod 3$).",
        "solution": """
<p>Liczba dzieli się przez $15 = 3 \\cdot 5$, gdy dzieli się przez 3 i przez 5 jednocześnie ($\\operatorname{NWD}(3, 5) = 1$).</p>
<ul class="list-disc pl-5 space-y-1">
  <li><strong>Podzielność przez 5:</strong> Dla $n \\ge 1$ liczba $100^n = 10^{2n}$ kończy się zerem. Zatem $100^n + 5$ kończy się cyfrą 5, co oznacza podzielność przez 5.</li>
  <li><strong>Podzielność przez 3:</strong> Liczba $100^n + 5 = 100\\dots05$ ma sumę cyfr równą $1 + 0 + \\dots + 0 + 5 = 6$. Ponieważ 6 dzieli się przez 3, cała liczba dzieli się przez 3.</li>
</ul>
<p><strong>Wniosek:</strong> Liczba jest podzielna przez 3 i 5, zatem dzieli się przez 15. $c.n.d.$</p>
""",
        "answer": "$3 \\mid (100^n + 5)$ oraz $5 \\mid (100^n + 5) \\implies 15 \\mid (100^n + 5)$."
    },
    {
        "id": "dowod-63",
        "number": "DOWÓD 63",
        "title": "Suma liczb $XXX + XX + X$ podzielna przez 41",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Udowodnij, że suma liczb: trzycyfrowej, dwucyfrowej i jednocyfrowej postaci $XXX + XX + X$ jest podzielna przez 41, jeżeli $X$ oznacza dowolną cyfrę różną od zera.",
        "hint": "Rozpisz liczby w systemie dziesiętnym: $XXX = 100X + 10X + X = 111X$.",
        "solution": """
<p><strong>Krok 1:</strong> Zapisujemy liczby w układzie dziesiętnym:</p>
$$XXX = 100X + 10X + X = 111X$$
$$XX = 10X + X = 11X$$
$$X = X$$
<p><strong>Krok 2:</strong> Dodajemy je do siebie:</p>
$$S = 111X + 11X + X = 123X$$
<p><strong>Krok 3:</strong> Zauważmy, że $123 = 41 \\cdot 3$:</p>
$$S = 41 \\cdot (3X)$$
<p><strong>Wniosek:</strong> Ponieważ $X \\in \\{1, 2, \\dots, 9\\}$, to $3X$ jest liczbą całkowitą. Zatem suma $S$ jest podzielna przez 41. $c.n.d.$</p>
""",
        "answer": "$S = 41 \\cdot (3X)$, $3X \\in \\mathbb{C} \\implies 41 \\mid S$."
    },
    {
        "id": "dowod-64",
        "number": "DOWÓD 64",
        "title": "Cyliczna suma liczb trzycyfrowych $ABC + CAB + BCA$",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że suma liczb trzycyfrowych postaci $ABC + CAB + BCA$ jest podzielna przez 111, wiedząc, że $A, B, C$ oznaczają dowolne cyfry i $A \\neq 0, B \\neq 0, C \\neq 0$.",
        "hint": "Zapisz każdą liczbę jako sumę setek, dziesiątek i jedności.",
        "solution": """
<p><strong>Krok 1:</strong> Rozpisujemy liczby w systemie pozycyjnym:</p>
$$ABC = 100A + 10B + C$$
$$CAB = 100C + 10A + B$$
$$BCA = 100B + 10C + A$$
<p><strong>Krok 2:</strong> Dodajemy stronami:</p>
$$S = (100A + 10A + A) + (100B + 10B + B) + (100C + 10C + C)$$
$$S = 111A + 111B + 111C = 111(A + B + C)$$
<p><strong>Wniosek:</strong> Suma cyfr $A + B + C$ jest liczbą całkowitą, stąd suma $S$ jest podzielna przez 111. $c.n.d.$</p>
""",
        "answer": "$S = 111(A + B + C) \\implies 111 \\mid S$."
    },
    {
        "id": "dowod-65",
        "number": "DOWÓD 65",
        "title": "Podzielność $12!$ przez $2^{10}$",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "podstawa",
        "statement": "Wykaż, że iloczyn $1 \\cdot 2 \\cdot 3 \\cdot 4 \\cdot \\dots \\cdot 11 \\cdot 12$ jest podzielny przez $2^{10}$.",
        "hint": "Wypisz czynniki parzyste z iloczynu $12!$ i zsumuj wykładniki potęg dwójki w ich rozkładzie.",
        "solution": """
<p><strong>Krok 1:</strong> Z iloczynu $12!$ wybieramy wszystkie czynniki parzyste:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>$2 = 2^1$</li>
  <li>$4 = 2^2$</li>
  <li>$6 = 2^1 \\cdot 3$</li>
  <li>$8 = 2^3$</li>
  <li>$10 = 2^1 \\cdot 5$</li>
  <li>$12 = 2^2 \\cdot 3$</li>
</ul>
<p><strong>Krok 2:</strong> Sumujemy wykładniki przy podstawie 2:</p>
$$1 + 2 + 1 + 3 + 1 + 2 = 10$$
<p>*(Można także użyć wzoru Legendre'a: $E_2(12!) = \\lfloor \\frac{12}{2} \\rfloor + \\lfloor \\frac{12}{4} \\rfloor + \\lfloor \\frac{12}{8} \\rfloor = 6 + 3 + 1 = 10$)*.</p>
<p><strong>Wniosek:</strong> Iloczyn zawiera czynnik $2^{10}$, a więc dzieli się przez $2^{10}$. $c.n.d.$</p>
""",
        "answer": "$12! = 2^{10} \\cdot k$ ($k \\in \\mathbb{C}$) $\\implies 2^{10} \\mid 12!$."
    },
    {
        "id": "dowod-66",
        "number": "DOWÓD 66",
        "title": "Podzielność $p^2 + 5$ przez 7 gdy $7 \\mid (p - 3)$",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Dana jest liczba $p$ taka, że liczba $p-3$ jest podzielna przez 7. Wykaż, że liczba $p^2 + 5$ też jest podzielna przez 7.",
        "hint": "Zapisz $p - 3 = 7k \\implies p = 7k + 3$ dla $k \\in \\mathbb{C}$ i wstaw do $p^2 + 5$.",
        "solution": """
<p><strong>Założenie:</strong> $p - 3 = 7k \\implies p = 7k + 3$ dla pewnego $k \\in \\mathbb{C}$.</p>
<p><strong>Krok 1:</strong> Obliczamy wartość wyrażenia $p^2 + 5$:</p>
$$p^2 + 5 = (7k + 3)^2 + 5 = 49k^2 + 42k + 9 + 5 = 49k^2 + 42k + 14$$
<p><strong>Krok 2:</strong> Wyłączamy 7 przed nawias:</p>
$$p^2 + 5 = 7(7k^2 + 6k + 2)$$
<p><strong>Wniosek:</strong> Dla $k \\in \\mathbb{C}$ wyrażenie $7k^2 + 6k + 2$ jest liczbą całkowitą, co dowodzi, że $p^2 + 5$ dzieli się przez 7. $c.n.d.$</p>
""",
        "answer": "$p^2 + 5 = 7(7k^2 + 6k + 2) \\implies 7 \\mid (p^2 + 5)$."
    },
    {
        "id": "dowod-67",
        "number": "DOWÓD 67",
        "title": "Podzielność $4^{202} + 2 \\cdot 4^{101} \\cdot 6^{101} + 6^{202}$ przez 100",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że liczba $4^{202} + 2 \\cdot 4^{101} \\cdot 6^{101} + 6^{202}$ jest podzielna przez 100.",
        "hint": "Zwiń wyrażenie ze wzoru na kwadrat sumy $(a + b)^2$. Zbadaj ostatnie cyfry $4^{101}$ i $6^{101}$.",
        "solution": """
<p><strong>Krok 1:</strong> Stosujemy wzór na kwadrat sumy $a^2 + 2ab + b^2 = (a + b)^2$ dla $a = 4^{101}$ i $b = 6^{101}$:</p>
$$4^{202} + 2 \\cdot 4^{101} \\cdot 6^{101} + 6^{202} = (4^{101} + 6^{101})^2$$
<p><strong>Krok 2:</strong> Badamy cyfrę jedności sumy w nawiasie:</p>
<ul class="list-disc pl-5 space-y-1">
  <li>Dla nieparzystych potęg czwórki ostatnią cyfrą jest 4 ($4^1=4, 4^3=64, \\dots$), więc $4^{101}$ kończy się cyfrą 4.</li>
  <li>Dowolna potęga szóstki kończy się cyfrą 6, więc $6^{101}$ kończy się cyfrą 6.</li>
  <li>Cyfra jedności sumy $4^{101} + 6^{101}$ to $4 + 6 = 10 \\implies 0$.</li>
</ul>
<p><strong>Krok 3:</strong> Skoro suma kończy się zerem, jest podzielna przez 10 ($4^{101} + 6^{101} = 10m$, $m \\in \\mathbb{C}$):</p>
$$(4^{101} + 6^{101})^2 = (10m)^2 = 100m^2$$
<p><strong>Wniosek:</strong> Liczba jest podzielna przez 100. $c.n.d.$</p>
""",
        "answer": "$(4^{101} + 6^{101})^2 = (10m)^2 = 100m^2 \\implies 100 \\mid L$."
    },
    {
        "id": "dowod-68",
        "number": "DOWÓD 68",
        "title": "Nieistnienie wielomianu o współczynnikach całkowitych",
        "category": "zbior",
        "category_label": "Zbiór maturalny",
        "level": "rozszerzenie",
        "statement": "Wykaż, że nie istnieje wielomian $W(x)$ stopnia trzeciego o współczynnikach całkowitych, który spełnia warunki: $W(1)=5$ i $W(-1)=4$.",
        "hint": "Załóż postać $W(x) = ax^3 + bx^2 + cx + d$ ($a,b,c,d \\in \\mathbb{C}$), oblicz $W(1) - W(-1)$ i wykaż sprzeczność z całkowitością sumy $a + c$.",
        "solution": """
<p><strong>Dowód nie wprost:</strong> Załóżmy, że taki wielomian istnieje. Ogólna postać wielomianu stopnia trzeciego to:</p>
$$W(x) = ax^3 + bx^2 + cx + d, \\quad a, b, c, d \\in \\mathbb{C}, \\quad a \\neq 0$$
<p><strong>Krok 1:</strong> Wyznaczamy wartości dla $x = 1$ oraz $x = -1$:</p>
$$W(1) = a + b + c + d = 5$$
$$W(-1) = -a + b - c + d = 4$$
<p><strong>Krok 2:</strong> Odejmujemy równania stronami:</p>
$$W(1) - W(-1) = (a + b + c + d) - (-a + b - c + d)$$
$$5 - 4 = 2a + 2c \\iff 1 = 2(a + c)$$
$$a + c = \\frac{1}{2}$$
<p><strong>Wniosek:</strong> Ponieważ $a, c \\in \\mathbb{C}$, to suma $a + c$ musi być liczbą całkowitą. Otrzymaliśmy $a + c = \\frac{1}{2} \\notin \\mathbb{C}$, co stanowi sprzeczność. Taki wielomian nie istnieje. $c.n.d.$</p>
""",
        "answer": "$a + c = \\frac{1}{2} \\notin \\mathbb{C}$ – sprzeczność z całkowitością współczynników."
    }
]
