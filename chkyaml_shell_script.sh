#!/bin/bash

YAML_FILE="./file.yaml"

if [ -e ${YAML_FILE} ]; then
    if ! ./chkyaml.py ${YAML_FILE}; then
        echo "YAML syntax ERROR"
        exit 1
    fi
    echo "YAML syntax OK"
fi
