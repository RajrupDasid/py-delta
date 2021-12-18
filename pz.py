fhand_="How much wood would a wood chucker chuck if a wood chucker could chuck wood"
fhand =fhand_.split() 
counts = {}
for word in fhand:
    counts[word] = counts.get(word, 0 ) + 1
count = {}
for k,v in counts.items():
    count[v] = k
print(count)
