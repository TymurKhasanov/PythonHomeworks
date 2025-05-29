list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5] #Test data from preconditions
list2 = [99, 7, 3, 101, 12, 22, 67]
print("You have 2 options to choose from:\n" #just text
"a)  Default test data:\n" #description of A option
f"{list1} \n"
f"{list2} \n"
"b) Enter your own test data") #description of B option
user_input_result=input("Enter the letter:\n") #user inputs some letter here
if user_input_result == "b": 
    print("Enter the first list of numbers separated by spaces. For example, '1 2 3 4'")