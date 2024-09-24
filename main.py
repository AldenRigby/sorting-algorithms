#use this chunk of code to get an input from the user
go = True
userInput = []
while go:
    try:
        tempUserInput = input("Enter a set of numbers, separated by spaces.").split(" ")
        for i in tempUserInput:
            userInput.append(int(i))
        go = False
    except:
        print("That isn't a valid list.")
#userInput should now be a list of numbers