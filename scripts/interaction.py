from brownie import FundMe,accounts
from scripts.helpful_functions import get_account

def interaction_fund():
    account=get_account()
    fund_me=FundMe[-1]
    entrance_fee=fund_me.getEntranceFee()
    tx= fund_me.fund({"from":account, "value":entrance_fee })
    tx.wait(1)
    print("contract funded with " , entrance_fee, "amount of ETH !")

def interaction_withdraw():
    account=get_account()
    fund_me=FundMe[-1]
    tx1= fund_me.withdraw({"from":account})
    tx1.wait(1)
    print(" you have withdrawn funds from the contract ! ")



    
def main():
    interaction_fund()
    interaction_withdraw()