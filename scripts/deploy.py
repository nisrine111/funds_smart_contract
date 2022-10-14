from brownie import FundMe,accounts,network,config,MockV3Aggregator
from scripts.helpful_functions import get_account, LOCAL_ENV,deploy_mocks

def deploy_fund_me():
    account=get_account()
    # to deploy we need the price feed for the constructor
    price_feed_address=""
    if network.show_active() in LOCAL_ENV:
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
    if network.show_active() in config["networks"]:
        price_feed_address=config["networks"][network.show_active()]["price_feed_address"]
    
    fund_me= FundMe.deploy(price_feed_address,
    {"from": account})
    print( " the smart contract FundMe was deployed successfully !")
    return fund_me


def main():
    deploy_fund_me()