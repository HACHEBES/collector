from functions import sbor
from web3 import Web3

wallets = []
seeds = []

with open('wallets.txt','r') as file:
    for line in file:
        wallets.append(line.strip())

with open('seeds.txt','r') as file:
    for line in file:
        seeds.append(line.strip())

for i in range(len(wallets)):

    destination_address = wallets[i]
    seed = seeds[i]
    sbor('bsc', Web3.to_checksum_address(destination_address), seed)
    sbor('fantom',Web3.to_checksum_address(destination_address), seed)
    sbor('avalanche', Web3.to_checksum_address(destination_address), seed)
    sbor('polygon', Web3.to_checksum_address(destination_address), seed)
    sbor('optimism', Web3.to_checksum_address(destination_address), seed)
    sbor('arbitrum', Web3.to_checksum_address(destination_address), seed)
    print(f'Вывели с {i+1} кошелька\n')

