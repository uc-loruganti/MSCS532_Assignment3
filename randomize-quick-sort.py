import random

def randomize_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    if low < high:
        pi = randomize_partition(arr, low, high)
        partition(arr, low, pi - 1)
        partition(arr, pi + 1, high)
    return arr

if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    print("Original array:", sample_array)
    sorted_array = partition(sample_array, 0, len(sample_array) - 1)
    print("Sorted array:", sorted_array)