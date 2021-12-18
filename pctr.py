#finding count of words 
word='Manjaro'
count=0
for i in word:
    if i=='a':
        count=count+1
print(count)

string ="openSUSE"
count_init=0
for it in string:
    if it=='o':
        count_init+=1
print(count_init)
data = 'From info@indiancybersecuritysolutions.com Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
data = 'From info@indiancybersecuritysolutions.com Sat Jan  5 09:14:16 2008'
start = data.find('@')
print(start)
end = data.find(' ', start)
print(end)
domain = data[start+1:end-4]
print(domain)