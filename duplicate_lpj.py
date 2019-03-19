
from collections import Counter
def lpj(n_list):
    cal_n=Counter(n_list)
    max=cal_n.most_common(1)
    if max[0][1]>1:
        return True
    else:
        return False

assert lpj([1,2,3]) is False , 'fail'
assert lpj([1,1,2]) is True , 'fail'