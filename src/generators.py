def filter_by_currency(transactions: list[dict], currency: str = "USD") -> list[dict]: #тут указать что возвращает
    '''Функция принимает на вход список словарей, представляющих транзакции
    и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной'''

    # Проходим по каждой транзакции в списке
    for transaction in transactions:
        # Проверяем, соответствует ли валюта транзакции заданной
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency: #тут указать что возвращает
            yield transaction  # Возвращаем транзакцию, если валюта совпадает

# Пример использования функции
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
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
for i in range(len(transactions)):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> str:
    '''Генератор который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.'''
    for transaction in transactions:
        # получаем описание
        description = transaction.get('description')
        if description:  # если есть описание
            yield description


descriptions = transaction_descriptions(transactions)
for i in range(len(transactions)):  # Iterate based on number of transactions
    print(next(descriptions))




