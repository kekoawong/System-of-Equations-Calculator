from scipy.signal import residue
import pandas as pd
import convert

# INPUT

# numerator
n = [14,106,216,48]
# denominator
k = [1, 8, 16, 0, 0]

# END INPUT

ans = residue(n,k)
final_dict = {
    'Pole': [],
    'Residue': [],
    'PolarRep': [],
    'Degree': []
}
p = []
for res in ans[0]:
    p.append(convert.to_polar(res))

degree = {}
# append to dict
for i in range(len(ans[1])):
    # get degree of pole, as function will format answers in increasing degree (according to docs)
    pole = ans[1][i]
    if pole in degree:
        degree[pole] += 1
    else:
        degree[pole] = 1
    # append to ans
    final_dict['Pole'].append(pole)
    final_dict['Residue'].append(ans[0][i])
    final_dict['PolarRep'].append(p[i])
    final_dict['Degree'].append(degree[pole])


df = pd.DataFrame(final_dict)
# displaying the results
print('Numerator:')
print(n)
print('Denominator:')
print(k)
print(df)
