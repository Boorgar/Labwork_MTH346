# Find GCD of following pairs of intergers
# (a) 2021019, 1431471
# (b) 1234567, 234569
# (c) 1234567, 56789

#%%
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(2021019, 1431471))
print(gcd(1234567, 234569))
print(gcd(1234567, 56789))