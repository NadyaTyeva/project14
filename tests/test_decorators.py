import pytest
import os
from src.decorators import log

@log()
def my_function(x: int, y: int) -> int:
    '''складывает два значения'''
    return x + y

@log("../logs/mylog.txt")
def my_function_file(x: int, y: int) -> int:
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

def test_log_file_ok():
    my_function_file(2, 3)
    with open("../logs/mylog.txt", "r", encoding = "utf-8") as file:
        logs = file.read()
    assert "my_function_file ok\n" in logs

def test_log_file_arror():
    my_function_file(2, "3")
    with open("../logs/mylog.txt", "r", encoding = "utf-8") as file:
        logs = file.read()
    assert "my_function_file error: TypeError. Inputs: (2, '3'), {}\n" in logs
