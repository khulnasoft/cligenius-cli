#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place types_cli tests --exclude=__init__.py
black types_cli tests
isort types_cli tests
