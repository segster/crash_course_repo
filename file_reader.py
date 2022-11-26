
filename = 'text_files/pi_digits.txt'
filename2 = 'text_files/leaf-01.txt'
#with open (filename) as file_object:
#    contents = file_object.read()
#print (contents)
#print (contents.rstrip())

#above closes file as no more code under 'with open'

#with open (filename2) as file_object:
#    for  line in file_object:
#        print (line.rstrip())

print ("First Program - ")
with open (filename) as file_object:
    lines  = file_object.readlines()
print ("End First Program")

#for line in lines:
#    print(line.rstrip())

###working with a files contents outs the 'with' construct

print ("Second Program use lines object")
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print (pi_string)
print (len(pi_string))
print ("End Second Program\n")


filename3 = 'text_files/pi_million_digits.txt'

with open (filename3) as million_file:
    lines  = million_file.readlines()

pi_string2 = ''
for line in lines:
    pi_string2 += line.rstrip()

print (f"{pi_string2[:52]}....")
print ("length of PI is..",len(pi_string2))

##is your birthday in PI?

birthday = input("Enter your birthday in for ddmmyy: ")
if birthday in pi_string2:
    print ("your birtday appears in the first million digits of Pi!!")
else:
    print ("Awww never minds ...check the next million digits!")


filename4 = 'text_files/in_python.txt'

with open (filename4) as inpython:
    contents = inpython.read()
    #contents = contents.replace('Python', 'Pasacal')
    #or this way
print (contents.replace('Python', 'C'))


print ("\n...Looping over the lines")
with open (filename4) as inpython:
    #inpython = inpython.replace('Python','C')
    for line in inpython:
        #chaining methods together
        print(line.rstrip().replace('Python', 'Cobol'))


print ("\n...Looping over the lines")
with open (filename2) as inpython:
    lines  = inpython.readlines()
    print (lines)

for line in lines:
    print (line.rstrip())

