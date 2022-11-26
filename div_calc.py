###Exceptions####
#P:194

#print (5/0)

try:
    print(5/2)
except ZeroDivisionError:
    print ("you madman - u cant devide by zero!!")

###
print ("Give ne two numbers and I'll divide them:")
print ("Enter q to quit")


while True:
    first_number  = input("input first number:")
    if first_number == 'q':
        break
    second_number = input("Input second number:")
    if second_number == 'q':
         break

    try:
        answer  = int(first_number) /  int(second_number)
    except ZeroDivisionError:
        print("you madman - u cant devide by zero!!")
    else:
        print (int(answer))

