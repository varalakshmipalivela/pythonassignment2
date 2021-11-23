data = data2 = ""
with open('abc.txt') as fp:
    data = fp.read()
with open('test.txt') as fp:
    data2 = fp.read()
data += "\n"
data += data2
with open ('file3.txt', 'w') as fp:
    fp.write(data)
