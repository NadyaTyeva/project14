import pytest
from src.search_for_operations import dictionary_search

def test_dictionary_search():
    # Тестовые данные
    search_term = "Перевод организации"
    expected_result = [list_of_dictionaries[0], list_of_dictionaries[4]]  # Ожидаем два совпадения
    result = dictionary_search(list_of_dictionaries, search_term)

    assert result == expected_result  # Проверка на равенство

def test_dictionarysearch_no_match():
    search_term = "неизвестный перевод"
    expected_result = []  # Ожидаем пустой результат
    result = dictionarysearch(listofdictionaries, search_term)

    assert result == expected_result  # Проверка на равенство

def test_sorting_by_description():
    expected_result = {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1
    }
    result = sorting_by_description(list_of_dictionaries, list_description)

    assert result == expected_result  # Проверка на равенство

# Запуск тестов
if __name__ == "__main__":
    pytest.main()

"""Этот код представляет собой набор тестов для функций dictionarysearch и sortingbydescription. 
Первый тест проверяет корректность поиска по описанию, 
второй — обработку случая, когда совпадений нет, 
а третий — правильность подсчета операций по категориям."""