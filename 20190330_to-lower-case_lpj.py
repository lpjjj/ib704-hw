def lpj_lower(s):
    str=[]
    Str = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g','H': 'h','I': 'i','J': 'j','K': 'k','L': 'l','M': 'm','N': 'n','O': 'o','P': 'p','Q': 'q','R': 'r','S': 's','T': 't','U': 'u','V': 'v','W': 'w','X': 'x','Y': 'y','Z': 'z'}
    for c in s :
        if c in Str :
            str.append(Str[c])
        else:
            str.append(c)
    return "".join(str)
assert lpj_lower("ASDSDFDgfdg") == "ASDSDFDgfdg".lower(),'fall'
