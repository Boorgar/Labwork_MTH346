#Find the GCD of following pairs of integers
def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)

if __name__=="__main__":
#a)	2021019 and 1431471
   x = 2021019
   y = 1431471
   print("gcd(", x, ",", y, ") = ", gcd(x, y)) # gcd(2021019,1431471) = 2019
#b)	1234567 and 234569
   h = 1234567
   k = 234569
   print("gcd(", h, ",", k, ") = ", gcd(h, k)) # gcd(1234567,234569) = 127
 #c)	1234567 and 56789

   m = 1234567
   n = 56789
   print("gcd(", m, ",", n, ") = ", gcd(m, n))  # gcd(1234567,56789) = 1
 
 
