from web3 import Web3
import csv, os
from brownie import network
from dotenv import load_dotenv

load_dotenv()

def get_balance_of_everyone():
    pass

def read_data(path):
    with open(path, 'r') as file:
        reader = csv.reader(file,delimiter=";")
        data_accounts = [{"name": i, "address": j} for i, j in reader]
    return data_accounts

def main(path):
    api_key = os.environ['INFURA_2']
    w3 = Web3(Web3.HTTPProvider(f"https://{network.show_active()}.infura.io/v3/{api_key}"))

    data_accounts = read_data(path)
    for address in data_accounts:  
        try: balance = w3.eth.get_balance(address["address"]) / 10**18
        except: print(f"{address['address']};{address['name']};{None}")
        else: print(f"{address['address']};{address['name']};{balance}")
