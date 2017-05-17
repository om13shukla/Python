import sys

import random

from StringProblems import StringProblems

def get_input_string():
    str1 = raw_input("Enter a STRING to test: ")
    return str1


def get_multi_list():
    ls=[]
    for i in range(4):
        tls=[]
        for j in range(4):
            tls.append(random.randint(1,9))
        ls.append(tls)
    k=random.randint(0,4)
    l=random.randint(0,4)
    ls[k][l]=0

    print "Adding a ZERO at [",k,"][",l,"]"
    print "Random List: ",ls     
    return ls

str_in=get_input_string()
str_prlblms = StringProblems(str_in.lower())
"""
result = str_prlblms.chk_unique_chars()
if result:
    print "found repeated charecter: ",result
else:
    print "All unique chars in the String: ",str_in

"""
#str_prlblms.str_reverse()
#str_prlblms.chk_palin()
#str_prlblms.chk_perm()
#str_prlblms.replace_space()
#str_prlblms.str_comp()
str_prlblms.make_zero(get_multi_list())
