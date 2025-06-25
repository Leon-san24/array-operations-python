# Explanation: Quicksort Algorithm

## Introduction
Quicksort is a sorting algorithm that selects a number from the list and then moves all smaller numbers to the left of it and all larger numbers to the right.

---

## How it Works

### Recursive Approach for Increased Speed

The function of Quicksort consists of sorting the elements based on a "divider" and then splitting the list and applying the algorithm again to both parts.



---

## Step-by-Step Example

Given the list `[4, 2, 5, 1, 3]`:

1. **First Pass:**
   - Choose divider => 3
   - Compare 4 and 3 → swap: `[3, 2, 5, 1, 4]` move end down
   - Compare 3 and 3 → no swap: : `[3, 2, 5, 1, 4]` move i up
   - Compare 2 and 3 → no swap: : `[3, 2, 5, 1, 4]` move i up
   - Compare 5 and 3 → swap: : `[3, 2, 1, 5, 4]` move end down
   - i == end → break

2. **Second Pass Part 1:**
   - Given sublist `[5, 4]`:
   - Choose divider => 4
   - Compare 5 and 4 → swap: : `[4, 5]` move end down
   - i == end → break

   **Second Pass Part 2:**
   - Given sublist `[3, 2, 1]`
   - Choose divider => 1
   - Compare 3 and 1 → swap: : `[1, 2, 3]` move end down
   - Compare 1 and 1 → no swap: `[1, 2, 3]` move i up
   - Compare 2 and 1 → no swap: `[1, 2, 3]` move i up
   - i == end → break

3. **Third Pass Part 1:**
   - Given sublist `[5]`:
   - Only one element → break

   **Third Pass Part 2:**
   - Given sublist `[4]`:
   - Only one element → break

   **Third Pass Part 3:**
   - Given sublist `[2, 3]`:
   - Choose divider => 3
   - Compare 2 and 3 → no swap: `[2, 3]` move i up
   - i == end → break

   **Third Pass Part 4:**
   - Given sublist `[1]`:
   - Only one element → break

4. **Fourth Pass Part 1:**
   - Given sublist `[3]`:
   - Only one element → break

   **Fourth Pass Part 2:**
   - Given sublist `[2]`:
   - Only one element → break

5. **Now the list is sorted.**

---

## Properties of the QuickSort Algorithm

- **Easy to understand**
- **Complexity:** Very efficient
- **In-place:** No additional memory needed

---

## Conclusion

Quicksort is easy to understand but a bit more complex in its application due to recursion, compared to other sorting algorithms. However, it is a fast and efficient algorithm.