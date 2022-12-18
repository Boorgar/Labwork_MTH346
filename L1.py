# Find last 3 digits of 2018^2019
# Find remainder when 20182019^20192018 is divided by 12345
# Find remainder when 9^9^9 is divided by 1001

# Cat's comment: Below are rough solutions. Needs improvement

#%%
a = 2018
b = 2019

def get_last_3_digits(num, power):
    return pow(num, power, 1000)

get_last_3_digits(a, b)

#%%
a = 20182019
b = 20192018

def get_remainder(num, power, divisor):
    return pow(num, power, divisor)

get_remainder(a, b, 12345)

#%%
a = 9
b = 9
c = 9

def get_remainder(num, power, divisor):
    return pow(num, power, divisor)

get_remainder(a, b**c, 1001)

