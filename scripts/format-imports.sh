#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort --recursive  --force-single-line-imports --thirdparty types_cli --apply types_cli tests
sh ./scripts/format.sh
