import csv

import pandas as pd
from typing import Any

PATH_TO_CSV = "transactions.csv"
PATH_TO_EXCEL = "transactions_excel.xlsx"


def financial_transactions_csv(PATH_TO_CSV):
    ''' Функция для считывания финансовых операций из csv-файла и выдачи списка словарей с транзакциями '''
    result = []  # Список для хранения преобразованных строк
    with open(PATH_TO_CSV, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')  # Чтение файла с разделителем `;`

        for row in reader:
            # Преобразование строки в нужный формат
            transformed_row = {
                'id': row['id'],
                'state': row['state'],
                'date': row['date'],
                'amount': row['amount'],
                'currency_name': row['currency_name'],
                'currency_code': row['currency_code'],
                'from': row['from'],
                'to': row['to'],
                'description': row['description']
            }
            result.append(transformed_row)  # Добавление преобразованного словаря в список

    return result


def transactions_from_excel(PATH_TO_EXCEL: Any) -> Any:
    ''' Функция для считывания финансовых операций из excel-файла и выдачи списка словарей с транзакциями '''
    df = pd.read_excel(PATH_TO_EXCEL)
    transactions = df.to_dict(orient='records')
    return transactions


if __name__ == "__main__":
    transaction = financial_transactions_csv(PATH_TO_CSV)
    print(transaction)
