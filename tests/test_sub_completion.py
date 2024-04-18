import os
import subprocess


def test_script_completion_run():
    result = subprocess.run(
        ["coverage", "run", "-m", "types_cli"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "___MAIN__.PY_COMPLETE": "complete_bash",
            "_PYTHON _M TYPES_CLI_COMPLETE": "complete_bash",
            "COMP_WORDS": "types tests/assets/sample.py run hello --",
            "COMP_CWORD": "4",
            "_TYPES_COMPLETE_TESTING": "True",
        },
    )
    assert "--name" in result.stdout
