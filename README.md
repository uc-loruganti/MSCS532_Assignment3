# MSCS532_Assignment3

## Reports:
Randomized Quick Sort analysis : [randomizeQS-analysis.md](randomizeQS-analysis.md)

Deterministic vs. Randomized Quick Sort analysis : [QS-Comparison.md](QS-Comparison.md)

Hash Table analysis : [hashtable-analysis.md](hashtable-analysis.md)

## Usage

### Quicksort 

#### `randomize_quick_sort.py`

Sorts a list of numbers using the Randomized Quicksort algorithm.

**Usage:**
```bash
python randomize_quick_sort.py --elements <num1> <num2> ...
```

**Example:**
```bash
python randomize_quick_sort.py --elements 5 2 9 1 7 4
```

#### `deterministic_quick_sort.py`

Sorts a list of numbers using Deterministic Quicksort, which selects the first element as the pivot.

**Usage:**
```bash
python deterministic_quick_sort.py --elements <num1> <num2> ...
```

**Example:**
```bash
python deterministic_quick_sort.py --elements 5 2 9 1 7 4
```

### Performance Analysis

#### `performance_analysis.py`

Runs an empirical analysis comparing the performance of Deterministic and Randomized Quicksort across different data distributions (random, sorted, reverse-sorted, and repeated elements) and prints the results to the console.

**Usage:**
```bash
python performance_analysis.py
```

### Universal Hash Table

#### `hashtable-universalhash.py`

Implements a persistent command-line hash table that uses universal hashing. 

**Usage:**
```bash
python performance_analysis.py
```

**Output:**
```
Universal Hash Table Implementation
Search key 5: apple
Search key 15: banana
Search key 25: cherry
Search key 15 after deletion: None
```


