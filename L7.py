# a) A mod 5^4 = 363, 16 | A, find last 4 digits of A
# b) Do Chinese remaindering for 12345 → 6789, 56789 → 54292.
# c) Do chinese remaindering for 41 → 30, 152 → 87, 263 → 127. 

import math
#%%
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_euclidean(b % a, a)
        return g, x - (b // a) * y, y

# modular inverse driver function
def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m

def crt(m, x):
    while True:
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + \
                modinv(m[0],m[1]) * x[1] * m[0]

        temp2 = m[0] * m[1]

        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x

        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m
        
        if len(x) == 1:
            break

    return x[0]

# driver segment
m = [363, 16]
x = [5**4, 0]

print("a) Last 4 digits of A:", crt(m, x)%10000)

#%%
m = [12345, 56789]
x = [6789, 54292]
tmp = m.copy()
a = 0
n = math.prod(m)
for i in range(2):
    tmp[i] = n // m[i]
    b = tmp[i] % m[i]
    t = modinv(b, m[i])
    e = tmp[i] * t
    a += x[i] * e
a = a % n
print("b) A =", a)

#%%
m = [41, 152, 263]
x = [30, 87, 127]
tmp = m.copy()
a = 0
n = math.prod(m)
for i in range(2):
    tmp[i] = n // m[i]
    b = tmp[i] % m[i]
    t = modinv(b, m[i])
    e = tmp[i] * t
    a += x[i] * e
a = a % n
print("b) C =", a)
