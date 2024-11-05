import pytest
from io import StringIO
import sys

def format_table(benchmarks, algos, results):
    max_benchmark_width = max(len(b) for b in benchmarks)
    max_algo_width = max(len(a) for a in algos)
    
    header = f"| {'Benchmark':<{max_benchmark_width}} | " + \
             " | ".join(f"{algo:<{max_algo_width}}" for algo in algos) + " |"
    
    separator = "-" * len(header)

    rows = []
    for i, benchmark in enumerate(benchmarks):
        row = f"| {benchmark:<{max_benchmark_width}} | " + \
              " | ".join(f"{results[i][j]:<{max_algo_width}.2f}" for j in range(len(algos))) + " |"
        rows.append(row)
    
    print(header)
    print(separator)
    for row in rows:
        print(row)

def test1(capsys):
    format_table(["best case", "worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark  | quick sort  | merge sort  | bubble sort |
--------------------------------------------------------
| best case  | 1.23        | 1.56        | 2.00        |
| worst case | 3.30        | 2.90        | 3.90        |''' in captured.out

def test2(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark      | quick sort  | merge sort  | bubble sort |
------------------------------------------------------------
| best case      | 1.23        | 1.56        | 2.00        |
| the worst case | 3.30        | 2.90        | 3.90        |''' in captured.out

if __name__ == "__main__":
    pytest.main()