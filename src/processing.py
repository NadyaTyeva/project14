from typing import Any


def filter_by_state(list_of_dictionaries: list[dict[str, Any]], state: str) -> list[dict[str, Any]]:
    '''Функция принимает список словарей и опционально значение state
    для ключа и возвращает новый список словарей,
    содержащий только те словари,
    у которых state соответствует указанному значению.'''
    filtered_data = []
    for i in list_of_dictionaries:
        if i.get("state") == state:
            filtered_data.append(i)
        else:
            continue
    return filtered_data
    #return [dictionary for dictionary in list_of_dictionaries if dictionary.get('state') == state]



def sort_by_date(list_of_dictionaries: list[dict[str, Any]], reversed: bool) -> list[dict[str, Any]]:
    '''Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    и возвращает новый список, отсортированный по дате'''
    sorted_list = sorted(
        list_of_dictionaries,
        key=lambda new_list_of_dict: new_list_of_dict["date"],
        reverse=reversed,
    )
    return sorted_list
