
from enum import Enum
import struct

class MessageType(Enum):
    Heartbeat = "0"

class FixMessageFactory:
    @staticmethod
    def createFromArgs( messageArgs ):
        message = Heartbeat()
        return message

#class FixHeader:


class FixMessage:

    class FixHeader:
        BeginString   =   8
        BodyLength    =   "9"
        MsgType       =  "35"
        SenderCompID  =  "49"
        TargetCompID  =  "56"

        def __init__(self, major, minor, messageType, sender, target):
            self.major = major
            self.minor = minor
            self.messageType = messageType
            self.sender = sender
            self.target = target

        def getRawBytes(self, messageLen):
            rawBytes = bytearray()
            print("BeginString={}".format(self.BeginString))
            print("major={}".format(self.major))
            print("minor={}".format(self.minor))
            beginString = "{}=FIX.{}.{}\n".format(self.BeginString, self.major, self.minor)
            rawBytes.extend( beginString.encode('ascii') )

            messageLength = "{}={}\n".format( self.BodyLength, messageLen )
            rawBytes.extend( messageLength.encode('ascii') )

            return rawBytes

    def __init__(self):
#8=FIX.4.1|9=61|35=A|34=1|49=EXEC|52=20121105-23:24:06|56=BANZAI|98=0|108=30|10=003|
# Header:
#  8=FIX.4.2^A
#  9=<len>^A
# 35=<msgtype>^A
# 49=<sender>^A
# 56=<target>^A
        major = 4
        minor = 1
        sender = "EXEC"
        target = "BANZAI"
        messageType = MessageType.Heartbeat
        self.header = FixMessage.FixHeader(major, minor, messageType, sender, target)
        self.messageLen = 100
#        self.header
#        self.header.append("{}=FIX.{}.{}\n".format(FixHeader.BeginString, major, minor))
        #self.header.append( 0xA )
        #self.header[FixHeader.BodyLength] = ""
        #self.header[FixHeader.MsgType] = ""
        #self.header[FixHeader.SenderCompID] = sender
        #self.header[FixHeader.TargetCompID] = target

    def getRawBytes(self):
        rawBytes = bytearray()
        rawHeaderBytes = self.header.getRawBytes(self.messageLen)
        #print("self.header: {}".format(self.header[0]))
        #rawBytes.extend(map(ord, self.header[0] ))
#        rawBytes.append(0x0A)

        rawBytes.extend( rawHeaderBytes )
        #return rawHeaderBytes
        return rawBytes

class Heartbeat(FixMessage):
    TestReqId = 112

    def __init__(self):
        super().__init__()

