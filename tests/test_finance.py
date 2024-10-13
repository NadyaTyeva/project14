import json
import pytest
import pandas as pd
from unittest.mock import patch
from src.finance import financial_transactions_csv


@patch('src.finance.pd')
def test_financial_transactions_csv(mocked_pandas):

    mocked_pandas.read_csv.return_value = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02'],
        'amount': [100, 200],
        'description': ['Payment A', 'Payment B']
    })

    result = financial_transactions_csv("transactions.csv")

    assert result == [
        {'date': '2023-01-01', 'amount': 100, 'description': 'Payment A'},
        {'date': '2023-01-02', 'amount': 200, 'description': 'Payment B'}
    ]
    mocked_pandas.read_csv.assert_called_once_with("transactions.csv")

#
#
#
# @patch('pd.read_csv')
# def test_financial_transactions_csv(mock_get):
#     mock_data = pd.DataFrame({
#         'date': ['2023-01-01', '2023-01-02'],
#         'amount': [100, 200],
#         'description': ['Income', 'Expense']
#     })
#     mock_read_csv.return_value = mock_data
#
#     # Запуск тестируемой функции
#     result = financial_transactions_csv("transactions.csv")
#
#     # результат, который ожидаем
#     expected_result = [
#         {'date': '2023-01-01', 'amount': 100, 'description': 'Income'},
#         {'date': '2023-01-02', 'amount': 200, 'description': 'Expense'}
#     ]
#
#     # Проверка что результат ожидаемы равен полученному
#     self.assertEqual(result, expected_result)
#     mock_read_csv.assert_called_once_with("transactions.csv")

