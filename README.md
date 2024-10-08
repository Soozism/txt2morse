# txt2morse

## Overview

`txt2morse` is a Python script that translates English text into Morse code using the `match-case` statement. The program takes input from the user and outputs the corresponding Morse code. Each letter and digit is converted based on its Morse code equivalent, with spaces in the input being converted to slashes (`/`) to represent word separation.

This script demonstrates the usage of Python's `match-case` control structure, which was introduced in Python 3.10 to provide a cleaner and more readable alternative to multiple `if-elif` statements for pattern matching.

---

## Features

- **Text Input**: User inputs a string of text to be translated into Morse code.
- **Morse Code Conversion**: Each character in the input is converted into its corresponding Morse code.
- **Word Separation**: Spaces between words are represented by a `/` in the Morse code output.

---

## How It Works

1. **User Input**: The script prompts the user to input a text string.
2. **Character Conversion**: The script loops through each character of the input string and uses a `match-case` block to convert each character to its Morse code equivalent.
3. **Morse Code Output**: After all characters have been converted, the result is printed out.

---

## Example Usage

### Input:
```
Please input your text: hello world
```

### Output:
```
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

---

## Requirements

- **Python version**: Python 3.10 or later (since the `match-case` statement is used, which was introduced in Python 3.10).
  
To check your Python version, run:
```bash
python --version
```

---

## Installation and Usage

1. **Clone the repository or download the script**.
   - Save the script as `txt2morse.py`.

2. **Run the script**:
   ```bash
   python txt2morse.py
   ```

3. **Input your text** when prompted.

---

## Code Explanation

- The program reads input from the user using `input()` and converts it to lowercase using `txt.lower()`.
- A `match-case` block is used to compare each character in the input and append its corresponding Morse code to the `morse_code` string.
- For spaces, the Morse code equivalent is `/` (slash), and for unsupported characters, the program does nothing (`pass`).
- The Morse code string is printed with each character separated by a space for clarity.

---

## License

This script is free to use for educational purposes. Contributions and improvements are welcome!
