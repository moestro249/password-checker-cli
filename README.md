# password-checker-cli

A console tool that checks the strength of a password and lists every problem it finds.

## Features
- Checks minimum length (8 characters)
- Requires a lowercase letter, an uppercase letter, a digit and a special character
- Rejects very common passwords (for example `password` or `123456`)
- Reports all problems at once, not just the first one
- Hides the password while you type it

## Requirements
- Python 3.11 (the version it was developed with)

## Usage
```
git clone https://github.com/moestro249/password-checker-cli
cd password-checker-cli
python main.py
```

Type a password when prompted. The program prints either `Password is strong` or a list of problems.

## Tests
```
pip install pytest
python -m pytest
```

## Project structure
- `checker.py` - `check_password`, returns a list of problems (an empty list means the password passed all checks)
- `main.py` - the command-line entry point
- `test_checker.py` - tests for every rule

## Limitations
- The common-password check compares the whole password with a small built-in list, so `Password1!` passes even though it is weak.
- The tool does not measure randomness or guess how long cracking would take; it only checks simple rules.