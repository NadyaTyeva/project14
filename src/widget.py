from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: Union[str]) -> str:
    ''' Функция обрабатывает информацию как о картах, так и о счетах. '''
    if len(card_or_account) < 24:
        return "Введите корректный номер карты или счета"
    else:
        if "Счет" in card_or_account:
            nomer = card_or_account[-20:]
            if nomer.isdigit() is True:
                return card_or_account[:4] + " " + get_mask_account(card_or_account[5:])
            else:
                return "Введите корректный номер карты или счета"
        else:
            nomer = card_or_account[-16:]
            if nomer.isdigit() is True:
                return card_or_account[:-16] + get_mask_card_number(card_or_account[-16:])
            else:
                return "Введите корректный номер карты или счета"


def get_date(date: Union[str]) -> str:
    ''' Функция принимает строку с датой и возвращает в формате "ДД.ММ.ГГГГ"'''
    if len(date) < 10:
        return "дата некорректна"
    else:
        return date[8:10] + "." + date[5:7] + "." + date[:4]
