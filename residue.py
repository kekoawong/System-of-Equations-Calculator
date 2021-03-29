from scipy.signal import residue
import pandas as pd
import convert

# INPUT

# numerator
n = [1, 5, 8, 4]
# denominator
k = [1, 4, 8, 8, 4]

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
    # append to answer
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
