from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def filter() -> list[dict[str, Any]]:
    return [
       {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
       ]


@pytest.fixture
def state_canceled() -> str:
    return 'CANCELED'


def test_filter_by_state_canceled(filter: list[dict[str, Any]], state_canceled: str) -> list[dict[str, Any]]:
    assert filter_by_state(filter, state_canceled) == [
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
       ]


@pytest.fixture
def state_executed() -> str:
    return 'EXECUTED'


def test_filter_by_state_executed(filter: list[dict[str, Any]], state_executed: str) -> list[dict[str, Any]]:
    assert filter_by_state(filter, state_executed) == [
       {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      ]


@pytest.fixture
def state_none() -> str:
    return 'None'


def test_filter_by_state_none(filter: list[dict[str, Any]], state_none: str) -> list[dict[str, Any]]:
    assert filter_by_state(filter, state_none) == []


@pytest.fixture
def reversed() -> bool:
    return True


def test_sort_by_date_true(filter: list[dict[str, Any]], reversed: bool) -> list[dict[str, Any]]:
    assert sort_by_date(filter, reversed) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def reversed_false() -> bool:
    return False


def test_sort_by_date_false(filter: list[dict[str, Any]], reversed_false: bool) -> list[dict[str, Any]]:
    assert sort_by_date(filter, reversed_false) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},

        ]
