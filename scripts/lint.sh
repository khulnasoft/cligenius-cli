#!/usr/bin/env bash

set -e
set -x

mypy types_cli
black types_cli tests --check
isort types_cli tests --check-only
