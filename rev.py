def reverse_string1(str):
    str1=""
    for i in str:
        str1=i+str1
    return str1
str1 ="Microsoft"
print ("Reversed string is ",str1)

#using while loop
str="Microsoft"
reverse_string=""
count=len(str)
while count>0:
    reverse_string+=str[count-1]
    count-=1
print(reverse_string)

#using recursive function

def reverse_text(str):
    if len(str)==0:
        return str
    else:
        return  reverse_text(str[1:])+str[0]
str="openSUSE"
print(reverse_text(str))

