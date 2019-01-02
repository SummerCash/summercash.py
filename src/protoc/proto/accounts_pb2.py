# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/accounts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/accounts.proto',
  package='accounts',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14proto/accounts.proto\x12\x08\x61\x63\x63ounts\"5\n\x0eGeneralRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\nprivateKey\x18\x02 \x01(\t\"\"\n\x0fGeneralResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xcb\x04\n\x08\x41\x63\x63ounts\x12\x43\n\nNewAccount\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12G\n\x0e\x41\x63\x63ountFromKey\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12G\n\x0eGetAllAccounts\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12I\n\x10MakeEncodingSafe\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12L\n\x13RecoverSafeEncoding\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12?\n\x06String\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12>\n\x05\x42ytes\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x12N\n\x15ReadAccountFromMemory\x12\x18.accounts.GeneralRequest\x1a\x19.accounts.GeneralResponse\"\x00\x62\x06proto3')
)




_GENERALREQUEST = _descriptor.Descriptor(
  name='GeneralRequest',
  full_name='accounts.GeneralRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='accounts.GeneralRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='privateKey', full_name='accounts.GeneralRequest.privateKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=87,
)


_GENERALRESPONSE = _descriptor.Descriptor(
  name='GeneralResponse',
  full_name='accounts.GeneralResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='accounts.GeneralResponse.message', index=0,
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
  serialized_start=89,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['GeneralRequest'] = _GENERALREQUEST
DESCRIPTOR.message_types_by_name['GeneralResponse'] = _GENERALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeneralRequest = _reflection.GeneratedProtocolMessageType('GeneralRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERALREQUEST,
  __module__ = 'proto.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.GeneralRequest)
  ))
_sym_db.RegisterMessage(GeneralRequest)

GeneralResponse = _reflection.GeneratedProtocolMessageType('GeneralResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERALRESPONSE,
  __module__ = 'proto.accounts_pb2'
  # @@protoc_insertion_point(class_scope:accounts.GeneralResponse)
  ))
_sym_db.RegisterMessage(GeneralResponse)



_ACCOUNTS = _descriptor.ServiceDescriptor(
  name='Accounts',
  full_name='accounts.Accounts',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=126,
  serialized_end=713,
  methods=[
  _descriptor.MethodDescriptor(
    name='NewAccount',
    full_name='accounts.Accounts.NewAccount',
    index=0,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AccountFromKey',
    full_name='accounts.Accounts.AccountFromKey',
    index=1,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllAccounts',
    full_name='accounts.Accounts.GetAllAccounts',
    index=2,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MakeEncodingSafe',
    full_name='accounts.Accounts.MakeEncodingSafe',
    index=3,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RecoverSafeEncoding',
    full_name='accounts.Accounts.RecoverSafeEncoding',
    index=4,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='String',
    full_name='accounts.Accounts.String',
    index=5,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Bytes',
    full_name='accounts.Accounts.Bytes',
    index=6,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadAccountFromMemory',
    full_name='accounts.Accounts.ReadAccountFromMemory',
    index=7,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTS)

DESCRIPTOR.services_by_name['Accounts'] = _ACCOUNTS

# @@protoc_insertion_point(module_scope)
