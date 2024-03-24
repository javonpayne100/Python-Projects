#Javon Payne
#27OCT2020
#Find_The_Largest


number1 = int(input("Enter a number between 1 and 100 (-1 to stop): "))
number2 = int(input("Enter a number between 1 and 100 (-1 to stop): "))
number3 = int(input("Enter a number between 1 and 100 (-1 to stop): "))

def find_the_largest(num1, num2, num3):
    if (num1 > num2) and (num1 > 3):
        largest = num1
    elif (num2 > num1) and (num2 > num3):
        largest = num2
    elif (num3 > num1) and (num3 > num2):
        largest = num3
    elif (num1 == -1) or (num2 == -1) or (num3 == -1):
        print("The End. . .")
    

large = find_the_largest(large)
print("The largest number is", large)
#Main
for i in range(6):
    print(i, end=" ")
    large = find_the_largest(numbers)



    
    choice = input()
    choices = int(choice)
    choicesTaken = choice + 1

    counter= 0
    while numbers != "-1":
        counter += 1
        if numbers < 1 and number > 100:
            print("Try Again! Enter a number between 1-100: ")
        else:       
            large = find_the_largest(number)
    if numbers == largest:
        print("The largest number is: ", large)
        
    


   

        

