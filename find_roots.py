# import numpy library 
import numpy as np 
  
# Enter the coefficients of the polymial into the array 
coeff = [1,3,4,3,0,-1,-2,0,0]
deg = len(coeff) - 1
print("Degree: " + str(deg))
# round the roots
for num in np.roots(coeff):
    num = round(num.real, 3) + round(num.imag, 3) * 1j
    print(num)
