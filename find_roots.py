# import numpy library 
import numpy as np 
  
# Enter the coefficients of the polymial into the array 
coeff = [1,3,2,2]
# round the roots
for num in np.roots(coeff):
    num = round(num.real, 3) + round(num.imag, 3) * 1j
    print(num)
