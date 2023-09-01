"""
Author :: K HARI HARA KUMAR
Program about :: creating a simple calculator
Date created :: 11-03-2023
Date modified :: 12-03-2023
modules used :: -

"""
take_user_input = input("Enter formula in specific format :(eg. 1 + 2 ) ")
try:
    list1 = take_user_input.split(" ")
    print(list1)
    if list1[1] == '+':
        print("The result is :::",int(list1[0]) + int(list1[2]))
    elif list1[1] == '-':
        print("The result is :::",int(list1[0]) - int(list1[2]))
    elif list1[1] == '*':
        print("The result is :::",int(list1[0]) * int(list1[2]))
    # elif l1[1] == '/':
    #   print(int(l1[0])/int(l1[2]))
    # elif l1[1] == '/' and l1[2] == '0':
    #    print("Invalid !!!")
    elif list1[1] == '/':
        print("The result is :::",int(list1[0]) / int(list1[2]))
    else:
        print("FORMULAERROR: formula format is not followed ")
except Exception:
    print("FORMULA-ERROR")


"""
here in this program we used elif conditions and exceptional handling 
formula should be in given format otherwise it throws error message 
eg:  22 * 33
to manipulate the given formula 
we split the formula and given to list1
eg: ['22', '*', '33']
index   0,  1   ,2 
so,here checking for (*,+,/,-) if there, it gives result
otherwise it error is handled by exception block as FORMULA ERROR


"""

