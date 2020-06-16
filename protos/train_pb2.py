# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/train.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protos.optimizer_pb2
import protos.preprocessor_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/train.proto',
  package='fast_semantic_segmentation.protos',
  serialized_pb=_b('\n\x12protos/train.proto\x12!fast_semantic_segmentation.protos\x1a\x16protos/optimizer.proto\x1a\x19protos/preprocessor.proto\"\xb6\x04\n\x0bTrainConfig\x12\x16\n\nbatch_size\x18\x01 \x01(\r:\x02\x33\x32\x12O\n\x11preprocessor_step\x18\x02 \x03(\x0b\x32\x34.fast_semantic_segmentation.protos.PreprocessingStep\x12+\n\x1dkeep_checkpoint_every_n_hours\x18\x03 \x01(\r:\x04\x31\x30\x30\x30\x12?\n\toptimizer\x18\x04 \x01(\x0b\x32,.fast_semantic_segmentation.protos.Optimizer\x12\x1e\n\x14\x66ine_tune_checkpoint\x18\x05 \x01(\t:\x00\x12#\n\x19\x66ine_tune_checkpoint_type\x18\x06 \x01(\t:\x00\x12(\n\x19\x66reeze_fine_tune_backbone\x18\x07 \x01(\x08:\x05\x66\x61lse\x12\x14\n\tnum_steps\x18\x08 \x01(\r:\x01\x30\x12!\n\x14\x62\x61tch_queue_capacity\x18\t \x01(\x05:\x03\x31\x35\x30\x12\"\n\x17num_batch_queue_threads\x18\n \x01(\x05:\x01\x38\x12\"\n\x17prefetch_queue_capacity\x18\x0b \x01(\x05:\x01\x35\x12%\n\x17\x61\x64\x64_regularization_loss\x18\x0c \x01(\x08:\x04true\x12\x1b\n\x13quantize_with_delay\x18\r \x01(\x05\x12\x1c\n\x11num_queue_threads\x18\x0e \x01(\x05:\x01\x38')
  ,
  dependencies=[protos.optimizer_pb2.DESCRIPTOR,protos.preprocessor_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRAINCONFIG = _descriptor.Descriptor(
  name='TrainConfig',
  full_name='fast_semantic_segmentation.protos.TrainConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='fast_semantic_segmentation.protos.TrainConfig.batch_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preprocessor_step', full_name='fast_semantic_segmentation.protos.TrainConfig.preprocessor_step', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keep_checkpoint_every_n_hours', full_name='fast_semantic_segmentation.protos.TrainConfig.keep_checkpoint_every_n_hours', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='fast_semantic_segmentation.protos.TrainConfig.optimizer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_tune_checkpoint', full_name='fast_semantic_segmentation.protos.TrainConfig.fine_tune_checkpoint', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_tune_checkpoint_type', full_name='fast_semantic_segmentation.protos.TrainConfig.fine_tune_checkpoint_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='freeze_fine_tune_backbone', full_name='fast_semantic_segmentation.protos.TrainConfig.freeze_fine_tune_backbone', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_steps', full_name='fast_semantic_segmentation.protos.TrainConfig.num_steps', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_queue_capacity', full_name='fast_semantic_segmentation.protos.TrainConfig.batch_queue_capacity', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=150,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_batch_queue_threads', full_name='fast_semantic_segmentation.protos.TrainConfig.num_batch_queue_threads', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prefetch_queue_capacity', full_name='fast_semantic_segmentation.protos.TrainConfig.prefetch_queue_capacity', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_regularization_loss', full_name='fast_semantic_segmentation.protos.TrainConfig.add_regularization_loss', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantize_with_delay', full_name='fast_semantic_segmentation.protos.TrainConfig.quantize_with_delay', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_queue_threads', full_name='fast_semantic_segmentation.protos.TrainConfig.num_queue_threads', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8,
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
  serialized_start=109,
  serialized_end=675,
)

_TRAINCONFIG.fields_by_name['preprocessor_step'].message_type = protos.preprocessor_pb2._PREPROCESSINGSTEP
_TRAINCONFIG.fields_by_name['optimizer'].message_type = protos.optimizer_pb2._OPTIMIZER
DESCRIPTOR.message_types_by_name['TrainConfig'] = _TRAINCONFIG

TrainConfig = _reflection.GeneratedProtocolMessageType('TrainConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRAINCONFIG,
  __module__ = 'protos.train_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.TrainConfig)
  ))
_sym_db.RegisterMessage(TrainConfig)


# @@protoc_insertion_point(module_scope)