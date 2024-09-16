import pytest

from src.widget import mask_account_card


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

def test_mask_account_card(number: str, expected: str) -> None:
    assert mask_account_card(card_or_account) == mask_card_or_account


#if __name__ == '__main__':
#  assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'

@pytest.fixture
def base_card_or_account() -> list[float]:
   return 'Visa Platinum 7000792289606361'

def test_mask_account_card(base_card_or_account):
  assert mask_account_card(base_card_or_account) == 'Visa Platinum 7000 79** **** 6361'