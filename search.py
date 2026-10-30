# ==========================================
# SEARCH ALGORITHMS
# ==========================================


# ------------------------------------------
# Linear Search
# Time Complexity: O(n)
# ------------------------------------------

def linear_search(data, target):

    comparisons = 0

    for i in range(len(data)):

        comparisons += 1

        if data[i] == target:
            return i, comparisons

    return -1, comparisons


# ------------------------------------------
# Binary Search
# Time Complexity: O(log n)
# ------------------------------------------

def binary_search(data, target):

    left = 0
    right = len(data) - 1

    comparisons = 0

    while left <= right:

        comparisons += 1

        mid = (left + right) // 2

        if data[mid] == target:

            return mid, comparisons

        elif data[mid] < target:

            left = mid + 1

        else:

            right = mid - 1

    return -1, comparisons


# ------------------------------------------
# Generate Dataset
# ------------------------------------------

def generate_dataset(size):

    return list(range(size))