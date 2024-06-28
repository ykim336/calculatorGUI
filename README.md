# Calculator GUI Application

Welcome to the Calculator GUI Application! This project is designed to help you gain experience with QtDesigner, a powerful tool for designing and building graphical user interfaces (GUIs) using the Qt framework.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Calculator GUI Application is a basic calculator that supports standard arithmetic operations. It serves as an excellent starting point for learning how to use QtDesigner to create and manage a user interface. By the end of this project, you will be familiar with the basics of QtDesigner and how to integrate the generated UI files into a Python application using PyQt.

## Features
- Simple and intuitive user interface
- Supports addition, subtraction, multiplication, and division
- Real-time display of calculations and results
- Error handling for invalid inputs and division by zero

## Installation
Follow these steps to set up the Calculator GUI Application on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/calculator-gui.git
   cd calculator-gui

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Ensure you have QtDesigner installed:
- You can download and install QtDesigner as part of the Qt framework from Qt's official website.

## Usage
To run the Calculator GUI Application, follow these steps:

1. **Open QtDesigner:**
   - Use QtDesigner to open and edit the `calculator.ui` file. You can modify the layout, add buttons, labels, and other widgets as needed.

2. **Generate the Python code from the UI file:**
   ```bash
   pyuic5 calculator.ui -o calculator_ui.py

3. Run the application
   ```bash
   python main.py



