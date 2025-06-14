
# Linear Search Using Recursion

def LinearSearch_recursion(l1,x,index):
    if(len(l1) == index):
        return False


    return l1[index] == x or LinearSearch_recursion(l1,x,index+1)
    
    #answer_recursion = LinearSearch_recursion(l1,x,index+1)

    # if(answer_recursion == True):
    #     return True
    
    # if(l1[index] == x):
    #     return True
    # return False

   # return l1[index] == x or answer_recursion

l1 = [i for i in range(100000)]
answer = LinearSearch_recursion(l1,10,0)

print(answer)