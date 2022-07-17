# 1. maximum of three numbers
def max_of_three(x,y,z) :
    return max(x,y,z)
print(max_of_three(4,8,5))
print()


# 2.Write a Python function to sum of all the numbers in a list
def sum_of_num(sample_list) :
    return sum(sample_list)
sample_list = (4,6,7,8,9,3)
print(sum_of_num(sample_list))
print()


# 3.Write a Python function to multiply all the numbers in a list.
def multi(sample_list) :
    total = 1
    for i in sample_list :
        total = total * i
    return total   
sample_list = (8, 2, 3, -1, 7)
print(multi(sample_list))
print()


# 4.Write a Python program to reverse a string
#method_1
def string_reverse(string) :
    string=string[::-1]
    return string
print(string_reverse("4321dcba"))
#method_2
def string_reverse(string) :
    r_str = ''
    index = len(string)
    while index > 0 :
        r_str = r_str + string[index-1]
        index = index - 1
    return r_str
print(string_reverse("4321dcba"))
print()


# 5.Write a Python function to calculate the factorial of a number (a non-negative integer).
def factorial(n) :
    num = 1
    while n > 0 :
        num = num * n
        n = n - 1
    return num
print(factorial(5))
print(factorial(8))


# 6. Write a Python function to check whether a number falls in a given range.
def check_num(n) :
    if n in range(3,9) :
        return f"{n} is in  the range"
    else :
        return "Outside of the range"
print(check_num(2))    
print(check_num(5))


# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#method_1
def upper_lower(string) :
    upper = []
    lower = []
    for i in string :
        if i.isupper() :
            upper.append(i)
        elif i.islower(): 
            lower.append(i)
        else :
            pass
    print(f"total no. of Upper letter is : {len(upper)}")
    print(f"total no. of Upper letter is : {len(lower)}")
print(upper_lower('The Gang of Robbers Are Gone'))
print()

#method_2
def upper_lower(string) :
    check = {"Upper case" : 0 , "Lower case" : 0}
    for i in string :
        if i.isupper() :
            check["Upper case"] = check["Upper case"] + 1
        elif i.islower() :
            check["Lower case"] = check["Lower case"] + 1
        else :
            pass
    print("Total no. of Upper case : ",check["Upper case"])
    print("Total no. of Lower case : ",check['Lower case'])
print(upper_lower('You Are Super Awesome DUDE!'))
print()


# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list
def unique_num(sample_list) :
    unique_list = []
    for i in sample_list :
        if i not in unique_list :
            unique_list.append(i)
    return unique_list
print(unique_num([5,3,4,5,3,3,3,1,1,0,5,5,6,7,8,8,9,1,1,2,4]))
print()


# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
def check_prime(n) :
    if n==1 :
        return False
    elif n==2 :
        return True
    else :
        for x in range(2,n) :
            if n%x == 0 :
                return False
            else :
                return True
print(check_prime(5))
print()


# 10. Write a Python program to print the even numbers from a given list.
def find_even(sample_list) :
    even_list = []
    for num in sample_list :
        if num%2 == 0 :
            even_list.append(num)
    return even_list
print(find_even([1,2,3,4,5,6,7,8,9,10,45,25,12,11]))
print(find_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print()


#11. Write a Python function to check whether a number is perfect or not.
def perfect_num(n) :
    sum = 0
    for x in range(1,n) :
        if n%x  == 0 :
            sum = sum + x
    return sum == n , f"{sum} is perfect number"
print(perfect_num(6))   #1+2+3=6  
print(perfect_num(28))  #1+2+4+7+14 = 28
print(perfect_num(5))
print()


# 12. Write a Python function that checks whether a passed string is palindrome or not.
def ispalindrome(string) :
    left_pos = 0
    right_pos = len(string) - 1
    while right_pos >= left_pos :
        if not string[left_pos] == string[right_pos] :
            return False
        left_pos += 1
        right_pos -= 1
    return True
print(ispalindrome("azaza"))
print(ispalindrome("yes"))
print(ispalindrome("madam"))


# 13. Write a Python function that prints out the first n rows of Pascal's triangle.
from math import factorial
def pascal_triangle(n) :
    for i in range(n) :
        for j in range(n-i+1) :
            print(end=" ")     # for left side spacing
        for j in range(i+1) :
            print(factorial(i)//( factorial(j)*factorial(i-j) ), end=" ")
        print()
print(pascal_triangle(3))
print(pascal_triangle(5))
print()


# 14. Write a Python function to check whether a string is a pangram or not. Go to the editor
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
import string 
def ispangram(string) :
    alphabet = set(string.ascii_lowercase)
    return set(string.lower()) >= alphabet 
string ='The quick brown fox jumps over the lazy dog'
print(ispangram((string)))


# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def hyphen_sep_words(my_words) : # words = 'banana-apple-kim-ing'
    items=[n for n in my_words]
    items.sort()
    print('-'.join(items))
my_words = input().split('-')
print(hyphen_sep_words(my_words))


#  16. Write a Python function to create and print a list where the values are square of numbers between 1 and 20 (both included)
def squared_num() :
    squared = list()
    for i in range(1,21):
        squared.append(i**2)
    return squared
print(squared_num())


# 18. Write a Python program to access a function inside a function.
def test(n) :
    def add(m) :
        nonlocal n
        return n+m
    return add
# func = test(int(input()))
func = test(4)
print(func(5))
print(func(3))