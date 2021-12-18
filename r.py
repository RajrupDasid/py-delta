#python reversing string usifng for loop

def reverse_string(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str1="openSUSE"
print(reverse_string(str))

#python reversing string using recursive
def rev_string(str):
    if len(str)==0:
        return str
    else:
        return rev_string(str[1:])+str[0]
str="openSUSE"
print(rev_string(str))

