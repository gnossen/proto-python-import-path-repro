# Repro of https://github.com/protocolbuffers/protobuf/issues/1491

This repo houses a reproduction case of
https://github.com/protocolbuffers/protobuf/issues/1491, an issue that makes it
exceedingly difficult to deal with transitive imports in the Python bindings for
both Protobuf and gRPC.

`src/main.py` includes comments explaining the basic problem as well as the
various workarounds that have developed in the community as a response.
