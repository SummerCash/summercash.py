# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.build.chainconfig_pb2 as chainconfig__pb2


class ConfigStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NewChainConfig = channel.unary_unary(
        '/config.Config/NewChainConfig',
        request_serializer=chainconfig__pb2.GeneralRequest.SerializeToString,
        response_deserializer=chainconfig__pb2.GeneralResponse.FromString,
        )
    self.Bytes = channel.unary_unary(
        '/config.Config/Bytes',
        request_serializer=chainconfig__pb2.GeneralRequest.SerializeToString,
        response_deserializer=chainconfig__pb2.GeneralResponse.FromString,
        )
    self.String = channel.unary_unary(
        '/config.Config/String',
        request_serializer=chainconfig__pb2.GeneralRequest.SerializeToString,
        response_deserializer=chainconfig__pb2.GeneralResponse.FromString,
        )
    self.WriteToMemory = channel.unary_unary(
        '/config.Config/WriteToMemory',
        request_serializer=chainconfig__pb2.GeneralRequest.SerializeToString,
        response_deserializer=chainconfig__pb2.GeneralResponse.FromString,
        )
    self.ReadChainConfigFromMemory = channel.unary_unary(
        '/config.Config/ReadChainConfigFromMemory',
        request_serializer=chainconfig__pb2.GeneralRequest.SerializeToString,
        response_deserializer=chainconfig__pb2.GeneralResponse.FromString,
        )
    self.GetTotalSupply = channel.unary_unary(
        '/config.Config/GetTotalSupply',
        request_serializer=chainconfig__pb2.GeneralRequest.SerializeToString,
        response_deserializer=chainconfig__pb2.GeneralResponse.FromString,
        )


class ConfigServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def NewChainConfig(self, request, context):
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

  def WriteToMemory(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadChainConfigFromMemory(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTotalSupply(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConfigServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NewChainConfig': grpc.unary_unary_rpc_method_handler(
          servicer.NewChainConfig,
          request_deserializer=chainconfig__pb2.GeneralRequest.FromString,
          response_serializer=chainconfig__pb2.GeneralResponse.SerializeToString,
      ),
      'Bytes': grpc.unary_unary_rpc_method_handler(
          servicer.Bytes,
          request_deserializer=chainconfig__pb2.GeneralRequest.FromString,
          response_serializer=chainconfig__pb2.GeneralResponse.SerializeToString,
      ),
      'String': grpc.unary_unary_rpc_method_handler(
          servicer.String,
          request_deserializer=chainconfig__pb2.GeneralRequest.FromString,
          response_serializer=chainconfig__pb2.GeneralResponse.SerializeToString,
      ),
      'WriteToMemory': grpc.unary_unary_rpc_method_handler(
          servicer.WriteToMemory,
          request_deserializer=chainconfig__pb2.GeneralRequest.FromString,
          response_serializer=chainconfig__pb2.GeneralResponse.SerializeToString,
      ),
      'ReadChainConfigFromMemory': grpc.unary_unary_rpc_method_handler(
          servicer.ReadChainConfigFromMemory,
          request_deserializer=chainconfig__pb2.GeneralRequest.FromString,
          response_serializer=chainconfig__pb2.GeneralResponse.SerializeToString,
      ),
      'GetTotalSupply': grpc.unary_unary_rpc_method_handler(
          servicer.GetTotalSupply,
          request_deserializer=chainconfig__pb2.GeneralRequest.FromString,
          response_serializer=chainconfig__pb2.GeneralResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'config.Config', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
