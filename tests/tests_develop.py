import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
   "card_or_account",
    "mask_card_or_account",
    [
       ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
       ("Счет 73654108430135874305", "Счет **4305")

   ]

)

def test_mask_account_card(card_or_account, mask_card_or_account):
    assert mask_account_card(card_or_account) == mask_card_or_account


#if __name__ == '__main__':
#  assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000 79** **** 6361'

#@pytest.fixture
#def base_card_or_account() -> list[float]:
#   return 'Visa Platinum 7000792289606361'

#def test_mask_account_card(base_card_or_account):
#  assert mask_account_card(base_card_or_account) == 'Visa Platinum 7000 79** **** 6361'