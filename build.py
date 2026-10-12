# -*- coding: utf-8 -*-
"""
Generator strony sprawdzian.html
Łączy zadania ze zbioru, podręcznika (tematy 4.1 i 4.2) oraz bazy tematów 1 i 2.
"""

from tasks_zbior import TASKS_ZBIOR
from tasks_podrecznik import TASKS_PODRECZNIK
from tasks_tematy import TASKS_TEMATY

ALL_TASKS = TASKS_ZBIOR + TASKS_PODRECZNIK + TASKS_TEMATY

print(f"Liczba zadań ze zbioru: {len(TASKS_ZBIOR)}")
print(f"Liczba zadań z podręcznika: {len(TASKS_PODRECZNIK)}")
print(f"Liczba zadań z tematów 1 i 2: {len(TASKS_TEMATY)}")
print(f"Łącznie zadań w zestawie: {len(ALL_TASKS)}")

def render_task(task):
    is_r = task['level'] == 'rozszerzenie'
    level_badge = (
        '<span class="px-2.5 py-0.5 rounded-md text-[11px] font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20"><i class="fa-solid fa-crown text-[10px] mr-1"></i>Rozszerzenie (R)</span>'
        if is_r else
        '<span class="px-2.5 py-0.5 rounded-md text-[11px] font-semibold bg-sky-500/10 text-sky-300 border border-sky-500/20">Poziom podstawowy</span>'
    )
    category_badge = f'<span class="px-2.5 py-0.5 rounded-md text-[11px] bg-slate-800 text-slate-400 border border-slate-700">{task["category_label"]}</span>'
    
    return f"""
    <article id="{task['id']}" data-title="{task['number']}. {task['title']}" data-category="{task['category']}" data-level="{task['level']}" class="task-card bg-slate-900/50 border border-slate-800/80 rounded-2xl p-5 sm:p-6 transition hover:border-slate-700/80 shadow-lg">
      <div class="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-800/60">
        <div class="flex items-center gap-2.5 flex-wrap">
          <span class="px-2.5 py-1 rounded-lg bg-indigo-600/20 text-indigo-300 font-mono text-xs font-bold border border-indigo-500/30">
            {task['number']}
          </span>
          <h2 class="text-base sm:text-lg font-bold text-white tracking-tight">{task['title']}</h2>
        </div>
        <div class="flex items-center gap-2 flex-wrap">
          {level_badge}
          {category_badge}
        </div>
      </div>

      <div class="py-4 text-sm sm:text-base text-slate-200 leading-relaxed">
        {task['statement']}
      </div>

      <div class="p-3.5 rounded-xl bg-indigo-950/20 border border-indigo-800/30 text-xs text-indigo-200/90 flex items-start gap-3 mb-4">
        <i class="fa-solid fa-lightbulb text-indigo-400 mt-0.5 text-sm"></i>
        <div>
          <strong class="font-semibold text-indigo-300 block mb-0.5">Wskazówka & Kluczowa Metoda:</strong>
          {task['hint']}
        </div>
      </div>

      <button onclick="toggleSolution('{task['id']}')" class="w-full py-2.5 px-4 rounded-xl bg-slate-800/60 hover:bg-slate-800 text-slate-300 hover:text-white text-xs font-semibold border border-slate-700/60 transition flex items-center justify-between group">
        <span class="flex items-center gap-2">
          <i class="fa-solid fa-graduation-cap text-indigo-400 group-hover:rotate-12 transition"></i>
          Pokaż pełne omówienie i rozwiązanie krok po kroku
        </span>
        <i id="icon-{task['id']}" class="solution-icon fa-solid fa-chevron-down text-slate-500 group-hover:text-white transition"></i>
      </button>

      <div id="solution-{task['id']}" class="task-solution hidden mt-4 pt-4 border-t border-slate-800/80 space-y-4 text-sm text-slate-300">
        <div class="space-y-3 leading-relaxed">
          {task['solution']}
        </div>

        <div class="p-4 rounded-xl bg-emerald-950/30 border border-emerald-800/40 text-emerald-200">
          <div class="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-emerald-400 mb-1">
            <i class="fa-solid fa-circle-check"></i>
            Podsumowanie / Wniosek:
          </div>
          <div class="text-sm font-semibold text-white">
            {task['answer']}
          </div>
        </div>
      </div>
    </article>
    """

tasks_html = "\n".join(render_task(t) for t in ALL_TASKS)

TEMPLATE = """<!DOCTYPE html>
<html lang="pl" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sprawdzian: Dowody Algebraiczne & Teoria Liczb &bull; Matematyka ZSE</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
  <script>
    function renderMathOnPage() {
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ],
          throwOnError: false,
          macros: {
            "\\degree": "^{\\circ}",
            "°": "^{\\circ}",
            "\\tg": "\\operatorname{tg}",
            "\\ctg": "\\operatorname{ctg}",
            "\\arctg": "\\operatorname{arctg}",
            "\\arcctg": "\\operatorname{arcctg}",
            "\\sphericalangle": "\\angle",
            "\\measuredangle": "\\angle"
          }
        });
      }
    }
    document.addEventListener("DOMContentLoaded", renderMathOnPage);
    window.addEventListener("load", renderMathOnPage);
  </script>
  <style>
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: #0f172a; }
    ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #475569; }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans selection:bg-indigo-500 selection:text-white">

  <!-- Header -->
  <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex flex-col md:flex-row items-center justify-between gap-3">
      <div class="flex items-center gap-3 w-full md:w-auto justify-between">
        <a href="index.html" class="flex items-center gap-2.5 group">
          <div class="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center text-white shadow-md shadow-indigo-500/20 group-hover:scale-105 transition">
            <i class="fa-solid fa-graduation-cap"></i>
          </div>
          <div>
            <span class="text-sm font-bold text-white tracking-wide block">Baza Zadań Maturalnych</span>
            <span class="text-[11px] text-slate-400 block -mt-0.5">mgr M. Kucharska, mgr A. Piłat</span>
          </div>
        </a>
        <a href="index.html" class="md:hidden text-xs text-indigo-400 bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700">
          <i class="fa-solid fa-house"></i> Home
        </a>
      </div>

      <nav class="flex items-center gap-1.5 overflow-x-auto w-full md:w-auto pb-1 md:pb-0 text-xs">
        <a href="index.html" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800/60 transition hidden lg:inline-flex items-center gap-1">
          <i class="fa-solid fa-house"></i>
        </a>
        
        <a href="1_liczby_rzeczywiste.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-calculator"></i>
          <span>1. Liczby rzeczywiste</span>
        </a>
        
        <a href="2_zbiory_i_wzory.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-layer-group"></i>
          <span>2. Zbiory i wzory</span>
        </a>
        
        <a href="3_funkcje_i_wlasnosci.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-chart-line"></i>
          <span>3. Funkcje</span>
        </a>
        
        <a href="4_funkcja_liniowa.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-bezier-curve"></i>
          <span>4. Liniowa</span>
        </a>
        
        <a href="5_funkcja_kwadratowa.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-superscript"></i>
          <span>5. Kwadratowa</span>
        </a>
        
        <a href="6_ciagi.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-arrow-trend-up"></i>
          <span>6. Ciągi</span>
        </a>
        
        <a href="7_wielomiany.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-cubes"></i>
          <span>7. Wielomiany</span>
        </a>
        
        <a href="8_funkcje_wymierne.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-slate-300 hover:text-white hover:bg-slate-800/60">
          <i class="fa-solid fa-divide"></i>
          <span>8. Wymierne</span>
        </a>

        <!-- Sprawdzian Tab (Active) -->
        <a href="sprawdzian.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap bg-gradient-to-r from-amber-600 to-orange-600 text-white font-bold shadow-md shadow-orange-500/20 border border-amber-400/30">
          <i class="fa-solid fa-fire text-amber-200 animate-pulse"></i>
          <span>Sprawdzian</span>
        </a>
      </nav>
    </div>
  </header>

  <!-- Hero Header -->
  <section class="border-b border-slate-800 bg-gradient-to-b from-orange-950/30 via-slate-900/60 to-slate-950 py-10 px-4 sm:px-6 relative overflow-hidden">
    <div class="max-w-7xl mx-auto relative">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20 mb-3">
            <i class="fa-solid fa-bullseye text-amber-400"></i> Zestaw Przygotowawczy do Sprawdzianu
          </div>
          <h1 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
            Dowody Algebraiczne & Teoria Liczb
          </h1>
          <p class="text-sm sm:text-base text-slate-400 mt-2 max-w-3xl leading-relaxed">
            Kompleksowy zestaw powtórzeniowy obejmujący: <strong>Zbiór maturalny (Dowód 35–68)</strong>, 
            zadania ze zdjęć podręcznika (<strong>Temat 4.1: Dowody w algebrze 1</strong> oraz <strong>Temat 4.2: Dowody w algebrze 2</strong>) 
            oraz wybrane zadania dowodowe ze <strong>sprawdzianów z Tematów 1 i 2</strong>.
          </p>
        </div>
        <div class="flex items-center gap-3 flex-wrap">
          <button id="toggle-all-btn" onclick="toggleAllSolutions()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium border border-slate-700 transition flex items-center gap-2 shadow">
            <i class="fa-regular fa-eye"></i> <span id="toggle-all-text">Rozwiń wszystkie rozwiązania</span>
          </button>
        </div>
      </div>

      <!-- Quick Stats -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-6">
        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
          <div class="text-xl font-bold text-amber-400">__COUNT__</div>
          <div class="text-xs text-slate-400">Wszystkich zadań z dowodami</div>
        </div>
        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
          <div class="text-xl font-bold text-sky-400">4 Zestawy</div>
          <div class="text-xs text-slate-400">Zbiór + Podręcznik 4.1 & 4.2 + Baza</div>
        </div>
        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
          <div class="text-xl font-bold text-emerald-400">100%</div>
          <div class="text-xs text-slate-400">Rozwiązań krok po kroku</div>
        </div>
        <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
          <div class="text-xl font-bold text-indigo-400">KaTeX</div>
          <div class="text-xs text-slate-400">Format egzaminacyjny CKE</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 py-8 flex-1 w-full grid grid-cols-1 lg:grid-cols-4 gap-8">
    
    <!-- Sidebar TOC -->
    <aside class="hidden lg:block lg:col-span-1">
      <div class="sticky top-24 bg-slate-900/60 border border-slate-800 rounded-2xl p-4 max-h-[calc(100vh-7rem)] overflow-y-auto">
        <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3 flex items-center justify-between">
          <span>Spis Zadań</span>
          <span class="text-amber-400 font-mono" id="task-badge-count">__COUNT__ zadań</span>
        </h3>
        <div class="space-y-1 text-xs" id="sidebar-toc">
        </div>
      </div>
    </aside>

    <!-- Task List & Filters -->
    <div class="lg:col-span-3 space-y-6">
      
      <!-- Theory Box -->
      <div class="p-6 rounded-2xl bg-amber-950/20 border border-amber-800/40 shadow-xl space-y-4">
        <div class="flex items-center gap-3 border-b border-amber-800/40 pb-3">
          <div class="w-8 h-8 rounded-lg bg-amber-600/30 text-amber-400 flex items-center justify-center font-bold">
            <i class="fa-solid fa-scale-balanced"></i>
          </div>
          <h2 class="text-lg font-bold text-white tracking-wide">Kompendium Metod Dowodzenia na Sprawdzian</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5 text-xs text-slate-300">
          <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
            <h3 class="font-semibold text-amber-300 flex items-center gap-1.5"><i class="fa-solid fa-divide"></i> Podzielność & Iloczyny</h3>
            <p>Iloczyn $k$ kolejnych liczb całkowitych jest podzielny przez $k!$.</p>
            <p>Wśród 3 kolejnych liczb jest podzielna przez 3 i parzysta: $6 \\mid P$.</p>
            <p>Wśród 4 kolejnych liczb iloczyn dzieli się przez 24 ($4!$).</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
            <h3 class="font-semibold text-amber-300 flex items-center gap-1.5"><i class="fa-solid fa-calculator"></i> Arytmetyka reszt</h3>
            <p>Kwadrat liczby całkowitej: $n^2 \\equiv 0$ lub $1 \\pmod 3$.</p>
            <p>Kwadrat liczby całkowitej: $n^2 \\equiv 0, 1$ lub $4 \\pmod 8$.</p>
            <p>Zapis reszt: $n = mq + r$, gdzie $r \\in \\{0, 1, \\dots, m-1\\}$.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
            <h3 class="font-semibold text-amber-300 flex items-center gap-1.5"><i class="fa-solid fa-chart-line"></i> Średnie: AM &ge; GM</h3>
            <p>Dla $a, b \\ge 0$: $\\frac{a + b}{2} \\ge \\sqrt{ab} \\iff a + b \\ge 2\\sqrt{ab}$.</p>
            <p>Dla $ab > 0$: $\\frac{a}{b} + \\frac{b}{a} \\ge 2$.</p>
            <p>Dla $ab < 0$: $\\frac{a}{b} + \\frac{b}{a} \\le -2$.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
            <h3 class="font-semibold text-amber-300 flex items-center gap-1.5"><i class="fa-solid fa-superscript"></i> Różnice potęg</h3>
            <p>$a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + \\dots + b^{n-1})$.</p>
            <p>$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$.</p>
            <p>$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
            <h3 class="font-semibold text-amber-300 flex items-center gap-1.5"><i class="fa-solid fa-square-root-variable"></i> Suma kwadratów &ge; 0</h3>
            <p>Kwadrat $(A - B)^2 \\ge 0$ dla dowolnych $A, B \\in \\mathbb{R}$.</p>
            <p>$2(a^2 + b^2 + c^2) - 2(ab+bc+ca) = (a-b)^2 + (b-c)^2 + (c-a)^2 \\ge 0$.</p>
            <p>Dopełnianie do kwadratu w trójmianach dwóch zmiennych.</p>
          </div>
          <div class="p-3 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
            <h3 class="font-semibold text-amber-300 flex items-center gap-1.5"><i class="fa-solid fa-certificate"></i> Wskazówki CKE</h3>
            <p>Pamiętaj o zdefiniowaniu dziedziny zmiennych ($k \\in \\mathbb{C}$).</p>
            <p>Wyciągnij żądany dzielnik przed nawias ($m \\cdot k$).</p>
            <p>Zawsze zakończ formalnym wnioskiem i $c.n.d.$</p>
          </div>
        </div>
      </div>

      <!-- Filters & Search Bar -->
      <div class="p-4 rounded-xl bg-slate-900/40 border border-slate-800 space-y-3">
        <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
          <div class="relative w-full sm:w-80">
            <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 text-xs"></i>
            <input type="text" id="search-input" onkeyup="filterTasks()" placeholder="Szukaj zadania (np. 35, 195, sześcian, 4.1)..."
              class="w-full pl-9 pr-3 py-1.5 rounded-lg bg-slate-800/80 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 transition">
          </div>
          
          <!-- Level Filter -->
          <div class="flex items-center gap-1.5 text-xs flex-wrap w-full sm:w-auto">
            <span class="text-slate-500 text-[11px] mr-1 hidden sm:inline">Poziom:</span>
            <button onclick="setLevelFilter('all', event)" class="level-btn active px-2.5 py-1 rounded-md bg-indigo-600 text-white font-medium">Wszystkie</button>
            <button onclick="setLevelFilter('podstawa', event)" class="level-btn px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300">Podstawa</button>
            <button onclick="setLevelFilter('rozszerzenie', event)" class="level-btn px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300">Rozszerzenie (R)</button>
          </div>
        </div>

        <!-- Category Filter -->
        <div class="flex items-center gap-1.5 text-xs flex-wrap border-t border-slate-800/80 pt-2.5">
          <span class="text-slate-500 text-[11px] mr-1">Źródło:</span>
          <button onclick="setCategoryFilter('all', event)" class="cat-btn active px-2.5 py-1 rounded-md bg-amber-600 text-white font-medium">Wszystkie źródła (__COUNT__)</button>
          <button onclick="setCategoryFilter('zbior', event)" class="cat-btn px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300">Zbiór Maturalny (35–68) [34]</button>
          <button onclick="setCategoryFilter('podrecznik-41', event)" class="cat-btn px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300">Podręcznik 4.1 (Podzielność) [13]</button>
          <button onclick="setCategoryFilter('podrecznik-42', event)" class="cat-btn px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300">Podręcznik 4.2 (Nierówności) [13]</button>
          <button onclick="setCategoryFilter('temat-1-2', event)" class="cat-btn px-2.5 py-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300">Działy 1 i 2 (Baza) [8]</button>
        </div>
      </div>

      <!-- Task Cards Wrapper -->
      <div class="space-y-6" id="tasks-wrapper">
__TASKS__
      </div>

    </div>
  </main>

  <!-- Footer -->
  <footer class="border-t border-slate-800 bg-slate-900/60 py-8 px-4 sm:px-6 mt-16 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto space-y-2">
      <p>Baza Zadań i Rozwiązań Maturalnych z Matematyki &bull; mgr M. Kucharska, mgr A. Piłat &bull; ZSE</p>
      <p class="text-slate-600">Przygotowanie do sprawdzianu: Dowody algebraiczne, podzielnościowe, nierówności i teoria liczb.</p>
    </div>
  </footer>

  <script>
    function toggleSolution(id) {
      const sol = document.getElementById('solution-' + id);
      const icon = document.getElementById('icon-' + id);
      if (sol) {
        sol.classList.toggle('hidden');
        if (window.renderMathInElement) renderMathInElement(sol);
      }
      if (icon) {
        icon.classList.toggle('fa-chevron-down');
        icon.classList.toggle('fa-chevron-up');
      }
    }

    let allExpanded = false;
    function toggleAllSolutions() {
      allExpanded = !allExpanded;
      const solutions = document.querySelectorAll('.task-solution');
      const icons = document.querySelectorAll('.solution-icon');
      solutions.forEach(s => {
        if (allExpanded) {
          s.classList.remove('hidden');
          if (window.renderMathInElement) renderMathInElement(s);
        } else {
          s.classList.add('hidden');
        }
      });
      icons.forEach(ic => {
        if (allExpanded) {
          ic.classList.remove('fa-chevron-down');
          ic.classList.add('fa-chevron-up');
        } else {
          ic.classList.remove('fa-chevron-up');
          ic.classList.add('fa-chevron-down');
        }
      });
      document.getElementById('toggle-all-text').innerText = allExpanded ? 'Zwiń wszystkie rozwiązania' : 'Rozwiń wszystkie rozwiązania';
    }

    let currentCategory = 'all';
    let currentLevel = 'all';

    function filterTasks() {
      const query = document.getElementById('search-input').value.toLowerCase();
      const cards = document.querySelectorAll('.task-card');
      let visibleCount = 0;

      cards.forEach(c => {
        const text = c.innerText.toLowerCase();
        const matchesQuery = !query || text.includes(query);
        const matchesCategory = currentCategory === 'all' || c.getAttribute('data-category') === currentCategory;
        const matchesLevel = currentLevel === 'all' || c.getAttribute('data-level') === currentLevel;

        if (matchesQuery && matchesCategory && matchesLevel) {
          c.classList.remove('hidden');
          visibleCount++;
        } else {
          c.classList.add('hidden');
        }
      });

      const badge = document.getElementById('task-badge-count');
      if (badge) badge.innerText = visibleCount + ' zadań';
    }

    function setCategoryFilter(cat, ev) {
      currentCategory = cat;
      document.querySelectorAll('.cat-btn').forEach(btn => {
        btn.classList.remove('bg-amber-600', 'text-white', 'font-medium');
        btn.classList.add('bg-slate-800', 'text-slate-300');
      });
      if (ev && ev.target) {
        ev.target.classList.add('bg-amber-600', 'text-white', 'font-medium');
        ev.target.classList.remove('bg-slate-800', 'text-slate-300');
      }
      filterTasks();
    }

    function setLevelFilter(lvl, ev) {
      currentLevel = lvl;
      document.querySelectorAll('.level-btn').forEach(btn => {
        btn.classList.remove('bg-indigo-600', 'text-white', 'font-medium');
        btn.classList.add('bg-slate-800', 'text-slate-300');
      });
      if (ev && ev.target) {
        ev.target.classList.add('bg-indigo-600', 'text-white', 'font-medium');
        ev.target.classList.remove('bg-slate-800', 'text-slate-300');
      }
      filterTasks();
    }

    window.addEventListener('DOMContentLoaded', () => {
      const toc = document.getElementById('sidebar-toc');
      const cards = document.querySelectorAll('.task-card');
      
      cards.forEach(card => {
        const id = card.id;
        const title = card.getAttribute('data-title') || id;
        const isR = card.getAttribute('data-level') === 'rozszerzenie';
        const a = document.createElement('a');
        a.href = '#' + id;
        a.className = 'block px-2.5 py-1.5 rounded hover:bg-slate-800 text-slate-300 hover:text-white transition truncate flex items-center justify-between';
        a.innerHTML = `<span class="truncate">${title}</span> ${isR ? '<span class="text-[10px] bg-amber-500/20 text-amber-300 px-1 rounded font-mono ml-1">R</span>' : ''}`;
        toc.appendChild(a);
      });
    });
  </script>
</body>
</html>
"""

html_content = TEMPLATE.replace("__TASKS__", tasks_html).replace("__COUNT__", str(len(ALL_TASKS)))

with open("sprawdzian.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Wygenerowano pomyślnie plik sprawdzian.html!")
