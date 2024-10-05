import json
import os


def load_transactions(file_path):
    # Проверяем, существует ли файл
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data



print(load_transactions('../data/operations.json'))

