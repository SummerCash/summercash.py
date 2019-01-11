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
        "NewAccount",
        "AccountFromKey",
        "GetAllAccounts",
        "MakeEncodingSafe",
        "RecoverSafeEncoding",
        "String",
        "Bytes",
        "ReadAccountFromMemory"
    ]

    params = [
        "",
        "0x2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d494863416745424245494158364351337a6a6d715a7050732b71316c5771412b44307678636b3474685468797075345543536c75537850502b346b4a6c39750a4f6134624c6b324b795a696f523559314b784b4b43584250496b7a7a4f42393741626d67427759464b34454541434f6867596b4467595941424141324b7254420a2b6b762f4148504f4d325a55543847342b322b6a36426b66532b784832755878387a577a47467069585354772f527649706b467850376e4a646f6d796b5733610a66786145684b4134464c56385642766c6677484478444971523247676d63683957616439665959486d4e76674a4b68546b45506d5470465278696e6d52504c4e0a54705774725a57746c5645347a4e785371566878676966517979366b5264302f376e2f663753725850513d3d0a2d2d2d2d2d454e442050524956415445204b45592d2d2d2d2d0a",
        ""
    ]

    for method in methods:
        r = accounts.CallMethod(method, "", "")
        print(r)

def TestChain():
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

def TestCommon():
    methods = [
        "Encode",
        "EncodeString",
        "Decode",
        "DecodeString"
    ]

    for method in methods:
        r = common.CallMethod(method, "", "")
        print(r)

def TestCoordinationChain():
    methods = [
        "SyncNetwork",
        "GetPeers",
        "Bytes",
        "String"
    ]

    for method in methods:
        r = coordinationchain.CallMethod(method)
        print(r)

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