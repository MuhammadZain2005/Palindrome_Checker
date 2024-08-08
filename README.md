# Palindrome Checker

## Description

The **Palindrome Checker** is a Python program that determines whether a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

## Features

- **Ignores Punctuation and Spaces:** The program automatically removes all punctuation and spaces from the string before checking for palindrome properties.
- **Case Insensitive:** The program converts the string to lowercase to ensure that the check is case insensitive.
- **Continuous Checking:** Users can check multiple strings in a single session until they decide to exit the program.
- **User-Friendly Interface:** The program provides clear instructions and feedback to the user.

## How It Works

The program performs the following steps:

1. **Input:** The user inputs a string to check for palindrome properties.
2. **Cleaning:** The program removes all punctuation and spaces from the input string and converts it to lowercase.
3. **Checking:** The program compares the cleaned string with its reversed version.
4. **Output:** The program prints whether the original string is a palindrome or not.
5. **Repeat/Exit:** The user can check another string or type 'exit' to close the program.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script file `palindrome_checker.py`.
2. Run the script using Python:

    ```bash
    python palindrome_checker.py
    ```

3. Enter a string when prompted to check if it's a palindrome.
4. Type `exit` to quit the program.

### Example

```bash
$ python palindrome_checker.py

Enter a string to check for palindrome (or type 'exit' to quit): A man, a plan, a canal, Panama!
Congrats, it's a palindrome!

Enter a string to check for palindrome (or type 'exit' to quit): Hello World
Sorry, it's not a palindrome.

Enter a string to check for palindrome (or type 'exit' to quit): exit
Exiting the Palindrome Checker. Goodbye!
```
## Program Structure

- **`clean_string(s)`**: Removes punctuation and spaces, converts the string to lowercase.
- **`is_palindrome(s)`**: Checks if the cleaned string is a palindrome.
- **`main()`**: Manages user input/output and handles program flow.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
