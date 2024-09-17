from typing import Any

import pytest

from src.processing import filter_by_state


@pytest.fixture
def filter(): # Имя фикстуры — любое
    return [
       {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
       ]

@pytest.fixture
def state():
    return "CANCELED"


def test_filter_by_state(filter, state):
    assert filter_by_state(filter, state) == [
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
       ]

# Не важно, что предыдущий тест сделал с коллекцией.
# Здесь она будет новая, так как pytest вызывает coll() заново
#def test_func2(coll):
#    assert func2(coll) == # тут ожидаемое значение

#@pytest.mark.parametrize(
#    "list_of_dictionaries, new_list_of_dictionaries",
#    [(
#      [
#       {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
 #      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#       ],
 #      [
 #      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
  #     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
  #     ]
 #   )]
#)

#def test_filter_by_state(list_of_dictionaries: list[dict[str, Any]], new_list_of_dictionaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
 #   assert filter_by_state(list_of_dictionaries) == new_list_of_dictionaries


#@pytest.mark.parametrize(
#    "list_dictionaries, state",
#    [
#       ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED"),
#       ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], "EXECUTED"),
#   ],
#)
#def test_filter_by_state(list_dictionaries: Any, state: Any) -> Any:
#    try:
#        assert filter_by_state(list_dictionaries) == state
#    except AssertionError:
#       print("Некорректные данные")


#@pytest.mark.parametrize(
#   "date_list_dictionaries, expected",
#   [
#       ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED"),
#       ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], "EXECUTED"),
#   ],
#)
#def test_sort_by_date(date_list_dictionaries: Any, expected: Any) -> Any:
#   try:
#       assert sort_by_date(date_list_dictionaries) == expected
#   except AssertionError:
#        print("Некорректные данные")