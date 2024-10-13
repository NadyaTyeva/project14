import pandas as pd
filename = "transactions.csv"
filename_excel = "transactions_excel.xlsx"


def financial_transactions_csv(filename):
    ''' Функция для считывания финансовых операций из csv-файла и выдачи списка словарей с транзакциями'''
    reading_financial_transactions = pd.read_csv(filename)
    financial_transactions = reading_financial_transactions.to_dict(orient='records')
    return financial_transactions

def transactions_from_excel(filename_excel):
    ''' Функция для считывания финансовых операций из excel-файла и выдачи списка словарей с транзакциями '''
    df = pd.read_excel(filename_excel)
    transactions = df.to_dict(orient='records')

    return transactions


if __name__ == "__main__":
    transaction = financial_transactions_csv(filename)
    print(transaction)





