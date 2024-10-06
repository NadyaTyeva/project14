from unittest.mock import patch
from unittest.mock import Mock, patch
from src.external_api import conversion_currency
import requests
import os
import pytest
from typing import Any
from dotenv import load_dotenv
from src.external_api import conversion_currency

load_dotenv()
access_key = os.getenv("API_KEY")
headers = {"access_key": "access_key=" + access_key}


@patch("requests.get")
def test_conversion_currency_rub(mock_get: Any) -> Any:
    mock_get.return_value.json.return_value = 31957.58
    assert (
        conversion_currency(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )


@patch("requests.get")
def test_conversion_currency_usd(mock_get: Any) -> Any:
    mock_get.return_value.json.return_value = 31957.58
    assert (
        conversion_currency(
          {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
              "amount": "8221.37",
              "currency": {
                "name": "USD",
                "code": "USD"
              }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
          }
        )
        == 8221.37
    )


if __name__ == '__main__':
    unittest.main()
