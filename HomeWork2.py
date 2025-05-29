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

#logic for "b" option
if user_input_result == "b": 
    list1=input("Enter the first list of numbers separated by spaces. For example, '1 2 3 4':\n") #user inputs some numbers here
    list1 = [int(num) for num in list1.split()]
    print(list1)
    list2=input("Enter the second list of numbers separated by spaces. For example, '1 2 3 4':\n") #user inputs some numbers here
    list2 = [int(num) for num in list2.split()]
    print(list2)

#logic for "a" option
elif user_input_result == "a":
    print("You chosed default test data. I understand you, mate:D")
    print(list1)
    print(list2)

#logic for not 'a' and not 'b' option's selected
else:
    print ("Oh, it looks like you don't know what to choose, so I chosed 'a' for you. There are the lists: ")
    print(list1)
    print(list2)

#Step 3 instructions
print("Instructions for Step 3:")
text = ("a) Display a list of elements which exist in both lists. For example: if number 5 is present in both lists, then display it; if number 10 is present only in one list, then do not display it.\n"
"b) Display a list of elements (from both lists) which exist only in one list. For example: if number 5 is present in both links, then do not display it; if number 10 is present only in one list, then display it.\n"
"c) Display both lists sorted in ascending order\n"
"d) Display both lists sorted in descending order\n"
"e) Print a list of all elements of two lists that are less than 30")
print(text)

#Step 3 final math
while True:
    step3_input = input("Select an action (a, b, c, d, e):\n")

#a) Display a list of elements which exist in both lists
    if step3_input == "a":
        exist_in_both_lists_result = [] #empty list so we can fill it
        for number in list1: #comparing number
            if number in list2:
                exist_in_both_lists_result.append(number) #filling the list
        print ("Final Result", exist_in_both_lists_result) #printing the final result

#a) Display a list of elements (from both lists) which exist only in one list
    elif step3_input == "b":
        do_not_exist_in_both_lists_result = [] #empty list so we can fill it
        for number in list1: #comparing that numbers from list1 are not present in the list 2
            if number not in list2:
                do_not_exist_in_both_lists_result.append(number) #filling the list that are not in the list 2
        for number in list2: #comparing that number from list2 are not present in the list 1
            if number not in list1:
             do_not_exist_in_both_lists_result.append(number) #filling the list that are not in the list 1
        print ("Final Result", do_not_exist_in_both_lists_result) #printing the final result

#c) Display both lists sorted in ascending order
    elif step3_input == "c":
        asclist = sorted(list1+list2) #all numbers in 1 list and sorted
        print("Both lists sorted in ascending order:",asclist)

#d) Display both lists sorted in ascending order
    elif step3_input == "d":
        desclist = sorted(list1+list2, reverse=True) #all numbers in 1 list and sorted and desc
        print("Both lists sorted in descending order:",desclist)

#e) Print a list of all elements of two lists that are less than 30
    elif step3_input == "e":
        twolists = sorted(list1+list2)  #all numbers in 1 list (descided to sort the numbers also)
        lessthirty = [] #creating new list to fill in all number < 30
        for number in twolists :
            if number < 30 : #checking that numbers are less than 30
                lessthirty.append(number) #adding them to the list
        print("List of all elements and less than 30:",lessthirty)

#The logic if anything other than the necessary letters is entered
    else:
        print("Wrong letter, mate. Please re-enter:")   