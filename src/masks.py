import logging

from typing import Union
from utils import PATH_TO_PROJECT

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler('../logs/masks.log', mode="w", encoding="UTF-8")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)


def get_mask_card_number(card_or_account: Union[str]) -> str:
    """Функция маскирует номер банковской карты."""
    if len(card_or_account) == 16:
        logger.info("Получаем реквизиты карты с зашифрованным номером")
        return f"{str(card_or_account)[:4]} {str(card_or_account)[4:6]}** **** {str(card_or_account)[12:]}"
    else:
        logger.error("Ошибка! Введен некорректный номер карты")
        return "Введите корректный номер карты"

print(get_mask_card_number("1234567891234567"))


def get_mask_account(card_or_account_: Union[str]) -> str:
    """Функция маскирует номер банковского счета."""
    if len(card_or_account_) == 20:
        logger.info("Получаем реквизиты счета с зашифрованным номером")
        return f"**{str(card_or_account_)[-4:]}"
    else:
        logger.error("Ошибка! Введен некорректный номер счета")
        return "Введите корректный номер счета"

print(get_mask_account("12345678912345678932"))