from brownie import accounts, config, EasyToken

inital_supply = 1000
token_name = "TOKEN"
token_symbol = "TKN"

def main():
    #this is the account that we are deploying from 
    #it simulates deploying from meta mask
    account = accounts[0]
    # from:account showing where the funds all coming from 
    erc20 = EasyToken.deploy(inital_supply,token_name,token_symbol, {"from": account}
    )