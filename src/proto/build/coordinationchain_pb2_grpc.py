# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.build.coordinationchain_pb2 as coordinationchain__pb2


class CoordinationChainStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SyncNetwork = channel.unary_unary(
        '/coordinationchain.CoordinationChain/SyncNetwork',
        request_serializer=coordinationchain__pb2.GeneralRequest.SerializeToString,
        response_deserializer=coordinationchain__pb2.GeneralResponse.FromString,
        )
    self.GetPeers = channel.unary_unary(
        '/coordinationchain.CoordinationChain/GetPeers',
        request_serializer=coordinationchain__pb2.GeneralRequest.SerializeToString,
        response_deserializer=coordinationchain__pb2.GeneralResponse.FromString,
        )
    self.Bytes = channel.unary_unary(
        '/coordinationchain.CoordinationChain/Bytes',
        request_serializer=coordinationchain__pb2.GeneralRequest.SerializeToString,
        response_deserializer=coordinationchain__pb2.GeneralResponse.FromString,
        )
    self.String = channel.unary_unary(
        '/coordinationchain.CoordinationChain/String',
        request_serializer=coordinationchain__pb2.GeneralRequest.SerializeToString,
        response_deserializer=coordinationchain__pb2.GeneralResponse.FromString,
        )


class CoordinationChainServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SyncNetwork(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPeers(self, request, context):
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


def add_CoordinationChainServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SyncNetwork': grpc.unary_unary_rpc_method_handler(
          servicer.SyncNetwork,
          request_deserializer=coordinationchain__pb2.GeneralRequest.FromString,
          response_serializer=coordinationchain__pb2.GeneralResponse.SerializeToString,
      ),
      'GetPeers': grpc.unary_unary_rpc_method_handler(
          servicer.GetPeers,
          request_deserializer=coordinationchain__pb2.GeneralRequest.FromString,
          response_serializer=coordinationchain__pb2.GeneralResponse.SerializeToString,
      ),
      'Bytes': grpc.unary_unary_rpc_method_handler(
          servicer.Bytes,
          request_deserializer=coordinationchain__pb2.GeneralRequest.FromString,
          response_serializer=coordinationchain__pb2.GeneralResponse.SerializeToString,
      ),
      'String': grpc.unary_unary_rpc_method_handler(
          servicer.String,
          request_deserializer=coordinationchain__pb2.GeneralRequest.FromString,
          response_serializer=coordinationchain__pb2.GeneralResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'coordinationchain.CoordinationChain', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
