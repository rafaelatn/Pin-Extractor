# 🔐 Pin Extractor

> Extract secret numeric PIN codes from structured poems using positional word analysis.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
---

## 📖 Overview

**Pin Extractor** is a lightweight Python utility that generates secret numeric codes from multi-line text inputs.

The algorithm works by:

- Splitting each poem into lines.
- Selecting the word at the same index as the line number.
- Appending the length of that word to form a numeric PIN.
- If the word does not exist, `0` is appended instead.

The result is a list of numeric PINs, one per poem.

---

## ⚙️ How It Works

For each poem:

| Line Index | Selected Word Position |
|------------|------------------------|
| 0          | Word 0                 |
| 1          | Word 1                 |
| 2          | Word 2                 |
| ...        | ...                    |

---

## 🧠 Example

### Implementation

```python
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes


poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"

poem3 = "There\nonce\nwas\na\ndragon"

print(pin_extractor([poem, poem2, poem3]))
```

### Output

```python
['53460', '55560', '50000']
```
