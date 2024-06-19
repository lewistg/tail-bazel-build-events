#!/usr/bin/env python3

import json
import argparse
import time
import proto.build_event_stream_pb2 as build_event_stream_pb2
from google.protobuf.json_format import MessageToDict

INT_32_BYTE_SIZE = 4
LEAST_SEVEN_BITS = 0x7F
MOST_SIGNIFICANT_BIT = 0x80

parser = argparse.ArgumentParser(
    prog="tail-bazel-beps",
    description="Outputs the Build Events Protocol messages that bazel writes to a given file.",
)
parser.add_argument(
    "filename",
    help="The file bazel appends BEP messages to. This argument should probably always match some <file> argument being passed into bazel using the --build_event_binary_file=<file> option.",
)


class BuildEventStream:
    """Stream of Build Event Protocol (BEP) messages.

    When a bazel command is run using the `--build_event_binary_file=<file>`
    option, then bazel will write BEP messages to the specified file. Bazel
    writes the events as they happen, and this class can be used to read the
    messages as they are written. See [1] for information.

    [1]: https://bazel.build/remote/bep
    """

    def __init__(self, events_file_path):
        self._events_file_path = events_file_path

    def __enter__(self):
        self._events_file = open(self._events_file_path, "rb")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._events_file.close()

    def __iter__(self):
        return self

    def __next__(self):
        return self._read_next_event()

    def _read_next_event(self):
        """Reads next available message from the BEP message file.

        Note: The format of the binary BEP message file looks like this:
        ```
        [<message-length><message>][<message-length><message>]...
        ```
        """

        event_size = self._read_var_int_32()
        event_bytes = self._read_next_bytes(event_size)
        build_event = build_event_stream_pb2.BuildEvent()
        build_event.ParseFromString(event_bytes)
        return build_event

    def _read_var_int_32(self):
        """Reads a variable length 32-bit non-negative integer.

        "Variable length" because the integer's bits are stored across a variable
        length sequnce of bytes. The most significant bit in each byte
        represents a continuation flag; a non-zero value indicates the next
        byte is part of the current integer. The remaning 7 bits in each byte
        contain the integer's bits stored in littl-endian order.

        For a fuller explanation see [1].

        [1]: https://protobuf.dev/programming-guides/encoding/#varints
        """
        result = 0
        i = 0
        while i < INT_32_BYTE_SIZE:
            next_byte = self._read_next_bytes(1)[0]
            next_bits = next_byte & LEAST_SEVEN_BITS
            next_bits <<= i * 7
            result |= next_bits
            if not (next_byte & MOST_SIGNIFICANT_BIT):
                break
            i += 1
        return result

    def _read_next_bytes(self, num_bytes):
        data = bytearray()
        while len(data) < num_bytes:
            next_bytes = self._events_file.read(num_bytes - len(data))
            if not next_bytes:
                time.sleep(0.1)
            else:
                data.extend(next_bytes)
        return bytes(data)


def main():
    args = parser.parse_args()

    with BuildEventStream(args.filename) as build_event_stream:
        for event in build_event_stream:
            event_dict = MessageToDict(event)
            print(json.dumps(event_dict, indent=2))


if __name__ == "__main__":
    main()
