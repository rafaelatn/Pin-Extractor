# Pin Extractor

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
---

This project is a Python implementation of a text-based PIN generation algorithm called **PIN Extractor**.

It processes poems (multi-line texts) and generates numeric secret codes based on the structure of each line. The algorithm analyzes word positions and extracts numbers according to a specific positional rule.

---

## Features

- Generate secret PIN codes from multi-line text inputs  
- Process multiple poems at once  
- Use positional word indexing logic  
- Automatically handle lines with insufficient words  
- Return a list of generated PIN codes  
- Simple and lightweight implementation  

---

## Project Structure

- `pin_extractor()` – Core function responsible for generating PIN codes  
- Text input – One or more poems passed as a list  
- Output – A list of numeric strings representing the extracted secret codes  

---

## How It Works

For each poem:

1. The poem is split into individual lines.
2. Each line is analyzed based on its position (index).
3. The algorithm attempts to access the word at the same index as the line number.
4. If the word exists:
   - The length of that word is added to the secret code.
5. If the word does not exist:
   - The digit `0` is added instead.
6. The final PIN is constructed by concatenating these digits.
7. The function returns a list containing one PIN per poem.

This creates a deterministic numeric pattern derived directly from the poem’s structure.

---

## Example Usage

Input:
- A list containing one or more multi-line strings (poems)

Output:
- A list of numeric strings representing the generated PINs

Example output:

```python
['5344', '5426', '11111']
```

Each number corresponds to one processed poem.

---

## Input Requirements

- The function expects a **list of strings**.
- Each string should contain one poem.
- Line breaks must be represented using `\n`.
- If a line does not contain enough words for its index position, `0` will be used automatically.

---

## Technologies Used

- Python 3

---

## Purpose of the Project

This project was created to practice:

- String manipulation  
- List processing  
- Loop control and indexing  
- Conditional logic  
- Working with structured text data  

It demonstrates how textual patterns can be transformed into deterministic numeric codes using algorithmic logic.

---

## Notes

This implementation is intended for educational and logical exercise purposes only.  
It is **not** designed for real security or cryptographic applications.
