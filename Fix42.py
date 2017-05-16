
from enum import Enum
import struct

class MessageType(Enum):
    Heartbeat = "0"

class FixMessageFactory:
    @staticmethod
    def createFromArgs( messageArgs ):
        message = Heartbeat()
        return message

class FixHeader:
    BeginString   =   "8"
    BodyLength    =   "9"
    MsgType       =  "35"
    SenderCompID  =  "49"
    TargetCompID  =  "56"


class FixMessage:
    def __init__(self):
# Header:
#  8=FIX.4.2^A
#  9=<len>^A
# 35=<msgtype>^A
# 49=<sender>^A
# 56=<target>^A
        major = 4
        minor = 2

        messageType = MessageType.Heartbeat
        sender = "JOHN"
        target = "NASDAQ"
        self.header = { }
        self.header[FixHeader.BeginString] = "FIX.{}.{}".format(major, minor)
        self.header[FixHeader.BodyLength] = ""
        self.header[FixHeader.MsgType] = ""
        self.header[FixHeader.SenderCompID] = sender
        self.header[FixHeader.TargetCompID] = target

    def getRawBytes(self):
        rawBytes = bytearray()

        rawBytes.append(0x00)
        rawBytes.append(0x01)

        return rawBytes

class Heartbeat(FixMessage):
    TestReqId = 112

    def __init__(self):
        super().__init__()

