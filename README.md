# DAA-LAB-2-
algorithm-performance-tool-  Nitin Barna

A Python-based performance analysis and benchmarking tool designed to execute, measure, and compare different algorithms and code implementations.

The project provides a Streamlit-based interface where users can select algorithms, provide input sizes, run benchmarks, and visualize performance using execution time, memory usage, and operation counts.

📌 Project Overview

The Algorithm Performance Tool is developed to understand and analyze the practical performance of algorithms.

The tool compares theoretical algorithmic complexity with experimental results obtained by executing algorithms on different input sizes.

The project focuses on:

Algorithm execution
Execution time measurement
Memory usage measurement
Operation/comparison counting
Automated benchmarking
Complexity comparison
Performance visualization
Scalability analysis
🚀 Features

1. Search Algorithms

The project implements:

Linear Search
Binary Search
The search module records:

Search result
Number of comparisons
Execution time
Memory usage
2. Code Benchmarking

The benchmarking module compares:

Single Loop Traversal
Nested Loop Traversal
Recursive Factorial
Iterative Factorial
Performance is measured using different input sizes.

3. Automated Benchmarking Engine

The automated benchmarking engine executes selected algorithms for multiple input sizes automatically.

It records:

Algorithm name
Input size
Operation count
Execution time
Memory usage
Result
This makes it easier to analyze how algorithm performance changes as the input size increases.

4. Complexity Analysis

The project compares theoretical and experimental performance.

Algorithm	Time Complexity	Space Complexity
Linear Search	O(n)	O(1)
Binary Search	O(log n)	O(1)
Single Loop Traversal	O(n)	O(1)
Nested Loop Traversal	O(n²)	O(1)
Recursive Factorial	O(n)	O(n)
Iterative Factorial	O(n)	O(1)
5. Performance Visualization

The Streamlit interface provides comparative charts for:

Search algorithm execution time
Search comparisons
Factorial execution time
Factorial memory usage
Loop execution time
Loop memory usage
These visualizations help identify growth trends and scalability differences between algorithms.

🛠️ Technologies Used

Programming Language

Python
Libraries

Streamlit
Pandas
NumPy
Matplotlib
Memory Profiler
Jupyter
Development Environment

Visual Studio Code
Python Virtual Environment
Git
GitHub
📁 Project Structure

algorithm-performance-tool-RudraJuyal/
│
├── app.py
│
├── search.py
├── benchmark_table.py
├── benchmark_engine.py
│
├── pages/
│   ├── 1_Search.py
│   ├── 2_Benchmark.py
│   ├── 3_Automated_Benchmark.py
│   └── 4_Visualizations.py
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── venv/
    └── (local virtual environment - not uploaded to GitHub)
The venv/ directory is excluded from GitHub using .gitignore.
⚙️ Installation

1. Clone the Repository

git clone https://github.com/Rudra1806yal/algorithm-performance-tool-RudraJuyal.git
Move into the project directory:

cd algorithm-performance-tool-RudraJuyal
2. Create a Virtual Environment

python -m venv venv
Activate the environment on Windows:

venv\Scripts\activate
3. Install Required Libraries

Install the dependencies using:

pip install -r requirements.txt
Alternatively:

pip install streamlit pandas matplotlib memory_profiler numpy jupyter
▶️ Running the Application

After activating the virtual environment, run:

streamlit run streamlit_app.py
Streamlit will start the application and provide a local URL, usually:

http://localhost:8501
Open the URL in a web browser to access the application.

🖥️ Application Modules

Home

The home page provides an overview of the Algorithm Performance Tool.

Search

Allows users to compare:

Linear Search
Binary Search
Users can specify an input size and search value.

Benchmark

Allows users to execute and compare:

Single Loop Traversal
Nested Loop Traversal
Recursive Factorial
Iterative Factorial
Automated Benchmark

Automatically executes selected algorithms for multiple input sizes and produces a performance table.

Visualizations

Displays charts comparing execution time, memory usage, and operation/comparison counts.

📊 Performance Metrics

Execution Time

Execution time measures how long an algorithm takes to complete.

The project uses Python's:

time.perf_counter()
for high-resolution timing.

Memory Usage

Memory consumption is measured using Python's:

tracemalloc
The peak memory usage is recorded during execution.

Operation Count

Operation counts help determine how much computational work an algorithm performs.

For search algorithms, the number of comparisons is recorded.

For loop and factorial implementations, iterations or recursive operations can be counted.

📈 Complexity and Scalability

The project demonstrates how different complexity classes affect scalability.

Binary Search

O(log n)
Binary Search scales efficiently because the search space is divided approximately in half after every comparison.

Linear Search

O(n)
The number of comparisons increases approximately linearly with the input size.

Single Loop

O(n)
The number of operations grows linearly with the input.

Nested Loop

O(n²)
The number of operations grows quadratically, causing performance to decrease rapidly for large inputs.

Recursive Factorial

Time: O(n)
Space: O(n)
The recursive implementation uses additional call-stack memory.

Iterative Factorial

Time: O(n)
Space: O(1)
The iterative implementation avoids recursive call-stack overhead.

🔬 Experimental Observations

The benchmarking experiments demonstrate the following general trends:

Binary Search performs fewer comparisons than Linear Search for large sorted datasets.
Linear Search shows approximately linear growth in execution time.
Single Loop Traversal demonstrates linear growth.
Nested Loop Traversal grows much faster because of its quadratic complexity.
Recursive Factorial requires additional stack memory.
Iterative Factorial provides better auxiliary-space efficiency.
Operation counts provide useful information about algorithmic work.
Experimental execution times can vary depending on the computer and system workload.
The experimental results are therefore used together with theoretical complexity analysis to understand algorithm performance.

🎯 Project Objectives

The main objectives of this project are:

To implement different searching and algorithmic programs.
To measure execution time for different input sizes.
To measure memory consumption.
To count algorithmic operations and comparisons.
To automate the benchmarking process.
To compare theoretical and experimental complexity.
To visualize algorithm performance using charts.
To understand scalability and efficiency.
To analyze time-space trade-offs.
To provide an easy-to-use performance analysis interface.
📚 Key Learning Outcomes

Through this project, the following concepts are demonstrated:

Algorithm analysis
Big-O notation
Time complexity
Space complexity
Searching algorithms
Recursion
Iteration
Performance measurement
Benchmarking
Data visualization
Python programming
Streamlit application development
Git and GitHub
Virtual environments
⚠️ Notes

Experimental execution times may vary depending on:

Processor performance
Available RAM
Python version
Operating-system activity
Background applications
Python interpreter overhead
Memory allocation
System load
Therefore, theoretical complexity should be used to understand the growth pattern, while experimental measurements represent the practical performance on the system used for testing.

👨‍💻 Author

Nitin Barna

Bachelor of Computer Applications
AI & Data Science

