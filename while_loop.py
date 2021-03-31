# Ask the user to choose one of two options:
user_input = input("Do you want to Print me Hello on Screen? P/Q. P for Yes & Q for Quit. ")
u_input = user_input.lower()

# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
if u_input == "p":
    
        while u_input == "p":
            print("Hello")
            user_input = input("Do you want me run this program again? P/Q. P for Yes & Q for Quit. ")
            u_input = user_input.lower()
            
        # if they type 'q', our program should terminate.
        print("You have terminated the Program. Thank you to visit me.")
        
else:
    print("Quit!.")