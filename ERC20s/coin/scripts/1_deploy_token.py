from brownie import accounts, config, TokenERC20

inital_supply = 1000
token_name = "TOKEN"
token_symbol = "TKN"

def main():
    #this is the account that we are deploying from 
    #it simulates deploying from meta mask
    #account = accounts[0]
    account = accounts.add(config["wallet"]["from_key"])
    # from:account showing where the funds all coming from 
    erc20 = TokenERC20.deploy(inital_supply,token_name,token_symbol, {"from": account}
    )