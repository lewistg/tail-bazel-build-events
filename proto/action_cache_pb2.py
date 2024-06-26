# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: proto/action_cache.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'proto/action_cache.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/action_cache.proto\x12\x05\x62laze\"\xc8\x03\n\x15\x41\x63tionCacheStatistics\x12\x15\n\rsize_in_bytes\x18\x01 \x01(\x04\x12\x17\n\x0fsave_time_in_ms\x18\x02 \x01(\x04\x12\x0c\n\x04hits\x18\x03 \x01(\x05\x12\x0e\n\x06misses\x18\x04 \x01(\x05\x12=\n\x0cmiss_details\x18\x05 \x03(\x0b\x32\'.blaze.ActionCacheStatistics.MissDetail\x12\x17\n\x0fload_time_in_ms\x18\x06 \x01(\x04\x1aT\n\nMissDetail\x12\x37\n\x06reason\x18\x01 \x01(\x0e\x32\'.blaze.ActionCacheStatistics.MissReason\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\"\xb2\x01\n\nMissReason\x12\x18\n\x14\x44IFFERENT_ACTION_KEY\x10\x00\x12\x12\n\x0e\x44IFFERENT_DEPS\x10\x01\x12\x19\n\x15\x44IFFERENT_ENVIRONMENT\x10\x02\x12\x13\n\x0f\x44IFFERENT_FILES\x10\x03\x12\x19\n\x15\x43ORRUPTED_CACHE_ENTRY\x10\x04\x12\x0e\n\nNOT_CACHED\x10\x05\x12\x1b\n\x17UNCONDITIONAL_EXECUTION\x10\x06\x42\x35\n+com.google.devtools.build.lib.actions.cacheB\x06Protosb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.action_cache_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.devtools.build.lib.actions.cacheB\006Protos'
  _globals['_ACTIONCACHESTATISTICS']._serialized_start=36
  _globals['_ACTIONCACHESTATISTICS']._serialized_end=492
  _globals['_ACTIONCACHESTATISTICS_MISSDETAIL']._serialized_start=227
  _globals['_ACTIONCACHESTATISTICS_MISSDETAIL']._serialized_end=311
  _globals['_ACTIONCACHESTATISTICS_MISSREASON']._serialized_start=314
  _globals['_ACTIONCACHESTATISTICS_MISSREASON']._serialized_end=492
# @@protoc_insertion_point(module_scope)
