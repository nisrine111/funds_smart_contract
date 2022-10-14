from brownie import FundMe,accounts,network,config,MockV3Aggregator
decimals= 8
initial_answer= 200000000000

LOCAL_ENV=["development"]
FORKED_ENV=['mainnet-fork','mainnet-fork-dev']
def get_account():
    if network.show_active() in LOCAL_ENV or network.show_active in FORKED_ENV:
        return accounts[0]
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print("you re currently on ", network.show_active(), "network , mocks must be deployed !")
    print('deploying mocks ...')
    account=get_account()
    if len(MockV3Aggregator )<0:
        MockV3Aggregator.deploy(decimals,initial_answer,{"from":account})
    print("Mocks deployed successfully:")
    