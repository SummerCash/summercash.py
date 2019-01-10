from server import Server
import accounts
import chain
import chainconfig
import common
import coordinationchain
import crypto
import transaction

server = Server("")

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
        myAccounts = accounts.Accounts(server)
        r = myAccounts.CallMethod(method, "", "")
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
        myChain = chain.Chain(server)
        r = myChain.CallMethod(method, "")
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
        myChainConfig = chainconfig.ChainConfig(server)
        r = myChainConfig.CallMethod(method, "")
        print(r)

def TestCommon():
    methods = [
        "Encode",
        "EncodeString",
        "Decode",
        "DecodeString"
    ]
    for method in methods:
        myCommon = common.Common(server)
        r = myCommon.CallMethod(method, "", "")
        print(r)

def TestCoordinationChain():
    methods = [
        "SyncNetwork",
        "GetPeers",
        "Bytes",
        "String"
    ]
    for method in methods:
        myCoordinationChain = coordinationchain.CoordinationChain(server)
        r = myCoordinationChain.CallMethod(method)
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
        myCrypto = crypto.Crypto(server)
        r = myCrypto.CallMethod(method, "", "")
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
        myTransaction = transaction.Transaction(server)
        r = myTransaction.CallMethod(method, "", "", "", "", "")
        print(r)

TestAccounts()
TestChain()
TestChainconfig()
TestCommon()
TestCoordinationChain()
TestCrypto()
TestTransaction()