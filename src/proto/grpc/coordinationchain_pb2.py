# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coordinationchain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='coordinationchain.proto',
  package='coordinationchain',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x63oordinationchain.proto\x12\x11\x63oordinationchain\"\x10\n\x0eGeneralRequest\"\"\n\x0fGeneralResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xe5\x02\n\x11\x43oordinationChain\x12V\n\x0bSyncNetwork\x12!.coordinationchain.GeneralRequest\x1a\".coordinationchain.GeneralResponse\"\x00\x12S\n\x08GetPeers\x12!.coordinationchain.GeneralRequest\x1a\".coordinationchain.GeneralResponse\"\x00\x12P\n\x05\x42ytes\x12!.coordinationchain.GeneralRequest\x1a\".coordinationchain.GeneralResponse\"\x00\x12Q\n\x06String\x12!.coordinationchain.GeneralRequest\x1a\".coordinationchain.GeneralResponse\"\x00\x62\x06proto3')
)




_GENERALREQUEST = _descriptor.Descriptor(
  name='GeneralRequest',
  full_name='coordinationchain.GeneralRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=62,
)


_GENERALRESPONSE = _descriptor.Descriptor(
  name='GeneralResponse',
  full_name='coordinationchain.GeneralResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='coordinationchain.GeneralResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['GeneralRequest'] = _GENERALREQUEST
DESCRIPTOR.message_types_by_name['GeneralResponse'] = _GENERALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeneralRequest = _reflection.GeneratedProtocolMessageType('GeneralRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERALREQUEST,
  __module__ = 'coordinationchain_pb2'
  # @@protoc_insertion_point(class_scope:coordinationchain.GeneralRequest)
  ))
_sym_db.RegisterMessage(GeneralRequest)

GeneralResponse = _reflection.GeneratedProtocolMessageType('GeneralResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERALRESPONSE,
  __module__ = 'coordinationchain_pb2'
  # @@protoc_insertion_point(class_scope:coordinationchain.GeneralResponse)
  ))
_sym_db.RegisterMessage(GeneralResponse)



_COORDINATIONCHAIN = _descriptor.ServiceDescriptor(
  name='CoordinationChain',
  full_name='coordinationchain.CoordinationChain',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=101,
  serialized_end=458,
  methods=[
  _descriptor.MethodDescriptor(
    name='SyncNetwork',
    full_name='coordinationchain.CoordinationChain.SyncNetwork',
    index=0,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPeers',
    full_name='coordinationchain.CoordinationChain.GetPeers',
    index=1,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Bytes',
    full_name='coordinationchain.CoordinationChain.Bytes',
    index=2,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='String',
    full_name='coordinationchain.CoordinationChain.String',
    index=3,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COORDINATIONCHAIN)

DESCRIPTOR.services_by_name['CoordinationChain'] = _COORDINATIONCHAIN

# @@protoc_insertion_point(module_scope)