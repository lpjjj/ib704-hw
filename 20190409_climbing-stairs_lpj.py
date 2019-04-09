
def climbstairs(n) :
    way=[]
    for i in range(1,n+1) :
        if i ==1 or i==2 :
            way.append(i)
        else :
            add = way[i-3]+way[i-2]
            way.append(add)
    return way[-1]

assert climbstairs(1) == 1, 'Fail'
assert climbstairs(2) == 2, 'Fail'
assert climbstairs(3) == 3, 'Fail'
assert climbstairs(4) == 5, 'Fail'
assert climbstairs(5) == 8, 'Fail'
assert climbstairs(6) == 13, 'Fail'
assert climbstairs(45) == 1836311903, 'Fail'

