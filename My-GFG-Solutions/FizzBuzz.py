
'''
The FizzBuzz Program

You are given a number a and you have to print your answer according to the following:

If the number is divisible by 3, you print "Fizz" (without quotes)
If the number is divisible by 5, you print "Buzz" (without quotes)
If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
In any other case, you print the number itself
Note: You should add a new-line character after print statement.

Examples:

Input: a = 3
Output: Fizz
Explanation: Here, the number is divisible by 3, so Fizz is printed.
Input: a = 5
Output: Buzz
Explanation: Here the number is divisible by 5, so Buzz is printed.
Input: a = 15
Output: FizzBuzz
Explanation: Here, the number 15 is divisible by both 3 and 5, so FizzBuzz is printed.
Constraints:
1 <= a <= 100
'''

a = int(input())

if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
else:
    print(a)