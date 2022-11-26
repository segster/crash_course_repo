##P197

filename = 'alice.txt'

try:
    with open (filename, encoding='utf8') as f:
        contents = f.read()
except FileNotFoundError:
    print  (f"Sorry, the file named  {filename} does not exist")



title = contents.split()

#split = title.split()

print (title)

num_words = len(title)
print (f"The number of words in {filename} is {num_words}")
