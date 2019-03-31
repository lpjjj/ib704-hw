def ugly2 (n):
    order=[1]
    none=[]
    while pow(2, 31) > n and n != 0:
        for i in range(1,n):

            if i%2==0 and i%3==0 and i%5==0:
                order.append(i)
            elif (i%2==0 and i%3==0) or (i%2==0 and i%5==0) or (i%3==0 and i%5==0):
                order.append(i)
            elif (i%2==0 or i%3==0 or i%5==0) and i%7!=0:
                    order.append(i)
            else:
                none.append(i)
        return order
    # order.index = range(1, len(order) + 1)

print(ugly2(260))

#still not finish

