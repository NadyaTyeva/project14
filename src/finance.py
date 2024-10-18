import pandas as pd
from typing import Any
from src.utils import PATH_TO_PROJECT

PATH_TO_CSV = "transactions.csv"
PATH_TO_EXCEL = "transactions_excel.xlsx"

def financial_transactions_csv(PATH_TO_CSV) -> Any:
    ''' Функция для считывания финансовых операций из csv-файла и выдачи списка словарей с транзакциями '''
    reading_financial_transactions = pd.read_csv(PATH_TO_CSV)
    financial_transactions = reading_financial_transactions.to_dict(orient='records')
    return financial_transactions


def transactions_from_excel(PATH_TO_EXCEL: Any) -> Any:
    ''' Функция для считывания финансовых операций из excel-файла и выдачи списка словарей с транзакциями '''
    df = pd.read_excel(PATH_TO_EXCEL)
    transactions = df.to_dict(orient='records')
    return transactions


if __name__ == "__main__":
    transaction = financial_transactions_csv(PATH_TO_CSV)
    print(transaction)
