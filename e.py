def reversing(text):
    if len(text)==0:
        return text
    else:
        return reversing(text[1:])+text[0]
text="openSUSE"
print(reversing(text))
