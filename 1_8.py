# Find Jacobi notation (or Legendre notation): (1983 | 2017), (873 | 2019), (474993 | 1003001)

#%%
def jacobi(a, n):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        if n % 8 in [1, 7]:
            return 1
        if n % 8 in [3, 5]:
            return -1
    if a >= n:
        return jacobi(a % n, n)
    if a % 2 == 0:
        return jacobi(2, n) * jacobi(a // 2, n)
    if a % 4 == 3 and n % 4 == 3:
        return -jacobi(n, a)
    return jacobi(n, a)

print(jacobi(1983, 2017))
print(jacobi(873, 2019))
print(jacobi(474993, 1003001))
