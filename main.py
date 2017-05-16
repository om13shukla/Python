import sys

from StringProblems import StringProblems

def get_input_string():
    str1 = raw_input("Enter a STRING to test: ")
    return str1

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
str_prlblms.replace_space()
