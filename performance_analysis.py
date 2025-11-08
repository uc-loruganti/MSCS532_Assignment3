import time
import random
import sys

# Set a higher recursion limit
sys.setrecursionlimit(20000)

# Import the sorting algorithms from their respective files
from deterministic_quick_sort import quick_sort as deterministic_qs
from randomize_quick_sort import quick_sort as randomized_qs

def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def generate_repeated_elements_array(size):
    # Elements will be in the range 0 to size/10
    return [random.randint(0, size // 10) for _ in range(size)]

def time_algorithm(sort_function, arr):
    arr_copy = arr[:]  # Work on a copy to not affect other tests
    start_time = time.perf_counter()
    sort_function(arr_copy, 0, len(arr_copy) - 1)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    sizes = [100, 1000, 5000, 10000]
    datasets = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse-Sorted": generate_reverse_sorted_array,
        "Repeated Elements": generate_repeated_elements_array,
    }

    print(f"{'Dataset':<20} | {'Size':<10} | {'Deterministic QS (s)':<25} | {'Randomized QS (s)':<20}")
    print("-" * 85)

    for name, generator in datasets.items():
        for size in sizes:
            arr = generator(size)
            
            # Time Deterministic Quicksort
            try:
                det_time = time_algorithm(deterministic_qs, arr)
                det_time_str = f"{det_time:.6f}"
            except RecursionError:
                det_time_str = "RecursionError"

            # Time Randomized Quicksort
            try:
                rand_time = time_algorithm(randomized_qs, arr)
                rand_time_str = f"{rand_time:.6f}"
            except RecursionError:
                rand_time_str = "RecursionError"

            print(f"{name:<20} | {size:<10} | {det_time_str:<25} | {rand_time_str:<20}")
        print("-" * 85)

if __name__ == "__main__":
    main()
