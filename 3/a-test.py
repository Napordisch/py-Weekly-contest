import sys
from a import stream_switcher, ToStdout, ToStderr, ToDevnull
with stream_switcher(stdout=ToDevnull, stderr=ToStdout):
    print("Hello", file=sys.stderr)
    print("Hello")
