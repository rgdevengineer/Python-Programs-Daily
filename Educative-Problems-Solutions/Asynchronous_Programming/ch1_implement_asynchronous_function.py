
'''
Challenge 1: Implement an Asynchronous Function
In this challenge, you are required to implement an asynchronous coroutine function.

Problem Statement
Implement an asynchronous coroutine function to add two variables and sleep for the duration of the sum. 
Use the asyncio loop to call the function with two numbers.
Input
Two number n1 and n2
Output
The sum of two numbers
Sample Input
n1 = 1, n2 = 2
Sample Output
3
'''

import asyncio

async def sum(n1,n2):
    print('Sum numbers', n1, '+', n2)
    await asyncio.sleep(1)
    print('End Sum', n1, '+', n2)
    return n1 + n2
loop = asyncio.get_event_loop()

n1 = 1
n2 = 2