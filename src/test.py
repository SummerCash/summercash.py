import src.accounts as accounts
import src.chain as chain
import src.chainconfig as chainconfig
import src.common as common
import src.coordinationchain as coordinationchain
import src.crypto as crypto
import src.transaction as transaction
import src.main as main

import argparse


def TestAccounts():
    methods = [
        {"method": "NewAccount", "address": "", "privateKey": ""},
        {"method": "AccountFromKey", "address": "", "privateKey": "0x2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d494863416745424245494163796255696f3642464835314c77674b78644d426b67306b424f6b526f71443833346b626f586158497864324a566f4b3270424e0a6c356e7043425357385164436143546662466450493238766f6c695655715277614b6567427759464b34454541434f6867596b44675959414241475a55456a540a52706c5a35512b6d372b796f54776f62326879612f2b566149744170657153504d66572b796739736247734c63474d486e6f31703532536345777648473834330a53542f55336e31506c48377a4f6651786e414365706b68344847384a4e48796b2b646558555742674e444c5a635135764a685a785635464437796448307673410a2b77694b2b565837642b585a4d562f6833304c5872506346774e374a4b4e6c4d2f625451362f395863513d3d0a2d2d2d2d2d454e442050524956415445204b45592d2d2d2d2d0a"},
        {"method": "GetAllAccounts", "address": "", "privateKey": ""},
        {"method": "MakeEncodingSafe", "address": "0x0401995048d3469959e50fa6efeca84f0a1b", "privateKey": ""},
        {"method": "RecoverSafeEncoding", "address": "0x0401995048d3469959e50fa6efeca84f0a1b", "privateKey": ""},
        {"method": "String", "address": "0x0401995048d3469959e50fa6efeca84f0a1b", "privateKey": ""},
        {"method": "Bytes", "address": "0x0401995048d3469959e50fa6efeca84f0a1b", "privateKey": ""},
        {"method": "ReadAccountFromMemory", "address": "0x0401995048d3469959e50fa6efeca84f0a1b", "privateKey": ""},
    ]

    for method in methods:
        r = accounts.CallMethod(method['method'], method['address'], method['privateKey']) # Call method
        print(r) # Log response

def TestChain():
    methods = [
        {"method": "GetBalance", "address": "0x0401995048d3469959e50fa6efeca84f0a1b"},
        {"method": "Bytes", "address": "0x0401995048d3469959e50fa6efeca84f0a1b"},
        {"method": "String", "address": "0x0401995048d3469959e50fa6efeca84f0a1b"},
        {"method": "ReadChainFromMemory", "address": "0x0401995048d3469959e50fa6efeca84f0a1b"},
        {"method": "QueryTransaction", "address": "0x307894355fbc47b854498df993ab1869c25b0aaed313de0903e5cc225aea90f9"},
        {"method": "GetNumTransactions", "address": "0x0401995048d3469959e50fa6efeca84f0a1b"},
    ]

    for method in methods:
        r = chain.CallMethod(method['method'], method['address']) # Call method
        print(r) # Log response

def TestChainConfig():
    methods = [
        {"method": "NewChainConfig", "genesisPath": "config/genesis.json"},
        {"method": "Bytes", "genesisPath": ""},
        {"method": "String", "genesisPath": ""},
        {"method": "WriteToMemory", "genesisPath": ""},
        {"method": "ReadChainConfigFromMemory", "genesisPath": ""},
        {"method": "GetTotalSupply", "genesisPath": ""},
    ]

    for method in methods:
        r = chainconfig.CallMethod(method['method'], method['genesisPath']) # Call method
        print(r) # Log response

def TestCommon():
    methods = [
        {"method": "Encode", "input": "test", "s": ""},
        {"method": "EncodeString", "input": "test", "s": ""},
        {"method": "Decode", "input": "", "s": "0x74657374"},
        {"method": "DecodeString", "input": "", "s": "0x74657374"},
    ]

    for method in methods:
        r = common.CallMethod(method['method'], method['input'], method['s']) # Call method
        print(r) # Log response

def TestCoordinationChain():
    methods = [
        {"method": "SyncNetwork"},
        {"method": "GetPeers"},
        {"method": "Bytes"},
        {"method": "String"},
    ]

    for method in methods:
        r = coordinationchain.CallMethod(method['method']) # Call method
        print(r) # Log response

def TestCrypto():
    methods = [
        "Sha3",
        "Sha3String",
        "Sha3n",
        "Sha3nString",
        "Sha3d",
        "Sha3dString"
    ]

    for method in methods:
        r = crypto.CallMethod(method, "", "")
        print(r)

def TestTransaction():
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
        r = transaction.CallMethod(method, "", "", "", "", "")
        print(r)

# HandleArgs - handle initializing and getting test arguments
def HandleArgs():
    parser = argparse.ArgumentParser(description='start SummerCash.py tests') # Init parser

    parser.add_argument('--provider', metavar='provider', type=str) # Add provider IP argument
    args = parser.parse_args() # Parse arguments

    if args.provider is not None: # Check provider flag set
        main.SourceAPI(args.provider) # Set provider
    else:
        main.SourceAPI("https://localhost:8080") # Set to default provider

HandleArgs() # Handle init/get args

TestAccounts()
TestChain()
TestChainConfig()
TestCommon()
TestCoordinationChain()
TestCrypto()
TestTransaction()