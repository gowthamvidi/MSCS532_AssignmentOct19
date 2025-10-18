import random
import time

# --- Deterministic Quicksort ---
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  # choosing the last element as pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# --- Randomized Quicksort ---
def randomized_quicksort(arr):
    """Randomized Quicksort where pivot is chosen randomly from subarray."""
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x >= pivot and i != pivot_index]

    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# --- Helper for timing ---
def measure_time(sort_func, arr):
    start = time.perf_counter()
    result = sort_func(arr.copy())
    end = time.perf_counter()
    return round(end - start, 6), result

# --- Hardcoded Inputs ---
if __name__ == "__main__":
    # Small input sizes for clear demonstration
    inputs = {
        "Random (n=10)": [random.randint(0, 100) for _ in range(10)],
        "Sorted (n=10)": list(range(10)),
        "Reverse-sorted (n=10)": list(range(10, 0, -1)),
        "Nearly-sorted (n=10)": [1, 2, 3, 5, 4, 6, 7, 9, 8, 10],
        "Few-unique (n=10)": [random.choice([1, 2, 3]) for _ in range(10)],
        "Large Random (n=1000)": [random.randint(0, 10000) for _ in range(1000)]
    }

    print(f"{'Distribution':<25}{'Algorithm':<20}{'Time (sec)':<15}{'First 10 elements of result'}")
    print("-" * 85)

    for label, arr in inputs.items():
        for func in [quicksort, randomized_quicksort]:
            t, result = measure_time(func, arr)
            print(f"{label:<25}{func.__name__:<20}{t:<15}{str(result[:10])}")

    print("\nNotes:")
    print("- Deterministic Quicksort performs poorly on sorted/reverse-sorted data due to bad pivot selection.")
    print("- Randomized Quicksort is more stable across input types, avoiding consistent worst-case splits.")
    print("- On large random inputs, both have roughly O(n log n) performance but random pivoting gives better consistency.")
