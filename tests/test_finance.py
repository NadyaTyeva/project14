import json
import pytest
import pandas as pd
from unittest.mock import patch
from src.finance import financial_transactions_csv,transactions_from_excel


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

@patch('src.finance.pd')
def test_transactions_from_excel(mocked_pandas):

    mocked_pandas.read_excel.return_value = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02'],
        'amount': [100, 200],
        'description': ['Payment A', 'Payment B']
    })

    result = transactions_from_excel("transactions_excel.xlsx")

    assert result == [
        {'date': '2023-01-01', 'amount': 100, 'description': 'Payment A'},
        {'date': '2023-01-02', 'amount': 200, 'description': 'Payment B'}
    ]
    mocked_pandas.read_excel.assert_called_once_with("transactions_excel.xlsx")