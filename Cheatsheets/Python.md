# Python Quick Reference

| Task | Example |
|---|---|
| Version | `python --version` |
| Run a script | `python script.py` |
| Create virtual environment | `python -m venv .venv` |
| Activate on POSIX shell | `source .venv/bin/activate` |
| Install declared dependencies | `python -m pip install -r requirements.txt` |
| Compile-check syntax | `python -m py_compile script.py` |
| SHA-256 file digest | `python -c "import hashlib,pathlib; p=pathlib.Path('file'); print(hashlib.sha256(p.read_bytes()).hexdigest())"` |

Use a project virtual environment, pin and review dependencies, and do not execute untrusted scripts on a sensitive host.
