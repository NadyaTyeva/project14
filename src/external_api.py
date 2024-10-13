import os
import requests
from dotenv import load_dotenv
from typing import Any


def conversion_currency(transaction: Any) -> Any:
    """Функция, конвертирующая сумму из иностранной валюты в рубли"""
    from_curr = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    load_dotenv()  # Загружаем переменные окружения из .env
    access_key = os.getenv("API_KEY")  # Получаем токен доступа из переменных окружения

    headers = {"apikey": access_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_curr}&amount={amount}"

    if from_curr == "RUB":
        return amount
    elif from_curr != "RUB":
        result = requests.get(url, headers=headers)
        new_amount = result.json()
        return new_amount["result"]


if __name__ == "__main__":
    print(
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
    )
