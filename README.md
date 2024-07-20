# Fermat's Last Theorem Near Misses

## Overview

This project is designed to find "near misses" of Fermat's Last Theorem in the form $(x^n + y^n \approx z^n)$. Fermat's Last Theorem states that there are no natural numbers $(x, y, z)$ such that $(x^n + y^n = z^n)$ for $(n > 2)$. This program searches for combinations of $(x, y, z)$ that are close to satisfying this equation for given values of $(n)$ and $(k)$.

## Program Description

This program allows an interactive user to search for "near misses" in the formula $(x^n + y^n \approx z^n)$, where $(x, y, z, n, k)$ are positive integers. It systematically searches for the smallest relative miss and outputs the results.

## Requirements

- **Python 3.x**: Ensure Python is installed on your machine.

## Usage

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Run the script:

   ```sh
   python assignment1_fermat.py
   ```

3. Follow the on-screen instructions to enter values for $(n)$ and $(k)$:

   - $(n)$: The power to use in the equation (must be between 3 and 11).
   - $(k)$: The upper limit for $(x)$ and $(y)$ (must be greater than 10).

4. The program will display the smallest relative miss found for the given values of $(n)$ and $(k)$.

5. After the search is complete, you can choose to explore smallest misses for other values of $(n)$ and $(k)$ by typing "yes" or "no" when prompted.

## Program Structure

### Main Components

- **find_near_misses(n, k)**: This function performs the main search for near misses. It iterates over possible values of $(x)$ and $(y)$ from 10 to $(k)$, calculates $(x^n + y^n)$, and finds the integer $(z)$ that is closest to $(x^n + y^n)$. It computes the actual miss and relative miss, updating the smallest miss found.

- **main()**: This function handles user input and validation for $(n)$ and $(k)$, and calls the `find_near_misses` function.

### Execution

- The script continuously runs the `main` function, allowing the user to explore different values of $(n)$ and $(k)$. It asks the user if they want to continue after each run.

## Example

### Sample Output
