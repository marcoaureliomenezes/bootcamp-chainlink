from brownie import RegisterAccess, TauanToken, TokenShop, config, network
from scripts.utils import get_account


def deploy_register_access():
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    tx = RegisterAccess.deploy({'from': owner}, publish_source=is_verified)
    return tx

def deploy_my_token():
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    tx = TauanToken.deploy({'from': owner}, publish_source=is_verified)
    return tx

def deploy_token_store():
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    tx = TokenShop.deploy(TauanToken[-1].address, {'from': owner}, publish_source=is_verified)
    return tx  

def main():
    res = deploy_my_token()
    print(res)