from typing import Union


def get_mask_card_number(card_or_account: Union[str, int]) -> str:
    """Функция маскирует номер банковской карты."""
    return f"{str(card_or_account)[:4]} {str(card_or_account)[4:6]}** **** {str(card_or_account)[12:]}"


def get_mask_account(card_or_account: Union[str, int]) -> str:
    """Функция маскирует номер банковского счета."""
    return f"**{str(card_or_account)[-4:]}"
