#!/usr/bin/env python3

import sys

CR = "\x0d"
LF = "\x0a"
CRLF = CR+LF

terminator = CRLF

sys.stdout.write("check\n")
if isinstance(terminator, int):
    sys.stdout.write("OK\n")
int(LF)
