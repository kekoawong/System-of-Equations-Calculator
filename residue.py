from scipy.signal import residue
import pandas as pd
import convert

# numerator
n = [6, 36, 32, -464]
# denominator
k = [1, 14, 94, 336, 680]
ans = residue(n,k)
final_dict = {
    'Pole': [],
    'Residue': [],
    'PolarRep': [],
}
p = []
for res in ans[0]:
    p.append(convert.to_polar(res))

# append to dict
for i in range(len(ans[1])):
    final_dict['Pole'].append(ans[1][i])
    final_dict['Residue'].append(ans[0][i])
    final_dict['PolarRep'].append(p[i])

df = pd.DataFrame(final_dict)

# displaying the results
print('Numerator:')
print(n)
print('Denominator:')
print(k)
print(df)
