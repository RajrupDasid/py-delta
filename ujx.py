chars="How mch time i have to pissingoff"
chat={}
for i in chars:
    chat[i]=chat.get(i,0)+1
chats={}
for k,v in chat.items():
    chats[v]=k
print(chats)
    
def reverse_string(text):
    if len(text)==0:
        return text
    else:
        return reverse_string(text[1:])+text[0]
print(reverse_string("Manjaro"))