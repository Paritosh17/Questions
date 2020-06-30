def MaxReducedString(s):
    temp = [] 
    for i in s:
        if temp and temp[len(temp)-1] == i: 
            temp.pop()
        else:
            temp.append(c)    
    temp = ''.join(temp)
    return temp or 'Empty String'