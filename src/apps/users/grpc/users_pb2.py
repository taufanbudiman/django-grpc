# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: src/apps/users/grpc/users.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'src/apps/users/grpc/users.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsrc/apps/users/grpc/users.proto\x12\ncore.users\"\x11\n\x0fUserListRequest\"=\n\x10UserListResponse\x12)\n\x07results\x18\x01 \x03(\x0b\x32\x18.core.users.UserResponse\"V\n\x0cUserResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\x05\x65mail\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x05\n\x03_idB\x08\n\x06_email\"!\n\x13UserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x9e\x01\n\x0eUserController\x12\x43\n\x04List\x12\x1b.core.users.UserListRequest\x1a\x1c.core.users.UserListResponse\"\x00\x12G\n\x08Retrieve\x12\x1f.core.users.UserRetrieveRequest\x1a\x18.core.users.UserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.apps.users.grpc.users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERLISTREQUEST']._serialized_start=47
  _globals['_USERLISTREQUEST']._serialized_end=64
  _globals['_USERLISTRESPONSE']._serialized_start=66
  _globals['_USERLISTRESPONSE']._serialized_end=127
  _globals['_USERRESPONSE']._serialized_start=129
  _globals['_USERRESPONSE']._serialized_end=215
  _globals['_USERRETRIEVEREQUEST']._serialized_start=217
  _globals['_USERRETRIEVEREQUEST']._serialized_end=250
  _globals['_USERCONTROLLER']._serialized_start=253
  _globals['_USERCONTROLLER']._serialized_end=411
# @@protoc_insertion_point(module_scope)
