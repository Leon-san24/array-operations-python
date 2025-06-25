# Explanation: MergeSort Algorithm

## Introduction
MergeSort is a powerful, recursive **sorting algorithm** that uses the "divide and conquer" approach. The file `algorithms/sort_list.py` provides a clear Python implementation of this principle.

---

## How It Works

### 1. Recursive Splitting

The `merge_sort(pList)` function recursively divides the input list in half until the resulting sublists each contain only one element. A list with a single element is, by definition, already sorted.


if len(pList) <= 1:
    return pList


### 2. Recursive Calls to merge_sort

The list is split into a left and a right half:

mid = len(pList) // 2
left = merge_sort(pList[:mid])
right = merge_sort(pList[mid:])

Each half is sorted independently through further recursive calls of `merge_sort`.

### 3. Merging the Sublists

Once the sublists are sorted, the `merge(pLeft, pRight)` helper function combines them. It compares the smallest remaining items in both lists and appends the smaller one to the result. When one list runs out of items, any remaining elements from the other list are added to the result.


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

## Example (Process)

Given the list `[3, 1, 4, 2]`:
1. **Split:** `[3, 1]` and `[4, 2]`
2. **Recursion:** `[3], [1], [4], [2]`
3. **Merge:** 
   - `[3]` and `[1]` → `[1, 3]`
   - `[4]` and `[2]` → `[2, 4]`
4. **Final Merge:** `[1, 3]` and `[2, 4]` → `[1, 2, 3, 4]`

---

## Advantages of MergeSort

- **Stable:** Preserves the order of equal elements
- **Performance:** Always O(n log n), even in the worst case
- **Good for large datasets** and external sorting

---

## Implementation in `sort_list.py`

The implementation follows the principle described above:
- `merge_sort(pList)` for splitting and recursion,
- `merge(pLeft, pRight)` for merging sorted sublists,
- well-documented with docstrings and straightforward logic.

---

## Conclusion

MergeSort is an elegant and efficient algorithm for sorting, appreciated for its recursive structure and consistent performance. The implementation in `sort_list.py` clearly demonstrates its functionality and provides an excellent starting point for further exploration.

