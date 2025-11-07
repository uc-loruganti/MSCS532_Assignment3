import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomize_partition(arr, low, high):
    # pick a random pivot and swap with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def quick_sort(arr, low, high):
    if low < high:
        # partitioning index 
        pi = randomize_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    print("Original array:", sample_array)
    quick_sort(sample_array, 0, len(sample_array) - 1)
    print("Sorted array:", sample_array)
