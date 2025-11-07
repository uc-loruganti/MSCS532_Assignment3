
import argparse

# Quick Sort Implementation.
# Returns the index of the pivot element after partitioning
def partition(arr, low, high):
    # pivot element is taken to be the first element
    pivot = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[i] = arr[i], arr[low]
    return i

# Recursive function to perform quick sort
def quick_sort(arr, low, high):
    # if low index is less than high index then only we need to sort
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        # Recursively sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    print("Quick Sort Implementation")
    parser = argparse.ArgumentParser(description="Quick Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    print("Original array:", elements)
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array:", elements)
