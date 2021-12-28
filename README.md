# Electrical Circuits Calculators
Various helper scripts for solving complex equations for electrical circuits course and problems relating to electrical signals with real and imaginary parts.

## Organization
* **convert.py**: Contains helper functions to convert between polar and rectangular form.
* **find_roots.py**: Finds the complex roots of an equation.
* **linear_solve.py**: Will solve a linear system of equations, with the user inputting the equations in complex form.
* **residue.py**: Script used to solve for the [residue](https://en.wikipedia.org/wiki/Residue_(complex_analysis)) of the input.

## Usage
The scripts *convert.py, find_roots.py*, and *residue.py* have manuel inputs within the script, but *linear_solve.py* will take user command line input with the following usage:
```
Usage:
        linear_solve.py num_equations
        0=equation1
        0=equation2
        ...
        0=equationN
    
    Notes on input form:
        Must use all mathematical signs i.e. must do (5)*x instead of (5)x
        Will take complex numbers in polar or rectangular form
        Polar form in format Magnitude<Angle
```

## Dependencies
* [scipy](https://scipy.org/)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [sympy](https://www.sympy.org/en/index.html)
