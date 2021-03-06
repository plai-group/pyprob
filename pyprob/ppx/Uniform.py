# automatically generated by the FlatBuffers compiler, do not modify

# namespace: ppx

import flatbuffers

class Uniform(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsUniform(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Uniform()
        x.Init(buf, n + offset)
        return x

    # Uniform
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Uniform
    def Low(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Uniform
    def High(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Tensor import Tensor
            obj = Tensor()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def UniformStart(builder): builder.StartObject(2)
def UniformAddLow(builder, low): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(low), 0)
def UniformAddHigh(builder, high): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(high), 0)
def UniformEnd(builder): return builder.EndObject()
