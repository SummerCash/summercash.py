import src.accounts as accounts
import src.chain as chain
import src.chainconfig as chainconfig
import src.common as common
import src.coordinationchain as coordinationchain
import src.crypto as crypto
import src.transaction as transaction
import src.main as main
import argparse


def test_accounts():
    methods = [
        "NewAccount",
        "AccountFromKey",
        "GetAllAccounts",
        "MakeEncodingSafe",
        "RecoverSafeEncoding",
        "String",
        "Bytes",
        "ReadAccountFromMemory"
    ]

    for method in methods:
        r = accounts.CallMethod(method, "", "")
        print(r)


def test_chain():
    methods = [
        "GetBalance",
        "Bytes",
        "String",
        "ReadChainFromMemory",
        "QueryTransaction",
        "GetNumTransactions"
    ]

    for method in methods:
        r = chain.CallMethod(method, "")
        print(r)


def TestChainConfig():
    methods = [
        "NewChainConfig",
        "Bytes",
        "String",
        "WriteToMemory",
        "ReadChainConfigFromMemory",
        "GetTotalSupply"
    ]

    for method in methods:
        r = chainconfig.CallMethod(method, "")
        print(r)


def test_common():
    methods = [
        "Encode",
        "EncodeString",
        "Decode",
        "DecodeString"
    ]

    for method in methods:
        r = common.call_method(method, "", "")
        print(r)


def test_coordination_chain():
    methods = [
        "SyncNetwork",
        "GetPeers",
        "Bytes",
        "String"
    ]

    for method in methods:
        r = coordinationchain.call_method(method)
        print(r)


def test_crypto():
    methods = [
        "Sha3",
        "Sha3String",
        "Sha3n",
        "Sha3nString",
        "Sha3d",
        "Sha3dString"
    ]

    for method in methods:
        r = crypto.call_method(method, "", "")
        print(r)


def test_transaction():
    methods = [
        "NewTransaction",
        "TransactionFromBytes",
        "Publish",
        "Bytes",
        "String",
        "SignTransaction",
        "VerifyTransactionSignature"
    ]

    for method in methods:
        r = transaction.call_method(method, "", "", "", "", "")
        print(r)


parser = argparse.ArgumentParser(description='Start SummerCash.py tests')  # Init parser

parser.add_argument('--provider', metavar='provider', type=str)  # Add provider IP argument
args = parser.parse_args()  # Parse arguments

if args.provider != "":  # Check provider flag set
    main.source_api(main.get_provider())  # Set provider
else:
    main.source_api("https://localhost:8080")  # Set to default provider

print(main.get_provider()) # Log provider
test_accounts()
test_chain()
TestChainConfig()
test_common()
test_coordination_chain()
test_crypto()
test_transaction()
