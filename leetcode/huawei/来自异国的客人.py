k,n,m = 10,2,4

real_val = ''
while k >0:
    real_val += str(k%m)
    k//=m

print(real_val)