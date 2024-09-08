from typing import Union


def mask_account_card(card_or_account: Union[str]) -> str:
    ''' Функция обрабатывает информацию как о картах, так и о счетах. '''
    if "Счет" in card_or_account:
        from masks import get_mask_account
        return card_or_account[:4] + " " + get_mask_account(card_or_account[5:])

    else:
        from masks import get_mask_card_number
        return card_or_account[:-16] + " " + get_mask_card_number(card_or_account[-16:])

print(mask_account_card("Visa Platinum 7000792289606361"))


def get_date(date: Union[str]) -> str:
    ''' Функция принимает строку с датой и возвращает в формате "ДД.ММ.ГГГГ"'''
   return date[8:10] + "." + date [5:7] + "." + date [:4]

date = input()
print(get_date(date))

