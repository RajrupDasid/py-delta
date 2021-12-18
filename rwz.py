with open('rwx.text','r') as f:
    size=5
    files=f.read(size)
    print(files,end='')
    f.seek(0)
    files=f.read(size)
    print(files)