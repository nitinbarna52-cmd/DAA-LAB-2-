
import time
import tracemalloc


# ==========================================================
# SEARCH ALGORITHMS
# ==========================================================

def linear_search(input_size):

    data = list(range(input_size))

    # Worst-case target
    target = input_size - 1

    comparisons = 0

    for i in range(len(data)):

        comparisons += 1

        if data[i] == target:

            return i, comparisons

    return -1, comparisons


def binary_search(input_size):

    # Binary Search requires sorted data
    data = list(range(input_size))

    # Worst-case target
    target = input_size - 1

    low = 0
    high = len(data) - 1

    comparisons = 0

    while low <= high:

        mid = (low + high) // 2

        comparisons += 1

        if data[mid] == target:

            return mid, comparisons

        elif data[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    return -1, comparisons


# ==========================================================
# LOOP ALGORITHMS
# ==========================================================

def single_loop(input_size):

    operations = 0

    total = 0

    for i in range(input_size):

        total += i

        operations += 1

    return total, operations


def nested_loop(input_size):

    operations = 0

    total = 0

    for i in range(input_size):

        for j in range(input_size):

            total += 1

            operations += 1

    return total, operations


# ==========================================================
# RECURSIVE FACTORIAL
# ==========================================================

def recursive_factorial(input_size):

    operations = 0

    def factorial(n):

        nonlocal operations

        operations += 1

        if n <= 1:

            return 1

        return n * factorial(n - 1)

    result = factorial(input_size)

    return result, operations


# ==========================================================
# ITERATIVE FACTORIAL
# ==========================================================

def iterative_factorial(input_size):

    operations = 0

    result = 1

    for i in range(1, input_size + 1):

        result *= i

        operations += 1

    return result, operations


# ==========================================================
# AVAILABLE ALGORITHMS
# ==========================================================

ALGORITHMS = {

    "Linear Search":
        linear_search,

    "Binary Search":
        binary_search,

    "Single Loop Traversal":
        single_loop,

    "Nested Loop Traversal":
        nested_loop,

    "Recursive Factorial":
        recursive_factorial,

    "Iterative Factorial":
        iterative_factorial

}


# ==========================================================
# RUN ONE BENCHMARK
# ==========================================================

def run_benchmark(function, input_size):

    # ------------------------------------------------------
    # Start memory measurement
    # ------------------------------------------------------

    tracemalloc.start()

    # ------------------------------------------------------
    # Start timer
    # ------------------------------------------------------

    start_time = time.perf_counter()

    # ------------------------------------------------------
    # Execute algorithm
    # ------------------------------------------------------

    output = function(input_size)

    # ------------------------------------------------------
    # End timer
    # ------------------------------------------------------

    end_time = time.perf_counter()

    # ------------------------------------------------------
    # Get memory usage
    # ------------------------------------------------------

    current_memory, peak_memory = tracemalloc.get_traced_memory()

    # ------------------------------------------------------
    # Stop memory measurement
    # ------------------------------------------------------

    tracemalloc.stop()

    # ------------------------------------------------------
    # Calculate execution time
    # ------------------------------------------------------

    execution_time = end_time - start_time

    # ------------------------------------------------------
    # Convert bytes to MB
    # ------------------------------------------------------

    memory_usage = peak_memory / (1024 * 1024)

    # ------------------------------------------------------
    # Check function output
    # ------------------------------------------------------

    if isinstance(output, tuple):

        result = output[0]

        operations = output[1]

    else:

        result = output

        operations = None

    # ------------------------------------------------------
    # Return benchmark information
    # ------------------------------------------------------

    return {

        "result":
            result,

        "operations":
            operations,

        "execution_time":
            execution_time,

        "memory_usage":
            memory_usage
    }


# ==========================================================
# AUTOMATED BENCHMARK ENGINE
# ==========================================================

def automated_benchmark(
    function,
    input_sizes,
    algorithm_name
):

    results = []

    for size in input_sizes:

        try:

            result = run_benchmark(
                function,
                size
            )

            results.append({

                "Algorithm":
                    algorithm_name,

                "Input Size":
                    size,

                "Operations / Comparisons":
                    result["operations"],

                "Execution Time (seconds)":
                    result["execution_time"],

                "Memory Usage (MB)":
                    result["memory_usage"],

                "Result":
                    result["result"]
            })

        except RecursionError:

            results.append({

                "Algorithm":
                    algorithm_name,

                "Input Size":
                    size,

                "Operations / Comparisons":
                    None,

                "Execution Time (seconds)":
                    None,

                "Memory Usage (MB)":
                    None,

                "Result":
                    "Recursion Error"
            })

        except Exception as error:

            results.append({

                "Algorithm":
                    algorithm_name,

                "Input Size":
                    size,

                "Operations / Comparisons":
                    None,

                "Execution Time (seconds)":
                    None,

                "Memory Usage (MB)":
                    None,

                "Result":
                    f"Error: {error}"
            })

    return results