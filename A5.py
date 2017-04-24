#Theory of Computation
#HW 5: A Recursive Descent Top-down Parser For Binary Postfix Notation 
#Zhenlin Jin
import operator
import time
ops = {'+' : operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def checkVal(string):
    if string[0].isdigit():
        count = 1
        #while(count >= 1):
        for char in string[1:]:
                if char in ['+', '-', '*', '/']:      #operators
                    count = count - 1
                if char.isdigit():          #operands
                    count = count + 1
                if count < 1:  #can't keep it above 1? forget it
                    print("The string is invalid")
                    return  
        if count == 1:  
            print('The string is valid')
            result = rdtdp(string) #pass to the parser
            print('The evaluation result is ', result)
        else:
            print("Invalid!") 
            return
    else: 
        print('Invalid!') 
        return 

def rdtdp(string):  #recursive descent top-down parser 
    if len(string) == 1: return string[0]
    else:
        mid = part_rule(string)
        string_l = string[:mid+1]
        string_r = string[mid+1 :-1]
        op = string[-1]
        op_char = op
        op_func = ops[op_char]
        op_l = int(rdtdp(string_l))
        op_r = int(rdtdp(string_r))
        result = op_func(op_l, op_r)
        return result

#partition rule for determing the mid value (index value)
def part_rule(string):
    i = 0
    count = 0
    stringVal = []
    while i < (len(string)):
        if string[i].isdigit():
            count = count + 1
            stringVal.append(count)
        if string[i] in ['+','-','*','/']:
            count = count - 1
            stringVal.append(count)
        i = i + 1
    #print('The validity count is: ', stringVal)
    rev = stringVal[::-1]
    del rev[0]          #delete the last element of the orginal string
    #print(rev)
    rev_mid = 1 + rev.index(1)     
    mid = len(string) - 1 - rev_mid 
    return mid

#make input a list of characters
while True:
    string = [x for x in input().split()]
    start_time = time.time()
    checkVal(string)
    print("--- %s secods ---" % (time.time() - start_time))
