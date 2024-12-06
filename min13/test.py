import matrixpower
import pytest

def test1(capsys):
    assert matrixpower.foreign_matrix_power([[1.0, 2.0], [3.0, 4.0]], 2) == [[7.0, 10.0], [15.0, 22.0]]

def test2(capsys):
    assert matrixpower.foreign_matrix_power([[1.0, 0.0], [0.0, 1.0]], 5) == [[1.0, 0.0], [0.0, 1.0]]

def test3(capsys):
    assert matrixpower.foreign_matrix_power([[2.0, 3.0], [5.0, 7.0]], 0) == [[1.0, 0.0], [0.0, 1.0]]

def test4(capsys):
    with pytest.raises(ValueError):
        matrixpower.foreign_matrix_power([[1.0, 2.0], [3.0, 4.0]], -1)