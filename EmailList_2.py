#Javon Payne
#13OCT2020
#Email_List2
 
#create a list    #Index00          #Index01        #Index02
emails = ["jpayne1@gmail.com","paynej@gmail.com", "jaypd@gmail.com"]


choice = None
while choice != "0":
    print(
        """

        Email list


        0 - Exit
        1 - Show Email list
        2 - Add an Email
        3 - Remove an Email
        """
     )   
    count = 1
    choice = input("Choice: ")
    print()    

    #exit
    if choice == "0":
        print("Good-bye.")
        break

    #List emails
    elif choice == "1":
        print("Here is your Email list.")
        for email in emails:
            print(str(count) + ")", email)
            count +=1   
        input("\n\nPress enter to continue. . .")    
               
    #Add an email
    elif choice == "2":
        email = str(input("Enter an email to add: "))
        symbols = "@"
        symbols = "."

        space = " "
        index2 = email.find("@") 
        index = email.find(".")  
        length = len(email)

        domainLength = length - index -1
        domainLength2 = index - index2 -1
        if space in email:
            print("The email cannot contain a space.")
        if index2 > index:
            print("The email must contain @ symbol followed by . symbol.")        
        #if index2 > index and space in email:
         #   print("The top level domain is", domainLength, "characters long.")
          #  print(email, "was not added to the list.")
        else:
            print(email, "was added to the list.")
            emails.append(email)
    
        input("\n\nPress enter to continue. . .")

    #remove an email
    elif choice == "3":
         print("Here is your email list.")
         for email in emails:
            print(str(count) + ")", email)
            count +=1

            ##incorporate index
         number = int(input("Remove which email?: "))
         email = emails[number - 1]
             
         if email in emails:              
             emails.remove(email)
             print(email, "was removed from the list.")
         else:
             print("email does not exist.")         
         input("\n\nPress enter to continue. . .")
        
    #some unknown choice
    else:
         print("Sorry, but", choice, "isn't a valid choice.")



















                        

