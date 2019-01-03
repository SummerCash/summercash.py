# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chainconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chainconfig.proto',
  package='config',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63hainconfig.proto\x12\x06\x63onfig\"%\n\x0eGeneralRequest\x12\x13\n\x0bgenesisPath\x18\x01 \x01(\t\"\"\n\x0fGeneralResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9f\x03\n\x06\x43onfig\x12\x43\n\x0eNewChainConfig\x12\x16.config.GeneralRequest\x1a\x17.config.GeneralResponse\"\x00\x12:\n\x05\x42ytes\x12\x16.config.GeneralRequest\x1a\x17.config.GeneralResponse\"\x00\x12;\n\x06String\x12\x16.config.GeneralRequest\x1a\x17.config.GeneralResponse\"\x00\x12\x42\n\rWriteToMemory\x12\x16.config.GeneralRequest\x1a\x17.config.GeneralResponse\"\x00\x12N\n\x19ReadChainConfigFromMemory\x12\x16.config.GeneralRequest\x1a\x17.config.GeneralResponse\"\x00\x12\x43\n\x0eGetTotalSupply\x12\x16.config.GeneralRequest\x1a\x17.config.GeneralResponse\"\x00\x62\x06proto3')
)




_GENERALREQUEST = _descriptor.Descriptor(
  name='GeneralRequest',
  full_name='config.GeneralRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='genesisPath', full_name='config.GeneralRequest.genesisPath', index=0,
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
  serialized_start=29,
  serialized_end=66,
)


_GENERALRESPONSE = _descriptor.Descriptor(
  name='GeneralResponse',
  full_name='config.GeneralResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='config.GeneralResponse.message', index=0,
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
  serialized_start=68,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['GeneralRequest'] = _GENERALREQUEST
DESCRIPTOR.message_types_by_name['GeneralResponse'] = _GENERALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeneralRequest = _reflection.GeneratedProtocolMessageType('GeneralRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERALREQUEST,
  __module__ = 'chainconfig_pb2'
  # @@protoc_insertion_point(class_scope:config.GeneralRequest)
  ))
_sym_db.RegisterMessage(GeneralRequest)

GeneralResponse = _reflection.GeneratedProtocolMessageType('GeneralResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERALRESPONSE,
  __module__ = 'chainconfig_pb2'
  # @@protoc_insertion_point(class_scope:config.GeneralResponse)
  ))
_sym_db.RegisterMessage(GeneralResponse)



_CONFIG = _descriptor.ServiceDescriptor(
  name='Config',
  full_name='config.Config',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=105,
  serialized_end=520,
  methods=[
  _descriptor.MethodDescriptor(
    name='NewChainConfig',
    full_name='config.Config.NewChainConfig',
    index=0,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Bytes',
    full_name='config.Config.Bytes',
    index=1,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='String',
    full_name='config.Config.String',
    index=2,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteToMemory',
    full_name='config.Config.WriteToMemory',
    index=3,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadChainConfigFromMemory',
    full_name='config.Config.ReadChainConfigFromMemory',
    index=4,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTotalSupply',
    full_name='config.Config.GetTotalSupply',
    index=5,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONFIG)

DESCRIPTOR.services_by_name['Config'] = _CONFIG

# @@protoc_insertion_point(module_scope)
