# Explanation: BubbleSort Algorithm

## Introduction
The BubbleSort algorithm is a very simple sorting algorithm, as implemented in the function `bubble_sort(pList)` in `algorithms/sort_list.py`. BubbleSort repeatedly steps through the list, compares adjacent pairs and swaps them if they are in the wrong order.

---

## How It Works

### Iterative List Traversal

The `bubble_sort(pList)` function uses two nested loops:  
- The outer loop tracks how many times we've traversed the list  
- The inner loop compares and swaps each pair of adjacent elements if necessary


for i in range(len(pList)):
    for j in range(len(pList)-i-1):
        if pList[j] > pList[j+1]:
            pList[j], pList[j + 1] = pList[j + 1], pList[j]

With each pass of the inner loop, the largest unsorted element "bubbles up" to the end of the list—hence the term BubbleSort.

---

## Step-by-Step Example

Given the list `[4, 2, 3, 1]`:

1. **First pass:**
   - Compare 4 and 2 → swap: `[2, 4, 3, 1]`
   - Compare 4 and 3 → swap: `[2, 3, 4, 1]`
   - Compare 4 and 1 → swap: `[2, 3, 1, 4]`

2. **Second pass:**
   - Compare 2 and 3 → no swap
   - Compare 3 and 1 → swap: `[2, 1, 3, 4]`

3. **Third pass:**
   - Compare 2 and 1 → swap: `[1, 2, 3, 4]`

4. **Now, the list is sorted!**

---

## Characteristics of BubbleSort

- **Simple and easy to understand**
- **Stable:** Equal elements retain their relative order
- **Complexity:** O(n²); inefficient for large lists
- **In-place:** Requires no extra storage

---

## Implementation in `sort_list.py`

The implementation in this file follows traditional BubbleSort using nested loops.  
Thanks to the included docstrings, the function is well-documented and ideal for understanding how BubbleSort works in Python.

---

## Conclusion

While BubbleSort is not suitable for large datasets due to inefficiency, it’s excellent for didactic purposes and understanding the basics of sorting algorithms.  
The implementation in `sort_list.py` is a classic Python example of BubbleSort.

