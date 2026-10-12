# -*- coding: utf-8 -*-
"""
Aktualizuje nawigację we wszystkich plikach HTML w repozytorium:
- index.html (dodaje link w nawigacji oraz kartę sprawdzianu w katalogu)
- 1_liczby_rzeczywiste.html do 8_funkcje_wymierne.html (dodaje link w nawigacji)
"""

import glob
import re

nav_link_active = '''
        <!-- Sprawdzian Tab -->
        <a href="sprawdzian.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap bg-gradient-to-r from-amber-600 to-orange-600 text-white font-bold shadow-md shadow-orange-500/20 border border-amber-400/30">
          <i class="fa-solid fa-fire text-amber-200 animate-pulse"></i>
          <span>Sprawdzian</span>
        </a>'''

nav_link_inactive = '''
        <!-- Sprawdzian Tab -->
        <a href="sprawdzian.html" class="px-3 py-1.5 rounded-lg text-xs md:text-sm transition flex items-center gap-2 whitespace-nowrap text-amber-300 hover:text-white hover:bg-amber-600/20 border border-amber-500/30">
          <i class="fa-solid fa-fire text-amber-400"></i>
          <span>Sprawdzian</span>
        </a>'''

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Add link to nav if not present
if 'href="sprawdzian.html"' not in index_content:
    # insert before </nav> or after 8_funkcje_wymierne.html
    target = '<span>8. Funkcje wymierne</span>\n        </a>'
    if target in index_content:
        index_content = index_content.replace(target, target + '\n' + nav_link_inactive)
    else:
        # fallback replace
        index_content = index_content.replace('8_funkcje_wymierne.html', '8_funkcje_wymierne.html')
        target2 = '8_funkcje_wymierne.html" class="'
        idx = index_content.find('8_funkcje_wymierne.html')
        end_a = index_content.find('</a>', idx)
        if end_a != -1:
            index_content = index_content[:end_a+4] + '\n' + nav_link_inactive + index_content[end_a+4:]

# Add featured Sprawdzian Card in index.html above module 1
sprawdzian_card = '''
      <!-- Featured Sprawdzian Card -->
      <div class="col-span-full group relative flex flex-col md:flex-row items-center justify-between rounded-2xl bg-gradient-to-r from-amber-950/40 via-orange-950/30 to-slate-900/80 border border-amber-500/40 p-6 sm:p-8 hover:border-amber-400/70 transition-all duration-300 shadow-xl shadow-orange-500/10">
        <div class="space-y-3 max-w-3xl">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/40">
            <i class="fa-solid fa-fire text-amber-400 animate-pulse"></i> Nowy Moduł Sprawdzianowy
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
            Sprawdzian: Dowody Algebraiczne & Teoria Liczb
          </h2>
          <p class="text-sm text-slate-300 leading-relaxed">
            Kompletne materiały powtórzeniowe: <strong>34 dowody ze zbioru maturalnego (Dowód 35–68)</strong>, 
            wszystkie zadania i ćwiczenia ze stron 178–184 podręcznika (<strong>Temat 4.1: Podzielność</strong> oraz <strong>Temat 4.2: Nierówności</strong>) 
            oraz zadania sprawdzianowe z <strong>Tematów 1 i 2</strong>.
          </p>
          <div class="flex flex-wrap gap-2 pt-1 text-xs">
            <span class="px-2.5 py-1 rounded-md bg-slate-900/80 text-amber-300 border border-amber-500/30"><i class="fa-solid fa-check mr-1 text-emerald-400"></i>68+ Zadań z pełnymi rozwiązaniami</span>
            <span class="px-2.5 py-1 rounded-md bg-slate-900/80 text-slate-300 border border-slate-700"><i class="fa-solid fa-brain mr-1 text-indigo-400"></i>AM &ge; GM i sumy kwadratów</span>
            <span class="px-2.5 py-1 rounded-md bg-slate-900/80 text-slate-300 border border-slate-700"><i class="fa-solid fa-shield-halved mr-1 text-sky-400"></i>Podzielność, modulo i iloczyny</span>
          </div>
        </div>
        <div class="mt-6 md:mt-0 flex flex-col items-center gap-2">
          <a href="sprawdzian.html" class="inline-flex items-center gap-3 px-6 py-3.5 rounded-xl bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white font-bold text-sm shadow-xl shadow-orange-600/30 transition-all hover:scale-105 whitespace-nowrap">
            <i class="fa-solid fa-fire"></i>
            Otwórz Sprawdzian
            <i class="fa-solid fa-arrow-right"></i>
          </a>
          <span class="text-[11px] text-slate-400">Poziom podstawowy i rozszerzony</span>
        </div>
      </div>
'''

if 'Sprawdzian: Dowody Algebraiczne' not in index_content:
    grid_target = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">'
    if grid_target in index_content:
        index_content = index_content.replace(grid_target, grid_target + '\n' + sprawdzian_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print("Zaktualizowano index.html")

# 2. Update all module files 1 to 8
for filename in glob.glob('[1-8]_*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="sprawdzian.html"' not in content:
        target = '<span>8. Funkcje wymierne</span>\n        </a>'
        if target in content:
            content = content.replace(target, target + '\n' + nav_link_inactive)
        else:
            idx = content.find('8_funkcje_wymierne.html')
            if idx != -1:
                end_a = content.find('</a>', idx)
                if end_a != -1:
                    content = content[:end_a+4] + '\n' + nav_link_inactive + content[end_a+4:]
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Zaktualizowano nawigację w {filename}")
    else:
        print(f"Pominięto (już zaktualizowano): {filename}")

print("Wszystkie nawigacje zaktualizowane pomyślnie!")
