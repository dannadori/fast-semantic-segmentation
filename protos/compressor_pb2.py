# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/compressor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/compressor.proto',
  package='fast_semantic_segmentation.protos',
  serialized_pb=_b('\n\x17protos/compressor.proto\x12!fast_semantic_segmentation.protos\"j\n\x12\x43ommpressionConfig\x12T\n\x14\x63ompression_strategy\x18\x01 \x01(\x0b\x32\x36.fast_semantic_segmentation.protos.CompressionStrategy\"w\n\x13\x43ompressionStrategy\x12H\n\rfilter_pruner\x18\x01 \x01(\x0b\x32/.fast_semantic_segmentation.protos.FilterPrunerH\x00\x42\x16\n\x14\x63ompression_strategy\"\xc4\x02\n\x0c\x46ilterPruner\x12:\n\x05input\x18\x01 \x01(\x0b\x32+.fast_semantic_segmentation.protos.NodeName\x12;\n\x06output\x18\x02 \x01(\x0b\x32+.fast_semantic_segmentation.protos.NodeName\x12\x12\n\nnode_scope\x18\x03 \x01(\t\x12\x1f\n\x12\x63ompression_factor\x18\x04 \x01(\x02:\x03\x30.5\x12>\n\tskip_node\x18\x05 \x03(\x0b\x32+.fast_semantic_segmentation.protos.NodeName\x12\x46\n\x04node\x18\x06 \x03(\x0b\x32\x38.fast_semantic_segmentation.protos.SingleNodePruningSpec\"\xeb\x01\n\x15SingleNodePruningSpec\x12;\n\x06target\x18\x01 \x01(\x0b\x32+.fast_semantic_segmentation.protos.NodeName\x12;\n\x06source\x18\x02 \x01(\x0b\x32+.fast_semantic_segmentation.protos.NodeName\x12>\n\tfollowing\x18\x03 \x03(\x0b\x32+.fast_semantic_segmentation.protos.NodeName\x12\x18\n\nnode_scope\x18\x04 \x01(\t:\x04null\"\x18\n\x08NodeName\x12\x0c\n\x04name\x18\x01 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMMPRESSIONCONFIG = _descriptor.Descriptor(
  name='CommpressionConfig',
  full_name='fast_semantic_segmentation.protos.CommpressionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='compression_strategy', full_name='fast_semantic_segmentation.protos.CommpressionConfig.compression_strategy', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=62,
  serialized_end=168,
)


_COMPRESSIONSTRATEGY = _descriptor.Descriptor(
  name='CompressionStrategy',
  full_name='fast_semantic_segmentation.protos.CompressionStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filter_pruner', full_name='fast_semantic_segmentation.protos.CompressionStrategy.filter_pruner', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
      name='compression_strategy', full_name='fast_semantic_segmentation.protos.CompressionStrategy.compression_strategy',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=170,
  serialized_end=289,
)


_FILTERPRUNER = _descriptor.Descriptor(
  name='FilterPruner',
  full_name='fast_semantic_segmentation.protos.FilterPruner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='fast_semantic_segmentation.protos.FilterPruner.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output', full_name='fast_semantic_segmentation.protos.FilterPruner.output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_scope', full_name='fast_semantic_segmentation.protos.FilterPruner.node_scope', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compression_factor', full_name='fast_semantic_segmentation.protos.FilterPruner.compression_factor', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0.5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skip_node', full_name='fast_semantic_segmentation.protos.FilterPruner.skip_node', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='fast_semantic_segmentation.protos.FilterPruner.node', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  ],
  serialized_start=292,
  serialized_end=616,
)


_SINGLENODEPRUNINGSPEC = _descriptor.Descriptor(
  name='SingleNodePruningSpec',
  full_name='fast_semantic_segmentation.protos.SingleNodePruningSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='fast_semantic_segmentation.protos.SingleNodePruningSpec.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='fast_semantic_segmentation.protos.SingleNodePruningSpec.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='following', full_name='fast_semantic_segmentation.protos.SingleNodePruningSpec.following', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_scope', full_name='fast_semantic_segmentation.protos.SingleNodePruningSpec.node_scope', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("null").decode('utf-8'),
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
  ],
  serialized_start=619,
  serialized_end=854,
)


_NODENAME = _descriptor.Descriptor(
  name='NodeName',
  full_name='fast_semantic_segmentation.protos.NodeName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fast_semantic_segmentation.protos.NodeName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  ],
  serialized_start=856,
  serialized_end=880,
)

_COMMPRESSIONCONFIG.fields_by_name['compression_strategy'].message_type = _COMPRESSIONSTRATEGY
_COMPRESSIONSTRATEGY.fields_by_name['filter_pruner'].message_type = _FILTERPRUNER
_COMPRESSIONSTRATEGY.oneofs_by_name['compression_strategy'].fields.append(
  _COMPRESSIONSTRATEGY.fields_by_name['filter_pruner'])
_COMPRESSIONSTRATEGY.fields_by_name['filter_pruner'].containing_oneof = _COMPRESSIONSTRATEGY.oneofs_by_name['compression_strategy']
_FILTERPRUNER.fields_by_name['input'].message_type = _NODENAME
_FILTERPRUNER.fields_by_name['output'].message_type = _NODENAME
_FILTERPRUNER.fields_by_name['skip_node'].message_type = _NODENAME
_FILTERPRUNER.fields_by_name['node'].message_type = _SINGLENODEPRUNINGSPEC
_SINGLENODEPRUNINGSPEC.fields_by_name['target'].message_type = _NODENAME
_SINGLENODEPRUNINGSPEC.fields_by_name['source'].message_type = _NODENAME
_SINGLENODEPRUNINGSPEC.fields_by_name['following'].message_type = _NODENAME
DESCRIPTOR.message_types_by_name['CommpressionConfig'] = _COMMPRESSIONCONFIG
DESCRIPTOR.message_types_by_name['CompressionStrategy'] = _COMPRESSIONSTRATEGY
DESCRIPTOR.message_types_by_name['FilterPruner'] = _FILTERPRUNER
DESCRIPTOR.message_types_by_name['SingleNodePruningSpec'] = _SINGLENODEPRUNINGSPEC
DESCRIPTOR.message_types_by_name['NodeName'] = _NODENAME

CommpressionConfig = _reflection.GeneratedProtocolMessageType('CommpressionConfig', (_message.Message,), dict(
  DESCRIPTOR = _COMMPRESSIONCONFIG,
  __module__ = 'protos.compressor_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.CommpressionConfig)
  ))
_sym_db.RegisterMessage(CommpressionConfig)

CompressionStrategy = _reflection.GeneratedProtocolMessageType('CompressionStrategy', (_message.Message,), dict(
  DESCRIPTOR = _COMPRESSIONSTRATEGY,
  __module__ = 'protos.compressor_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.CompressionStrategy)
  ))
_sym_db.RegisterMessage(CompressionStrategy)

FilterPruner = _reflection.GeneratedProtocolMessageType('FilterPruner', (_message.Message,), dict(
  DESCRIPTOR = _FILTERPRUNER,
  __module__ = 'protos.compressor_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.FilterPruner)
  ))
_sym_db.RegisterMessage(FilterPruner)

SingleNodePruningSpec = _reflection.GeneratedProtocolMessageType('SingleNodePruningSpec', (_message.Message,), dict(
  DESCRIPTOR = _SINGLENODEPRUNINGSPEC,
  __module__ = 'protos.compressor_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.SingleNodePruningSpec)
  ))
_sym_db.RegisterMessage(SingleNodePruningSpec)

NodeName = _reflection.GeneratedProtocolMessageType('NodeName', (_message.Message,), dict(
  DESCRIPTOR = _NODENAME,
  __module__ = 'protos.compressor_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.NodeName)
  ))
_sym_db.RegisterMessage(NodeName)


# @@protoc_insertion_point(module_scope)
