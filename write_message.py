##Writing to an empty file

filename  = 'text_files/programming.txt'

with open (filename, 'w') as file_object:
    file_object.write("I love programming")

# Good - worked ok - created file in text_files ddirectory

# now write multiple lines

with open (filename, 'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("I love making games\n")

with open (filename) as new_object:
    for line in new_object:
        print (line.strip().rstrip())

#this will overwrite contents of file  using 'a' will append
with open (filename, 'w') as file_object:
    file_object.write("I love movies\n")
    file_object.write("I love making cars\n")

#check file to view new contents
with open (filename) as file_object:
    for line in file_object:
        print (line.strip().rstrip())


###try it

#filename2 = "text_files/guest.txt"

#with open (filename2, 'w') as file_object:
#    guest_name  = input ("Please enter your name: ")
#    file_object.write(guest_name)

#new file
filename3 = "text_files/guest_book.txt"

with open (filename3, 'a') as file_object:
    guest_name = ""
    while guest_name != "Q":
        guest_name = input ("Please enter your name: ")
        if guest_name == 'Q':
         break
        else:
            file_object.write(f"{guest_name}\n")
            print (f"Welcome to the hotel {guest_name}\n")

###New File for Poll program

filename4 = "text_files/poll.txt"
with open (filename4, 'a') as file_object:
    while True:
        response  =  input("Why do you like programming?:  ")
        if response == "Q":
            break
        else:
            file_object.write(f"{response}\n")

filename5 = "text_files/poll2.txt"

responses = []

while True:
    response  =  input("Why do you like programming?:  ")
    responses.append(response)

    continue_poll = input ("Would you like for someone else to respond? (y/n)")
    if continue_poll != 'y':
        break

with open (filename5,'a') as f:
    for response in responses:
        f.write(f"{response}`n")




