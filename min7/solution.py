import pytest
from io import StringIO
import sys

def deprecated(since=None, will_be_removed=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name = func.__name__
            if since and will_be_removed:
                print(f"Warning: function {name} is deprecated since version {since}. It will be removed in version {will_be_removed}.")
            elif since:
                print(f"Warning: function {name} is deprecated since version {since}. It will be removed in future versions.")
            elif will_be_removed:
                print(f"Warning: function {name} is deprecated. It will be removed in version {will_be_removed}.")
            else:
                print(f"Warning: function {name} is deprecated. It will be removed in future versions.")
                
            return func(*args, **kwargs)
        return wrapper
    return decorator

def test1(capsys):
    @deprecated()
    def foo1():
        print("Hello from foo1")

    foo1()
    captured = capsys.readouterr()
    assert "Warning: function foo1 is deprecated. It will be removed in future versions." in captured.out
    assert "Hello from foo1" in captured.out

def test2(capsys):
    @deprecated(since="4.2.0", will_be_removed="5.0.1")
    def foo2():
        print("Hello from foo2")

    foo2()
    captured = capsys.readouterr()
    assert "Warning: function foo2 is deprecated since version 4.2.0. It will be removed in version 5.0.1." in captured.out
    assert "Hello from foo2" in captured.out

def test3(capsys):
    @deprecated(since="4.2.0")
    def foo3():
        print("Hello from foo3")

    foo3()
    captured = capsys.readouterr()
    assert "Warning: function foo3 is deprecated since version 4.2.0. It will be removed in future versions." in captured.out
    assert "Hello from foo3" in captured.out

def test4(capsys):
    @deprecated(will_be_removed="5.0.1")
    def foo4():
        print("Hello from foo4")

    foo4()
    captured = capsys.readouterr()
    assert "Warning: function foo4 is deprecated. It will be removed in version 5.0.1." in captured.out
    assert "Hello from foo4" in captured.out

def test5(capsys):
    @deprecated()
    def foo5():
        print("Hello from foo5")

    foo5()
    captured = capsys.readouterr()
    assert "Warning: function foo5 is deprecated. It will be removed in future versions." in captured.out
    assert "Hello from foo5" in captured.out

if __name__ == "__main__":
    pytest.main()