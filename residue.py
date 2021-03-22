from scipy.signal import residue
import convert

n = [1,.5,-1.25]
k = [1,1,-1,-2]
ans = residue(n,k)
p = []
for n in ans[1]:
    p.append(convert.to_polar(n))

print('Polar representations:')
print(p)
print('Residues:')
print(ans[0])
print('Poles')
print(ans[1])
