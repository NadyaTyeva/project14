import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_or_account,mask_card_or_account",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("4692837565682847", "4692 83** **** 2847"),
        ("71583007", "Введите корректный номер карты"),
        ("", "Введите корректный номер карты"),
        ("4692837565682847124", "Введите корректный номер карты"),
    ]
)
def test_get_mask_card_number(card_or_account: str, mask_card_or_account: str) -> None:
    assert get_mask_card_number(card_or_account) == mask_card_or_account


@pytest.mark.parametrize(
    "account,mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("35383033474447895560", "**5560"),
        ("4353830", "Введите корректный номер счета"),
        ("435383035383033474447895560", "Введите корректный номер счета"),
        ("", "Введите корректный номер счета")

    ]

)
def test_get_mask_account(account: str, mask_account: str) -> None:
    assert get_mask_account(account) == mask_account
