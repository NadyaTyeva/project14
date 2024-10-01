import pytest

from src.decorators import log


@log()
def my_function(x: int, y: int) -> int:
    '''складывает два значения'''
    return x + y


def test_log_console_ok(capsys):
    my_function(2, 3)
    output = capsys.readouterr()
    assert output.out == "my_function ok\n"


def test_log_console_arror(capsys):
    my_function(2, "3")
    output = capsys.readouterr()
    assert output.out == "my_function error: TypeError. Inputs: (2, '3'), {}\n"
