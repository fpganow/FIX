#!/usr/bin/env python3

import unittest

from Fix42 import *


class Create_Fix42_Messages_Test(unittest.TestCase):
    """ Tests for creating, parsing and dumping Fix 4.2 messages """

    def test_create_Heartbeat(self):
#8=FIX.4.1|9=61|35=A|34=1|49=EXEC|52=20121105-23:24:06|56=BANZAI|98=0|108=30|10=003|
        # GIVEN
        messageArgs = [ MessageType.Heartbeat, { } ]

        # WHEN
        message = FixMessageFactory.createFromArgs( messageArgs )
        rawBytes = message.getRawBytes()

        # THEN
        self.assertEqual( rawBytes[0:10], "8=FIX.4.1\n".encode('ascii') )
        self.assertEqual( rawBytes[10:16], "9=100\n".encode('ascii') )

        splitArray = rawBytes.split("\n")
        print("len: {}".format( len(splitArray) ))

if __name__ == "__main__":
    unittest.main()
