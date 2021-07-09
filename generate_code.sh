#!/bin/bash

for FILE in protos/*.proto; do
  protoc -I protos \
    --python_out=src/protos \
    "$FILE"
done
