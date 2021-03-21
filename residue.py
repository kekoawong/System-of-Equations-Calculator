from scipy.signal import residue

n = [4,6,0,4]
k = [1,2,1.5,4,2]
ans = residue(n,k)

print('Residues:')
print(ans[0])
print('Poles')
print(ans[1])