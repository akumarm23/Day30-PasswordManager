# Password Manager GUI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8-grey.svg)](https://www.python.org/downloads/)
![Version](https://img.shields.io/badge/version-v0.1-red)

## Overview

The Password Manager GUI (`main.py`) is a simple graphical user interface (GUI) application built with Tkinter in Python. It allows users to generate secure passwords, save them along with website and email details, and retrieve passwords when needed. The application utilizes a JSON file (`data.json`) to store password data.

## Features

- Password generation with a mix of letters, numbers, and symbols.
- Ability to save website, email, and password details.
- Search functionality to find and display saved passwords.
- Dropdown menu for selecting pre-defined email addresses.
- Passwords are copied to the clipboard for easy use.

## Password Generator

- `generate()`: Generates a random password with a mix of characters.

## Save Password

- `save()`: Saves website, email, and password details to `data.json`.

## Find Password

- `find_json()`: Searches for and displays saved passwords.

## Dropdown Menu

- Displays pre-defined email addresses for quick selection.

## UI Setup

- Labels, buttons, and entry fields for creating the user interface.
- Canvas for displaying a logo.
- Options to search, generate passwords, add entries, and select email addresses.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/akumarm23/Day30-PasswordManager.git
   cd Day30-PasswordManager
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Use the application to generate, save, and retrieve passwords.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Feel free to contribute and enhance the functionality of this Password Manager GUI! Happy coding!