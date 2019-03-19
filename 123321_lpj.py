
def back (x):
    if x < 0 :
        x = -1*x
        x=str(x)
        x = x[::-1]
        x=int(x)
        x = -1 * x
        return x
    if pow(10,9) > x > 0 :
        x=str(x)
        x = x[::-1]
        x=int(x)
        return x
    else :
        return 0

# x =-1230
# # b=reverse(x)
# print(back(x))

# xstr = str(x)
# print(xstr)
# x = xstr[::-1]
# print(x)

assert back(123) == 321, 'Fail'
assert back(-123) == -321, 'Fail'
assert back(120) == 21, 'Fail'
assert back(1534236469) == 0, 'Fail'