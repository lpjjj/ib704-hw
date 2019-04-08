
def common (str1,str2,str3) :
    str=[]
    for c in str1 :
        if c in str2 and c in str3 and str1.find(c)==str2.find(c)==str3.find(c) :
            a=str1.find(c)
            str.append(str1[a])
        else : pass
    return "".join(str)
assert common("flower","flow","flight") == "fl",'fall'
assert common("dog","racecar","car") == "",'fall'
