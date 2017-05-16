#!/usr/bin/env python3

import unittest

from Fix42 import *


class Create_Fix42_Messages_Test(unittest.TestCase):
    """ Tests for creating, parsing and dumping Fix 4.2 messages """

    def test_create_Heartbeat(self):
        # GIVEN
        messageArgs = [ MessageType.Heartbeat, { } ]

        # WHEN
        message = FixMessageFactory.createFromArgs( messageArgs )
        rawBytes = message.getRawBytes()

        # THEN
        self.assertEqual( rawBytes[0], ord('8') )
        self.assertEqual( rawBytes[1], ord('=') )
        self.assertEqual( rawBytes[2], ord('F') )
        self.assertEqual( rawBytes[3], ord('I') )
        self.assertEqual( rawBytes[4], ord('X') )
        self.assertEqual( rawBytes[], ord('.') )
        self.assertEqual( rawBytes[],    0x0A  )

if __name__ == "__main__":
    unittest.main()
