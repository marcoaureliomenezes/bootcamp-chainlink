from scripts.utils import LOCAL_CHAIN_ENV, get_account
from brownie import network, exceptions, TokenShop, config
from web3 import Web3
import pytest, logging

logging.basicConfig(level='INFO')


@pytest.fixture
def token_shop():
    if network.show_active() != 'goerli': return
    token_shop = TokenShop[-1]
    # except: 
    #   OWNER = get_account(index=0)
    return token_shop

def test_token_shop_address(token_shop):
    if network.show_active() != 'goerli': pytest.skip("Testes somente para Goerli")
    OWNER = get_account()
    print(token_shop)
    