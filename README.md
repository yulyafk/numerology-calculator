# Numerology Calculator

## Description
This project is an application for calculating the Life Path Number based on the user's birth date and time. It uses the Prokerala API to retrieve the Life Path Number and its description.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yulyafk/numerology-calculator.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd numerology-calculator
    ```

3. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` file in the root directory of the project and add your `CLIENT_ID` and `CLIENT_SECRET`:**
    ```plaintext
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    ```

## Usage
1. **Run the application:**
    ```bash
    python numerology_calculator.py
    ```

2. **Enter your birth date and time in the "Numerology Calculator" application window to get your Life Path Number and its description.**

## Running Tests
1. **To run tests, execute the command:**
    ```bash
    pytest
    ```

2. **Close the "Numerology Calculator" application window without entering any data in it.**

3. **Check if the tests passed.**
