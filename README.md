# A-Simple_Text_Menu
In this example I will create a simple text menu using WHILE loop. If user enter "P" I will keep program running,, if the User enter"Q" I will quit the Program
# In this program I will use WHILE loop to make a Simple text Menu
# Ask the user to choose one of two options:
user_input = input("Do you want to Print me Hello on Screen? P/Q. P for Yes & Q for Quit.")
u_input = user_input.lower()

# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
if u_input == "p":
    
        while u_input == "p":
            print("Hello, We are running the Program.")
            user_input = input("Do you want me run this program again? P/Q. P for Yes & Q for Quit.")
            u_input = user_input.lower()
            
        # if they type 'q', our program should terminate.
        print("You have terminated the Program. Thank you to visit me.")
        
else:
    print("You Quit!.")

# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...


# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...