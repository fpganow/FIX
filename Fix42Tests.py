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


if __name__ == "__main__":
    unittest.main()
