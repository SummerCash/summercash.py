# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.build.crypto_pb2 as crypto__pb2


class CryptoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Sha3 = channel.unary_unary(
        '/crypto.Crypto/Sha3',
        request_serializer=crypto__pb2.GeneralRequest.SerializeToString,
        response_deserializer=crypto__pb2.GeneralResponse.FromString,
        )
    self.Sha3String = channel.unary_unary(
        '/crypto.Crypto/Sha3String',
        request_serializer=crypto__pb2.GeneralRequest.SerializeToString,
        response_deserializer=crypto__pb2.GeneralResponse.FromString,
        )
    self.Sha3n = channel.unary_unary(
        '/crypto.Crypto/Sha3n',
        request_serializer=crypto__pb2.GeneralRequest.SerializeToString,
        response_deserializer=crypto__pb2.GeneralResponse.FromString,
        )
    self.Sha3nString = channel.unary_unary(
        '/crypto.Crypto/Sha3nString',
        request_serializer=crypto__pb2.GeneralRequest.SerializeToString,
        response_deserializer=crypto__pb2.GeneralResponse.FromString,
        )
    self.Sha3d = channel.unary_unary(
        '/crypto.Crypto/Sha3d',
        request_serializer=crypto__pb2.GeneralRequest.SerializeToString,
        response_deserializer=crypto__pb2.GeneralResponse.FromString,
        )
    self.Sha3dString = channel.unary_unary(
        '/crypto.Crypto/Sha3dString',
        request_serializer=crypto__pb2.GeneralRequest.SerializeToString,
        response_deserializer=crypto__pb2.GeneralResponse.FromString,
        )


class CryptoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Sha3(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sha3String(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sha3n(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sha3nString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sha3d(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Sha3dString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CryptoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Sha3': grpc.unary_unary_rpc_method_handler(
          servicer.Sha3,
          request_deserializer=crypto__pb2.GeneralRequest.FromString,
          response_serializer=crypto__pb2.GeneralResponse.SerializeToString,
      ),
      'Sha3String': grpc.unary_unary_rpc_method_handler(
          servicer.Sha3String,
          request_deserializer=crypto__pb2.GeneralRequest.FromString,
          response_serializer=crypto__pb2.GeneralResponse.SerializeToString,
      ),
      'Sha3n': grpc.unary_unary_rpc_method_handler(
          servicer.Sha3n,
          request_deserializer=crypto__pb2.GeneralRequest.FromString,
          response_serializer=crypto__pb2.GeneralResponse.SerializeToString,
      ),
      'Sha3nString': grpc.unary_unary_rpc_method_handler(
          servicer.Sha3nString,
          request_deserializer=crypto__pb2.GeneralRequest.FromString,
          response_serializer=crypto__pb2.GeneralResponse.SerializeToString,
      ),
      'Sha3d': grpc.unary_unary_rpc_method_handler(
          servicer.Sha3d,
          request_deserializer=crypto__pb2.GeneralRequest.FromString,
          response_serializer=crypto__pb2.GeneralResponse.SerializeToString,
      ),
      'Sha3dString': grpc.unary_unary_rpc_method_handler(
          servicer.Sha3dString,
          request_deserializer=crypto__pb2.GeneralRequest.FromString,
          response_serializer=crypto__pb2.GeneralResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'crypto.Crypto', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
