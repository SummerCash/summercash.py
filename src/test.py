import src.accounts as accounts
import src.chain as chain
import src.chainconfig as chainconfig
import src.common as common
import src.coordinationchain as coordinationchain
import src.crypto as crypto
import src.transaction as transaction

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

TestAccounts()
TestChain()
TestChainConfig()
TestCommon()
TestCoordinationChain()
TestCrypto()
TestTransaction()