from typing import Union
from src.masks import get_mask_account
from src.masks import get_mask_card_number

def mask_account_card(card_or_account: Union[str]) -> str:
    ''' Функция обрабатывает информацию как о картах, так и о счетах. '''
    if "Счет" in card_or_account:
        return card_or_account[:4] + " "+ get_mask_account(card_or_account[5:])

    else:
        return card_or_account[:-16] + get_mask_card_number(card_or_account[-16:])





def get_date(date: Union[str]) -> str:
    ''' Функция принимает строку с датой и возвращает в формате "ДД.ММ.ГГГГ"'''
    return date[8:10] + "." + date[5:7] + "." + date[:4]



