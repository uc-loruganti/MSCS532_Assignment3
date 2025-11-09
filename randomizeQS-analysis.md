# Average-Case Analysis of Randomized Quicksort

This document provides an analysis of the average-case time complexity of Randomized Quicksort, demonstrating why it is O(n log n) with direct references to the [randomize_quick_sort.py](randomize_quick_sort.py) implementation.

### 1. Analysis

The dominant factor in Quicksort's runtime is the number of comparisons performed. In the provided code, these comparisons happen within the `partition` function, specifically in the `for` loop. The total running time is proportional to the total number of times the line `if arr[j] < pivot:` is executed across all calls to `partition`.

```python
# From randomize_quick_sort.py
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        # This comparison is the basis of the algorithm's runtime
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```


### 2. Using Indicator Random Variables

Let the set of input elements be `Z = {z_1, z_2, ..., z_n}`, where `z_i` is the i-th smallest element.
Let `X_ij` be the indicator random variable for the event that `z_i` and `z_j` are compared. The total number of comparisons `X` is `Σ Σ X_ij`.

To find the average-case complexity, we need `E[X] = Σ Σ P(z_i is compared with z_j)`.

### 3. Probability of Comparison

Two elements `z_i` and `z_j` (where `i < j`) are compared if and only if the **first pivot** selected from the subarray containing the range `{z_i, ..., z_j}` is either `z_i` or `z_j`. If any other element between them is chosen as the pivot first, they will be separated into different partitions and never be compared.

This crucial step of random pivot selection is handled by the `randomize_partition` function. It picks a random element within the current subarray `[low, high]` and swaps it with the last element, `arr[high]`, before calling the standard `partition` function.

```python
# From randomize_quick_sort.py
def randomize_partition(arr, low, high):
    # Pick a random pivot from the current subarray
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)
```

Because `random.randint(low, high)` chooses any index in the subarray with equal probability, any element in the set `{z_i, ..., z_j}` is equally likely to be the first pivot chosen from that set.

- The size of this set is `j - i + 1`.
- There are two "successful" outcomes for a comparison (the pivot is `z_i` or `z_j`).
- The probability of this event is: `P(z_i is compared with z_j) = 2 / (j - i + 1)`

### 4. Calculating the Expected Number of Comparisons

Substituting this probability back into our expectation formula gives:

`E[X] = Σ (from i=1 to n-1) Σ (from j=i+1 to n) [2 / (j - i + 1)]`

This summation can be shown to be bounded by the Harmonic series, leading to the result:

`E[X] < (n - 1) * 2 * H_n`

Where `H_n` (the n-th Harmonic number) is `O(log n)`.

Therefore, the total expected number of comparisons is `O(n log n)`.

### 5. Conclusion

The recursive structure of the `quick_sort` function defines how the problem is divided.

```python
# From randomize_quick_sort.py
def quick_sort(arr, low, high):
    if low < high:
        pi = randomize_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
```

The expected number of comparisons `E[X]` is `O(n log n)`. Since the runtime of `quick_sort` is dominated by these comparisons, the **average-case time complexity is O(n log n)**. The `randomize_partition` function is the key: it ensures that no specific input can consistently produce the unbalanced partitions that would lead to the O(n²) worst-case scenario.