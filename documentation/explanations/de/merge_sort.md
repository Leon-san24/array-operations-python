# Erklärung: MergeSort-Algorithmus

## Einleitung
Der MergeSort-Algorithmus ist ein leistungsstarkes, rekursives **Sortierverfahren** basierend auf dem "Teile-und-herrsche"-Prinzip. In der Datei `algorithms/sort_list.py` wird die Funktionsweise dieses Algorithmus in Python dargestellt.

---

## Funktionsweise

### 1. Rekursives Teilen der Liste
Die Funktion `merge_sort(pList)` teilt die Eingabeliste solange immer wieder in zwei Hälften, bis die zu sortierenden Teillisten nur noch aus einem Element bestehen. Listen mit nur einem Element sind per Definition bereits sortiert.


if len(pList) <= 1:
    return pList


### 2. Rekursiver Aufruf von merge_sort
Die Liste wird in eine linke (`left`) und rechte (`right`) Hälfte geteilt:

mid = len(pList) // 2
left = merge_sort(pList[:mid])
right = merge_sort(pList[mid:])

Jede Hälfte wird wiederum eigenständig sortiert, indem `merge_sort` erneut aufgerufen wird.

### 3. Das Mischen (Mergen) der Teillisten
Sobald die Unterlisten sortiert sind, übernimmt `merge(pLeft, pRight)` das Zusammenführen. Dabei werden stets die jeweils kleinsten noch nicht in die Ergebnisliste übernommenen Elemente beider Listen verglichen und das kleinere angehängt. Am Ende werden eventuelle Reste einer der beiden Listen direkt ans Ende der Ergebnisliste gehängt.


def merge(pLeft, pRight):
    sorted_list = []
    i = j = 0
    while i < len(pLeft) and j < len(pRight):
        if pLeft[i] < pRight[j]:
            sorted_list.append(pLeft[i])
            i += 1
        else:
            sorted_list.append(pRight[j])
            j += 1
    sorted_list.extend(pLeft[i:])
    sorted_list.extend(pRight[j:])
    return sorted_list


---

## Beispiel (Ablauf)

Gegeben die Liste `[3, 1, 4, 2]`:
1. **Teilen:** `[3, 1]` und `[4, 2]`
2. **Rekursion:** `[3], [1], [4], [2]`
3. **Sortiert Zusammenführen:** 
   - Merge `[3]` und `[1]` → `[1, 3]`
   - Merge `[4]` und `[2]` → `[2, 4]`
4. **Abschließendes Zusammenführen:** Merge `[1, 3]` und `[2, 4]` → `[1, 2, 3, 4]`

---

## Vorteile des MergeSort-Algorithmus

- **Stabilität:** Die relative Reihenfolge gleichwertiger Elemente bleibt erhalten.
- **Komplexität:** Garantiert immer eine Laufzeit von O(n log n), auch im schlechtesten Fall.
- **Geeignet für große Datenmengen** und externe Sortieraufgaben.

## Umsetzung in `sort_list.py`

Die Implementierung dort folgt exakt dem beschriebenen Prinzip:
- `merge_sort(pList)` für das Teilen und rekursive Sortieren,
- `merge(pLeft, pRight)` zum ordentlichen Zusammenführen,
- mit sauber dokumentierten Docstrings und nachvollziehbarer Logik.

---

## Fazit

MergeSort ist ein eleganter Algorithmus zum Sortieren, der durch seine rekursive Struktur und effizientes Mischen in der Praxis oft verwendet wird. Die Implementierung in `sort_list.py` eignet sich sehr gut, um das Funktionsprinzip zu verstehen und anzuwenden.

