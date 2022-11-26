

def self_calculator():
    print ("Enter 'q' to quit")
    while True:
        try:
            num1 = input("Please enter first number: ")
            if num1 == 'q':
                break

            num2 = input("Please enter second number: ")
            if num1 == 'q':
                break
            #print(result)
        except ValueError:
            print (f"Sorry you need to enter an number")
        else:
            sum = int(num1) + int(num2)
            print (f"the sum of {num1} and {num2} is {sum}")

#self_calculator()


filenames  = ['text_files\catss.txt', 'text_files\dogs.txt']

for filename in filenames:
    print (f"\nreading file {filename}")
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print (contents)
    except FileNotFoundError:
        #print ("  ...Sorry cant find that file")
        pass





