from typing import Union

def mask_account_card(card_or_account: Union[str]) -> str:
    ''' Функция обрабатывает информацию как о картах, так и о счетах. '''
    if "Счет" in card_or_account:
        return card_or_account[:4] + " **" + card_or_account[-4:]
    else:
        return card_or_account[:-12] + " " + card_or_account[-12:-10]+ "** **** " + card_or_account[-4:]

card_or_account = input()
print(mask_account_card(card_or_account))

def get_date(date: Union[str]) -> str:
    ''' Функция принимает строку с датой и возвращает в формате "ДД.ММ.ГГГГ"'''
    return date[8:10] + "." + date [5:7] + "." + date [:4]

date = input()
print(get_date(date))



