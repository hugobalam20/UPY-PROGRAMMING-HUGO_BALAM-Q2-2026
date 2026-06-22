# Git/GitHub Repository

This repository contains Python-based implementations, developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to establish a professional development environment using Git for version control and GitHub for remote collaboration.

---

## Project Description

### 1. Classwork 07 - Dígito Verificador (CW07)
The included Python script (`Digito_verificador.py`) is a utility program designed to automate the validation process for university identifiers. It challenges the program to calculate the check digit of a specific UTFSM roll number using the standard Modulo 11 mathematical algorithm.
The program processes the input string, applies the corresponding decreasing weights from 2 to 7 across the digits, computes the remainder, and determines the final verification character (supporting numbers from 0-9 and the character 'K').

### 2. Classwork 08 - Numerical Integration
The included Python script (`numerical_integration.py`) is a mathematical evaluation engine designed to approximate the area under a curve within a specific interval $[a, b]$ divided into $n = 1000$ subintervals. 
The program features dynamic runtime evaluation through input parsing, allowing users to write custom mathematical functions directly into the console. It supports four different evaluation methodologies selected via conditional blocks:
* **TRAP:** Approximates the definite integral using the Trapezoidal Rule by summing boundary and weighted intermediate values.
* **LRM / RRM / MRM:** Implements Riemann Sums utilizing Left, Right, or Midpoint rectangular evaluations by dynamically shifting the iteration bounds and calculating subinterval heights.

---

## Environment & Tools

* **Language:** Python 3.x
* **Version Control:** Git
* **Hosting Platform:** GitHub
* **Terminal Environment:** PowerShell / VS Code Terminal

---

## How to Run the Program

1. Ensure you have Python installed on your system.
2. Clone this repository or download the source files:

```bash
git clone https://github.com/hugobalam20/UPY-PROGRAMMING-HUGO-BALAM-Q2-2026.git
```
3. Navigate to the specific project directory and execute the desired script:

For Classwork 07:
```
cd CW07
python Digito_verificador.py
```

For Classwork 08:
```
cd Classwork-08-Numerical-Integration
python numerical_integration.py
```
---

## AI Use Declaration - Classwork 07

AI tools were partially utilized as an auxiliary assistant for generating the structural layout of the flowchart diagram and organizing the specific technical keywords for the vocabulary log. The core logic of the Modulo 11 check-digit algorithm and its Python implementation were fully conceptualized and coded by the author.

---

## AI Use Declaration - Classwork 08

AI tools were partially utilized as an auxiliary assistant for debugging, optimizing the string substitution workflow in the numerical integration loops, and formatting documentation layout. The mathematical integration logic, variable structures, and boundary constraints were fully designed and implemented by the author.


