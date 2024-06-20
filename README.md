# tail-bazel-build-events

When Bazel is invoked with the `--build_event_binary_file=<file>` option, Bazel
will write [Build Events Protocol](https://bazel.build/remote/bep) (BEP)
messages to the given file. The BEP messages describe steps, progress, and
information regarding a Bazel invocation. Bazel writes these messages
periodically during invocation to provide realtime-ish insights.

This repo contains a simple script that outputs the BEP messages as they're
written to the message file. The script is mainly just meant as a simple
example. You can expand on it however you like if you find it helpful.

## Example usage

In one shell:
```
$ touch /tmp/bep-events.bin
$ python3 main.py /tmp/bep-events.bin
```

In another shell:
```
$ bazel build --build_event_binary_file=/tmp/bep-events.bin //foo/bar/baz
```

## License

Bazel formats the BEP messages it writes to the message file as protobuf
messages. In Bazel's [official
repository](https://github.com/bazelbuild/bazel/tree/release-6.5.0), they
provide some `.proto` files that define the protobuf messages. These  `.proto`
files are set up to be compiled into a Java library. For this project I needed
to consume the messages using Python, so I copied the `.proto` files from
Bazel's repo into the `proto_src` directory. I updated the `required`-statement
paths. (The `*_pb2.py` files found in `proto` directory were compiled from
these `.proto` files.) Bazel uses the Apache-2.0 license, and this blurb is
meant to address term 4.b. of that license.
