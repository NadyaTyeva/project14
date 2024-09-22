from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, None, None]:
    '''Функция принимает на вход список словарей, представляющих транзакции
    и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной'''

    # Проходим по каждой транзакции в списке
    for transaction in transactions:
        # Проверяем, соответствует ли валюта транзакции заданной
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction  # Возвращаем транзакцию, если валюта совпадает

transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

currency = 'USD'

usd_transactions = filter_by_currency(transactions, currency)
for _ in range(3):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    '''Генератор который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.'''
    for transaction in transactions:
        # Получаем описание
        description = transaction.get('description')
        if description:  # Если есть описание
            yield description


descriptions = transaction_descriptions(transactions)
for _ in range(len(transactions)):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Generator[int, None, None]:
    '''Генератор который выдает номера банковских карт в формате
XXXX XXXX XXXX XXXX, где X — цифра номера карты'''
    for number in range(start, stop + 1):
        yield (f"{number:016}"[:4] + " " + f"{number:016}"[4:8] + " "
               + f"{number:016}"[8:12] + " " + f"{number:016}"[12:])


for card_number in card_number_generator(1, 5):
    print(card_number)
