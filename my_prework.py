# Question 1:
# Write a function to print "hello_USERNAME" is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("Hello " + user_name.upper())

hello_name("pearl")


# Question 2
#  Write a python, first_odds that prints the old numbers from 1-100 and returns nothing

def first_odds():
    i = 1
    while i <= 100:
        if i % 2 == 1:
            print(i)
        i = i + 1

first_odds()

# Quetion 3
#  Please write a Python function, max_num_in_lists to return the max number of a given list. The firts line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list([12, 7, 0, 3, 17]))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisble by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2200))
print(is_leap_year(2016))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True

print(is_consecutive([3, 4, 5, 6, 7, 8]))
print(is_consecutive([2, 4, 5, 6,]))


