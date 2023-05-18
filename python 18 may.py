Question 1.
 What is Python Programming Language and explain features of
Python Programming Language.
Answer - python is an interpreted language,it directly interpreted into machine instructions. Its easy to learn and its syntax is simple yet elegant.you can perform math operations like addition , substraction , multiplication , and division using arithmetic operations in python. You can also access several libraries that can help you with more advanced arithmetic problems.
Features like, code or source code: the sequence of instructions on program.
syntax - the set of legal structures and commands that can be used in aperticular way of python language.
output - the message printed in the program to the user.
console - the text box onto which output is printed..

Question 2.Write a Python Program to reverse only the vowels of a given
string.
Answer -
def reverse_vovels(str1):
    vowels = ""
    for char in str1;
        if char in  "aeiouAEIOU":
            vowels += char
    result_string = ""
    for char in str1:
        if char in "aeiouAEIOU":
            result_string += vowels[-1]
            vowels = vowels[:-1]
        else:
            result_string += char
    return result_string
print(reverse_vovels("Abhijeet"))
print(reverse_vovels("Python"))
print(reverse_vovels("Jetking"))  

Question 3.Write a Python Program to check whether a given integer is a
palindrome or not.
Answer -

num = input('Enter any number : ')
try :
    val = int(num)
    if num  == str(num) [::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number,Try Again !")      
    

Question 4.      Write a Python Program to remove the duplicate elements of a
given array of numbers such that each element appear only once
and return the new length of the given array.
Answer -
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list        
#Driver code here
duplicate = [2, 5, 7, 20, 2, 22, 4, 2]
print(Remove(duplicate))