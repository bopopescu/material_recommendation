# -*- coding:utf-8 -*-
#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from __future__ import absolute_import
from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from rpc_thrift.cython.cybinary_protocol import TCyBinaryProtocol
except:
  TCyBinaryProtocol = None



class RpcException(TException):
  """
  Attributes:
   - code
   - msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'code', None, None, ), # 1
    (2, TType.STRING, 'msg', None, None, ), # 2
  )

  def __init__(self, code=None, msg=None,):
    self.code = code
    self.msg = msg

  def read(self, iprot):
    if iprot.__class__ == TCyBinaryProtocol and self.thrift_spec is not None:
      iprot.read_struct(self)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.code = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.msg = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TCyBinaryProtocol and self.thrift_spec is not None:
      oprot.write_struct(self)
      return
    oprot.writeStructBegin('RpcException')
    if self.code is not None:
      oprot.writeFieldBegin('code', TType.I32, 1)
      oprot.writeI32(self.code)
      oprot.writeFieldEnd()
    if self.msg is not None:
      oprot.writeFieldBegin('msg', TType.STRING, 2)
      oprot.writeString(self.msg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.code)
    value = (value * 31) ^ hash(self.msg)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
