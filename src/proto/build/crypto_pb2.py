# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crypto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crypto.proto',
  package='crypto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63rypto.proto\x12\x06\x63rypto\"*\n\x0eGeneralRequest\x12\r\n\x05input\x18\x01 \x01(\x0c\x12\t\n\x01n\x18\x02 \x01(\r\"\"\n\x0fGeneralResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x80\x03\n\x06\x43rypto\x12\x39\n\x04Sha3\x12\x16.crypto.GeneralRequest\x1a\x17.crypto.GeneralResponse\"\x00\x12?\n\nSha3String\x12\x16.crypto.GeneralRequest\x1a\x17.crypto.GeneralResponse\"\x00\x12:\n\x05Sha3n\x12\x16.crypto.GeneralRequest\x1a\x17.crypto.GeneralResponse\"\x00\x12@\n\x0bSha3nString\x12\x16.crypto.GeneralRequest\x1a\x17.crypto.GeneralResponse\"\x00\x12:\n\x05Sha3d\x12\x16.crypto.GeneralRequest\x1a\x17.crypto.GeneralResponse\"\x00\x12@\n\x0bSha3dString\x12\x16.crypto.GeneralRequest\x1a\x17.crypto.GeneralResponse\"\x00\x62\x06proto3')
)




_GENERALREQUEST = _descriptor.Descriptor(
  name='GeneralRequest',
  full_name='crypto.GeneralRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='crypto.GeneralRequest.input', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n', full_name='crypto.GeneralRequest.n', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=24,
  serialized_end=66,
)


_GENERALRESPONSE = _descriptor.Descriptor(
  name='GeneralResponse',
  full_name='crypto.GeneralResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='crypto.GeneralResponse.message', index=0,
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
  __module__ = 'crypto_pb2'
  # @@protoc_insertion_point(class_scope:crypto.GeneralRequest)
  ))
_sym_db.RegisterMessage(GeneralRequest)

GeneralResponse = _reflection.GeneratedProtocolMessageType('GeneralResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERALRESPONSE,
  __module__ = 'crypto_pb2'
  # @@protoc_insertion_point(class_scope:crypto.GeneralResponse)
  ))
_sym_db.RegisterMessage(GeneralResponse)



_CRYPTO = _descriptor.ServiceDescriptor(
  name='Crypto',
  full_name='crypto.Crypto',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=105,
  serialized_end=489,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sha3',
    full_name='crypto.Crypto.Sha3',
    index=0,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sha3String',
    full_name='crypto.Crypto.Sha3String',
    index=1,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sha3n',
    full_name='crypto.Crypto.Sha3n',
    index=2,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sha3nString',
    full_name='crypto.Crypto.Sha3nString',
    index=3,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sha3d',
    full_name='crypto.Crypto.Sha3d',
    index=4,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sha3dString',
    full_name='crypto.Crypto.Sha3dString',
    index=5,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CRYPTO)

DESCRIPTOR.services_by_name['Crypto'] = _CRYPTO

# @@protoc_insertion_point(module_scope)
