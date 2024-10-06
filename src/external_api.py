import os
import requests
from dotenv import load_dotenv


def conversion_currency(transaction) -> float:
    """Функция, конвертирующая сумму из иностранной валюты в рубли"""
    from_curr = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    load_dotenv() # Загружаем переменные окружения из .env
    access_key = os.getenv("API_KEY") # Получаем токен доступа из переменных окружения

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
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {
                    "amount": "48223.05",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 41421565395219882431"
            }
        )
    )
