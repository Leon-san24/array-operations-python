# Erklärung: BubbleSort-Algorithmus

## Einleitung
Der BubbleSort-Algorithmus ist ein sehr einfacher Sortieralgorithmus, der in `algorithms/sort_list.py` unter der Funktion `bubble_sort(pList)` implementiert ist. BubbleSort arbeitet, indem er wiederholt benachbarte Paare von Elementen vergleicht und vertauscht, falls sie in der falschen Reihenfolge stehen.

---

## Funktionsweise

### Iteratives Durchlaufen der Liste

Die Funktion `bubble_sort(pList)` besteht aus zwei verschachtelten Schleifen:  
- Die äußere Schleife steuert, wie oft die Liste durchlaufen wird  
- Die innere Schleife vergleicht und vertauscht jeweils benachbarte Elemente


for i in range(len(pList)):
    for j in range(len(pList)-i-1):
        if pList[j] > pList[j+1]:
            pList[j], pList[j + 1] = pList[j + 1], pList[j]

In jedem Durchlauf der inneren Schleife „wandert“ das größte der verbleibenden unsortierten Elemente an das Ende der Liste („wie eine Blase nach oben“ – daher der Name).

---

## Schritt-für-Schritt-Beispiel

Gegeben die Liste `[4, 2, 3, 1]`:

1. **Erster Durchlauf:**
   - Vergleiche 4 und 2 → tausche: `[2, 4, 3, 1]`
   - Vergleiche 4 und 3 → tausche: `[2, 3, 4, 1]`
   - Vergleiche 4 und 1 → tausche: `[2, 3, 1, 4]`

2. **Zweiter Durchlauf:**
   - Vergleiche 2 und 3 → kein Tausch.
   - Vergleiche 3 und 1 → tausche: `[2, 1, 3, 4]`

3. **Dritter Durchlauf:**
   - Vergleiche 2 und 1 → tausche: `[1, 2, 3, 4]`

4. **Jetzt ist die Liste sortiert.**

---

## Eigenschaften des BubbleSort-Algorithmus

- **Einfach und leicht verständlich**
- **Stabil:** Gleiche Elemente behalten ihre Reihenfolge
- **Komplexität:** O(n²); ineffizient für große Listen
- **In-Place:** Es wird kein zusätzlicher Speicher benötigt

---

## Umsetzung in `sort_list.py`

Die Implementierung in der Datei entspricht dem klassischen BubbleSort mit verschachtelten Schleifen.  
Dank der Docstrings ist die Funktion gut dokumentiert und eignet sich hervorragend, um die Arbeitsweise unmittelbar am Code nachzuvollziehen.

---

## Fazit

BubbleSort ist zwar für große Listen wenig effizient, aber als Lehrbeispiel und zum Verständnis von Sortieralgorithmen sehr hilfreich.  
Die Implementierung in `sort_list.py` ist ein typisches Beispiel, wie BubbleSort in Python realisiert werden kann.

