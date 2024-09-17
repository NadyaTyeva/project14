from typing import Union


def get_mask_card_number(card_or_account: Union[str]) -> str:
    """Функция маскирует номер банковской карты."""
    if len(card_or_account) == 16:
        return f"{str(card_or_account)[:4]} {str(card_or_account)[4:6]}** **** {str(card_or_account)[12:]}"
    else:
        return "Введите корректный номер карты"


def get_mask_account(card_or_account_: Union[str]) -> str:
    """Функция маскирует номер банковского счета."""
    if len(card_or_account_) == 20:
        return f"**{str(card_or_account_)[-4:]}"
    else:
        return "Введите корректный номер счета"
