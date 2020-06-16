# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protos.pspnet_pb2
import protos.icnet_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model.proto',
  package='fast_semantic_segmentation.protos',
  serialized_pb=_b('\n\x12protos/model.proto\x12!fast_semantic_segmentation.protos\x1a\x13protos/pspnet.proto\x1a\x12protos/icnet.proto\"\x98\x01\n\x15\x46\x61stSegmentationModel\x12;\n\x06pspnet\x18\x01 \x01(\x0b\x32).fast_semantic_segmentation.protos.PSPNetH\x00\x12\x39\n\x05icnet\x18\x02 \x01(\x0b\x32(.fast_semantic_segmentation.protos.ICNetH\x00\x42\x07\n\x05model')
  ,
  dependencies=[protos.pspnet_pb2.DESCRIPTOR,protos.icnet_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FASTSEGMENTATIONMODEL = _descriptor.Descriptor(
  name='FastSegmentationModel',
  full_name='fast_semantic_segmentation.protos.FastSegmentationModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pspnet', full_name='fast_semantic_segmentation.protos.FastSegmentationModel.pspnet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icnet', full_name='fast_semantic_segmentation.protos.FastSegmentationModel.icnet', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='model', full_name='fast_semantic_segmentation.protos.FastSegmentationModel.model',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=99,
  serialized_end=251,
)

_FASTSEGMENTATIONMODEL.fields_by_name['pspnet'].message_type = protos.pspnet_pb2._PSPNET
_FASTSEGMENTATIONMODEL.fields_by_name['icnet'].message_type = protos.icnet_pb2._ICNET
_FASTSEGMENTATIONMODEL.oneofs_by_name['model'].fields.append(
  _FASTSEGMENTATIONMODEL.fields_by_name['pspnet'])
_FASTSEGMENTATIONMODEL.fields_by_name['pspnet'].containing_oneof = _FASTSEGMENTATIONMODEL.oneofs_by_name['model']
_FASTSEGMENTATIONMODEL.oneofs_by_name['model'].fields.append(
  _FASTSEGMENTATIONMODEL.fields_by_name['icnet'])
_FASTSEGMENTATIONMODEL.fields_by_name['icnet'].containing_oneof = _FASTSEGMENTATIONMODEL.oneofs_by_name['model']
DESCRIPTOR.message_types_by_name['FastSegmentationModel'] = _FASTSEGMENTATIONMODEL

FastSegmentationModel = _reflection.GeneratedProtocolMessageType('FastSegmentationModel', (_message.Message,), dict(
  DESCRIPTOR = _FASTSEGMENTATIONMODEL,
  __module__ = 'protos.model_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.FastSegmentationModel)
  ))
_sym_db.RegisterMessage(FastSegmentationModel)


# @@protoc_insertion_point(module_scope)