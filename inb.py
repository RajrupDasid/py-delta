with open ('test.text','r')as rf:
    with open('text_copy.text','w')as wf:
        for line in rf:
            wf.write(line)
            