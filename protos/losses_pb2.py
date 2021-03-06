# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/losses.proto

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
  name='protos/losses.proto',
  package='fast_semantic_segmentation.protos',
  serialized_pb=_b('\n\x13protos/losses.proto\x12!fast_semantic_segmentation.protos\"\xb8\x01\n\x04Loss\x12R\n\x13\x63lassification_loss\x18\x01 \x01(\x0b\x32\x35.fast_semantic_segmentation.protos.ClassificationLoss\x12!\n\x12use_auxiliary_loss\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x19\n\x0cignore_label\x18\x03 \x01(\r:\x03\x32\x35\x35\x12\x1e\n\x0fupsample_logits\x18\x04 \x01(\x08:\x05\x66\x61lse\"r\n\x12\x43lassificationLoss\x12O\n\x07softmax\x18\x01 \x01(\x0b\x32<.fast_semantic_segmentation.protos.SoftmaxClassificationLossH\x00\x42\x0b\n\tloss_type\"\x1b\n\x19SoftmaxClassificationLoss')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOSS = _descriptor.Descriptor(
  name='Loss',
  full_name='fast_semantic_segmentation.protos.Loss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification_loss', full_name='fast_semantic_segmentation.protos.Loss.classification_loss', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_auxiliary_loss', full_name='fast_semantic_segmentation.protos.Loss.use_auxiliary_loss', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_label', full_name='fast_semantic_segmentation.protos.Loss.ignore_label', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=255,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upsample_logits', full_name='fast_semantic_segmentation.protos.Loss.upsample_logits', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=59,
  serialized_end=243,
)


_CLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='ClassificationLoss',
  full_name='fast_semantic_segmentation.protos.ClassificationLoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='softmax', full_name='fast_semantic_segmentation.protos.ClassificationLoss.softmax', index=0,
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
      name='loss_type', full_name='fast_semantic_segmentation.protos.ClassificationLoss.loss_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=245,
  serialized_end=359,
)


_SOFTMAXCLASSIFICATIONLOSS = _descriptor.Descriptor(
  name='SoftmaxClassificationLoss',
  full_name='fast_semantic_segmentation.protos.SoftmaxClassificationLoss',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=388,
)

_LOSS.fields_by_name['classification_loss'].message_type = _CLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.fields_by_name['softmax'].message_type = _SOFTMAXCLASSIFICATIONLOSS
_CLASSIFICATIONLOSS.oneofs_by_name['loss_type'].fields.append(
  _CLASSIFICATIONLOSS.fields_by_name['softmax'])
_CLASSIFICATIONLOSS.fields_by_name['softmax'].containing_oneof = _CLASSIFICATIONLOSS.oneofs_by_name['loss_type']
DESCRIPTOR.message_types_by_name['Loss'] = _LOSS
DESCRIPTOR.message_types_by_name['ClassificationLoss'] = _CLASSIFICATIONLOSS
DESCRIPTOR.message_types_by_name['SoftmaxClassificationLoss'] = _SOFTMAXCLASSIFICATIONLOSS

Loss = _reflection.GeneratedProtocolMessageType('Loss', (_message.Message,), dict(
  DESCRIPTOR = _LOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.Loss)
  ))
_sym_db.RegisterMessage(Loss)

ClassificationLoss = _reflection.GeneratedProtocolMessageType('ClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _CLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.ClassificationLoss)
  ))
_sym_db.RegisterMessage(ClassificationLoss)

SoftmaxClassificationLoss = _reflection.GeneratedProtocolMessageType('SoftmaxClassificationLoss', (_message.Message,), dict(
  DESCRIPTOR = _SOFTMAXCLASSIFICATIONLOSS,
  __module__ = 'protos.losses_pb2'
  # @@protoc_insertion_point(class_scope:fast_semantic_segmentation.protos.SoftmaxClassificationLoss)
  ))
_sym_db.RegisterMessage(SoftmaxClassificationLoss)


# @@protoc_insertion_point(module_scope)
