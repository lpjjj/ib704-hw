from collections import Counter
def lpj (list) :
    initial=0
    list_index=[]
    cal_n = Counter(list)
    max = cal_n.most_common(1)
    if max[0][1] > 1:
        for n in range (list.count(max[0][0])) :
            index=initial
            a=max[0][0]
            initial=list[initial:].index(a)
            list_index.append(initial+index)
            initial=list_index[-1:][0]+1
        print(list_index)
        gap = []
        for n in range (len(list_index)-1) :
            gap.append(list_index[n+1]-list_index[n]-1)
            print(gap)
        return True
    else :
        return False


assert lpj([4,6,3,2,7,9,7,7]) is True, fail
assert lpj([4,6,3,2,7,9,5,1]) is False, fail