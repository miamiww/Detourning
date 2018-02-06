f = open("mycoolmanifesto.txt","w")
f.write("a specter\n")
f.write("is haunting me")
f.close()

with open("somecool_file.txt","w") as outfile:
    outfile.write("some lines of text")
    outfile.write("another line of text")

f = open("mycoolmanifesto.txt","r")
data = f.read()
print data
f.close()

f = open("somecool_file.txt","r")
lines = f.readlines()
print lines
f.close()
