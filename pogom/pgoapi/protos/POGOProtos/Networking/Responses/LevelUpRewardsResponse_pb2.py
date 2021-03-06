# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Responses/LevelUpRewardsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Inventory.Item import ItemAward_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemAward__pb2
from POGOProtos.Inventory.Item import ItemId_pb2 as POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Responses/LevelUpRewardsResponse.proto',
  package='POGOProtos.Networking.Responses',
  syntax='proto3',
  serialized_pb=_b('\n<POGOProtos/Networking/Responses/LevelUpRewardsResponse.proto\x12\x1fPOGOProtos.Networking.Responses\x1a)POGOProtos/Inventory/Item/ItemAward.proto\x1a&POGOProtos/Inventory/Item/ItemId.proto\"\x97\x02\n\x16LevelUpRewardsResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.POGOProtos.Networking.Responses.LevelUpRewardsResponse.Result\x12;\n\ritems_awarded\x18\x02 \x03(\x0b\x32$.POGOProtos.Inventory.Item.ItemAward\x12\x39\n\x0eitems_unlocked\x18\x04 \x03(\x0e\x32!.POGOProtos.Inventory.Item.ItemId\"5\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x13\n\x0f\x41WARDED_ALREADY\x10\x02\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Inventory_dot_Item_dot_ItemAward__pb2.DESCRIPTOR,POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LEVELUPREWARDSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='POGOProtos.Networking.Responses.LevelUpRewardsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AWARDED_ALREADY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=407,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_LEVELUPREWARDSRESPONSE_RESULT)


_LEVELUPREWARDSRESPONSE = _descriptor.Descriptor(
  name='LevelUpRewardsResponse',
  full_name='POGOProtos.Networking.Responses.LevelUpRewardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='POGOProtos.Networking.Responses.LevelUpRewardsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items_awarded', full_name='POGOProtos.Networking.Responses.LevelUpRewardsResponse.items_awarded', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items_unlocked', full_name='POGOProtos.Networking.Responses.LevelUpRewardsResponse.items_unlocked', index=2,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEVELUPREWARDSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=460,
)

_LEVELUPREWARDSRESPONSE.fields_by_name['result'].enum_type = _LEVELUPREWARDSRESPONSE_RESULT
_LEVELUPREWARDSRESPONSE.fields_by_name['items_awarded'].message_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemAward__pb2._ITEMAWARD
_LEVELUPREWARDSRESPONSE.fields_by_name['items_unlocked'].enum_type = POGOProtos_dot_Inventory_dot_Item_dot_ItemId__pb2._ITEMID
_LEVELUPREWARDSRESPONSE_RESULT.containing_type = _LEVELUPREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['LevelUpRewardsResponse'] = _LEVELUPREWARDSRESPONSE

LevelUpRewardsResponse = _reflection.GeneratedProtocolMessageType('LevelUpRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LEVELUPREWARDSRESPONSE,
  __module__ = 'POGOProtos.Networking.Responses.LevelUpRewardsResponse_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Responses.LevelUpRewardsResponse)
  ))
_sym_db.RegisterMessage(LevelUpRewardsResponse)


# @@protoc_insertion_point(module_scope)
