import time
from data import chains,ERC20_ABI
from web3.exceptions import TransactionNotFound
from web3.exceptions import ContractLogicError
from web3.exceptions import ValidationError
from web3 import Web3
def build_txn(
        *,
        web3: Web3,
        from_address: str,
        to_address: str,
        amount: float,
) -> dict[str, int | str]:

    gas_price = web3.eth.gas_price
    nonce = web3.eth.get_transaction_count(from_address)
    txn = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': int(Web3.to_wei(amount, 'ether')),
        'nonce': nonce,
        'gasPrice': gas_price,
    }
    gas = web3.eth.estimate_gas(txn)
    txn['gas'] = gas
    return txn

def privat(web3: Web3, seed: str):

    account = web3.eth.account.from_mnemonic(seed)
    private_key = account._private_key
    return private_key
def accept_txn(web3: Web3, transaction, private_key):

    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return txn_hash
def check_token_balance(web3: Web3, contract_address, wallet_address):
    contract = web3.eth.contract(contract_address, abi=ERC20_ABI)
    balance_of_token = contract.functions.balanceOf(wallet_address).call()
    token_decimals = contract.functions.decimals().call()
    ether_balance = balance_of_token / 10 ** token_decimals
    return ether_balance, balance_of_token
def transaction_price(web3: Web3, gas):
    gas_price_wei = web3.eth.gas_price
    transaction_price = Web3.from_wei(gas_price_wei * gas, 'ether')
    return float(transaction_price),gas_price_wei * gas
def approximately_gas(web3: Web3,
        from_address: str,  # checksum адрес
        to_address: str,  # checksum адрес
        amount: float,):
    try:
        gas_price = web3.eth.gas_price
        nonce = web3.eth.get_transaction_count(from_address)
        txn = {
            'chainId': web3.eth.chain_id,
            'from': from_address,
            'to': to_address,
            'value': int(Web3.to_wei(amount, 'ether')),
            'nonce': nonce,
            'gasPrice': gas_price,
        }
        gas = web3.eth.estimate_gas(txn)
        return float(gas)
    except ValueError as e:
        print(f'Нету нативки')
        gas = 1
        return gas

def wait_tx_finished(web3, hash, max_wait_time):
    start_time = time.time()
    while True:
        try:
            receipts = web3.eth.get_transaction_receipt(hash)
            status = receipts.get("status")
            if status == 1:
                return 1
            elif status is None:
                time.sleep(0.3)
            else:
                return 0
        except TransactionNotFound:
            if time.time() - start_time > max_wait_time:
                print(f'FAILED TX: {hash}')
                return 0
            time.sleep(1)
def transfer_token(web3, from_address, to_address, contract_address, token_symbol, token_balance_wei, private_key):
    try:

        transaction_data = {
            'chainId': web3.eth.chain_id,
            'from': from_address,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(from_address),
        }

        contract = web3.eth.contract(contract_address, abi=ERC20_ABI)
        transaction = contract.functions.transfer(to_address, token_balance_wei).build_transaction(transaction_data)
        hash = accept_txn(web3, transaction, private_key)
        print(f'Хэш вывода {token_symbol}: {hash.hex()}')
        txn_status = wait_tx_finished(web3, hash, 210)
        if txn_status == 1:

            print(f'Да есть жи {token_symbol} вывели')
        else:

            print(f'Фрэди фаз биар {token_symbol} не вывели')
    except ValueError as e:

        print(f'Ошибка при попытке вывода {token_symbol}: {e}')
    except ContractLogicError as a:

        print(f'Ошибка логики контракта {token_symbol}: {a}')
def stable_trans(web3, from_address, to_address, stable, contract_address, token_balance_wei, private_key):
    if stable == 'USDT':

        transfer_token(web3, from_address, to_address, contract_address, 'USDT', token_balance_wei, private_key)
    elif stable == 'USDC':

        transfer_token(web3, from_address, to_address, contract_address, 'USDC', token_balance_wei, private_key)
    else:

        print(f'Неподдерживаемый стабильный токен: {stable}')

def nativ_trans(chain,web3,checksum_address,checksum_address_desti,transaction_price_,privat_key):

    balance_wei = web3.eth.get_balance(checksum_address)
    balance_nativ = Web3.from_wei(balance_wei, 'ether')
    if chain == 'optimism':

        amount = float(balance_nativ) - transaction_price_ * 20
    else:

        amount = float(balance_nativ) - transaction_price_ * 1.2
    if amount < 0:

        return print('Очень мало нативок')
    print(amount)
    for i in range(5):

        try:

            transaction = build_txn(
                web3=web3,
                from_address=checksum_address,
                to_address=checksum_address_desti,
                amount=amount
            )
            hash = accept_txn(web3, transaction, privat_key)
            print(f'Хэш вывода native {hash.hex()}')
            txn_status_bnb = wait_tx_finished(web3, hash, 210)
            if txn_status_bnb == 1:

                print(f'Да есть жи {chain} вывели')
                break
            else:

                print(f'Фрэди фаз биар {chain} не вывели')
                break
        except ValueError as e:

            print(f'Псевдо не хватило {i + 1} раз')
        except ContractLogicError as e:

            print(f'Не хватило нативок')
def initialize_web3(rpc_url_test, seed):

    web3 = Web3(Web3.HTTPProvider(rpc_url_test))
    web3.eth.account.enable_unaudited_hdwallet_features()
    try:
        account = web3.eth.account.from_mnemonic(seed)
    except ValidationError as e:
        print('Сид фраза говна')
    privat_key = account._private_key
    from_address = account.address
    return web3, privat_key, from_address

def sbor(chain, to_address, seed):

    rpc_url_test = chains[chain]['rpc']
    usdt_contract_address = Web3.to_checksum_address(chains[chain]['usdt_contract_address'])
    usdc_contract_address = Web3.to_checksum_address(chains[chain]['usdc_contract_address'])

    web3, privat_key, from_address = initialize_web3(rpc_url_test, seed)
    print(f"Is connected {chain}: {web3.is_connected()}")

    usdt_balance, usdt_balance_wei = check_token_balance(web3, usdt_contract_address, from_address)
    usdc_balance, usdc_balance_wei = check_token_balance(web3, usdc_contract_address, from_address)

    print(f'Usdt in {chain} {usdt_balance}')
    print(f'Usdc in {chain} {usdc_balance}')

    appr_gas = approximately_gas(web3, from_address, to_address, 0.000000001)

    if appr_gas != 1:
        transaction_price_, transaction_price_wei = transaction_price(web3, appr_gas)

        if usdt_balance > 0:

            stable_trans(web3, from_address, to_address, "USDT", usdt_contract_address, usdt_balance_wei, privat_key)
        if usdc_balance > 0:

            stable_trans(web3, from_address, to_address, "USDC", usdc_contract_address, usdc_balance_wei, privat_key)

        nativ_trans(chain, web3, from_address, to_address, transaction_price_, privat_key)
