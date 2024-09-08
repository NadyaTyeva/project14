from typing import Union

def mask_account_card(card_or_account: Union[str, int]) -> str:
    ''' Функция обрабатывает информацию как о картах, так и о счетах. '''

    if "Счет" in card_or_account:
        return card_or_account[:4] + " **" + card_or_account[-4:]
    else:
        return card_or_account[:-12] + " " + card_or_account[-12:-10]+ "** **** " + card_or_account[-4:]

card_or_account = input()
print(mask_account_card(card_or_account))



