# Find m such that p | m^2 + 1 for p:
# p = 2029
# p = 474993
# p = 1003001


#%%
def squareRoot(p):
    if p % 4 != 1:
        return
    result = []
    for i in range(1, int((p-1)/2)+1):
        if pow(i, int((p-1)/2), p) == p-1:
            result.append(pow(i, int((p-1)/4), p))
            result.append(p - result[0])
            break
    return result



r = squareRoot(2029)
if r:
    print(r)
else:
    print("N/A")

r = squareRoot(474993)
if r:
    print(r)
else:
    print("N/A")

r = squareRoot(1003001)
if r:
    print(r)
else:
    print("N/A")