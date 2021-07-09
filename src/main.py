# You'd expect this to work

print("Attempting to import generated code.")
try:
    from protos import foo_pb2
except ImportError as e:
    import traceback
    traceback.print_exc()

# But it doesn't because of the line `import bar_pb2 as bar__pb2`
# Instead, some people do this:

print("Applying perplexing workaround.")

import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "protos"))

from protos import foo_pb2

print("Successful import.")
print("Read comments in src/main.py for more info.")

# But most people just hand-modify the line to say
# `from src.protos import bar_pb2 as bar__pb2`

# Those who are a bit more crafty will write a sed script that keeps them from
# having to hand-manipulate every time they regenerate.

# gRPC's _pb2_grpc.py files use the same import mechanism because we also have
# no idea what the proper absolute import prefix should be.
