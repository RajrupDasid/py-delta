#find the word count  and common word
fcount_="Manjaro and openSUSE are best Linux distro in this world"
counts={}
for word in fcount_:
    counts[word]=counts.get(word,0)+1
count={}
for key , value in counts.items():
    count[value]=key
print(count)

string="NASA-National Aeronautics and Space Administrition"
cs={}
for i in string:
    cs[i]=cs.get(word,0)+1
c={}
for k ,v in cs.items():
    c[v]=k
print(c)