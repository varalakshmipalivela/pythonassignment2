fo = open("assignment.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
fo = open("assignment.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");
fo.close()
