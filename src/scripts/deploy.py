from brownie import RegisterAccess, config, network
from scripts.utils import get_account


def deploy_register_access():
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    tx = RegisterAccess.deploy({'from': owner}, publish_source=is_verified)
    return tx


def main():
    res = deploy_register_access()
    print(res)