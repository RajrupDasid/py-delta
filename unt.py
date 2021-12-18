with open('/home/rajrup/AX400/detroit-kara.jpg', 'rb') as rf:
    with open('AX400.jpeg','wb') as wf:
        for line in rf:
            wf.write(line)