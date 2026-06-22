import math

# INPUT

pi = math.pi

a_input = input("Write the left endpoint of the interval: ")
b_input = input("Write the rigth endpoint of the interval: ")
f_x = input("Write the functions to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ")

# Parse and evaluate inputs
a = float(eval(a_input))
b = float(eval(b_input))

# Initialize variables and parameters
n = 1000
h = (b - a) / n
area = 0.0
shift = 0
constant = 0
variable = 0

# PROCESS

if method == "TRAP":
    variable = 1
    
    # Calculate the first term f(a)
    f_0 = f_x.replace("x", f"({a})")
    area += (h/2) * eval(f_0)
    
    # Sum the intermediate values multiplied by 2
    for i in range(variable, n):
        xi = a + (i * h)
        f_xi = f_x.replace("x", f"({xi})")
        area += (h/2) * 2 * eval(f_xi)
        
    # Calculate the last term f(b)
    f_xn = f_x.replace("x", f"({b})")
    area += (h/2) * eval(f_xn) 

else:
    # Set configuration based on Riemann Sum method (Left, Right, Midpoint)
    if method == "RRM":
        shift = 1
    if method == "MRM":
        constant = h / 2

    # Loop to sum the areas of the subintervals
    for i in range(shift, n + shift):
        if method == "MRM":
            xi = a + (i * h) + constant
        else:
            xi = a + (i * h)
            
        height = f_x.replace("x", f"({xi})")
        area += h * eval(height)

# OUTPUT

print(f"The integration of {f_x} is {area}")

