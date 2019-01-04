# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.build.common_pb2 as common__pb2


class CommonStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Encode = channel.unary_unary(
        '/common.Common/Encode',
        request_serializer=common__pb2.GeneralRequest.SerializeToString,
        response_deserializer=common__pb2.GeneralResponse.FromString,
        )
    self.EncodeString = channel.unary_unary(
        '/common.Common/EncodeString',
        request_serializer=common__pb2.GeneralRequest.SerializeToString,
        response_deserializer=common__pb2.GeneralResponse.FromString,
        )
    self.Decode = channel.unary_unary(
        '/common.Common/Decode',
        request_serializer=common__pb2.GeneralRequest.SerializeToString,
        response_deserializer=common__pb2.GeneralResponse.FromString,
        )
    self.DecodeString = channel.unary_unary(
        '/common.Common/DecodeString',
        request_serializer=common__pb2.GeneralRequest.SerializeToString,
        response_deserializer=common__pb2.GeneralResponse.FromString,
        )


class CommonServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Encode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EncodeString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Decode(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecodeString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommonServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Encode': grpc.unary_unary_rpc_method_handler(
          servicer.Encode,
          request_deserializer=common__pb2.GeneralRequest.FromString,
          response_serializer=common__pb2.GeneralResponse.SerializeToString,
      ),
      'EncodeString': grpc.unary_unary_rpc_method_handler(
          servicer.EncodeString,
          request_deserializer=common__pb2.GeneralRequest.FromString,
          response_serializer=common__pb2.GeneralResponse.SerializeToString,
      ),
      'Decode': grpc.unary_unary_rpc_method_handler(
          servicer.Decode,
          request_deserializer=common__pb2.GeneralRequest.FromString,
          response_serializer=common__pb2.GeneralResponse.SerializeToString,
      ),
      'DecodeString': grpc.unary_unary_rpc_method_handler(
          servicer.DecodeString,
          request_deserializer=common__pb2.GeneralRequest.FromString,
          response_serializer=common__pb2.GeneralResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'common.Common', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
