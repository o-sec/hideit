# Hideit

this is a small Python obfuscation utility that converts visible Python source code into invisible Unicode characters and generates a loader that decodes and executes the original code at runtime.

The resulting script appears visually empty or unreadable, while still being fully functional when executed by Python.

## How It Works

1. Reads a target Python file.
2. Encodes each character into a Unicode tag character (offset by `0xE0000`).
3. Generates a new Python file containing a decoder stub.
4. The stub reconstructs the original source code and executes it using `exec()`.

## Usage

```bash
python3 hideit.py <FILENAME.py>
````

Example:

```bash
python3 hideit.py example.py
```

This will create a new file:

```text
invisible_example.py
```

## Disclaimer

This repository contains a small proof-of-concept created **for educational, research, and proof-of-concept purposes only**.
The author takes no responsibility for misuse or unintended consequences.
