from scripts.utils import get_account
from brownie import network, exceptions, TauanToken, config
from web3 import Web3
import pytest, logging

logging.basicConfig(level='INFO')


@pytest.fixture
def tauan_token():
    if network.show_active() != 'goerli': return
    tauan_token = TauanToken[-1]
    # except: 
    #   OWNER = get_account(index=0)
    return tauan_token

def test_tauan_token_address(tauan_token):
    if network.show_active() != 'goerli': pytest.skip("Testes somente para Goerli")
    OWNER = get_account()
    print(tauan_token)
    