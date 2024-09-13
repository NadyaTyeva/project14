list_of_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
state = "CANCELED"


def filter_by_state(list_of_dictionaries: list[dict[str, any]], state: str ) -> list[dict[str, any]]:
   '''Функция принимает список словарей и опционально значение state
   для ключа и возвращает новый список словарей, 
   содержащий только те словари, 
   у которых state соответствует указанному значению.'''
   #list_state = []
   #for dictionary in list_of_dictionaries:
       #if dictionary.get('state') == state:
          # list_state.append(dictionary)
   return [dictionary for dictionary in list_of_dictionaries if dictionary.get('state') == state]


print(filter_by_state(list_of_dictionaries, state))


def sort_by_date(list_of_dictionaries: list[dict[str, any]], reversed: bool = True) -> list[dict[str, any]]:
    '''Функция принимает список словарей и необязательный параметр, задающий порядок ортировки
    и возращает новый список, отсортированный по дате'''
    sorted_list = sorted(
        list_of_dictionaries,
        key=lambda new_list_of_dict: new_list_of_dict["date"],
        reverse=reversed,
    )
    return sorted_list


print(sort_by_date(list_of_dictionaries, reversed))
