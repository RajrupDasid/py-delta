def reverse_string(text):
    if len(text)==0:
        return text
    else:
        return reverse_string(text[1:])+text[0]
print(reverse_string("Manjaro"))
t=2
t2=lambda t:t+1
print(t2(9))
print(t2)

def func(x):
    func2=lambda x:x+5
    return func2(x)+85
print(func(4))
