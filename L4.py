# a)Find x, y such that  ax + by = (a, b) for  a =123456789, b = 97654321

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)

    x = y1 - (b//a) * x1
    y = x1
 
    return gcd, x, y
 
a, b = 123456789, 97654321
g, x, y = gcdExtended(a, b)
print("gcd(", a, ",", b, ") = ", g) #gcd( 123456789 , 97654321 ) =  1
print("x:",x) #x: -325154
print("y:",y) #y: 411067

# b) Find the modular inverse of 37 mod 2019

def modinverse(a, m):
    g, x, y = gcdExtended(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

c = modinverse(37,2019)
print("Modular inverse:",c) #Modular inverse: 382

#c) Find the modular inverse of 37^2 mod 2019^2.

d = modinverse(37**2,2019**2)
print("Modular inverse:",d) #Modular inverse: 735472