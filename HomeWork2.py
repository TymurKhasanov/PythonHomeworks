#Test data from preconditions
list1 = [3, 8, 1, 6, 12, 99, 2, 200, 1000, 5] 
list2 = [99, 7, 3, 101, 12, 22, 67]
#just text
print("Let's start!!!")
print("You have 2 options to choose from:\n"
"a)  Default test data:\n" #description of A option
f"{list1} \n"
f"{list2} \n"
"b) Enter your own test data") #description of B option
#user inputs some letter here
user_input_result=input("Enter the letter:\n") 
#logic #1
if user_input_result == "b": 
    list1=input("Enter the first list of numbers separated by spaces. For example, '1 2 3 4':\n") #user inputs some numbers here
    list1 = [int(num) for num in list1.split()]
    print(list1)
    list2=input("Enter the second list of numbers separated by spaces. For example, '1 2 3 4':\n") #user inputs some numbers here
    list2 = [int(num) for num in list2.split()]
    print(list2)
elif user_input_result == "a":
    print("You chosed default test data. I understand you, mate:D")
    print(list1)
    print(list2)