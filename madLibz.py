#Javon Payne
#06DEC2020
#madLibz


#Example1
print("Creating a text file with the write() method.")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("That makes this line 2\n")
text_file.write("So this must be line 3\n")
text_file.close()

print("\nReading the newly created file.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

print("\nCreating a text file with the writelines() method.")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n",
         "This is line2\n",
         "So this must be line3\n"]
text_file.writelines(lines)
text_file.close()

print("\nReading the nexly created file.")

input("\n\nPress enter to continue. . .")


#Example2
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered the number.")
input("\n\nPress enter to continue. . .")
