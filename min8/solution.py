import math

#min6
def flatten(lst: list, depth = math.inf) -> list:
    if depth < 0:
        raise NameError('Negative depth')
    result = []
    for el in lst:
        if isinstance(el, list) and depth > 0:
            for fel in flatten(el, depth - 1):
                result.append(fel)
        else:
            result.append(el)
    return result

def format_table(benchmarks, algos, results):
    max_benchmark_width = max(len(x) for x in benchmarks)
    max_algo_width = max(len(x) for x in algos)
    max_results_width = max(len(str(x))+3 for x in flatten(results)) # 3 - '.00'
    max_width = max(max_benchmark_width, max_algo_width, max_results_width)
    
    header = f"| {'Benchmark':<{max_width}} | " + \
             " | ".join(f"{algo:<{max_width}}" for algo in algos) + " |"
    
    separator = "-" * len(header)

    rows = []
    for i, benchmark in enumerate(benchmarks):
        row = f"| {benchmark:<{max_width}} | " + \
              " | ".join(f"{results[i][j]:<{max_width}.2f}" for j in range(len(algos))) + " |"
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
    assert '''| Benchmark   | quick sort  | merge sort  | bubble sort |
---------------------------------------------------------
| best case   | 1.23        | 1.56        | 2.00        |
| worst case  | 3.30        | 2.90        | 3.90        |''' in captured.out

def test2(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark      | quick sort     | merge sort     | bubble sort    |
---------------------------------------------------------------------
| best case      | 1.23           | 1.56           | 2.00           |
| the worst case | 3.30           | 2.90           | 3.90           |''' in captured.out

def test3(capsys):
    format_table(["b", "w"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark   | quick sort  | merge sort  | bubble sort |
---------------------------------------------------------
| b           | 1.23        | 1.56        | 2.00        |
| w           | 3.30        | 2.90        | 3.90        |''' in captured.out
    
def test4(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[11212121212.23, 112121212.56, 212121212.0], [312121212.3, 212121212.9, 31212121212.9]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark         | quick sort        | merge sort        | bubble sort       |
---------------------------------------------------------------------------------
| best case         | 11212121212.23    | 112121212.56      | 212121212.00      |
| the worst case    | 312121212.30      | 212121212.90      | 31212121212.90    |''' in captured.out

def test5(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[10**16, 10**16, 10**16], [10**16, 10**16, 10**16]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark            | quick sort           | merge sort           | bubble sort          |
---------------------------------------------------------------------------------------------
| best case            | 10000000000000000.00 | 10000000000000000.00 | 10000000000000000.00 |
| the worst case       | 10000000000000000.00 | 10000000000000000.00 | 10000000000000000.00 |''' in captured.out
