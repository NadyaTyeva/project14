from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция маскирует номер банковской карты."""
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]} "


card_number = input()
print(get_mask_card_number(card_number))


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция маскирует номер банковского счета."""
    return f"**{str(account_number)[-4:]}"


account_number = input()
print(get_mask_account(account_number))
