from scripts.utils import get_account
from brownie import network, exceptions, RegisterAccess, config
from web3 import Web3
import pytest, logging

logging.basicConfig(level='INFO')


@pytest.fixture
def register_access():
    if network.show_active() != 'goerli': return
    register_access = RegisterAccess[-1]
    # except: 
    #   OWNER = get_account(index=0)
    return register_access

def test_register_access_is_I_owner(register_access):
    if network.show_active() != 'goerli': pytest.skip("Testes somente para Goerli")
    OWNER = get_account()
    assert OWNER == register_access.owner()

def test_register_access_is_owner_whitelisted(register_access):
    if network.show_active() != 'goerli': pytest.skip("Testes somente para Goerli")
    OWNER = get_account()
    assert register_access.whiteList(OWNER) == True

def test_register_access_is_owner_whitelisted2(register_access):
    if network.show_active() != 'goerli': pytest.skip("Testes somente para Goerli")
    THIRD_PARTY = "0x6B05894251fF61B1F18F10e7E14eea4777B6b954"
    assert register_access.whiteList(THIRD_PARTY) == False