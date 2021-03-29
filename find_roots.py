# import numpy library 
import numpy as np 
  
# Enter the coefficients of the polymial into the array 
coeff = [1, 106./14, 216./14, 48./14]
deg = len(coeff) - 1
print(coeff)
print("Degree: " + str(deg))
# round the roots
for num in np.roots(coeff):
    num = round(num.real, 3) + round(num.imag, 3) * 1j
    print(num)
