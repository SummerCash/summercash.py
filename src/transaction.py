import grpc

from proto.build import transaction_pb2, transaction_pb2_grpc

class Transaction:
    def __init__(self, channel):
        self.channel = channel
        self.stub = transaction_pb2_grpc.TransactionStub(channel)

    def NewTransaction(self, nonce, address, address2, amount, payload):
        response = self.stub.NewTransaction(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message

    def TransactionFromBytes(self, nonce, address, address2, amount, payload):
        response = self.stub.TransactionFromBytes(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message

    def Publish(self, nonce, address, address2, amount, payload):
        response = self.stub.Publish(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message

    def Bytes(self, nonce, address, address2, amount, payload):
        response = self.stub.Bytes(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message

    def String(self, nonce, address, address2, amount, payload):
        response = self.stub.String(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message

    def SignTransaction(self, nonce, address, address2, amount, payload):
        response = self.stub.SignTransaction(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message

    def VerifyTransactionSignature(self, nonce, address, address2, amount, payload):
        response = self.stub.VerifyTransactionSignature(
            chain_pb2.GeneralRequest(
                nonce=nonce,
                address=address,
                address2=address2,
                amount=amount,
                payload=payload
            )
        )
        return response.message