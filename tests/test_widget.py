import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "card_or_account,mask_card_or_account",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 6831982476m37658", "Введите корректный номер карты или счета"),
        ("Visa Gold 599", "Введите корректный номер карты или счета"),
        ("Visa Classic 683198247673n658", "Введите корректный номер карты или счета"),
    ]

)
def test_mask_account_card(card_or_account: str, mask_card_or_account: str) -> None:
    assert mask_account_card(card_or_account) == mask_card_or_account


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


def test_get_date(date):
    assert get_date(date) == "11.03.2024"


@pytest.fixture
def date_zero():
    return ""


def test_get_date_zero(date_zero):
    assert get_date(date_zero) == "дата некорректна"


@pytest.fixture
def date_error():
    return "11.03.202"


def test_get_date_error(date_error):
    assert get_date(date_error) == "дата некорректна"


@pytest.fixture
def date_error_():
    return "2024-03-11"


def test_get_date_(date_error_):
    assert get_date(date_error_) == "11.03.2024"
