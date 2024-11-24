def format_table(benchmarks, algos, results):
    column_width = []
    column_width.append(max([len(x) for x in benchmarks] + [len("Benchmark")]))
    for i in range(len(algos)):
        column_width.append(max([len(algos[i])] + [len(str(x[i]))+3 for x in results]))
    
    header = f"| {'Benchmark':<{column_width[0]}} | " + \
             " | ".join(f"{algo:<{column_width[i+1]}}" for i, algo in enumerate(algos)) + " |"
    
    separator = "-" * len(header)

    rows = []
    for i, benchmark in enumerate(benchmarks):
        row = f"| {benchmark:<{column_width[0]}} | " + \
              " | ".join(f"{results[i][j]:<{column_width[j+1]}.2f}" for j in range(len(algos))) + " |"
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
    assert '''| Benchmark  | quick sort | merge sort | bubble sort |
------------------------------------------------------
| best case  | 1.23       | 1.56       | 2.00        |
| worst case | 3.30       | 2.90       | 3.90        |''' in captured.out
    
def test2(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[11212121212.23, 112121212.56, 212121212.0], [312121212.3, 212121212.9, 31212121212.9]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark      | quick sort        | merge sort      | bubble sort      |
---------------------------------------------------------------------------
| best case      | 11212121212.23    | 112121212.56    | 212121212.00     |
| the worst case | 312121212.30      | 212121212.90    | 31212121212.90   |''' in captured.out

def test3(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[10**16, 10**16, 10**16], [10**16, 10**16, 10**16]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark      | quick sort           | merge sort           | bubble sort          |
---------------------------------------------------------------------------------------
| best case      | 10000000000000000.00 | 10000000000000000.00 | 10000000000000000.00 |
| the worst case | 10000000000000000.00 | 10000000000000000.00 | 10000000000000000.00 |''' in captured.out

def test4(capsys):
    format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[10**16, 10**5, 10**2], [10**16, 10**5, 10**2]])
    
    captured = capsys.readouterr()
    assert '''| Benchmark      | quick sort           | merge sort | bubble sort |
--------------------------------------------------------------------
| best case      | 10000000000000000.00 | 100000.00  | 100.00      |
| the worst case | 10000000000000000.00 | 100000.00  | 100.00      |''' in captured.out
