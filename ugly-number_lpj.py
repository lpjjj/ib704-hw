
def lpj(num):
    while pow(2, 31) >= num >= -pow(2, 31) and num != 0:
        if num % 2 == 0:
            num = num / 2
            if num == 1 or num == 3 or num == 5:return True
        elif num%3==0:
            num = num / 3
            if num == 1 or num == 2 or num == 5:return True
        elif num%5==0:
            num = num / 5
            if num == 1 or num == 2 or num == 3: return True
        else : return False
    else : return False

assert lpj(14) is False, 'fall'
assert lpj(30) is True , 'fall'
assert lpj(6) is True , 'fall'
assert lpj(4294967296) is False, 'fall'
assert lpj(2147483648) is True , 'fall'

