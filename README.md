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

### 3. Classwork 09 - Spanish Verb Conjugator (CW09)
The included Python script (`spanish_verb_conjugator.py`) is a linguistic automation tool designed to conjugate any regular Spanish verb ending in *-ar*, *-er*, or *-ir* in the present tense[cite: 10, 74].Built strictly utilizing Python built-in features, lists, and dictionaries without external libraries.
The program isolates the verb's core lexical components (`stem` and `ending`) via advanced string slicing.It then dynamically pairs the root with its corresponding grammatical suffix by synchronizing parallel collection indices within an optimized iterative loop

### 4. Classwork 10 - School Management System (CW10)
The included Python script (school_management_system.py) is an administrative simulation tool designed to replicate an academic records platform handling multi-role access controls (Student, Teacher, and Coordinator) within a single, continuous runtime loop. Developed under strict operational constraints without user-defined functions, the program manages global data persistence using multidimensional dictionaries and immutable tuples. It features infinite login verification, interactive data updates with nested correction loops for real-time grade modification, and boolean state controls to safely manage cross-role transitions and full system shutdowns.

### 5. Classwork 11 - The Mandelbrot Set (CW11)
The included Python script (mandelbrot_set_math.py) is a mathematical program designed to calculate the data points of the Mandelbrot Set fractal. 

The program reads configuration parameters (such as image resolution and coordinate limits) from an external file named config.txt. It then maps these coordinates to a grid and runs an iterative loop to check how fast each point escapes to infinity using the standard Mandelbrot formula. 

The results (the number of iterations achieved per pixel) are saved directly into a file named clase.csv. Additionally, this folder includes the complete pseudocode (PPP.txt) and the execution flowchart (Flowchart.png).

### 6. Classwork 12 - Mandelbrot Set Image Renderer (CW12)
The included Python script uses the Pillow (PIL) library to transform the raw coordinate data from `clase.csv` into a high-resolution PNG image. 

The program reads dimensions from `config.txt` and processes each row of the dataset. It applies a custom color smoothing algorithm that colors the interior of the Mandelbrot set black and creates a dynamic color gradient (shifting from deep blues to vibrant oranges) for the exterior pixels based on their escape velocity. It also includes error handling to prevent index overflows during pixel placement.

---

### 7. Classwork 13 - Error Handling (CW13)
The objective of this assignment is to refactor and optimize the implementations from Classwork 07, 08, and 09 by integrating robust, professional error handling mechanisms (`try-except` structures) based on defensive programming paradigms.
The scripts were re-engineered to capture specific operational and system exceptions—such as `ValueError`, `KeyError`, `ZeroDivisionError`, `SyntaxError`, and `NameError`—preventing sudden execution crashes due to malformed user inputs, unsupported syntax in dynamic string evaluations, or empty fields. Code blocks are strictly categorized into structural `# INPUT`, `# PROCESS`, and `# OUTPUT` operations to secure execution data streams and display clean, structured terminal alerts.

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
For Classwork 09:
```
cd CW09
python spanish_verb_conjugator.py
```
For Classwork 10:
```
cd CW10
python school_management_system.py
```
For Classwork 11:
```
cd Classwork-11-The-Mandelbrot-Set
python mandelbrot_set_math.py
```
For Classwork 12:
```
cd Classwork-12-Mandelbrot-Set-Image-Renderer
python render_mandelbrot.py
```
For Classwork 13:
```
cd Classwork-13-Error-Handling
# To run Verifier Digit with Error Handling:
python verifier_digit.py

# To run Numerical Integration with Error Handling:
python numerical_integration.py

# To run Spanish Verb Conjugator with Error Handling:
python spanish_verb_conjugator.py
```
---

## AI Use Declaration - Classwork 07

AI tools were partially utilized as an auxiliary assistant for generating the structural layout of the flowchart diagram and organizing the specific technical keywords for the vocabulary log. The core logic of the Modulo 11 check-digit algorithm and its Python implementation were fully conceptualized and coded by the author.

---

## AI Use Declaration - Classwork 08

AI tools were partially utilized as an auxiliary assistant for debugging, optimizing the string substitution workflow in the numerical integration loops, and formatting documentation layout. The mathematical integration logic, variable structures, and boundary constraints were fully designed and implemented by the author.

---

## AI Use Declaration - Classwork 09

AI tools were partially utilized as an auxiliary assistant for optimizing documentation syntax, formatting pseudocode structure, and verifying standard markdown layout. The implementation of structural arrays, dictionary mapping configurations, and sequential loop logic were entirely designed and coded by the author.

---

## AI Use Declaration - Classwork 10

AI tools were partially utilized as an auxiliary assistant for structural formatting of logical control flows, organizing multi-layered menu loops, and optimizing interactive terminal prompts. The design of multidimensional data mapping, boolean flow architectures, validation states, and sequential menu branching conditions were entirely designed and implemented by the author.

---

## AI Use Declaration - Classwork 11

AI tools were partially utilized as an auxiliary assistant for structural formatting of the markdown layout, rendering the architectural flowchart canvas, and refining the text parsing logic for file inputs. The core mathematical translation of the complex escape-time loops, boundary mapping functions, and matrix file generation were entirely conceptualized, designed, and coded by the author.

---

## AI Use Declaration - Classwork 12

AI tools were partially utilized as an auxiliary assistant for structuring the logical blocks of the conditional color mapping, organizing the exception handling flow, and formatting the markdown documentation layout. The configuration parsing, data array cleaning, and coordinate pixel rendering logic were entirely designed and implemented by the author.

---

## AI Use Declaration - Classwork 13

AI tools were partially utilized as an auxiliary assistant for structural formatting of the markdown layout, organizing the try-except conditional routing blocks, and expanding text parsing validation constraints. The core architecture of exception catching parameters, programmatic error redirection loops, and standard input sanitization workflows were entirely designed, integrated, and implemented by the author.

---





