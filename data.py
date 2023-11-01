import json

ERC20_ABI = json.loads('''[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"setupDecimals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]''')

chains = {
        'avalanche':
            {
                'rpc': 'https://avax.meowrpc.com',
                'usdt_contract_address': '0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7',
                'usdc_contract_address': '0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E'
            },
        'polygon':
            {
                'rpc': 'https://polygon-bor.publicnode.com',
                'usdt_contract_address': '0xc2132D05D31c914a87C6611C10748AEb04B58e8F',
                'usdc_contract_address': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
            },
        'optimism':
            {
                'rpc': 'https://optimism.publicnode.com',
                'usdt_contract_address': '0x94b008aA00579c1307B0EF2c499aD98a8ce58e58',
                'usdc_contract_address': '0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85'
            },
        'arbitrum':
            {
                'rpc': 'https://endpoints.omniatech.io/v1/arbitrum/one/public',
                'usdt_contract_address': '0xfd086bc7cd5c481dcc9c85ebe478a1c0b69fcbb9',
                'usdc_contract_address': '0xff970a61a04b1ca14834a43f5de4533ebddb5cc8'
            },
        'fantom':
            {
                'rpc': 'https://fantom.drpc.org',
                'usdt_contract_address': '0x049d68029688eabf473097a2fc38ef61633a3c7a',
                'usdc_contract_address': '0x28a92dde19d9989f39a49905d7c9c2fac7799bdf'
            },
        'bsc':
            {
                'rpc': 'https://1rpc.io/bnb',
                'usdt_contract_address': '0x049d68029688eabf473097a2fc38ef61633a3c7a',
                'usdc_contract_address': '0x28a92dde19d9989f39a49905d7c9c2fac7799bdf'
            }
    }