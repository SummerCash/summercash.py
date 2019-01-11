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
        {"method": "Sha3", "input": "test", "n": 0},
        {"method": "Sha3String", "input": "test", "n": 0},
        {"method": "Sha3n", "input": "test", "n": 2},
        {"method": "Sha3nString", "input": "test", "n": 2},
        {"method": "Sha3d", "input": "test", "n": 0},
        {"method": "Sha3dString", "input": "test", "n": 0},
    ]

    for method in methods:
        r = crypto.CallMethod(method['method'], method['input'], method['n']) # Call method
        print(r) # Log response

def TestTransaction():
    methods = [
        {"method": "NewTransaction", "nonce": 0, "address": "0x0401995048d3469959e50fa6efeca84f0a1b", "address2": "0x0401995048d3469959e50fa6efeca84f0a1b", "amount": 0, "payload": "test"},
        {"method": "TransactionFromBytes", "payload": "0x7b226e6f6e6365223a302c2273656e646572223a5b34382c3132302c342c312c3135332c38302c37322c3231312c37302c3135332c38392c3232392c31352c3136362c3233392c3233362c3136382c37392c31302c32375d2c22726563697069656e74223a5b34382c3132302c342c312c3135332c38302c37322c3231312c37302c3135332c38392c3232392c31352c3136362c3233392c3233362c3136382c37392c31302c32375d2c22616d6f756e74223a302c227061796c6f6164223a226447567a64413d3d222c227369676e6174757265223a6e756c6c2c2274696d65223a22323031392d30312d31315431383a31383a31322e3630363537333633375a222c2267656e65736973223a66616c73652c2268617368223a5b34382c3132302c36392c3232332c31392c38352c35302c39332c35302c3139352c3231342c38332c3231372c3138382c3138302c35382c3132322c3130352c362c3231312c3137362c3234372c3130322c36362c37382c3137392c3234312c3234352c3230362c31332c392c39365d7d0ast"},
        {"method": "Publish", "address": "0x307845df1355325d32c3d653d9bcb43a7a6906d3b0f766424eb3f1f5ce0d0960"},
        {"method": "Bytes", "address": "0x307845df1355325d32c3d653d9bcb43a7a6906d3b0f766424eb3f1f5ce0d0960"},
        {"method": "String", "address": "0x307845df1355325d32c3d653d9bcb43a7a6906d3b0f766424eb3f1f5ce0d0960"},
        {"method": "SignTransaction", "address": "0x307845df1355325d32c3d653d9bcb43a7a6906d3b0f766424eb3f1f5ce0d0960"},
        {"method": "VerifyTransactionSignature", "address": "0x307845df1355325d32c3d653d9bcb43a7a6906d3b0f766424eb3f1f5ce0d0960"},
    ]

    for method in methods:
        r = transaction.CallMethod(method['method'], method['nonce'], method['address'], method['address2'], method['amount'], method['payload']) # Call method
        print(r) # Log response

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