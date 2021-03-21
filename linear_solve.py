#!/usr/bin/python

import sympy as sym
import convert
import sys
import re

def parse_polar(polar_string):
    '''
    Takes polar string as magnitude<angle
    '''
    index = polar_string.find('<')
    magnitude = float(polar_string[:index])
    angle = float(polar_string[index+1:])
    return magnitude, angle

def solve(equations, variables):
    '''
    Take equations as a list and variables as a comma separated string
    '''
    '''eq2 = (-1-1j)*a + 1j*e
    eq4 = (-1+2j)*b - 1j*c - 1j*d
    eq5 = -1j*b - c
    eq3 =  -1j*b - 2*d + (1+1j)*e + 1<-15 convert.to_rect(1,-15)
    eq1 = 1j*a + (1+1j)*d + (-2-2j)*e + 1<0 convert.to_rect(1,0)

    (0.772<-105 - v)/(0.372+0.198j) - (v - 1<-30)/(0.1+0.65j)

    solution = sym.solve([eq1, eq2, eq3, eq4, eq5], sym.symbols('a,b,c,d,e'))'''
    parsed_equations = []

    # parse equations
    for e in equations:
        # convert all polar
        polar_regex = re.compile('([+-]?([0-9]*[.])?[0-9]+)<([+-]?([0-9]*[.])?[0-9]+)') # regex match for all_digits<(maybe minus sign)all_digits
        polars = re.findall(polar_regex, e)
        for p in polars:
            num = convert.to_rect(float(p[0]), float(p[2]))
            e = re.sub(polar_regex,str(num), e, 1)
        parsed_equations.append(e)
            
    solution = sym.solve(parsed_equations, sym.symbols(variables))

    return solution

def main(num_equations):

    # declare variables
    equations = []

    # get user input
    variables = input('Variables (as a comma separated list): ')

    print('Enter Equations: ')
    for n in range(num_equations):
        eq = str(input('0='))
        equations.append(eq)

    # call function to solve
    solution = solve(equations, variables)

    # convert to polar and print
    print()
    print("Solution:")
    for k, v in solution.items():
        num = convert.to_polar(complex(v))
        print(str(k) + ' = ' + str(num))

def usage(message):
    print('Error: ' + message)
    print('''
    Usage:
        main.py num_equations
        0=equation1
        0=equation2
        ...
        0=equationN
    
    Notes on input form:
        Must use all mathematical signs i.e. must do (5)*x instead of (5)x
        Will take complex numbers in polar or rectangular form
        Polar form in format Magnitude<Angle
    ''')
    exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage('Incorrect number of command line arguments')
    main(int(sys.argv[1]))