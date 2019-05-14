#function for atoi
def atoi(string):
    ans=0
    
    if string[0]=='-':
        sign=-1
    else:
        sign=1
        
    for i in range(0,len(string)):
        if i==0 and string[i]=='-':
            continue
            
        if '0'<= string[i] <='9':
            ans=ans*10 + (ord(string[i])-ord('0'))
        else:
            return -1
        
    return ans*sign
