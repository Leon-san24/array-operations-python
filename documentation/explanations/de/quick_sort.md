# Erklärung: BubbleSort-Algorithmus

## Einleitung
Der Quicksort ist ein sortier algoryhtmus der sich eine Zahl aus der Liste nimmt und dann alle kleineren Zahlen
auf die linke seite davon räumt und die größeren auf die recjte seite packt.

---

## Funktionsweise

### Rekursiver ansatz für erhöte Geschwindigkeit

Die Funktion des Quicksorts besteht daraus die Elemente anhand eines "divider" zu sortieren und
dann die Liste zu teilen und denn Algorythmus dann auf beide teile erneut anzuwenden



---

## Schritt-für-Schritt-Beispiel

Gegeben die Liste `[4, 2, 5, 1, 3]`:

1. **Erster Durchlauf:**
   - nehme divider => 3
   - Vergleiche 4 und 3 tausche : `[3, 2, 5, 1, 4]` setze ende runter
   - Vergleiche 3 und 3 kein tausch : `[3, 2, 5, 1, 4]` setze i hoch
   - Vergleiche 2 und 3 kein tausch : `[3, 2, 5, 1, 4]` setze i hoch
   - Vergleiche 5 und 3 tausche : `[3, 2, 1, 5, 4]` setze ende runter
   - i==ende also break

2. **Zweiter Durchlauf Teil 1:**
   - Gegebener Teil der Liste `[5, 4]`:
   - nehme divider => 4
   - Vergleiche 5 und 4 → tausche : `[4, 5]` setze ende runter.
   - i==ende also break

   **Zweiter Durchlauf Teil 2:**
   - Gegebener Teil der Liste `[3, 2, 1]`
   - nehme divider => 1
   - Vergleiche 3 und 1 → tausche : `[1, 2, 3]` setze ende runter.
   - Vergleiche 1 und 1 kein tausch : `[1, 2, 3]` setze i hoch
   - Vergleiche 2 und 1 kein tausch : `[1, 2, 3]` setze i hoch
   - i==ende also break

3. **Dritter Durchlauf Teil 1:**
   - Gegebener Teil der Liste `[5]`:
   - nur ein element also break

   **Dritter Durchlauf Teil 2:**
   - Gegebener Teil der Liste `[4]`:
   - nur ein element also break

   **Dritter Durchlauf Teil 3:**
   - Gegebener Teil der Liste `[2, 3]`:
   - nehme divider => 3
   - Vergleiche 2 und 3 kein tausch : `[2, 3]` setze i hoch
   - i==ende also break

   **Dritter Durchlauf Teil 4:**
   - Gegebener Teil der Liste `[1]`:
   - nur ein element also break

4. **Vierter Durchlauf Teil 1:**
   - Gegebener Teil der Liste `[3]`:
   - nur ein element also break

   **Vierter Durchlauf Teil 2:**
   - Gegebener Teil der Liste `[2]`:
   - nur ein element also break

5. **Jetzt ist die Liste sortiert.**

---

## Eigenschaften des QuickSort-Algorithmus

- **leicht verständlich**
- **Komplexität:** sehr Effizient
- **In-Place:** Es wird kein zusätzlicher Speicher benötigt

---

## Fazit

Quicksort ist Einfach verständlich aber durch die Rekursion etwas komplexer in der Anwendung als
andere Sortier Algorythmusse allerdings ein schneller und effizienter Algorythmus.

