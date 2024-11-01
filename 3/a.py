import sys
import os
from contextlib import contextmanager


class ToStdout:
    def __enter__(self):
        return sys.stdout

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ToStderr:
    def __enter__(self):
        return sys.stderr

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ToDevnull:
    def __enter__(self):
        self._file = open(os.devnull, 'w')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


@contextmanager
def stream_switcher(stdout=None, stderr=None):
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    if stdout is not None:
        sys.stdout = stdout().__enter__()
    if stderr is not None:
        sys.stderr = stderr().__enter__()

    try:
        yield
    finally:
        if stdout is not None:
            sys.stdout = original_stdout
        if stderr is not None:
            sys.stderr = original_stderr
