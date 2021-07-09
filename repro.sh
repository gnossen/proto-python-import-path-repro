#!/bin/bash

python3 -m virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
./generate_code.sh
python3 src/main.py

