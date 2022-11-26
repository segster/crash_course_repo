##

def count_words(filename):
    try:
        with open(filename, encoding='utf8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print error or silently pass
        #print(f"Sorry, the file named  {filename} does not exist")
        pass
    else:
        title = contents.split()
        # split = title.split()
        print(title)
        num_words = len(title)
        print(f"The number of words in {filename} is {num_words}")


filename = 'alice.txt'
count_words(filename)