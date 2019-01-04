# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.build.transaction_pb2 as transaction__pb2


class TransactionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NewTransaction = channel.unary_unary(
        '/transaction.Transaction/NewTransaction',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )
    self.TransactionFromBytes = channel.unary_unary(
        '/transaction.Transaction/TransactionFromBytes',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )
    self.Publish = channel.unary_unary(
        '/transaction.Transaction/Publish',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )
    self.Bytes = channel.unary_unary(
        '/transaction.Transaction/Bytes',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )
    self.String = channel.unary_unary(
        '/transaction.Transaction/String',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )
    self.SignTransaction = channel.unary_unary(
        '/transaction.Transaction/SignTransaction',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )
    self.VerifyTransactionSignature = channel.unary_unary(
        '/transaction.Transaction/VerifyTransactionSignature',
        request_serializer=transaction__pb2.GeneralRequest.SerializeToString,
        response_deserializer=transaction__pb2.GeneralResponse.FromString,
        )


class TransactionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def NewTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransactionFromBytes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Publish(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Bytes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def String(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VerifyTransactionSignature(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransactionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NewTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.NewTransaction,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
      'TransactionFromBytes': grpc.unary_unary_rpc_method_handler(
          servicer.TransactionFromBytes,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
      'Publish': grpc.unary_unary_rpc_method_handler(
          servicer.Publish,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
      'Bytes': grpc.unary_unary_rpc_method_handler(
          servicer.Bytes,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
      'String': grpc.unary_unary_rpc_method_handler(
          servicer.String,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
      'SignTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.SignTransaction,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
      'VerifyTransactionSignature': grpc.unary_unary_rpc_method_handler(
          servicer.VerifyTransactionSignature,
          request_deserializer=transaction__pb2.GeneralRequest.FromString,
          response_serializer=transaction__pb2.GeneralResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'transaction.Transaction', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
