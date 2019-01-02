# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/transaction.proto',
  package='transaction',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17proto/transaction.proto\x12\x0btransaction\"c\n\x0eGeneralRequest\x12\r\n\x05nonce\x18\x01 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x10\n\x08\x61\x64\x64ress2\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x01\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\"\"\n\x0fGeneralResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb1\x04\n\x0bTransaction\x12M\n\x0eNewTransaction\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x12S\n\x14TransactionFromBytes\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x12\x46\n\x07Publish\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x12\x44\n\x05\x42ytes\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x12\x45\n\x06String\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x12N\n\x0fSignTransaction\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x12Y\n\x1aVerifyTransactionSignature\x12\x1b.transaction.GeneralRequest\x1a\x1c.transaction.GeneralResponse\"\x00\x62\x06proto3')
)




_GENERALREQUEST = _descriptor.Descriptor(
  name='GeneralRequest',
  full_name='transaction.GeneralRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='transaction.GeneralRequest.nonce', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='transaction.GeneralRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address2', full_name='transaction.GeneralRequest.address2', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='transaction.GeneralRequest.amount', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='transaction.GeneralRequest.payload', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=40,
  serialized_end=139,
)


_GENERALRESPONSE = _descriptor.Descriptor(
  name='GeneralResponse',
  full_name='transaction.GeneralResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='transaction.GeneralResponse.message', index=0,
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
  serialized_start=141,
  serialized_end=175,
)

DESCRIPTOR.message_types_by_name['GeneralRequest'] = _GENERALREQUEST
DESCRIPTOR.message_types_by_name['GeneralResponse'] = _GENERALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeneralRequest = _reflection.GeneratedProtocolMessageType('GeneralRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENERALREQUEST,
  __module__ = 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.GeneralRequest)
  ))
_sym_db.RegisterMessage(GeneralRequest)

GeneralResponse = _reflection.GeneratedProtocolMessageType('GeneralResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERALRESPONSE,
  __module__ = 'proto.transaction_pb2'
  # @@protoc_insertion_point(class_scope:transaction.GeneralResponse)
  ))
_sym_db.RegisterMessage(GeneralResponse)



_TRANSACTION = _descriptor.ServiceDescriptor(
  name='Transaction',
  full_name='transaction.Transaction',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=178,
  serialized_end=739,
  methods=[
  _descriptor.MethodDescriptor(
    name='NewTransaction',
    full_name='transaction.Transaction.NewTransaction',
    index=0,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TransactionFromBytes',
    full_name='transaction.Transaction.TransactionFromBytes',
    index=1,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Publish',
    full_name='transaction.Transaction.Publish',
    index=2,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Bytes',
    full_name='transaction.Transaction.Bytes',
    index=3,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='String',
    full_name='transaction.Transaction.String',
    index=4,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SignTransaction',
    full_name='transaction.Transaction.SignTransaction',
    index=5,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyTransactionSignature',
    full_name='transaction.Transaction.VerifyTransactionSignature',
    index=6,
    containing_service=None,
    input_type=_GENERALREQUEST,
    output_type=_GENERALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSACTION)

DESCRIPTOR.services_by_name['Transaction'] = _TRANSACTION

# @@protoc_insertion_point(module_scope)
