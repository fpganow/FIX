#!/usr/bin/env python3

from unittest import TestCase
from hamcrest import (
    assert_that,
    equal_to
)

from Fix42 import *

import logging
logger = logging.getLogger(__name__.split(".")[0])

# FIX Message types

class TestFix42(TestCase):
    """ Tests for creating, parsing and dumping Fix 4.2 messages """

    def test_create_Heartbeat(self):
        # GIVEN
        messageArgs = [ MessageType.Heartbeat, { } ]

        # WHEN
        message = FixMessageFactory.createFromArgs( messageArgs )
        rawBytes = message.getRawBytes()

        # THEN
        logger.info("INFO")
        logger.debug("DEBUG")
        assert_that( rawBytes[0:10], equal_to("8=FIX.4.1\n".encode('ascii') ))
        assert_that( rawBytes[10:16], equal_to("9=100\n".encode('ascii') ))

#        splitArray = rawBytes.split("\n")
#        print("len: {}".format( len(splitArray) ))

    def test_parse_heartbeat(self):
        # GIVEN
        heartbeat_msg = "8=FIX.4.19=11235=049=BRKR56=INVMGR34=23552=19980604-07:58:28112=19980604-07:58:2810=157"

    def test_parse_ioi(self):
        # GIVEN
        ioi_msg = "8=FIX.4.19=15435=649=BRKR56=INVMGR34=23652=19980604-07:58:4823=11568528=N55=SPMI.MI54=227=20000044=10100.00000025=H10=159"

    def test_parse_LogOn(self):
        # GIVEN
        logon_msg = "#8=FIX.4.1|9=61|35=A|34=1|49=EXEC|52=20121105-23:24:06|56=BANZAI|98=0|108=30|10=003|"

if __name__ == "__main__":
    unittest.main()
