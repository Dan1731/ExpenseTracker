#!/usr/bin/bash

echo "Running Setup script!"

if [[ ! -d ".venv" ]]; then
    echo "No virtual env found, creating one"
    python3 -m venv .venv
    ./.venv/bin/pip install -r requirements.txt
fi

source .venv/bin/activate


